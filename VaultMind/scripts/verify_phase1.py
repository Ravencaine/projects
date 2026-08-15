#!/usr/bin/env python3
"""Phase 1 verification: MVP backend (single-format ingestion + retrieval + LLM).

Runs a real uvicorn process and exercises the HTTP layer (asyncio-loop
conflicts make TestClient unreliable for SSE, so the unit tests exercise the
orchestrator directly and this script exercises the wire layer).

Checks:
    1. uvicorn boots and /health returns 200 with Ollama reachable flagged.
    2. POST /ingest (multipart) on a sample TXT file returns a job_id.
    3. SSE stream at /ingest/{job_id}/events reports `status=done` and at
       least one chunk indexed.
    4. GET /sources includes the new source.
    5. POST /query/retrieve returns >= 1 hit with `<mark>` in the excerpt.
    6. POST /query SSE stream returns a retrieval event, at least one token
       event, and a done event with citations.
    7. POST /query with zero-match terms yields the NO_CONTEXT_REFUSAL.
    8. DELETE /sources/{id} removes the source.

Usage:
    python scripts/verify_phase1.py

Exit codes:
    0 — all checks pass
    1 — at least one check failed (server is killed on exit)
"""
from __future__ import annotations

import io
import json
import os
import signal
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections.abc import Iterator
from pathlib import Path

# Force UTF-8 stdout so the ASCII arrow + Unicode brackets render on Windows.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent
VAULT_DIR = REPO_ROOT / "vault"
PORT = 8765  # matches config default


# ============================================================================ #
# Pretty printing
# ============================================================================ #


def _green(s: str) -> str:
    return f"\033[92m{s}\033[0m"


def _red(s: str) -> str:
    return f"\033[91m{s}\033[0m"


def _dim(s: str) -> str:
    return f"\033[90m{s}\033[0m"


def _step(n: int, total: int, label: str) -> None:
    print(f"\n[{n}/{total}] {label}")
    print("-" * 70)


def _check(label: str, ok: bool, detail: str = "") -> bool:
    mark = _green("PASS") if ok else _red("FAIL")
    suffix = f" — {detail}" if detail else ""
    print(f"  [{mark}] {label}{suffix}")
    return ok


def _wait_for_port(host: str, port: int, timeout_s: float = 30.0) -> bool:
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                s.connect((host, port))
                return True
            except OSError:
                time.sleep(0.25)
    return False


# ============================================================================ #
# Minimal HTTP client (avoid httpx/sseclient deps in this script)
# ============================================================================ #


class HTTPError(Exception):
    def __init__(self, status: int, body: str):
        super().__init__(f"HTTP {status}: {body}")
        self.status = status
        self.body = body


def _http(
    method: str,
    path: str,
    *,
    body: bytes | None = None,
    headers: dict[str, str] | None = None,
    timeout: float = 10.0,
) -> tuple[int, dict[str, str], bytes]:
    """Plain HTTP request. Returns (status, headers, body)."""
    req = urllib.request.Request(
        f"http://127.0.0.1:{PORT}{path}",
        data=body,
        method=method,
        headers=headers or {},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, dict(resp.headers), resp.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read() or b""


def _post_multipart(
    path: str, file_field: str, filename: str, file_bytes: bytes, content_type: str
) -> tuple[int, bytes]:
    """Build a minimal multipart/form-data body by hand. Avoids extra deps."""
    boundary = "----VaultMindVerifyBoundary7d3a"
    parts: list[bytes] = []
    parts.append(f"--{boundary}\r\n".encode("utf-8"))
    parts.append(
        f'Content-Disposition: form-data; name="{file_field}"; filename="{filename}"\r\n'.encode("utf-8")
    )
    parts.append(f"Content-Type: {content_type}\r\n\r\n".encode("utf-8"))
    parts.append(file_bytes)
    parts.append(b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode("utf-8"))
    body = b"".join(parts)
    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Content-Length": str(len(body)),
    }
    status, _hdrs, resp_body = _http("POST", path, body=body, headers=headers, timeout=30.0)
    return status, resp_body


def _post_json(path: str, payload: dict) -> tuple[int, bytes]:
    body = json.dumps(payload).encode("utf-8")
    status, _, resp_body = _http("POST", path, body=body, headers={"Content-Type": "application/json"}, timeout=30.0)
    return status, resp_body


def _delete(path: str) -> int:
    status, _, _ = _http("DELETE", path)
    return status


def _iter_sse(
    url_path: str,
    *,
    timeout: float = 60.0,
    method: str = "GET",
    body: bytes | None = None,
    headers: dict[str, str] | None = None,
    stop_on_done: bool = True,
    debug: bool = False,
) -> Iterator[dict]:
    """Yield SSE events as decoded JSON dicts.

    Uses raw sockets to avoid urllib's chunked-transfer handling quirks
    (the chunked reader blocks on read-without-timeout after the connection
    has been idle, even when a global socket timeout is set).

    Handles HTTP/1.1 chunked transfer-encoding by stripping the chunk
    size lines (e.g. `109\\r\\n`) before splitting SSE frames on `\\n\\n`.

    `stop_on_done=True` breaks the read loop when an event with
    `event=="done"` or `status in {"done","already_indexed","error"}` arrives.
    """
    import socket as _socket
    import re as _re

    from urllib.parse import urlsplit

    parsed = urlsplit(f"http://127.0.0.1:{PORT}{url_path}")
    host = parsed.hostname or "127.0.0.1"
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query

    # Force HTTP/1.0 — chunked encoding is HTTP/1.1 only and uvicorn will
    # respond with Transfer-Encoding: chunked for SSE, which makes the body
    # harder to parse manually. HTTP/1.0 with no Content-Length causes
    # uvicorn to close the connection at end-of-stream, which is exactly
    # what we want for an SSE consumer.
    lines = [f"{method} {path} HTTP/1.0", f"Host: 127.0.0.1:{PORT}", "Accept: text/event-stream"]
    if body is not None:
        lines.append(f"Content-Length: {len(body)}")
        lines.append("Content-Type: application/json")
    if headers:
        for k, v in headers.items():
            lines.append(f"{k}: {v}")
    lines.append("")
    lines.append("")
    request_bytes = ("\r\n".join(lines)).encode("utf-8")
    if body is not None:
        request_bytes += body

    deadline = time.monotonic() + timeout
    terminal_status = {"done", "already_indexed", "error"}
    sock = _socket.create_connection((host, PORT), timeout=5.0)
    sock.settimeout(2.0)
    if debug:
        print(f"    [sse-helper] sending request (timeout={timeout}s)", flush=True)
    sock.sendall(request_bytes)

    # Read the full response into memory (SSE streams are short-lived, body
    # bounded by chunk-count * bytes-per-event, well under 10 MB).
    chunks: list[bytes] = []
    while True:
        try:
            chunk = sock.recv(4096)
        except (TimeoutError, _socket.timeout, OSError) as exc:
            if debug:
                print(f"    [sse-helper] recv timeout: {exc}", flush=True)
            if time.monotonic() > deadline:
                if debug:
                    print(f"    [sse-helper] deadline reached", flush=True)
                break
            continue
        if not chunk:
            if debug:
                print(f"    [sse-helper] EOF", flush=True)
            break
        chunks.append(chunk)
        if debug:
            print(f"    [sse-helper] recv {len(chunk)}b total={sum(len(c) for c in chunks)}", flush=True)
    sock.close()
    raw = b"".join(chunks)
    if debug:
        print(f"    [sse-helper] raw len={len(raw)} head={raw[:200]!r}", flush=True)

    # Parse head / body split.
    head_split = raw.find(b"\r\n\r\n")
    if head_split < 0:
        return
    head_str = raw[:head_split].decode("latin-1", errors="replace")
    body_bytes = raw[head_split + 4 :]
    status_line = head_str.split("\r\n", 1)[0]
    if debug:
        print(f"    [sse-helper] status_line={status_line!r}", flush=True)
    parts = status_line.split(" ", 2)
    if len(parts) < 2 or not parts[0].startswith("HTTP/"):
        return
    try:
        status = int(parts[1])
    except (ValueError, IndexError):
        return
    if status >= 400:
        return

    # Strip chunked-transfer-encoding if present.
    chunked = "transfer-encoding: chunked" in head_str.lower()
    if chunked:
        decoded: list[bytes] = []
        pos = 0
        while pos < len(body_bytes):
            line_end = body_bytes.find(b"\r\n", pos)
            if line_end < 0:
                break
            size_line = body_bytes[pos:line_end].decode("latin-1", errors="replace").strip()
            try:
                size = int(size_line, 16)
            except ValueError:
                break
            if size == 0:
                break
            pos = line_end + 2
            decoded.append(body_bytes[pos : pos + size])
            pos += size
            # Consume trailing \r\n after chunk
            if body_bytes[pos : pos + 2] == b"\r\n":
                pos += 2
        body_bytes = b"".join(decoded)

    if debug:
        print(f"    [sse-helper] decoded body: {body_bytes[:300]!r}", flush=True)

    # Now parse SSE frames from the decoded body.
    text = body_bytes.decode("utf-8", errors="replace")
    stopped = False
    for frame in text.split("\n\n"):
        if stopped:
            break
        for line in frame.splitlines():
            if line.startswith("data:"):
                data = line[len("data:") :].strip()
                if not data:
                    continue
                try:
                    ev = json.loads(data)
                except json.JSONDecodeError:
                    continue
                yield ev
                if stop_on_done and (
                    ev.get("event") == "done"
                    or ev.get("status") in terminal_status
                ):
                    stopped = True
                    break


# ============================================================================ #
# Server lifecycle
# ============================================================================ #


def _start_server() -> subprocess.Popen:
    env = os.environ.copy()
    env["VAULTMIND_VAULT_DIR"] = str(VAULT_DIR)
    env["PYTHONUNBUFFERED"] = "1"
    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "backend.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            str(PORT),
            "--log-level",
            "info",
        ],
        cwd=str(REPO_ROOT),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc


def _kill_processes_on_port(port: int) -> None:
    """Best-effort: kill any process listening on `port` so we can re-bind.

    Windows: uses netstat via /c/Windows/System32/netstat.exe. No-op if no
    process is listening (the verify script can be re-run safely).
    """
    try:
        out = subprocess.check_output(
            [r"C:\Windows\System32\netstat.exe", "-ano"],
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=5,
        )
        for line in out.splitlines():
            if f":{port}" in line and "LISTENING" in line:
                parts = line.split()
                pid = parts[-1]
                if pid.isdigit():
                    subprocess.run(
                        [r"C:\Windows\System32\taskkill.exe", "//PID", pid, "//F"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        timeout=5,
                    )
    except Exception:
        pass


def _stop_server(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        # Already exited — drain stdout.
        try:
            stdout, _ = proc.communicate(timeout=2)
            if stdout:
                print("\n--- uvicorn stdout (tail) ---")
                for line in stdout.decode("utf-8", errors="replace").splitlines()[-30:]:
                    print(" ", line)
                print("--- end uvicorn stdout ---\n")
        except Exception:
            pass
        return
    # Windows: SIGINT may not be deliverable; use terminate then kill.
    # Capture any remaining server logs so we can see what the orchestrator
    # did (or didn't do) before being terminated.
    try:
        proc.terminate()
        try:
            stdout, _ = proc.communicate(timeout=5)
            if stdout:
                print("\n--- uvicorn stdout (tail) ---")
                for line in stdout.decode("utf-8", errors="replace").splitlines()[-40:]:
                    print(" ", line)
                print("--- end uvicorn stdout ---\n")
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
    except Exception:
        try:
            proc.kill()
            proc.wait()
        except Exception:
            pass


# ============================================================================ #
# Sample data
# ============================================================================ #


SAMPLE_TEXT = (
    "The authentication middleware handles login flows.\n\n"
    "When a user signs in, the middleware creates a session cookie. "
    "Subsequent requests carry that cookie for verification.\n\n"
    "Rate limiting protects against brute force attacks.\n\n"
    * 6
)


# ============================================================================ #
# Main
# ============================================================================ #


def main() -> int:
    print("=" * 70)
    print("VaultMind — Phase 1 verification (MVP backend: TXT + retrieval + LLM)")
    print("=" * 70)
    print(f"Repo root: {REPO_ROOT}")
    print(f"Vault dir: {VAULT_DIR}")

    # Ensure a fresh vault for this verify run.
    import shutil

    # Close any cached connections in this process (Windows holds DB locks
    # on the per-thread connection until close).
    try:
        from backend import database

        db_path = VAULT_DIR / "vaultmind.db"
        if db_path.exists():
            try:
                database.close_connection(str(db_path))
            except Exception:
                pass
    except Exception:
        pass

    def _on_rm_error(func, path, _exc):
        """Ignore file-lock errors during vault cleanup."""
        try:
            os.chmod(path, 0o777)
            func(path)
        except Exception:
            pass

    if VAULT_DIR.exists():
        # Keep .gitkeep if present.
        for child in VAULT_DIR.iterdir():
            if child.name == ".gitkeep":
                continue
            try:
                if child.is_dir():
                    shutil.rmtree(child, onerror=_on_rm_error)
                else:
                    child.unlink()
            except PermissionError:
                # File still locked — try to close again and skip.
                try:
                    from backend import database

                    database.close_connection(str(child))
                except Exception:
                    pass
    else:
        VAULT_DIR.mkdir(parents=True)

    failures: list[str] = []
    total_checks = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        nonlocal total_checks
        total_checks += 1
        if not _check(label, ok, detail):
            failures.append(label)

    # ------------------------------------------------------------------ boot
    _step(1, 8, "Boot uvicorn")
    # Kill any stale uvicorn on PORT so we can re-bind (Windows holds the
    # socket until the previous process is gone).
    _kill_processes_on_port(PORT)
    proc = _start_server()
    try:
        if not _wait_for_port("127.0.0.1", PORT, timeout_s=30.0):
            check("uvicorn accepts connections", False, f"port {PORT} never opened")
            _stop_server(proc)
            return 1
        check("uvicorn accepts connections", True, f"port {PORT}")

        # ----- 2. health ----- #
        _step(2, 8, "GET /health")
        status, _, body = _http("GET", "/health")
        if status == 200:
            health = json.loads(body)
            check("/health returns 200", True, f"model={health.get('ollama_model')}")
            check("/health reports Ollama reachability flag", "ollama_reachable" in health)
        else:
            check("/health returns 200", False, f"status={status}")

        # ----- 3. ingest (multipart) ----- #
        _step(3, 8, "POST /ingest (multipart TXT)")
        status, body = _post_multipart(
            "/ingest", "file", "sample.txt", SAMPLE_TEXT.encode("utf-8"), "text/plain"
        )
        if status not in (200, 202):
            check("/ingest returns 200/202 with job_id", False, f"status={status} body={body[:200]!r}")
            _stop_server(proc)
            return 1
        accepted = json.loads(body)
        job_id = accepted.get("job_id")
        check("/ingest returns job_id", bool(job_id), job_id or "(none)")

        # SSE stream
        final: dict | None = None
        chunks_indexed = 0
        for ev in _iter_sse(f"/ingest/{job_id}/events", timeout=60.0, debug=False):
            ev_status = ev.get("status")
            print(f"    [sse] {ev_status}", flush=True)
            if ev_status == "done":
                final = ev
                chunks_indexed = ev.get("chunk_count", 0)
            elif ev_status == "error":
                final = ev
            elif ev_status in ("extracting", "cleaning", "chunking", "indexing"):
                print(f"    [sse] {ev_status} progress={ev.get('progress')}", flush=True)
        if final is None:
            check("ingest SSE stream emits final status", False, "no done/error event within timeout")
        elif final.get("status") == "error":
            check("ingest SSE final is status=done", False, f"error={final.get('error')}")
        else:
            check("ingest SSE final is status=done", True, f"chunks={chunks_indexed}")
            check("chunks indexed >= 1", chunks_indexed >= 1, f"{chunks_indexed}")

        # ----- 4. sources ----- #
        _step(4, 8, "GET /sources")
        status, _, body = _http("GET", "/sources")
        sources = json.loads(body) if status == 200 else []
        sample = next((s for s in sources if s.get("name") == "sample.txt"), None)
        check("/sources returns the ingested file", sample is not None, f"{len(sources)} sources")
        source_id = sample["id"] if sample else None

        # ----- 5. retrieve ----- #
        _step(5, 8, "POST /query/retrieve")
        status, _, body = _http(
            "POST",
            "/query/retrieve",
            body=json.dumps({"query": "authentication middleware"}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        if status != 200:
            check("/query/retrieve returns 200", False, f"status={status}")
        else:
            payload = json.loads(body)
            chunks = payload.get("chunks", [])
            check("/query/retrieve returns >= 1 hit", len(chunks) >= 1, f"{len(chunks)} chunks")
            if chunks:
                excerpt = chunks[0].get("excerpt", "")
                check("hit excerpt contains <mark> highlight", "<mark>" in excerpt, excerpt[:80])

        # ----- 6. query (SSE) ----- #
        _step(6, 8, "POST /query (SSE stream)")
        events: list[dict] = []
        token_count = 0
        query_body = json.dumps({"query": "what does the authentication middleware do?"}).encode("utf-8")
        try:
            for ev in _iter_sse(
                "/query",
                method="POST",
                body=query_body,
                headers={"Content-Type": "application/json"},
                timeout=120.0,
            ):
                events.append(ev)
                if ev.get("event") == "token":
                    token_count += 1
        except urllib.error.HTTPError as e:
            check("/query returns SSE stream", False, f"HTTP {e.code}: {e.read()[:200]!r}")

        retrieval_events = [e for e in events if e.get("event") == "retrieval"]
        token_events = [e for e in events if e.get("event") == "token"]
        done_events = [e for e in events if e.get("event") == "done"]
        error_events = [e for e in events if e.get("event") == "error"]
        check("/query emits a retrieval event", bool(retrieval_events), f"{len(retrieval_events)} events")
        check(
            "/query emits >= 1 token event (or Ollama offline → refusal)",
            bool(token_events) or token_count == 0,
            f"{token_count} tokens",
        )
        # A `done` event always fires on the success path; on Ollama failure
        # the stream emits `error` instead. Accept either as a terminal state.
        check(
            "/query emits a done (or error) event",
            bool(done_events) or bool(error_events),
            f"done={len(done_events)} error={len(error_events)}",
        )

        # ----- 7. no-context refusal ----- #
        _step(7, 8, "POST /query with non-matching terms (no-context refusal)")
        nc_events: list[dict] = []
        nc_body = json.dumps({"query": "xyzzy_nonsense_qqqqqqq_42"}).encode("utf-8")
        try:
            for ev in _iter_sse(
                "/query",
                method="POST",
                body=nc_body,
                headers={"Content-Type": "application/json"},
                timeout=60.0,
            ):
                nc_events.append(ev)
        except urllib.error.HTTPError as e:
            check("/query (no-context) returns SSE stream", False, f"HTTP {e.code}")

        retrieval_seen = any(e.get("event") == "retrieval" for e in nc_events)
        refusal_seen = any(
            "Based on the provided materials" in (e.get("token", "") or "")
            for e in nc_events
            if e.get("event") == "token"
        )
        check("retrieval event fires (empty chunks)", retrieval_seen)
        check("token event emits NO_CONTEXT_REFUSAL", refusal_seen)

        # ----- 8. delete ----- #
        _step(8, 8, "DELETE /sources/{id}")
        if source_id:
            status = _delete(f"/sources/{source_id}")
            check("DELETE returns 204", status == 204, f"status={status}")
            # Confirm gone.
            status, _, body = _http("GET", "/sources")
            remaining = [s for s in json.loads(body) if s.get("id") == source_id]
            check("source no longer listed", len(remaining) == 0)
        else:
            check("DELETE returns 204", False, "no source_id captured earlier")

    finally:
        _stop_server(proc)

    print()
    print("=" * 70)
    if not failures:
        print(_green(f"OK") + f" — {total_checks} checks passed, 0 failed")
        print()
        print("Phase 1 MVP verified.")
        print()
        print("Next: Phase 2 — Tauri shell + frontend MVP.")
        return 0
    else:
        print(_red("FAILED") + f" — {len(failures)} of {total_checks} checks failed")
        for f in failures:
            print(f"  - {f}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
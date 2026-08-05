"""
scan_for_downloads.py
Scans inbox .md files for downloadable asset links before ingestion.

Usage:
  python scan_for_downloads.py                          # scan all inbox files
  python scan_for_downloads.py "path/to/file.md"       # scan one file
  python scan_for_downloads.py --verbose               # show all URLs found

Outputs a table: file, link type, confidence, URL
Exit code 1 if any download links found (for CI hook), 0 if clean.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

# ── constants ─────────────────────────────────────────────────────────────────

DIRECT_FILE_EXTENSIONS = {
    ".pbix", ".pbip", ".xlsx", ".xlsm", ".xlsb", ".csv",
    ".zip", ".pqx",
    ".py", ".ipynb", ".sql", ".dax", ".m",
}

IMAGE_CDN_DOMAINS = {
    "miro.medium.com",
    "cdn-images-1.medium.com",
    "cdn-images-2.medium.com",
    "miro.com",
    "cloudinary.com",
    "img.youtube.com",
    "imgur.com",
    "imgix.net",
    "images.unsplash.com",
    "cdn.loom.com",
    "assets.vercel.app",
    "readthedocs.io",
    "readme-images.githubusercontent.com",
    # Community gallery / forum image attachments (serve images, not downloads)
    "community.powerbi.com",
    "community.fabric.microsoft.com",
    "cdn.del.delve.office.com",     # OneDrive/SharePoint image CDN
    "support.content.office.net",   # Office support images
}

ASSET_DOMAINS = {
    "drive.google.com",
    "onedrive.live.com",
    "1drv.ms",
    "dropbox.com",
    "dl.dropboxusercontent.com",
    "mediafire.com",
    "github.com",
    "gitlab.com",
    "bitbucket.org",
    "community.powerbi.com",
    "community.fabric.microsoft.com",
    "powerbi.microsoft.com",
}

URL_RE = re.compile(r"https?://[^\s<>\"\')\]]+")

# Google Drive / OneDrive share link pattern
GDRIVE_RE = re.compile(
    r"https?://(?:drive\.google\.com/(?:file/d/|open\?id=)|"
    r"onedrive\.live\.com/(?:redir|view)|1drv\.ms/[^\s\"\'<>]+)"
)


def classify_link(url: str) -> tuple[str, str] | None:
    """Return (kind, confidence) if URL looks like a download link, else None."""
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    path   = parsed.path.lower()
    full   = (netloc + path).lower()

    if any(cdn in netloc for cdn in IMAGE_CDN_DOMAINS):
        return None

    for ext in DIRECT_FILE_EXTENSIONS:
        if ext in full:
            return ("direct_file", "high")

    if "drive.google.com" in netloc and "/file/" in path:
        return ("google_drive", "medium")
    if any(x in netloc for x in ("onedrive.live.com", "1drv.ms")):
        return ("onedrive", "medium")
    if "dropbox.com" in netloc:
        return ("dropbox", "medium")

    if "github.com" in netloc or "raw.githubusercontent" in netloc:
        if any(k in full for k in ("/releases/", "/raw/", "/blob/", "/assets/")):
            return ("github", "high")
        return ("github", "low")

    if any(x in netloc for x in ("gitlab.com", "bitbucket.org")):
        if any(k in full for k in ("/releases/", "/raw/", "/blob/")):
            return ("vcs", "high")

    if "community.powerbi.com" in netloc or "community.fabric.microsoft.com" in netloc:
        return ("pbi_community", "high")

    if any(d in netloc for d in ASSET_DOMAINS):
        return (f"other_{netloc.split('.')[0]}", "low")

    return None


def scan_file(filepath: Path, verbose: bool = False) -> list[dict]:
    """Return download links found in a single .md file."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        print(f"  WARNING: could not read {filepath.name}: {e}", file=sys.stderr)
        return []

    urls  = URL_RE.findall(text)
    links = []
    seen  = set()

    for url in urls:
        if url in seen:
            continue
        # Heuristic: .pbix-named files almost certainly host PBIX on Drive/OneDrive
        if ".pbix" in filepath.name.lower() and GDRIVE_RE.match(url):
            links.append({
                "url": url,
                "kind": "google_drive",
                "confidence": "medium (heuristic: .pbix filename)",
            })
            seen.add(url)
            continue
        # Normal classification
        classified = classify_link(url)
        if classified:
            kind, conf = classified
            links.append({"url": url, "kind": kind, "confidence": conf})
            seen.add(url)
        elif verbose:
            links.append({"url": url, "kind": "other", "confidence": "n/a"})
            seen.add(url)

    return links


def main():
    parser = argparse.ArgumentParser(description="Scan inbox .md files for downloadable asset links.")
    parser.add_argument("file", nargs="?", help="Scan a specific file instead of all inbox files")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show all URLs (including non-download)")
    args = parser.parse_args()

    INBOX = Path("C:/Users/krlsa/Documents/00 Projects/The Vault/00.Inbox")
    if not INBOX.exists():
        print(f"ERROR: Inbox not found at {INBOX}", file=sys.stderr)
        return 1

    files = [Path(args.file)] if args.file else sorted(INBOX.glob("*.md"))

    all_results = {}
    for f in files:
        links = scan_file(f, verbose=args.verbose)
        if not args.verbose:
            links = [l for l in links if l["confidence"] != "n/a"]
        if links:
            all_results[f.name] = links

    if not all_results:
        print("No download links found.")
        return 0

    total_files = len(all_results)
    total_links = sum(len(v) for v in all_results.values())

    print(f"Download links found in {total_files} file(s) ({total_links} link(s))\n")
    print(f"{'File':<55} {'Kind':<18} {'Confidence':<28} URL")
    print("-" * 130)
    for fname, links in all_results.items():
        for link in links:
            print(f"{fname:<55} {link['kind']:<18} {link['confidence']:<28} {link['url']}")

    print(f"\n{total_files} file(s), {total_links} download link(s).")
    print("\nNOTE: Google Drive / OneDrive links are share links — file type")
    print("      cannot be determined from the URL. Visit to confirm before downloading.")
    return 1  # non-zero so hooks/CI can detect findings


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Scan Attachments/ for video files with no matching transcription note."""

import re, sys
from pathlib import Path

VAULT = Path("C:/Users/krlsa/Documents/00 Projects/The Vault")
ATTACH = VAULT / "99.System/Attachments"
TRANSCRIPT_DIR = VAULT / "99.System/InboxArchive/_VideoTranscripts"
VIDEO_EXTS = {".mp4", ".mkv", ".webm", ".avi", ".mov", ".wmv", ".flv", ".m4v"}

transcribed = {}
if TRANSCRIPT_DIR.exists():
    for f in TRANSCRIPT_DIR.rglob("*"):
        if f.is_file() and f.suffix == ".md":
            transcribed[f.stem.lower()] = f.relative_to(VAULT)

# Build skip set from _video-checked.md registry
checked = set()
checked_file = ATTACH / "_video-checked.md"
if checked_file.exists():
    for line in checked_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            checked.add(line.split("|")[0].strip())

unmatched = []

for item in ATTACH.glob("*"):
    videos = []
    if item.is_file() and item.suffix.lower() in VIDEO_EXTS:
        videos = [item]
    elif item.is_dir():
        videos = [vf for vf in item.rglob("*") if vf.is_file() and vf.suffix.lower() in VIDEO_EXTS]
    for vf in videos:
        # Skip if in checked registry — normalize to forward slashes
        rel = str(vf.relative_to(VAULT)).replace("\\", "/")
        if rel in checked:
            continue
        vid_stem = re.sub(r"[-_]+", " ", vf.stem.lower())
        vid_slug = re.sub(r"\s+", "-", vid_stem)
        matched = any(vid_slug in t or t in vid_slug or vid_stem in t for t in transcribed)
        if not matched:
            unmatched.append(str(vf.relative_to(VAULT)))

if unmatched:
    print(f"{len(unmatched)} unmatched video(s) found:")
    for v in sorted(unmatched):
        print(f"  * {v}")
    sys.exit(1)
else:
    print("No missed videos found.")
    sys.exit(0)

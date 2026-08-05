import os, re
from pathlib import Path

fname = next(f for f in os.listdir('00.Inbox') if 'Best Practice' in f)
print('Disk:', repr(fname))

# The note source field is corrupted: source: ""Why I Stopped Writing "Best Practice"...
# Fix: replace the entire source line with source: 'Why I Stopped Writing – Best Practice...'
# Use single-quotes, and the inner double-quotes become literal chars
fixed_source = fname.replace('"Best Practice"', '\u2014 Best Practice')
print('Fixed source:', repr(fixed_source))

src_dir = Path('01.Knowledge/DAX Code/Wiki')
for n in src_dir.glob('tejwani-dax-content-critique*'):
    text = n.read_text(encoding='utf-8')
    # Replace the corrupted source: line
    lines = []
    for line in text.split('\n'):
        if line.startswith("source: '"):
            lines.append(f"source: '{fixed_source}'")
            print(f'  Fixed: {n.name}')
        else:
            lines.append(line)
    n.write_text('\n'.join(lines), encoding='utf-8')

# Fix _INGESTED.md
ingested = Path('00.Inbox/_INGESTED.md')
content = ingested.read_text(encoding='utf-8')
content = re.sub(r'\n- source: [^\n]+\n  archived: 2026-08-01', '', content)
entry = f'\n- source: "{fname}"\n  archived: 2026-08-01\n'
content = content.rstrip() + entry
ingested.write_text(content, encoding='utf-8')
print('Registry fixed')

# Run safe_archive
import subprocess, sys
r = subprocess.run(
    [sys.executable, '99.System/Scripts/safe_archive.py', fname],
    capture_output=True, text=True, cwd=str(Path.cwd())
)
print('Archive stdout:', r.stdout[:400])
print('Archive stderr:', r.stderr[:200])
print('Archive exit:', r.returncode)

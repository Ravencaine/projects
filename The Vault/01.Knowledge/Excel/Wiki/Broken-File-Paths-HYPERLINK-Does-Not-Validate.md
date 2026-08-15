---
created: 2026-08-09
updated: 2026-08-09
source: "Excel HYPERLINK function • My Online Training Hub"
note_type: gotcha
tags: [excel, hyperlink, broken-link, file-path, validation, no-error, missing-file, path-check, testing]
---

# Broken File Paths — HYPERLINK Does Not Validate Existence

HYPERLINK accepts any text string as a link_location and does not check whether the referenced file or folder actually exists. A broken path produces a clickable link that leads nowhere — Excel gives no warning or error.

## The Problem

```
=HYPERLINK("C:\Reports\Q4.xlsx", "Q4 Report")
```

This formula looks valid but will produce a broken link if `Q4.xlsx` has been moved, renamed, or deleted. Excel will not indicate the file is missing — the link simply fails to open anything when clicked.

## Why No Error

HYPERLINK's link_location is a string. Excel treats it as text and creates a clickable link. There is no built-in validation step that checks the filesystem.

## What to Do

1. **Always test links manually** before sharing the file
2. Use OneDrive/SharePoint paths for shared files — they provide sync validation
3. Consider wrapping with IFERROR only if the link_location itself can be missing — but IFERROR does not detect broken paths, only formula errors
4. Keep file paths relative to a known root folder where possible
5. Store source files in a consistent location and document the path structure

## Key Insight

> Excel won't tell you if a URL is broken.

This applies equally to file paths. Treat link testing as a mandatory step before distributing any workbook with HYPERLINK-based navigation.

## Related

- [[Source-HYPERLINK-Function-Mynda-Treacy]] — source
- [[File-Folder-Hyperlinks]] — file and folder HYPERLINK use cases; this gotcha applies to both

---
created: 2026-08-09
updated: 2026-08-09
source: "Excel HYPERLINK function • My Online Training Hub"
note_type: reference
tags: [excel, hyperlink, file-link, folder-link, path, onedrive, sharepoint, external, shortcut]
---

# File and Folder Hyperlinks via HYPERLINK

HYPERLINK works with local file paths and folder paths, not just URLs. Use it to create an Excel-based hub that opens related files and folders with a single click.

## Syntax

```
=HYPERLINK("C:\path\to\file.ext", "Display Text")
=HYPERLINK("C:\path\to\folder\", "Open Folder")
```

## Examples

| Type | Formula | Display |
|------|---------|---------|
| PDF file | `=HYPERLINK("C:\Project\Specs.pdf", "Customer Requirements")` | Customer Requirements |
| Word doc | `=HYPERLINK("C:\Reports\Q1.docx", "Q1 Report")` | Q1 Report |
| Folder | `=HYPERLINK("C:\Reports\", "Open Reports Folder")` | Open Reports Folder |
| Excel file | `=HYPERLINK("C:\Data\Raw.xlsx", "Raw Data")` | Raw Data |

## Shared Workbooks — Use OneDrive or SharePoint Paths

For workbooks shared across a team (stored on OneDrive or SharePoint), use the cloud path instead of a local path:

```
=HYPERLINK("https://company.sharepoint.com/sites/Project/Deliverables/Specs.pdf", "Specifications")
```

This ensures everyone on the team can open the same links regardless of where the file is stored on their own device.

## Use Cases

- Project hub: single Excel file linking to all related documents, contracts, images
- Team resource centre: links to shared folders and key files
- Report dashboard: clickable shortcuts to underlying data files

## Related

- [[Source-HYPERLINK-Function-Mynda-Treacy]] — source
- [[Broken-File-Paths-HYPERLINK-Does-Not-Validate]] — HYPERLINK does not check if the path is valid or the file exists

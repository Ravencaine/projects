---
created: 2026-08-09
updated: 2026-08-09
source: "Excel HYPERLINK function • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-hyperlink-function"
published: 2025-11-11
note_type: source
tags: [excel, hyperlink, navigation, dynamic-link, xlookup, cell-function, toc, internal-link, external-link, friendly-name]
---

# Excel HYPERLINK Function — My Online Training Hub / Mynda Treacy

Source: My Online Training Hub. Published 2025-11-11. Author: Mynda Treacy — already in vault (10th source).

## Summary

Four use cases for the HYPERLINK function: (1) clean URLs with friendly names, (2) Table of Contents for sheet navigation, (3) file and folder shortcuts, (4) dynamic row-jumping via XLOOKUP + CELL("address"). Two gotchas: HYPERLINK does not validate file existence, and Ctrl+K creates static links that differ from formula-based dynamic links.

## HYPERLINK Syntax

```
=HYPERLINK(link_location, [friendly_name])
```

| Argument | Description |
|----------|-------------|
| link_location | URL, file path, or internal cell reference |
| friendly_name | Optional display text (defaults to link_location if omitted) |

## Four Use Cases

| # | Use Case | Link Pattern | Example friendly_name |
|---|---------|-------------|---------------------|
| 1 | Clean URLs | Web URL | "View Report" |
| 2 | Sheet TOC | `#&sheetName&!A1` | "North Report" |
| 3 | File/folder | `C:\path\file.ext` | "Customer Requirements" |
| 4 | Dynamic row | `#"&CELL("address", XLOOKUP(...))` | "Go to Order-1234" |

## Key Insights Extracted

- [[HYPERLINK-Syntax-Sheet-Name-Quoting]] — `reference` — `#"&sheet&!A1"` pattern; single quotes around sheet names with spaces; best practice to always include quotes
- [[CELL-address-Dynamic-Cell-Reference-Retrieval]] — `atomic` — `CELL("address", ref)` returns absolute address string of a cell; used to build dynamic HYPERLINK targets
- [[Sheet-Navigation-TOC-HYPERLINK]] — `pattern` — `HYPERLINK("#"&C6&"!A1", C6&" Report")`; sheet name cell + # prefix + A1 target; Table of Contents for multi-sheet workbooks
- [[File-Folder-Hyperlinks]] — `reference` — direct paths to files and folders; OneDrive/SharePoint paths for shared workbooks
- [[Dynamic-Hyperlink-XLOOKUP-CELL]] — `pattern` — `HYPERLINK("#"&CELL("address", XLOOKUP(...)), "Go to "&orderID)`; dynamic jump to matching row in a table
- [[Broken-File-Paths-HYPERLINK-Does-Not-Validate]] — `gotcha` — HYPERLINK accepts any path string; does not check if file/folder exists; always test links
- [[CtrlK-Static-vs-Formula-Dynamic-Hyperlink]] — `gotcha` — Ctrl+K inserts a static hyperlink object; formula-based HYPERLINK is dynamic and updates with data; do not confuse the two

## Author

- [[Author-Mynda-Treacy]] — extended (10th source)

---
created: 2026-08-09
updated: 2026-08-09
source: "Excel HYPERLINK function • My Online Training Hub"
note_type: pattern
tags: [excel, hyperlink, table-of-contents, toc, sheet-navigation, navigation, internal-link, hash-prefix, multi-sheet]
---

# Sheet Navigation TOC via HYPERLINK + #

`=HYPERLINK("#"&C6&"!A1", C6&" Report")` creates a clickable Table of Contents for a multi-sheet workbook. The `#` prefix makes it an internal link; the sheet name cell drives the destination dynamically.

## Formula

```
=HYPERLINK("#"&C6&"!A1", C6&" Report")
```

| Part | Value | Purpose |
|------|-------|---------|
| `"#"` | Literal | Marks as internal link within this workbook |
| `C6` | Sheet name cell | Dynamic — the TOC row's sheet name |
| `"!A1"` | Target cell | Landing cell on the destination sheet |
| `C6&" Report"` | Friendly name | Display text, e.g. "North Report" |

## Setup

1. Create a TOC sheet with a column of sheet names (e.g. C6 = "North", C7 = "South")
2. Use the formula in the adjacent column — sheet name drives the link destination
3. Each row links to the corresponding sheet

## With Single Quotes (for Spaces)

```
=HYPERLINK("#'"&C6&"'!A1", C6&" Report")
```

Best practice: always include single quotes around the sheet name to avoid breakage if the name changes to include a space.

## Navigation Buttons Alternative

For a visual approach:
1. Insert → Shape (rounded rectangle) → type the sheet name
2. Ctrl+K → "Place in This Document" → select the target sheet
3. Repeat for each sheet
4. Colour-code shapes to show the currently selected sheet

Combine with hidden sheet tabs (File → Options → Advanced → Display options → untick Show sheet tabs) for a sleek controlled dashboard experience.

## Related

- [[Source-HYPERLINK-Function-Mynda-Treacy]] — source
- [[HYPERLINK-Syntax-Sheet-Name-Quoting]] — single-quote quoting for sheet names with spaces
- [[Dynamic-Hyperlink-XLOOKUP-CELL]] — dynamic HYPERLINK targeting a specific row rather than a sheet landing cell

---
created: 2026-08-09
updated: 2026-08-09
source: "Excel HYPERLINK function • My Online Training Hub"
note_type: reference
tags: [excel, hyperlink, syntax, quote, sheet-name, single-quote, link-location, friendly-name, best-practice]
---

# HYPERLINK Syntax and Sheet-Name Quoting

`=HYPERLINK(link_location, [friendly_name])` — HYPERLINK accepts URLs, file paths, and internal cell references. Sheet name references with spaces or special characters must be wrapped in single quotes.

## Syntax

```
=HYPERLINK(link_location, [friendly_name])
```

| Argument | Required | Description |
|----------|---------|-------------|
| link_location | Yes | URL, file path, or internal cell/sheet reference |
| friendly_name | No | Display text (defaults to link_location if omitted) |

## Internal Sheet Links

| Scenario | Formula | Notes |
|---------|---------|-------|
| No spaces in sheet name | `=HYPERLINK("#SheetName!A1", "Go")` | Works without quotes |
| Spaces or special chars | `=HYPERLINK("#'Sales Data'!A1", "Go")` | Single quotes required |
| Best practice | `=HYPERLINK("#'"&C6&"'!A1", "Go")` | Always quote via concatenation |

## Why Single Quotes Around Sheet Names

Excel requires sheet names with spaces or special characters (spaces, hyphens, ampersands, etc.) to be enclosed in single quotes in cell references. The `#` prefix indicates an internal link within the workbook.

## Best Practice: Always Quote

It is good practice to always wrap the sheet name in single quotes, even when no spaces are present. This avoids silent breakage if the sheet name is later changed to include a space.

## Related

- [[Source-HYPERLINK-Function-Mynda-Treacy]] — source
- [[Sheet-Navigation-TOC-HYPERLINK]] — practical TOC pattern using this quoting
- [[Dynamic-Hyperlink-XLOOKUP-CELL]] — dynamic row-jumping using the same internal link pattern

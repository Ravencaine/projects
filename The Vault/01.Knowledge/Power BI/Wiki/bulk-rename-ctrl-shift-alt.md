---
created: 2026-08-11
updated: 2026-08-11
source: "11-Power-BI-Tips-Guy-in-a-Cube-Transcript.md"
note_type: snippet
tags: [power-bi, dax, dax-editor, snippet]
---

# Bulk Rename with Ctrl+Shift+Alt in Tabular Editor

Tabular Editor or DAX formula bar: select multiple measures → Ctrl+Shift+Alt → type replacement text → Apply. All selected measures with matching text are renamed in one operation.

## Usage

```txt
# In Tabular Editor or DAX formula bar:
Select: [AVG Revenue], [AVG Cost], [AVG Units]
Ctrl+Shift+Alt → replace "AVG" with "Average"
Result: [Average Revenue], [Average Cost], [Average Units]
```

## Warning

If the replacement text appears inside other words within the name, those are also replaced. e.g. replacing "AVG" won't affect "SAVINGS" but replacing "Revenue" would catch "RevenueTotal" if that text exists inside a measure name. Verify exact match before applying.

## Related

- [[tabular-editor-bulk-edit-measures]] — multi-select for format, display folders in Model view

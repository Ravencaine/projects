---
created: 2026-08-09
updated: 2026-08-09
source: "Build an Automated Excel Database • My Online Training Hub"
note_type: atomic
tags: [excel, unique, counta, duplicate-detection, warning, banner, excel-table, aggregate]
---

# COUNTA(UNIQUE(...)) <> COUNTA(...) Warning Banner

`=IF(B6="","",IF(COUNTA(UNIQUE(ClientData[Email]))<>COUNTA(ClientData[Email]),"⚠️ Duplicate Customers Exist",""))` placed in a banner cell detects whether the table contains duplicate values and displays a warning.

## Formula

```
=IF(B6="","",
  IF(COUNTA(UNIQUE(ClientData[Email]))<>COUNTA(ClientData[Email]),
    "⚠️ Duplicate Customers Exist",
  ""))
```

## How It Works

| Step | Expression | Result |
|------|-----------|--------|
| 1 | `UNIQUE(ClientData[Email])` | Distinct email values from the table |
| 2 | `COUNTA(UNIQUE(...))` | Count of distinct emails |
| 3 | `COUNTA(ClientData[Email])` | Total count of all emails |
| 4 | `<>` | Not equal → TRUE if any duplicates exist |
| 5 | Outer IF | Shows warning only when B6 is not empty |

## The Pattern

```
COUNTA(UNIQUE(column)) <> COUNTA(column)
```

This is a generic duplicate-detection pattern: if the count of unique values does not equal the total count, duplicates exist.

## Display Layer

The banner is placed in a prominent cell. Conditional formatting applied to the banner cell (red fill + white text) makes the warning stand out visually.

## Related

- [[Source-Automated-Excel-Database-Mynda-Treacy]] — source
- [[XMATCH-for-Form-Level-Duplicate-Detection]] — form-level duplicate detection (proactive, pre-entry); this banner detects duplicates post-entry

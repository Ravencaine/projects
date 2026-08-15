---
created: 2026-08-09
updated: 2026-08-09
source: "Excel HYPERLINK function • My Online Training Hub"
note_type: pattern
tags: [excel, hyperlink, dynamic, xlookup, cell-address, row-jump, navigation, hash-prefix, internal-link, order, lookup]
---

# Dynamic Hyperlink to Matching Row via HYPERLINK + XLOOKUP + CELL

`=HYPERLINK("#"&CELL("address", XLOOKUP(D6, Orders[OrderID], Orders[OrderID])), "Go to "&D6)` — a dynamic HYPERLINK that jumps directly to the row matching a lookup value. Combine with a dropdown of Order IDs for a one-click row-jump navigation system.

## Formula

```
=IFERROR(
  HYPERLINK(
    "#"&CELL("address",
      XLOOKUP(D6, Orders[OrderID], Orders[OrderID])
    ),
    "Go to "&'Dynamic Hyperlinks'!D6
  ),
"Order not found")
```

## How It Works

| Step | Expression | Result |
|------|-----------|--------|
| 1 | `XLOOKUP(D6, Orders[OrderID], Orders[OrderID])` | Returns the cell containing the matching Order ID |
| 2 | `CELL("address", ...)` | Converts that cell reference to an absolute address string, e.g. `$A$47` |
| 3 | `"#"&...` | Makes it an internal link within the workbook |
| 4 | `HYPERLINK(...)` | Creates a clickable link using the resolved address |
| 5 | `IFERROR(...)` | Returns "Order not found" if XLOOKUP finds nothing |

## Architecture

```
┌─────────────────────────┐
│ D6: Order ID dropdown   │  (e.g. "ORD-1234")
└────────────┬────────────┘
             │ XLOOKUP
             ▼
┌─────────────────────────┐
│ Orders[OrderID] column  │  → finds the row containing ORD-1234
└────────────┬────────────┘
             │ CELL("address", ...)
             ▼
┌─────────────────────────┐
│ $A$47 (address string)  │  → the cell's absolute address
└────────────┬────────────┘
             │ "#"&...
             ▼
┌─────────────────────────┐
│ HYPERLINK(...)          │  → clickable: "Go to ORD-1234"
└─────────────────────────┘
```

## Friendly Name

The display text is `"Go to "&D6` — combines the literal text with the selected Order ID. For example: "Go to ORD-1234".

## Related

- [[Source-HYPERLINK-Function-Mynda-Treacy]] — source
- [[CELL-address-Dynamic-Cell-Reference-Retrieval]] — CELL("address") is the bridge between the lookup result and the HYPERLINK text argument
- [[XLOOKUP-AutoFill-Related-Data-from-Dropdown]] — same author; XLOOKUP in a related context (auto-fill from dropdown); cross-link

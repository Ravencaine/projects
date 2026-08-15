---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Drop-Down Lists in Excel • My Online Training Hub"
note_type: atomic
tags: [excel, filter, unique, sort, exclude, exclude-items, discontinued, active, dropdown]
---

# FILTER + UNIQUE + SORT for Excluding Dropdown Items

`=SORT(UNIQUE(FILTER(ProductsTbl[Product], ProductsTbl[Status]="Active", "")))` generates a dropdown list that excludes items by a condition (e.g. only Active products, not Discontinued). No manual list maintenance needed.

## Formula

```
=SORT(UNIQUE(FILTER(ProductsTbl[Product], ProductsTbl[Status]="Active", "")))
```

| Step | Expression | Output |
|------|-----------|--------|
| 1 | `ProductsTbl[Status]="Active"` | TRUE/FALSE array |
| 2 | `FILTER(ProductsTbl[Product], ...)` | Only products where Status = Active |
| 3 | `UNIQUE(...)` | Distinct products |
| 4 | `SORT(...)` | Alphabetically sorted |

## Why Not Two Lists

Maintaining two separate lists (Active products + Discontinued products) doubles maintenance effort. One source list with a FILTER condition means adding a product defaults to the active list unless explicitly marked Discontinued.

## Combine with XLOOKUP

Pair the filtered dropdown with XLOOKUP to auto-fill related details (price, stock level):
```
=XLOOKUP(ProductCell, ProductsTbl[Product], ProductsTbl[Price], "")
```

## Related

- [[Source-Dynamic-Drop-Down-Lists-Mynda-Treacy]] — source
- [[FILTER-Boolean-AND-OR-Logic]] — FILTER's boolean logic; extend with AND conditions to exclude multiple statuses

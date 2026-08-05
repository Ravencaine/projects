---


title: "DISTINCTCOUNT"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, aggregation]
note_type: function
description: "DISTINCTCOUNT — counts unique values in a column. Handles blank values. More efficient than COUNTROWS(DISTINCT()). From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# DISTINCTCOUNT

Counts the number of unique values in a column.

## Syntax

```
DISTINCTCOUNT( <column> )
```

## Arguments

| Argument | Description |
|----------|-------------|
| `column` | The column to count unique values from |

## Behavior

- Counts each **unique value once**, regardless of how many times it appears
- Includes blank values in the count (unless filtered)
- Commonly used for counting distinct customers, products, transactions, etc.

## Example

```dax
-- Count of distinct customers who made a purchase
Distinct Customers :=
DISTINCTCOUNT( 'Sales'[CustomerID] )
```

## DISTINCTCOUNT vs. COUNTROWS(DISTINCT())

| Approach | Example |
|----------|---------|
| `DISTINCTCOUNT` | `DISTINCTCOUNT( Sales[ProductID] )` — native, efficient |
| `COUNTROWS(DISTINCT())` | `COUNTROWS( DISTINCT( Sales[ProductID] ) )` — equivalent but less efficient |

DISTINCTCOUNT is the preferred approach — it's purpose-built and faster.

## Related Functions

- `COUNT` — counts non-blank values (includes duplicates)
- `COUNTROWS` — counts all rows (including duplicates)
- `DISTINCT()` — returns the distinct values as a table (use in CALCULATETABLE)

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

---


title: "COUNTROWS"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, aggregation]
note_type: pattern
description: "COUNTROWS — count rows in a table or after a filter. Used in DAX KPIs, denominator in DIVIDE patterns, and row-count filters. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# COUNTROWS

Counts the number of rows in a table — either the entire table or a filtered subset.

## Syntax

```
COUNTROWS( <table> )
```

## Arguments

| Argument | Description |
|----------|-------------|
| `table` | A table reference, or an expression that returns a table (e.g., `FILTER(...)`) |

## Behavior

- Counts all rows **including** those with blank values
- Commonly used as the denominator in a `DIVIDE` pattern to calculate ratios
- Often used in KPI numerators

## Common Pattern: Ratio with COUNTROWS

```dax
-- Percentage of orders with discount
Discount% :=
DIVIDE(
    COUNTROWS( FILTER( 'Sales', 'Sales'[Discount] > 0 ) ),
    COUNTROWS( 'Sales' )
)
```

## Related Functions

- `COUNT` — counts non-blank values in a column
- `DISTINCTCOUNT` — counts unique values
- `COUNTA` — counts non-blank (includes text)
- `COUNTBLANK` — counts blank cells
- `COUNTROWS( DISTINCT( ... ) )` — count unique (less efficient than DISTINCTCOUNT)

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

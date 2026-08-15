---
created: 2026-08-09
updated: 2026-08-09
source: "DAX X Functions in Power BI Explained.md"
source_url: https://databear.com/dax-x-functions-power-bi/
note_type: source
tags: [dax, x-functions, iterator, sumx, averagex, minx, maxx, concatenatex, row-context, virtual-table, databear, boniface-muchendu]
---

# DAX X Functions in Power BI Explained

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2026-01-19
> **URL:** https://databear.com/dax-x-functions-power-bi/
> **Routed to:** DAX Code

## Summary

X functions iterate over a table expression row-by-row (row context), evaluate a calculation per row, then aggregate. Core concept: virtual table created per iteration. Covers SUMX, AVERAGEX, MINX, MAXX, CONCATENATEX with practical examples including CONCATENATEX for displaying filter context.

## Key Claims

### How X Functions Work
- X = row context: evaluates expression for each row in a virtual table before aggregating
- Virtual table: temporary invisible table created by DAX per iteration
- Unlike column aggregators (SUM, AVERAGE): X functions process row expressions
- Use DIVIDE not `/` to avoid errors on zero denominators

### Common X Functions

| Function | Returns |
|----------|---------|
| `SUMX` | Sum over table expression |
| `AVERAGEX` | Average of row-by-row expression |
| `MINX` / `MAXX` | Min/max from evaluated rows |
| `CONCATENATEX` | Concatenates text with delimiter |

### Real-World Example: Average Sale Per Unit
```dax
Average Sale Amount per Unit =
AVERAGEX(
    'Internet Sales',
    DIVIDE('Internet Sales'[SalesAmount], 'Internet Sales'[OrderQuantity])
)
```
Averages per transaction vs per unit — X functions get the unit-level average.

### CONCATENATEX for Filter Context
```dax
Colors Filtered =
VAR SelectedColors = VALUES('Product'[Color])
VAR TotalColors = CALCULATETABLE(VALUES('Product'[Color]), ALL('Product'))
VAR ColorList = CONCATENATEX(SelectedColors, 'Product'[Color], ", ")
RETURN
    IF(
        COUNTROWS(SelectedColors) = COUNTROWS(TotalColors),
        "All Colors",
        ColorList
    )
```
Displays "All Colors" when no filter active, comma-separated list otherwise. Used in card visuals, titles, labels.

### Use Cases
- Weighted averages
- Aggregations based on calculated columns
- Dynamic KPIs / benchmarks
- Displaying selected values in readable format
- Row-by-row logic with full control

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX X Functions in Power BI Explained.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |

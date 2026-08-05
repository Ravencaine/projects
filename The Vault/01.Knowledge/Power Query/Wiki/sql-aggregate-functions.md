---


title: "SQL Aggregate Functions"
created: 2026-07-28
updated: 2026-08-02
tags: [sql, reference, pattern]
note_type: reference
description: "SQL aggregate functions — COUNT, SUM, MIN, MAX, AVG. With GROUP BY examples. From Dunlop Chapter 5."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# SQL Aggregate Functions

## Functions

| Function | Returns |
|----------|---------|
| `COUNT(*)` | Number of non-empty rows matching condition |
| `SUM(column)` | Sum of all values in column |
| `MIN(column)` | Lowest value |
| `MAX(column)` | Highest value |
| `AVG(column)` | Arithmetic mean |

## Examples

```sql
-- Count all rows
SELECT COUNT(*) FROM offices

-- Count rows matching a condition
SELECT COUNT(*) FROM offices WHERE region = 'CH'

-- Sum of all sales
SELECT SUM(sales) FROM offices

-- Sum with condition
SELECT SUM(sales) FROM offices WHERE region = 'CH'
```

## GROUP BY Aggregates

```sql
-- Subtotals by region
SELECT region, COUNT(*) FROM offices GROUP BY region

-- Sum by region
SELECT region, SUM(sales) FROM offices GROUP BY region
```

## Source Reference

Chapter 5, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

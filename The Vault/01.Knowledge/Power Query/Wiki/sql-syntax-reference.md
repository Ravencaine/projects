---


title: "SQL Syntax Reference"
created: 2026-07-28
updated: 2026-08-02
tags: [sql, reference, pattern]
note_type: reference
description: "SQL SELECT syntax reference — clauses, aggregate functions, equijoin, GROUP BY, HAVING, ORDER BY. From Dunlop Chapter 5."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# SQL Syntax Reference

Standard SQL SELECT statement structure as used in PowerPivot/Excel SQL queries.

## Syntax

```sql
SELECT [DISTINCT] <columns>
FROM <table(s)>
[WHERE <condition>]
[GROUP BY <column expression>]
[HAVING <group filter condition>]
[ORDER BY <sort expression>]
```

## Clause Reference

| Clause | Purpose |
|--------|---------|
| `SELECT` | Names columns or expressions to return. Use `*` for all columns. |
| `FROM` | Specifies table(s). Multiple tables without WHERE = Cartesian product. |
| `WHERE` | Row-level filter. Also specifies JOIN condition (equijoin). |
| `GROUP BY` | Groups rows for aggregation (SUM, COUNT, etc.) |
| `HAVING` | Filters groups after aggregation (unlike WHERE, which filters rows) |
| `ORDER BY` | Sorts result set. ASC (default) or DESC. |

## Field Alias with AS

```sql
SELECT SUM(sales) AS TotalSales
FROM offices
```

## Square Brackets for Spaces

```sql
SELECT [last name], [unit price]
FROM employees
```

## Table Qualifiers

When fields from multiple tables share names, qualify with table name:

```sql
SELECT employees.id, orders.[employee id]
FROM employees, orders
WHERE employees.id = orders.[employee id]
```

## Source Reference

Chapter 5, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

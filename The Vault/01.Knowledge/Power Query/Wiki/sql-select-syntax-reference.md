---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: reference
tags: [sql, reference, select, syntax, powerpivot]
---

# SQL SELECT Syntax: FROM, WHERE, GROUP BY, HAVING, ORDER BY

Complete reference for the SQL SELECT statement syntax used in the PowerPivot Table Import Wizard and MSQuery.

## Quick Reference

```sql
SELECT [DISTINCT] <column_list> [AS <alias>]
FROM <table_name(s)>
[WHERE <row_condition>]
[GROUP BY <column_expression>]
[HAVING <group_condition>]
[ORDER BY <sort_column> [ASC|DESC]]
```

## Clause Reference

| Clause | Purpose | Required |
|--------|---------|----------|
| `SELECT` | Names columns or expressions to return; `*` = all columns | Yes |
| `DISTINCT` | Eliminates duplicate rows from results | No |
| `AS` | Gives a column an alias in the output | No |
| `FROM` | Specifies the table(s) to query | Yes |
| `WHERE` | Row-level filter; links tables (equijoin) and/or excludes rows | No |
| `GROUP BY` | Groups rows for aggregation | No |
| `HAVING` | Filters groups (applied after GROUP BY) | No |
| `ORDER BY` | Sorts the result set | No |

## Decision Questions

| Clause | Question to Ask |
|--------|----------------|
| `SELECT` | What columns or expressions should be displayed? |
| `FROM` | In which table(s) are these columns? |
| `WHERE` | What conditions link the tables? What row-level filters are needed? |
| `GROUP BY` | What values define groups for aggregation (SUM, COUNT, etc.)? |
| `HAVING` | What group-level conditions should filter after aggregation? |
| `ORDER BY` | In what order should the result rows appear? |

## Examples

```sql
-- Basic filter
SELECT name, address FROM addrlist WHERE zip = "94704"

-- Multi-table with equijoin (link employees to orders)
SELECT employees.id, employees.[last name], orders.[employee id]
FROM employees, orders
WHERE employees.id = orders.[employee id]

-- Aggregate with GROUP BY
SELECT region, COUNT(*) FROM offices GROUP BY region
SELECT region, SUM(sales) FROM offices GROUP BY region

-- Three-table join (employees → orders → order details)
SELECT employees.[last name],
       SUM([order details].[unit price] * [order details].quantity) AS TotalValue
FROM employees, orders, [order details]
WHERE employees.id = orders.[employee id]
  AND orders.[order id] = [order details].[order id]
GROUP BY employees.[last name]
```

## Notes

- Field names with spaces must be enclosed in square brackets: `[last name]`
- Table names with spaces must be enclosed in single quotes: `'Order Details'`
- Cross-table field references use `tablename.fieldname` syntax
- When importing via the Table Import Wizard, omit the `FROM` table name if only one table is selected

## Related

- [[sql-equijoin-vs-cartesian-product]] — the critical WHERE JOIN condition
- [[sql-aggregate-functions]] — COUNT, SUM, MIN, MAX, AVG with GROUP BY
- [[powerpivot-data-model-load-access-diagram-view-relationships]] — PowerPivot as the visual counterpart to SQL imports

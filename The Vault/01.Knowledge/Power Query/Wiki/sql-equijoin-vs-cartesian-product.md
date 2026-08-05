---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [sql, join, equijoin, cartesian-product, cross-join]
---

# Equijoin in SQL: Cartesian Product vs. WHERE Clause Join

When querying multiple tables in the PowerPivot Table Import Wizard, omitting the WHERE join condition produces a Cartesian product — pairing every row of the first table with every row of the second. An equijoin uses a WHERE condition to match rows correctly.

## Purpose

Multi-table SQL queries in PowerPivot require an explicit join condition. Without it, every row from Table A is paired with every row from Table B — producing a result set size of A × B rows. An equijoin (equality-based join) restricts the pairing to rows where a key matches.

## Components

- Two or more tables with a shared key field
- `WHERE` clause with equality condition: `table1.key = table2.key`
- The shared field is typically a primary key (PK) / foreign key (FK) relationship

## Structure

```sql
-- WRONG: Cartesian product (every row × every row)
SELECT employees.id, employees.[last name], orders.[employee id]
FROM employees, orders
-- No WHERE clause: 9 employees × 48 orders = 432 rows (all paired)

-- CORRECT: Equijoin (only matching rows)
SELECT employees.id, employees.[last name], orders.[employee id]
FROM employees, orders
WHERE employees.id = orders.[employee id]
-- Returns: 48 rows (one per order, with the correct employee name)
```

## Example

Northwind employees → orders:
- Employees table: 9 rows
- Orders table: 48 rows
- **Without WHERE:** 9 × 48 = 432 rows (every employee paired with every order — meaningless)
- **With WHERE:** 48 rows (each order linked to its correct employee)

Three-table chain (employees → orders → order details):
```sql
SELECT employees.[last name],
       SUM([order details].[unit price] * [order details].quantity)
FROM employees, orders, [order details]
WHERE employees.id = orders.[employee id]
  AND orders.[order id] = [order details].[order id]
GROUP BY employees.[last name]
```

## Notes

- Dunlop's example: the Table Import Wizard imports relationships from Access automatically, but a custom SQL query bypasses those — you must specify the join manually
- Always verify row count: 432 rows from a 9×48 cross product is an immediate signal the WHERE clause is missing
- Field names with spaces: enclose in square brackets `[order id]`

## Related

- [[sql-select-syntax-reference]] — full SELECT syntax
- [[sql-aggregate-functions]] — aggregation on joined tables
- [[powerpivot-data-model-load-access-diagram-view-relationships]] — PowerPivot's visual relationship model (auto-detected joins)

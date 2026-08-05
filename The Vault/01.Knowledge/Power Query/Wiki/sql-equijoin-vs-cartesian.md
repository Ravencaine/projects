---


title: "SQL Equijoin vs Cartesian Product"
created: 2026-07-28
updated: 2026-08-02
tags: [sql, pattern, reference]
note_type: reference
description: "The critical importance of the WHERE JOIN condition — equijoin vs. Cartesian product. Every row from table A paired with every row from table B when WHERE is omitted. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# SQL Equijoin vs. Cartesian Product

When querying multiple tables in SQL, the WHERE clause is **not optional**: omitting it produces a Cartesian product.

## The Rule

```
With WHERE (equijoin):   9 employees × 48 orders → 48 rows (correct)
Without WHERE:            9 employees × 48 orders → 432 rows (Cartesian product)
```

## Correct Equijoin

```sql
SELECT employees.[last name], orders.[order id]
FROM employees, orders
WHERE employees.id = orders.[employee id]
```

Result: one row per order (correct).

## Cartesian Product (No WHERE)

```sql
SELECT * FROM employees, orders
```

Result: **every row from employees paired with every row from orders**. Both tables are fully crossed — 9 employees × 48 orders = 432 rows.

## Three-Table Join

```sql
SELECT employees.[last name],
       SUM([order details].[unit price] * [order details].quantity) AS TotalSales
FROM employees, orders, [order details]
WHERE employees.id = orders.[employee id]
  AND orders.[order id] = [order details].[order id]
GROUP BY employees.[last name]
```

Two relationships used to link three tables. The `orders` table is a **link table**: no fields from it are displayed.

## Source Reference

Chapter 5, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

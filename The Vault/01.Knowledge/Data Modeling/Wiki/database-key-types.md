---


title: "Database Key Types"
created: 2026-07-28
updated: 2026-08-02
tags: [data-modeling, concept]
note_type: pattern
description: "Database key types — primary key, candidate key, composite key, foreign key, source table, related table. From Dunlop Chapter 4."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Database Key Types

## Primary Key

A field (or fields) that **uniquely identifies** each record in a table. The go-to identifier for the table.

- For people data requiring tax reporting: Social Security Number (SSN)
- Must be unique and non-null
- One primary key per table

## Candidate Key

Any field (or combination of fields) that can **uniquely identify any record** without referring to any other data.

- A table may have **multiple** candidate keys
- The primary key is the **best** among the candidates — chosen for brevity, stability, and predictability

## Composite Key

A primary key (or candidate key) made up of **more than one column**.

```sql
-- Example: composite key for an order line item
PRIMARY KEY (OrderID, LineItemID)
```

Both columns together guarantee uniqueness — neither column alone does.

## Foreign Key

A field (or fields) in **one table** that uniquely identifies a row in **another table**.

```
employees.dept  →  departments.deptcode
     ↑                  ↑
  foreign key         primary key
```

The foreign key points to the primary key of another table. Enables the relationship.

## Source Table vs. Related Table

| | Source Table | Related Table |
|--|--|--|
| Where the relationship starts | Yes | No |
| Contains the foreign key | Yes (typically) | No |
| Where lookup values come from | — | Yes |

In the employees/departments example: `employees` is the source, `departments` is the related table.

## Source Reference

Chapter 4, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

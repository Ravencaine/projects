---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
note_type: pattern
tags: [database-design, schema, migration, normalization, foreign-key, pattern]
---

# Database Schema First Migration Pattern

**Type:** Pattern · **KB:** Data Modeling · **Source:** [[source-excel-postgres-weekend-yadullah]]

Design the normalized schema **before** writing migration code. The schema design itself is the first data quality audit — it surfaces duplicates, inconsistencies, and missing relationships that flat-row spreadsheets hide. This step is skipped at the developer's peril.

## Why schema first

When you sketch actual tables (customers, orders, payments), you must:
- Define what each entity **is**
- Define what **relationships** exist between entities
- Define what **cannot be missing** (NOT NULL)
- Define what **must be unique** (UNIQUE)
- Define what **must reference another table** (FOREIGN KEY)

Each decision exposes data that doesn't fit. Before a single line of Python runs, years of accumulated bad data become visible.

## Schema design process

```
Flat spreadsheet (1 sheet, many columns)
    ↓
Entities identified (customers, orders, payments)
    ↓
Attributes assigned per entity
    ↓
Relationships defined (orders → customers via FK)
    ↓
Constraints defined (UNIQUE on email, NOT NULL on order_date)
    ↓
Data quality problems surface here
    ↓
Migration script written against clean schema
```

## Schema sketch example

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    order_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    invoice_paid BOOLEAN
);
```

## What goes wrong without schema first

- Migration script imports dirty data without cleaning it
- Bad data enters the database
- Postgres constraints could have caught it — but schema wasn't designed first
- Database inherits all the problems of the spreadsheet

## Related

- [[normalized-tables-vs-flat-rows]] — what schema design reveals about data
- [[postgres-constraint-enforcement]] — constraints defined during schema design
- [[excel-to-postgres-migration-workflow]] — full workflow including schema-first step

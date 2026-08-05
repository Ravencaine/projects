---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, referential-integrity, constraints, cloud-warehouse, query-optimization]
---

# Referential Integrity with RELY Constraint

Declare explicit FOREIGN KEY constraints with the `RELY` keyword in cloud data warehouses (Snowflake, Redshift, BigQuery). The `RELY` keyword tells the query planner it can safely eliminate unnecessary joins — dropping joins that do not affect the query result — for significant query acceleration.

## The Pattern

```sql
/* Explicit primary key */
ALTER TABLE dim_customer
    ADD CONSTRAINT pk_dim_customer
    PRIMARY KEY (customer_key);

/* Foreign key with RELY — activates RI for query optimization */
ALTER TABLE fact_sales_clustered
    ADD CONSTRAINT fk_sales_customer
    FOREIGN KEY (customer_key)
    REFERENCES dim_customer(customer_key)
    RELY;
```

## How RELY Works

Without RELY: the query planner assumes foreign key relationships may have violations (missing foreign key values), and must validate the join even when the join columns are not selected in the query.

With RELY: the planner trusts the constraint and can eliminate the join if the join columns are not needed for the result — reducing query scope.

## BI Tool Setting

In Power BI, the "Assume referential integrity" model option achieves the same result at the semantic layer:

| Setting | Effect |
|---|---|
| OFF | LEFT JOIN (validates every foreign key) |
| ON | INNER JOIN (trusts the relationship) |

Tested: with RELY + "Assume referential integrity" ON, a flat table query (12 seconds) vs star schema (0.8 seconds).

## Related

- [[star-schema-fact-table-principles]] — `atomic`
- [[star-schema-grain-locking-constraint]] — `pattern`

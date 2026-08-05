---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, grain, unique-constraint, data-quality, duplicate-prevention]
---

# Grain Locking with UNIQUE Constraint

Lock the grain of a fact table with an explicit UNIQUE constraint on the combination of columns that defines one row. This is the definitive enforcement mechanism for preventing silent duplicate counting — the most common and most invisible fact table defect.

## The Pattern

```sql
/* Lock the grain to prevent silent duplicate counting */
ALTER TABLE fact_sales_clustered
    ADD CONSTRAINT uq_sales_grain
    UNIQUE (transaction_id, product_id);
```

`transaction_id` + `product_id` is the grain: one product per transaction. No combination of these two values can appear twice in the table.

## Why Enforce at the Database

| Method | Protects Against |
|---|---|
| Business process documentation | Only as good as the process being followed |
| ETL deduplication logic | Only as good as the last ETL run |
| UNIQUE constraint | Database-enforced — duplicates rejected at insert time |

## Grain Declaration Best Practices

1. Document the grain in a comment on the table
2. Add a UNIQUE constraint in the DDL
3. Test with a known duplicate scenario before production
4. Include a check for duplicate grain violations in data quality monitoring

## Related

- [[star-schema-fact-table-principles]] — `atomic`
- [[star-schema-degenerate-dimensions]] — `pattern`

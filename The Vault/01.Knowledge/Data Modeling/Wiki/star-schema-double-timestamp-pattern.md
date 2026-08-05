---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, timestamp, late-data, data-quality, dual-timestamp]
---

# Double Timestamp Pattern

Store two separate date/time columns in a fact table — `order_date` (when the customer placed the order) and `warehouse_processing_date` (when the warehouse actually processed it). This prevents Black Friday and high-volume event data from breaking trends.

## The Problem

Tracking only `transaction_time` causes trend lines to spike artificially when processing backlog is cleared. Orders placed on Black Friday may not reach the warehouse until 3 days later — a single timestamp makes it impossible to separate actual sales timing from operational lag.

## Schema

```sql
CREATE TABLE fact_sales_optimized (
    order_date_key           INT NOT NULL,
    warehouse_processing_date_key INT NOT NULL,
    -- ...
    is_late_arrival         BOOLEAN DEFAULT FALSE,
    original_expected_date_key INT,
    -- ...
)
PARTITION BY order_date_key;
```

Two separate foreign keys to `dim_date` — one for the business event, one for the operational reality.

## Why It Matters

| Scenario | Single Timestamp | Double Timestamp |
|---|---|---|
| Black Friday backlog cleared after 3 days | Sales trend spikes when backlog clears | Sales trend stays accurate; backlog visible as late_arrival flag |
| Reporting on orders placed in October | Processing dates bleed into November | Filter by order_date_key for true sales reporting |
| Identifying operational bottlenecks | Not possible | Compare processing_date - order_date for lag analysis |

## Related

- [[star-schema-late-arrival-handling]] — `pattern`
- [[star-schema-fact-table-principles]] — `atomic`

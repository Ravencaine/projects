---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, late-arrival, data-quality, history-preservation]
---

# Late Arrival Handling

Late-arriving data is data that arrives after the reporting period has closed — orders placed in October that do not reach the warehouse until November, for example. Star schema fact tables must handle this without breaking historical trend accuracy.

## The Pattern

Two key columns handle late arrivals:

```sql
is_late_arrival         BOOLEAN DEFAULT FALSE,
original_expected_date_key INT,
```

- `is_late_arrival` — flags rows where `order_date_key` differs from `warehouse_processing_date_key`
- `original_expected_date_key` — tracks what the expected date would have been (for trend analysis of expected vs actual)

## Query Pattern for Accurate Historical Reporting

```sql
SELECT
    d.full_date AS reported_sales_date,
    COUNT(DISTINCT f.transaction_id) AS total_orders,
    SUM(f.normalized_usd_revenue) AS true_revenue,
    SUM(CASE WHEN f.is_late_arrival = TRUE
             THEN f.normalized_usd_revenue
             ELSE 0 END) AS late_arriving_revenue
FROM fact_sales_optimized f
INNER JOIN dim_date d ON f.order_date_key = d.date_key
WHERE f.warehouse_processing_date_key >= 20201101
GROUP BY d.full_date;
```

Reports auto-adjust to historical reality — late-arriving revenue is identified and reported against the correct original period.

## Related

- [[star-schema-double-timestamp-pattern]] — `pattern`
- [[star-schema-fact-table-principles]] — `atomic`

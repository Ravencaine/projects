---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [dax, pattern, non-additive-measures, fact-table, performance, additive, semantic-layer]
---

# Non-Additive Measures Audit

Non-additive measures are numeric fields that cannot be meaningfully summed across dimensions without additional logic. They silently cripple star schema performance — forcing the BI tool to recalculate on every aggregation. Most engineers miss them until dashboards run 10–100x slower than expected.

## What Makes a Measure Non-Additive

The test: **"Can I sum this across all dimensions without logic breaks?"**

| Additive | Non-Additive |
|---|---|
| `SUM(revenue)` | `AVG(price)` — sum of averages is meaningless |
| `SUM(units_sold)` | `AVG(order_value)` — sum of averages ≠ average |
| `SUM(quantity)` | `discount_rate` — sum of rates ≠ total rate |
| `SUM(total_cost)` | `profit_margin` — percentage of a sum |

## The Cost

Non-additive fields in a fact table force the semantic layer to recalculate on every query at every aggregation level. A "monthly average order value" report took 14 seconds — replaced with `SUM(order_total) / COUNT(orders)` in the semantic layer → **1.2 seconds**.

## Auto-Detection Query (Cloud Data Warehouse)

```sql
SELECT
    table_name,
    column_name,
    data_type
FROM information_schema.columns
WHERE table_name = 'fact_sales_clustered'
  AND data_type IN ('numeric', 'decimal', 'double precision', 'real')
  AND column_name NOT ILIKE '%count%'
  AND column_name NOT ILIKE '%total%'
  AND column_name NOT ILIKE '%sum%'
  AND column_name NOT ILIKE '%qty%';
```

Flags potential non-additive fields: numerics that don't contain count/total/sum/qty in the name.

## The Fix

Replace non-additive fields with their additive components:
- Replace `discount_rate` → `total_discounts`
- Replace `average_cost` → `total_cost` + `quantity`
- Calculate ratios at the semantic layer: `SUM(total_discounts) / SUM(sales_amount)`

## Related

- [[star-schema-fact-table-principles]] — `atomic`

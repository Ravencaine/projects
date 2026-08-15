---
created: 2026-08-09
updated: 2026-08-09
source: "Data Analysis Expressions (DAX) in Power BI.md"
note_type: atomic
tags: [dax, filter, performance, iterator, cardinality, fact-table, dimension-table]
---

# FILTER: Filter Dimension Tables, Not Fact Tables

When using `FILTER` inside CALCULATE, always apply it to the smallest table possible — typically a dimension table, not the fact table.

## Rule

```dax
-- SLOW: FILTER scans the fact table (millions of rows)
CALCULATE(
    [Sales Amount],
    FILTER('Sales', 'Sales'[Color] = "Red")
)

-- FAST: FILTER scans the dimension table (thousands of rows)
-- The relationship propagates the filter to the fact table efficiently
CALCULATE(
    [Sales Amount],
    FILTER('Product', 'Product'[Color] = "Red")
)
```

## Why

- `FILTER` iterates row-by-row over the table it receives
- Fact tables (Sales, Transactions) contain millions of rows — full scan is expensive
- Dimension tables (Product, Customer, Geography) contain thousands of rows — scan is fast
- The relationship between dimension and fact propagates the filter context efficiently

## Decision Matrix

| Table size | Example | FILTER suitable? |
|-----------|---------|-----------------|
| Fact (millions rows) | Sales, Transactions | No — too slow |
| Dimension (thousands rows) | Product, Customer, Date | Yes — use these |
| Bridge/lookup | Bridge tables | Only if small |

## Generalization

The same principle applies to any iterator used with CALCULATE:

```dax
-- Prefer filtering the dimension
CALCULATETABLE(
    'Product',
    FILTER('Product', 'Product'[Category] = "Electronics")
)
```

The relationship will handle the rest. Let the engine do the work it is optimized for.

## Related

- [[filter-context-vs-row-context]] — context foundations
- [[dax-performance-patterns]] — broader DAX performance patterns

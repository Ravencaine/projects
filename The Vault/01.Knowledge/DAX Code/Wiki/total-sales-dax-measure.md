---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: function
tags: [dax, power-bi, retail, sum, sales]
---

# Total Sales DAX Measure

Sums the Sales column across all rows in the fact table to produce total revenue.

## Signature

```dax
Total Sales := SUM ( Sales[Sales] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `Sales[Sales]` | Column | Numeric Sales column in the fact table |

## Returns

A single decimal value — total revenue across all transactions in the current filter context.

## Examples

```dax
Total Sales := SUM ( Sales[Sales] )

-- With filter context (e.g., specific year, region):
Total Sales YTD := TOTALYTD(
    [Total Sales],
    'Calendar'[Date]
)
```

## Notes

- `SUM` ignores rows filtered out by context (slicers, visuals, row-level filters).
- Always reference the fact table column, not a calculated column in the same table — this allows DAX to use the column's storage engine optimizations.
- For more complex scenarios (semi-additive measures, distinct counts), use `SUMX` instead.

## Related

- [[total-profit-dax-measure]] — `function`
- [[total-orders-dax-measure]] — `function`
- [[average-order-value-dax]] — `function`

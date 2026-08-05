---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: function
tags: [dax, power-bi, retail, profit, sum]
---

# Total Profit DAX Measure

Sums the Profit column to show net financial return after costs. Used alongside Total Sales to evaluate true business performance.

## Signature

```dax
Total Profit := SUM ( Sales[Profit] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `Sales[Profit]` | Column | Numeric Profit column (Sales minus COGS and deductions) |

## Returns

A single decimal value — total profit in the current filter context.

## Examples

```dax
Total Profit := SUM ( Sales[Profit] )

-- Profit Margin (ratio):
Profit Margin :=
    DIVIDE (
        [Total Profit],
        [Total Sales],
        BLANK()
    )
```

## Notes

- Profit values can be negative (loss) — `SUM` will return negative totals when most transactions are unprofitable.
- Pair with Total Sales in every visual and KPI card — never show profit without revenue for context.
- Profit Margin = Total Profit / Total Sales reveals the true efficiency of each product, category, or region.

## Related

- [[total-sales-dax-measure]] — `function`
- [[gross-margin-calculation-in-dax]] — `function`
- [[revenue-vs-profit-distinction]] — `atomic`

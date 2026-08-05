---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: pattern
tags: [power-bi, pattern, category, sales, profit, comparison]
---

# Category Comparison: Sales vs Profit

A side-by-side or clustered bar chart comparing Total Sales and Total Profit across product categories, revealing which categories generate revenue without proportional profit.

## Purpose

Exposes the critical gap between revenue and profit at the category level. High-sales categories that are low-profit require pricing review, discount strategy revision, or supplier cost negotiation.

## Components

- **Clustered bar chart** or **dual-axis combination chart**
- **Category** on the X-axis
- **Bars**: Total Sales (one colour), Total Profit (second colour)
- **Optional**: Profit Margin line overlay showing margin % per category

## Structure

```dax
Total Sales := SUM ( Sales[Sales] )
Total Profit := SUM ( Sales[Profit] )

Profit Margin :=
    DIVIDE (
        [Total Profit],
        [Total Sales],
        BLANK()
    )
```

## Example

| Category | Total Sales | Total Profit | Profit Margin |
|----------|-----------|--------------|--------------|
| Technology | $500,000 | $85,000 | 17% |
| Furniture | $400,000 | -$20,000 | -5% |
| Office Supplies | $300,000 | $15,000 | 5% |

Furniture is a revenue driver but a profit drain — discount or cost review needed.

## Variations

- **Waterfall chart**: shows contribution to total profit from each category
- **Scatter chart**: plot all products with Sales on X, Profit on Y, bubble size = Quantity — identifies outlier high-revenue, negative-profit products
- **Matrix with conditional formatting**: colour-code profit cells red/amber/green

## Related

- [[revenue-vs-profit-distinction]] — `atomic`
- [[executive-kpi-card-row]] — `pattern`
- [[product]] — `pattern`

---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: function
tags: [dax, power-bi, retail, aov, divide]
---

# Average Order Value (AOV) DAX Measure

Average revenue per customer order. A key metric for understanding purchasing behavior and evaluating pricing and cross-sell strategies.

## Signature

```dax
Average Order Value :=
    DIVIDE (
        [Total Sales],
        [Total Orders],
        BLANK()
    )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `[Total Sales]` | Measure | Sum of all sales revenue |
| `[Total Orders]` | Measure | Count of distinct orders |
| `BLANK()` | Value | Fallback when denominator is zero |

## Returns

A decimal value — average revenue per order in the current filter context.

## Examples

```dax
-- AOV by Customer Segment:
Average Order Value Segment :=
    DIVIDE (
        [Total Sales],
        [Total Orders],
        BLANK()
    )

-- AOV trend over time:
Average Order Value Monthly :=
    DIVIDE (
        [Total Sales],
        [Total Orders],
        BLANK()
    )
```

## Notes

- AOV increases when customers buy more per transaction — achieved through bundling, upselling, or minimum order thresholds.
- AOV is typically higher for Corporate segments than Consumer segments (business purchases are larger).
- Monitor AOV alongside Total Orders — if AOV rises but Total Orders falls, you may be alienating small customers.

## Related

- [[total-sales-dax-measure]] — `function`
- [[total-orders-dax-measure]] — `function`
- [[customer-segmentation-retail]] — `atomic`

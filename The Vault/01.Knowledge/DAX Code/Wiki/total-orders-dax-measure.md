---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: function
tags: [dax, power-bi, retail, count, orders]
---

# Total Orders DAX Measure

Counts the total number of distinct customer orders in the dataset.

## Signature

```dax
Total Orders := DISTINCTCOUNT ( Sales[Order ID] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `Sales[Order ID]` | Column | Unique order identifier column |

## Returns

An integer — the count of distinct orders in the current filter context.

## Examples

```dax
Total Orders := DISTINCTCOUNT ( Sales[Order ID] )

-- Orders per Region:
Total Orders Region :=
    CALCULATE (
        [Total Orders],
        ALLEXCEPT ( 'Geography', 'Geography'[Region] )
    )
```

## Notes

- **Use `DISTINCTCOUNT`**, not `COUNTROWS`, when one order can span multiple rows (line items per order). `COUNTROWS` counts rows; `DISTINCTCOUNT` counts unique orders.
- If Order ID is not unique per transaction, concatenate Order ID with line item number before counting.
- Comparing Total Orders to Total Sales reveals whether growth is driven by order volume or higher-value individual purchases.

## Related

- [[total-sales-dax-measure]] — `function`
- [[average-order-value-dax]] — `function`
- [[retail-kpi-framework]] — `atomic`

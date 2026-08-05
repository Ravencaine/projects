---
created: 2026-07-27
updated: 2026-08-02
source: "TREATAS in DAX: Connecting Unrelated Tables Like Magic"
note_type: function
tags: [dax, treatas, function, virtual-relationship, filter-context]
---

# TREATAS Function

Applies a set of values from one expression as a filter to a target column — without requiring an active or inactive relationship between the tables.

## Signature

```dax
TREATAS ( <TableExpression>, <Column>[, <Column> [, ...]] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<TableExpression>` | table | A single-column table of values to apply as filters (e.g., VALUES(), TOPN(), FILTER()) |
| `<Column>` | column | Target column(s) to filter — must have compatible data type |

## Returns

A **table**. Since TREATAS returns a table, it must be used as a filter argument inside CALCULATE() or CALCULATETABLE(), or as a table expression.

## Examples

**Filter Sales by top N products from Products table (no relationship needed):**

```dax
Sales by Top Products =
CALCULATE (
    [Total Sales],
    TREATAS (
        TOPN(10, VALUES(Products[ProductName]), [Total Sales], DESC),
        Products[ProductName]
    )
)
```

**Using TREATAS to filter a bridge/gateway fact:**

```dax
Revenue for Selected Campaigns =
CALCULATE (
    [Total Sales],
    TREATAS (
        VALUES(Campaigns[CampaignID]),
        Sales[CampaignID]
    )
)
```

**Dynamic segmentation — filter by parameter values:**

```dax
Revenue for Price Segment =
CALCULATE (
    [Total Sales],
    TREATAS (
        VALUES(PriceSegments[ProductKey]),
        Sales[ProductKey]
    )
)
```

## Notes

- Both sides must have the **same data type** (e.g., both integer, both string). Mismatched types cause an error.
- Unlike USERELATIONSHIP, no existing relationship is required or modified.
- TREATAS works as a filter argument only inside CALCULATE or CALCULATETABLE — it cannot be used standalone as a measure.
- Performance: TREATAS on large sets (millions of values) is expensive — prefer filtering at the source data layer when possible.

## Related

- [[treatas-vs-userelationship-comparison]] — includes CROSSFILTER
- [[treatas-multi-date-metrics]] — `pattern` — Multi-date KPIs (Shipped Qty, Overdue Payments, Cash Received) all driven by a single Date slicer
- [[treatas-strictness-gotcha]] — `gotcha` — Data type alignment requirements and blank propagation
- [[treatas-dynamic-segmentation-pattern]] — `pattern` — Parameter/what-if table segmentation via TREATAS
- [[userelationship-function]] — the relationship-based alternative to TREATAS for role-playing dimensions

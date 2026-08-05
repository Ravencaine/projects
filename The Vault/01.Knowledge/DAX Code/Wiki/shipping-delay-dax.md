---
created: 2026-08-01
updated: 2026-08-02
source: "RELATIONSHIP in DAX - Unlocking Role - Playing Dimensions.md"
note_type: atomic
tags: [dax, averagex, datediff, role-playing-dates, iterator, beginner]
---

# Shipping Delay: Real-World Role-Playing Example

The source article's practical example: calculating the average number of days between Invoice Date and Ship Date for each sales transaction — using role-playing dimensions and USERELATIONSHIP.

## The Core Calculation

```dax
Average Shipping Delay =
AVERAGEX (
    Sales,
    DATEDIFF ( Sales[InvoiceDate], Sales[ShipDate], DAY )
)
```

`AVERAGEX` iterates over the Sales table (respecting any active filters), evaluating `DATEDIFF` for each row. `DATEDIFF` with `DAY` returns the calendar difference in whole days.

## Why AVERAGEX Instead of SUMX / COUNTX?

| Function | Returns | Use Case |
|----------|---------|----------|
| `AVERAGEX` | Average of the expression | Average delay, average price, average time |
| `SUMX` | Sum of the expression | Total delay, total revenue |
| `COUNTX` | Count of rows | Number of late shipments, transaction count |

`AVERAGEX` is correct here because the goal is the *average* delay across transactions, not the total.

## Alternative: Using USERELATIONSHIP

The shipping delay calculation doesn't need USERELATIONSHIP — it uses the raw date columns directly on the fact table. However, the same metric could be expressed using the Date dimension for filtering:

```dax
Average Shipping Delay (By Date Slice) =
CALCULULATE (
    AVERAGEX (
        Sales,
        DATEDIFF ( Sales[InvoiceDate], Sales[ShipDate], DAY )
    ),
    USERELATIONSHIP ( Sales[ShipDate], 'Date'[Date] )
)
```

This version lets the Date slicer control the Ship Date perspective while still calculating the delay against Invoice Date.

## DATEDIFF Behavior Notes

- `DATEDIFF ( start, end, DAY )` returns: `end - start` in days
- Negative result = ShipDate before InvoiceDate (back-ordered or fulfilled early)
- Can return blanks if either date column is NULL

## Related

- [[uselationship-function]] — activating inactive relationships for alternate date perspectives
- [[role-playing-dimensions-pattern]] — single Date table approach for multi-date scenarios
- [[iterator-functions-sumx]] — AVERAGEX, SUMX, and iterator pattern deep dive

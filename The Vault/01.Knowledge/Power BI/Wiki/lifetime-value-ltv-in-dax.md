---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, marketing, customer-lifetime-value, ltv, clv]
note_type: pattern

---

# Customer Lifetime Value (LTV) in DAX

Estimating the total revenue a customer will generate over their relationship with the business.

## Simple LTV

```dax
Avg Customer Value :=
DIVIDE( SUM( 'Orders'[Revenue] ), DISTINCTCOUNT( 'Orders'[CustomerID] ) )

Avg Customer Lifespan :=
AVERAGE( 'Customers'[TenureMonths] ) / 12

LTV :=
[Avg Customer Value] * [Avg Customer Lifespan] * 12
```

## Cohort-based LTV

```dax
Cohort LTV :=
SUMX(
    SUMMARIZECOLUMNS(
        'Customers'[Cohort],
        "CohortRevenue", SUM( 'Orders'[Revenue] ),
        "CohortSize", DISTINCTCOUNT( 'Orders'[CustomerID] )
    ),
    DIVIDE( [CohortRevenue], [CohortSize] )
)
```

## Notes

- Use historical averages for future projections
- LTV / CAC (Customer Acquisition Cost) > 3 is considered healthy

## Related

- [[customer-churn-rate-dax]]
- [[mrr-and-arr-metrics-in-dax]]

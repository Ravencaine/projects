---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, saas, mrr, arr, subscription]
note_type: pattern

---

# MRR and ARR Metrics in DAX

Tracking recurring revenue from subscription business models.

## Monthly Recurring Revenue (MRR)

```dax
MRR :=
SUMX(
    'Subscriptions',
    'Subscriptions'[MonthlyRate] * 'Subscriptions'[Units]
)
```

## Annual Recurring Revenue (ARR)

```dax
ARR := [MRR] * 12
```

## MRR Components

```dax
New MRR :=
SUMX(
    FILTER( 'Subscriptions', 'Subscriptions'[Type] = "New" ),
    'Subscriptions'[MonthlyRate]
)

Expansion MRR :=
SUMX(
    FILTER( 'Subscriptions', 'Subscriptions'[Type] = "Expansion" ),
    'Subscriptions'[MonthlyRate]
)

Churned MRR :=
SUMX(
    FILTER( 'Subscriptions', 'Subscriptions'[Type] = "Churned" ),
    'Subscriptions'[MonthlyRate]
)

Net New MRR := [New MRR] + [Expansion MRR] - [Churned MRR]
```

## Notes

- Always use the contracted rate, not usage-based charges
- ARR = MRR * 12 for monthly subscriptions
- Net New MRR is the single best metric for subscription health

## Related

- [[gross-margin-calculation-in-dax]]
- [[customer-churn-rate-dax]]
- [[customer-lifetime-value-ltv-dax]]

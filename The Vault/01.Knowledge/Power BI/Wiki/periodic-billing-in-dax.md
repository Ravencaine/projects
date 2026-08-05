---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "saas", "billing", "subscription", "revenue"]
note_type: pattern

---

# Periodic Billing in DAX

Tracking billing events and deferred revenue for subscription businesses.

## Pattern

```dax
Billing This Period :=
SUMX(
    FILTER( 'Subscriptions', 'Subscriptions'[BillingDate] <= MAX( 'Dates'[Date] ) ),
    'Subscriptions'[MonthlyAmount]
)

Deferred Revenue :=
SUMX(
    'Subscriptions',
    VAR __Remaining =
        DATEDIFF( MAX( 'Dates'[Date] ), 'Subscriptions'[NextBillingDate], MONTH )
    RETURN
    MAX( 0, __Remaining ) * 'Subscriptions'[MonthlyAmount]
)
```

## Notes

- Deferred revenue = revenue collected but not yet earned
- Recognized monthly as the service is delivered

## Related

- [[mrr-and-arr-metrics-in-dax]]
- [[customer-lifetime-value-ltv-dax]]

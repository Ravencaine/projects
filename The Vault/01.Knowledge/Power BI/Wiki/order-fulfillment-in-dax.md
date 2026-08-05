---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "operations", "order-fulfillment", "supply-chain", "pipeline"]
note_type: pattern

---

# Order Fulfillment in DAX

Tracking the order fulfillment pipeline across stages.

## Pattern

```dax
Orders by Stage :=
COUNTROWS(
    SUMMARIZECOLUMNS(
        'Orders'[Stage],
        "Count", COUNTROWS( 'Orders' )
    )
)

Avg Days Per Stage :=
AVERAGEX(
    'Orders',
    DATEDIFF( 'Orders'[StageStart], 'Orders'[StageEnd], DAY )
)
```

## Notes

- Use a stage dimension table for multi-stage pipelines
- Track throughput per stage to identify bottlenecks

## Related

- [[on-time-in-full-otif-dax]]
- [[order-cycle-time-oct-dax]]

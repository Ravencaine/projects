---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, operations, inventory, turnover]
note_type: pattern

---

# Inventory Turnover in DAX

Measuring how many times inventory is sold and replaced in a period.

## Formula

```
Inventory Turnover = COGS / Average Inventory
Days Inventory Outstanding = 365 / Inventory Turnover
```

## DAX Pattern

```dax
Inventory Turnover :=
DIVIDE(
    SUM( 'Inventory'[COGS] ),
    AVERAGEX(
        SUMMARIZECOLUMNS( 'Dates'[Month], "AvgInv", SUM( 'Inventory'[Value] ) ),
        [AvgInv]
    )
)

Days Inventory Outstanding := DIVIDE( 365, [Inventory Turnover] )
```

## Notes

- Higher turnover = faster-moving inventory
- Compare against industry benchmarks
- Very high turnover may indicate stock-outs (lost sales)

## Related

- [[days-on-hand-inventory-in-dax]]
- [[stock-out-analysis-in-dax]]
- [[on-time-in-full-otif-dax]]

---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "finance", "investment-return", "modified-dietz", "performance"]
note_type: pattern

---

# Modified Dietz Return in DAX

Estimating portfolio return when cash flows occur during the measurement period.

## Formula

```
Modified Dietz Return = ( Ending Value - Beginning Value - Cash Flows )
                       / ( Beginning Value + Weighted Cash Flows )
```

## DAX Pattern

```dax
Modified Dietz :=
VAR __Beginning = [StartValue]
VAR __Ending = [EndValue]
VAR __CashFlows = SUM( 'CashFlows'[Amount] )
VAR __WeightedFlows =
    SUMX(
        'CashFlows',
        'CashFlows'[Amount]
            * ( DATEDIFF( 'CashFlows'[Date], [PeriodEnd], DAY ) / [TotalDays] )
    )
RETURN
DIVIDE( __Ending - __Beginning - __CashFlows,
        __Beginning + __WeightedFlows )
```

## Notes

- Used when calculating performance for periods with inflows/outflows
- More accurate than simple return when cash is added during the period

## Related

- [[npv-and-irr-calculations-in-dax]]
- [[compound-interest-in-dax]]

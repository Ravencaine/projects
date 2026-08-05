---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "hr", "hcva", "human-capital", "value-add"]
note_type: pattern

---

# Human Capital Value Added (HCVA) in DAX

Measuring the value employees add relative to their total cost.

## Formula

```
HCVA = ( Revenue - Operating Costs ) / Total Employee Cost
```

## DAX Pattern

```dax
HCVA :=
DIVIDE(
    SUM( 'Financials'[Revenue] ) - SUM( 'Financials'[OperatingCosts] ),
    SUM( 'Employees'[TotalCost] )
)
```

## Notes

- Higher HCVA = more revenue generated per dollar of employee investment
- Useful for comparing business units or departments

## Related

- [[turnover-rate]]
- [[bradford-factor-dax]]
- [[pay-equality-analysis-in-dax]]

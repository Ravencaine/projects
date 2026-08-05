---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "project", "earned-value", "evm"]
note_type: pattern

---

# Earned Value Management (EVM) in DAX

Tracking project performance using earned value methodology.

## Key Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| Planned Value (PV) | Budgeted cost of scheduled work | What was planned |
| Earned Value (EV) | Budgeted cost of completed work | What was accomplished |
| Actual Cost (AC) | Actual cost of completed work | What was spent |

## DAX Formulas

```dax
Planned Value :=
SUMX(
    FILTER(
        ALL( 'Project' ),
        'Project'[Start] <= MAX( 'Dates'[Date] )
    ),
    'Project'[PV] * MIN( 1, DIVIDE( MAX('Dates'[Date]) - 'Project'[Start], 'Project'[Finish] - 'Project'[Start] ) )
)

Earned Value :=
SUMX(
    'Project',
    'Project'[PV] * 'Project'[% Complete]
)

Actual Cost :=
SUM( 'Project'[AC] )
```

## Derived Metrics

```dax
Schedule Variance (SV)  := [EV] - [PV]
Cost Variance (CV)      := [EV] - [AC]
Schedule Performance Index (SPI) := DIVIDE( [EV], [PV] )
Cost Performance Index (CPI)    := DIVIDE( [EV], [AC] )
```

## Notes

- SPI/CPI > 1 = ahead/on-budget; < 1 = behind/over-budget
- Use at WBS or phase level for actionable reporting

## Related

- [[burndown-chart-in-dax]]
- [[schedule-variance-and-spi-in-dax]]
- [[cost-performance-index-cpi-in-dax]]

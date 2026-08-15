---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, hr, employee-satisfaction, survey, engagement]
note_type: pattern

---

# Employee Satisfaction in DAX

Analyzing employee engagement survey results.

## Pattern

```dax
Satisfaction Score :=
AVERAGE( 'Survey'[Score] )

Satisfaction by Department :=
SUMMARIZECOLUMNS(
    'Employees'[Department],
    "AvgScore", AVERAGE( 'Survey'[Score] ),
    "ResponseRate", DIVIDE( COUNTROWS( 'Survey' ), COUNTROWS( 'Employees' ) )
)
```

## Notes

- Combine with eNPS questions for engagement benchmarking
- Track trends over time with rolling surveys

## Related

- [[net-promoter-score-nps-dax]]
- [[value_add]]

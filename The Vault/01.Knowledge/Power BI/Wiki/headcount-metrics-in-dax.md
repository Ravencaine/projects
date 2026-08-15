---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, hr, headcount, workforce]
note_type: pattern

---

# Headcount Metrics in DAX

Tracking current, average, and period-end headcount for workforce analytics.

## Current Headcount

```dax
Current Headcount :=
CALCULATE(
    SUM( 'Employees'[Count] ),
    'Dates'[Date] = MAX( 'Dates'[Date] )
)
```

## Average Headcount (Time Period)

```dax
Average Headcount :=
AVERAGEX(
    SUMMARIZECOLUMNS(
        'Dates'[Month],
        "Monthly HC", [Current Headcount]
    ),
    [Monthly HC]
)
```

## Period-End Headcount

```dax
Period End HC :=
CALCULATE(
    SUM( 'Employees'[Count] ),
    'Dates'[Date] = MAX( 'Dates'[Date] ),
    REMOVEFILTERS( 'Dates' )
)
```

## Notes

- Always use a date table to enable time-based filtering
- Average headcount is the correct denominator for ETR
- Combine with department/location slicers for segment analysis

## Related

- [[turnover-rate]]
- [[pay-equality-analysis-in-dax]]
- [[value_add]]

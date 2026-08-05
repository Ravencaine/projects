---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "time-intelligence", "rolling-period", "moving-average"]
note_type: pattern

---

# Rolling Periods in DAX

Computing rolling sums, averages, or counts over a sliding time window.

## Purpose

Rolling periods smooth out volatility by aggregating over a fixed-length window (e.g., last 7 days, last 30 days, last 3 months).

## Rolling 30-Day Sales

```dax
Rolling 30 Day Sales :=
VAR __EndDate = MAX( 'Dates'[Date] )
VAR __StartDate = DATEADD( ALL( 'Dates'[Date] ), -30, DAY )
RETURN
SUMX(
    FILTER(
        ALL( 'Dates' ),
        'Dates'[Date] <= __EndDate
        && 'Dates'[Date] >= __StartDate
    ),
    [Sales Amount]
)
```

## Rolling 3-Month Average

```dax
Rolling 3 Month Avg :=
VAR __EndMonth = MAX( 'Dates'[Month] )
VAR __Table =
    FILTER(
        ALL( 'Dates' ),
        'Dates'[Month] <= __EndMonth
        && 'Dates'[Month] >= DATEADD( __EndMonth, -2, MONTH )
    )
RETURN
DIVIDE( SUMX( __Table, [Sales] ), 3 )
```

## Notes

- Sliding window requires filtering both upper and lower date bounds
- For large date ranges, use a date offset column in the date table

## Related

- [[no-calculate-time-intelligence-pattern]]
- [[quarter]]
- [[offset-based-date-calculations]]

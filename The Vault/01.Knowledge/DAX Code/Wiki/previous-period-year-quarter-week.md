---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, time-intelligence, previous-period, no-calculate]
note_type: pattern

---

# Previous Period/Year/Quarter/Week

Calculating the previous period value using the No CALCULATE approach.

## Purpose

Replace DATESUBLAGO, SAMEPERIODLASTYEAR with explicit FILTER + iterator logic.

## Structure

```dax
Sales Previous Period :=
SUMX(
    FILTER(
        ALL( 'Dates' ),
        'Dates'[Date] < MIN( 'Dates'[Date] )
    ),
    [Sales Amount]
)

Sales Previous Year :=
SUMX(
    FILTER(
        ALL( 'Dates' ),
        'Dates'[Date] = DATEADD( ALL( 'Dates'[Date] ), -1, YEAR )
    ),
    [Sales Amount]
)
```

## Notes

- Filter on `Date < MIN(Date)` captures the previous day/week/month depending on current context
- For year: use DATEADD with -1 YEAR as the comparison

## Related

- [[no-calculate-time-intelligence-pattern]]
- [[offset-based-date-calculations]]
- [[rolling-periods-in-dax]]

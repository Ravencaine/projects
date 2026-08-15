---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, date, offset, time-intelligence]
note_type: pattern

---

# Offset-based Date Calculations

Using integer offsets to shift date context instead of DAX time intelligence functions.

## Purpose

Instead of `SAMEPERIODLASTYEAR()` or `PARALLELPERIOD()`, compute the offset explicitly and use it to filter the date table.

## Structure

```dax
Sales N Months Ago :=
VAR __CurrentDate = MAX( 'Dates'[Date] )
VAR __Offset = -N
VAR __TargetDate = DATEADD( ALL( 'Dates'[Date] ), __Offset, MONTH )
VAR __Table =
    FILTER(
        ALL( 'Dates'[Date] ),
        'Dates'[Date] = __TargetDate
    )
RETURN
SUMX(
    __Table,
    [Sales]
)
```

## Common Offsets

| Calculation | Offset |
|---|---|
| Previous month | -1 MONTH |
| Same month last year | -1 YEAR |
| Next quarter | +1 QUARTER |
| 7 days ago | -7 DAY |
| Same period last year | -1 YEAR |

## Notes

- Works correctly even when the date table has gaps
- No dependency on DAX time intelligence internals
- Can be parameterized easily (N as a slicer value)

## Related

- [[no-calculate-time-intelligence-pattern]]
- [[date-table-creation-in-dax]]
- [[quarter]]

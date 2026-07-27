---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, time-intelligence]
---

# Time Intelligence Functions Overview

Time intelligence functions perform calculations over date ranges: year-to-date, period comparisons, running totals, and date shifts.

## Key Principles

- All time intelligence functions require a **date table** (a table with a contiguous set of dates marked as a date table in the model)
- Functions return a **table of dates** that is then fed into CALCULATE to modify the filter context
- Fiscal year calendars are supported via optional parameters

## Core Functions

| Function | Purpose |
|----------|---------|
| `TOTALYTD` | Year-to-date total |
| `TOTALQTD` | Quarter-to-date total |
| `TOTALMTD` | Month-to-date total |
| `TOTALWTD` | Week-to-date total |
| `DATESYTD` | Table of dates from start of year to current date |
| `DATESQTD` | Table of dates from start of quarter to current date |
| `DATESMTD` | Table of dates from start of month to current date |
| `DATESWTD` | Table of dates from start of week to current date |
| `SAMEPERIODLASTYEAR` | Shifts dates back one year |
| `DATEADD` | Shifts dates by interval (year/quarter/month/day) |
| `PARALLELPERIOD` | Shifts an entire period back/forward |
| `PREVIOUSYEAR` | All dates in the previous year |
| `NEXTYEAR` | All dates in the next year |
| `PREVIOUSMONTH` | All dates in the previous month |
| `NEXTMONTH` | All dates in the next month |
| `PREVIOUSQUARTER` | All dates in the previous quarter |
| `NEXTQUARTER` | All dates in the next quarter |
| `CLOSINGBALANCEYEAR` | Value at the last day of the year |
| `OPENINGBALANCEYEAR` | Value at the first day of the year |
| `DATESBETWEEN` | Custom date range |
| `DATESINPERIOD` | Date range of N intervals |
| `FIRSTDATE` | First date in context |
| `LASTDATE` | Last date in context |

## Examples

```dax
-- Year-to-date sales
Sales YTD := TOTALYTD([Sales], 'Date'[Date])

-- Sales compared to same period last year
Sales vs LY := CALCULATE([Sales], SAMEPERIODLASTYEAR('Date'[Date]))

-- Running total over a custom date range
LTD Sales := CALCULATE(
    [Sales],
    DATESBETWEEN(
        'Date'[Date],
        DATE(2017, 7, 1),  -- earliest date
        MAX('Date'[Date])   -- latest date in context
    )
)

-- Shift dates back one year
LY := CALCULATE([Sales], DATEADD('Date'[Date], -1, YEAR))
```

## Notes

- `TOTALYTD` etc. are equivalent to wrapping `SUM` in `CALCULATE` with the corresponding `DATES...` function
- `SAMEPERIODLASTYEAR` returns only dates that exist in the same relative position last year — may not return a full 12 months if the date range is partial
- `PARALLELPERIOD` returns full periods even if the current period is partial
- All time intelligence functions are **not supported in DirectQuery mode** for calculated columns and RLS rules

## Related

- [[calculate]] — function
- [[datesytd]] — function
- [[sameperiodlastyear]] — function
- [[dateadd]] — function

---
created: 2026-07-27
updated: 2026-08-02
source: "Time Intelligence in DAX: The Secret Behind YTD, QTD, and SamePeriodLastYear"
note_type: pattern
tags: [dax, time-intelligence, ytd, datesytd, fiscal-year]
---

# YTD Calculation with ALLSELECTED() Protection

Uses DATESYTD() inside CALCULATE with optional ALLSELECTED() wrapping to produce year-to-date totals that remain correct when users apply non-standard date slicer selections.

## Purpose

Standard YTD breaks when the date slicer selects a non-contiguous range (e.g., "Last Quarter") because DATESYTD computes from January 1 to the max date in context. ALLSELECTED() captures the full user selection and computes YTD relative to that range.

## Components

- DATESYTD() — returns table of dates from year start to max date in context
- CALCULATE() — applies the DATESYTD table as a filter
- ALLSELECTED() — captures user-selected date range without removing visual-level filters

## Structure

```dax
-- Standard YTD (breaks with non-standard date slicer selections)
Sales YTD =
CALCULATE (
    [Total Sales],
    DATESYTD ( Date[Date] )
)

-- Fiscal year YTD (Oct 1 start, e.g.):
Sales FYTD =
CALCULATE (
    [Total Sales],
    DATESYTD ( Date[Date], "09/30" )
)

-- Robust YTD using DATESBETWEEN for full control
Sales YTD Robust =
VAR CurrentPeriod = MAX ( Date[Date] )
VAR YearStart     = STARTOFYEAR ( Date[Date] )
RETURN
    CALCULATE (
        [Total Sales],
        DATESBETWEEN ( Date[Date], YearStart, CurrentPeriod )
    )
```

## YTD vs LY Comparison

```dax
Sales YTD =
CALCULATE (
    [Total Sales],
    DATESYTD ( Date[Date] )
)

Sales YTD LY =
CALCULATE (
    [Total Sales],
    DATESYTD ( Date[Date] ),
    SAMEPERIODLASTYEAR ( Date[Date] )
)
```

## Related

- [[sameperiodlastyear-vs-parallelperiod]]
- [[totalmtd]]
- [[totalqtd]]
- [[var-in-dax]] — VAR is typically used to store the date period before passing it to time intelligence functions

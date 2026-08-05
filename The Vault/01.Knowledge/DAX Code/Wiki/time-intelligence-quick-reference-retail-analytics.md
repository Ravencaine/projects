---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Power BI DAX Measures for Retail Analytics Pt 1"
source_url: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171"
note_type: reference
tags: [dax, reference, time-intelligence, retail]
---

# Time Intelligence Quick Reference (Retail Analytics)

A condensed reference for the time intelligence functions used in retail DAX patterns — TOTALMTD, TOTALYTD, SAMEPERIODLASTYEAR, DATESBETWEEN, MAXX, and ALLSELECTED.

## Time Intelligence Functions

| Function | Returns | Use Case |
|----------|---------|----------|
| `TOTALMTD` | scalar | Month-to-date aggregate — sums from first of month through selected date |
| `TOTALYTD` | scalar | Year-to-date aggregate — sums from Jan 1 through selected date |
| `SAMEPERIODLASTYEAR` | table | Shifts current date filter back one year |
| `DATESBETWEEN` | table | Dynamic date range from start to end date |
| `DATESMTD` | table | Same as TOTALMTD but returns a table for CALCULATE |
| `DATESYTD` | table | Same as TOTALYTD but returns a table for CALCULATE |

## Pattern Reference

```dax
-- MTD Sales (syntactic sugar for CALCULATE + DATESMTD)
MEASURE [MTD Sales] = TOTALMTD(SUM('Sales'[NetAmount]), 'Date'[Date])

-- YTD Sales (syntactic sugar for CALCULATE + DATESYTD)
MEASURE [YTD Sales] = TOTALYTD(SUM('Sales'[NetAmount]), 'Date'[Date])

-- Year-over-Year
MEASURE [YOY Sales] =
CALCULATE(
    [Total Sales],
    ALL('Date'[Date]),
    SAMEPERIODLASTYEAR('Date'[Date])
)

-- Dynamic date range (respects user slicers)
DATESBETWEEN(
    'Date'[Date],
    MINX(ALLSELECTED('Date'), 'Date'[Date]),  -- earliest in slicer
    MAXX(ALLSELECTED('Date'), 'Date'[Date])    -- latest in slicer
)
```

## Key Behaviours

- ALL('Date'[Date]) removes the current date filter before applying SAMEPERIODLASTYEAR — without it, both periods overlap
- MAXX + ALLSELECTED finds the latest date in the user's slicer selection — needed for budget tables that store YTD amounts at month level
- ALLSELECTED respects visual-level slicers; ALL ignores all filters
- All time intelligence functions require a **contiguous date table** marked as a date table in Power BI

## Related

- [[totalmtd]] — function
- [[totalytd]] — function
- [[sameperiodlastyear]] — function
- [[datesbetween]] — function
- [[allselected]] — filter function
- [[averagex]] — iterator used in context transition patterns

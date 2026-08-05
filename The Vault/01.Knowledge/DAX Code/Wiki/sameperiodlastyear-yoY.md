---
created: 2026-08-01
updated: 2026-08-02
source: "Time Intelligence in DAX The Secret Behind YTD, QTD, and SamePeriodLastYear.md"
note_type: atomic
tags: [dax, time-intelligence, sameperiodlastyear, yoy, year-over-year, beginner]
---

# SAMEPERIODLASTYEAR: Year-over-Year Comparison

SAMEPERIODLASTYEAR shifts the current date range back exactly one year — enabling instant YoY comparisons. Combine with DIVIDE for growth percentages.

## What It Does

SAMEPERIODLASTYEAR reads the current date filter and returns the **same set of dates shifted back one year**.

```
Current filter: Jan 1 2025 → Mar 31 2025 (Q1 2025)
SAMEPERIODLASTYEAR returns: Jan 1 2024 → Mar 31 2024 (Q1 2024)
```

Then CALCULATE re-evaluates your measure in that shifted context.

## Basic YoY Pattern

```c
Total Sales = SUM(Sales[Revenue])

Sales LY =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR('Date'[Date])
)

YoY Growth % =
VAR Current = [Total Sales]
VAR LastYear = [Sales LY]
RETURN
    DIVIDE(Current - LastYear, LastYear)
```

## How SAMEPERIODLASTYEAR Decodes Under the Hood

1. DAX reads the current date filter (e.g., January–March 2025)
2. SAMEPERIODLASTYEAR shifts that range back exactly 1 year (January–March 2024)
3. CALCULATE re-evaluates `[Total Sales]` in the 2024 context
4. YoY formula compares the two

## Prerequisite: Continuous Date Column

SAMEPERIODLASTYEAR needs a **continuous Date column**: no gaps.

```
If Date table skips weekends or holidays → broken results
```

Always use a complete Date table (one row per day, no gaps) for accurate YoY.

## Common Dashboard Structure

```c
Sales MTD  = CALCULATE([Total Sales], DATESMTD('Date'[Date]))
Sales QTD  = CALCULATE([Total Sales], DATESQTD('Date'[Date]))
Sales YTD  = CALCULATE([Total Sales], DATESYTD('Date'[Date]))
Sales LY   = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
YoY %      = DIVIDE([Sales YTD] - [Sales LY], [Sales LY])
```

One matrix — MTD, QTD, YTD, LY, and YoY% side by side. Stakeholders compare periods at a glance.

## DATEADD vs SAMEPERIODLASTYEAR

| Function | Shifts by | Direction |
|----------|-----------|-----------|
| `SAMEPERIODLASTYEAR` | Fixed 1 year | Always back 1 year |
| `DATEADD` | Configurable | Any period, any direction |

```c
// Back 1 year (same as SAMEPERIODLASTYEAR)
Sales LY = CALCULATE([Total Sales], DATEADD('Date'[Date], -1, YEAR))

// Forward 1 year
Sales NextYear = CALCULATE([Total Sales], DATEADD('Date'[Date], 1, YEAR))

// Back 1 quarter
Sales LQ = CALCULATE([Total Sales], DATEADD('Date'[Date], -1, QUARTER))
```

## Related

- [[ytd-qtd-mtd-functions]] — these work alongside SAMEPERIODLASTYEAR
- [[time-intelligence-date-table-requirements]] — continuous date column prerequisite
- [[dax-functions-shortlist]] — SAMEPERIODLASTYEAR in Olatunji's 8-function shortlist

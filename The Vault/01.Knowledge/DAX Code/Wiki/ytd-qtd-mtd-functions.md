---
created: 2026-08-01
updated: 2026-08-02
source: "Time Intelligence in DAX The Secret Behind YTD, QTD, and SamePeriodLastYear.md"
note_type: atomic
tags: [dax, time-intelligence, ytd, qtd, mtd, datesytd, datesqtd, datesmtd, beginner]
---

# YTD, QTD, and MTD: Time Period Functions in DAX

Three functions that expand the date range dynamically — showing progress over time. All require CALCULATE and a marked Date table.

## The Holy Trinity

| Function | Period | What it does |
|----------|--------|--------------|
| `DATESYTD` | Year-to-Date | All dates from Jan 1 to current date in filter |
| `DATESQTD` | Quarter-to-Date | All dates from quarter start to current date |
| `DATESMTD` | Month-to-Date | All dates from month start to current date |

All three work **inside CALCULATE**, which modifies the filter context.

## Basic Pattern

```c
Total Sales = SUM(Sales[Revenue])

Sales YTD  = CALCULATE([Total Sales], DATESYTD('Date'[Date]))
Sales QTD  = CALCULATE([Total Sales], DATESQTD('Date'[Date]))
Sales MTD  = CALCULATE([Total Sales], DATESMTD('Date'[Date]))
```

`DATESYTD`, `DATESQTD`, and `DATESMTD` return a set of dates — CALCULATE uses those dates to filter what `[Total Sales]` evaluates over.

## How It Works

When the slicer shows March 2025:
- `DATESYTD('Date'[Date])` → returns Jan 1 2025 through March 31 2025
- `CALCULATE([Total Sales], DATESYTD(...))` → sums only rows in that date range

When the slicer changes to Q1 2025:
- `DATESYTD(...)` → still returns Jan 1 through March 31 2025
- Result updates dynamically to the selected period

## Slicer-Driven Period Switching

```c
Sales MTD = CALCULATE([Total Sales], DATESMTD('Date'[Date]))
Sales QTD = CALCULATE([Total Sales], DATESQTD('Date'[Date]))
Sales YTD = CALCULATE([Total Sales], DATESYTD('Date'[Date]))
```

CEO can switch between "Month", "Quarter", or "Full Year" slicer — each measure adapts automatically because the Date table's filter context changes.

## Fiscal Year Customization

By default, DATESYTD uses December 31 as the year end. Set a custom fiscal year end:

```c
// Fiscal year ends March 31
Sales FYTD = CALCULATE([Total Sales], DATESYTD('Date'[Date], "03/31"))

// Fiscal year ends June 30
Sales FYTD = CALCULATE([Total Sales], DATESYTD('Date'[Date], "06/30"))
```

Second parameter = end date of the fiscal year in `DD/MM` or `MM/DD` format (locale-aware).

## TOTALYTD / TOTALQTD Shorthand

Pre-packaged versions — CALCULATE + DATESYTD in one function:

```c
// These are equivalent:
Sales YTD v1 = CALCULATE([Total Sales], DATESYTD('Date'[Date]))
Sales YTD v2 = TOTALYTD([Total Sales], 'Date'[Date])

Sales QTD v1 = CALCULATE([Total Sales], DATESQTD('Date'[Date]))
Sales QTD v2 = TOTALQTD([Total Sales], 'Date'[Date])
```

Use whichever reads more clearly in your model.

## Related

- [[sameperiodlastyear-yoY]] — SAMEPERIODLASTYEAR works alongside these
- [[time-intelligence-date-table-requirements]] — prerequisite: marked Date table
- [[dax-common-mistakes-beginners]] — "no date table = wrong time intelligence results"

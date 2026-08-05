---


title: "TOTALYTD"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, time-intelligence]
note_type: pattern
description: "TOTALYTD — calculates a year-to-date total for an expression. Supports custom fiscal year-end dates. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# TOTALYTD

Evaluates the year-to-date value of an expression. Supports optional fiscal year-end specification.

## Syntax

```
TOTALYTD( <expression>, <dates> [, <filter>] [, <year_end_date>] )
```

## Arguments

| Argument | Description |
|----------|-------------|
| `expression` | The measure to aggregate (e.g., `SUM( Sales[Amount] )`) |
| `dates` | A date column |
| `filter` | Optional filter to apply |
| `year_end_date` | Optional fiscal year-end date (e.g., "06/30" for June 30 fiscal year) |

## Behavior

- Accumulates the expression from the start of the year to the last date visible in the filter context
- If `year_end_date` is omitted, uses a calendar year (January 1 to December 31)
- Works correctly with filters on date hierarchies

## Example: Standard Calendar YTD

```dax
Sales YTD :=
TOTALYTD(
    SUM( 'Sales'[Amount] ),
    'Date'[Date]
)
```

## Example: Fiscal Year YTD (ending June 30)

```dax
Sales YTD Fiscal :=
TOTALYTD(
    SUM( 'Sales'[Amount] ),
    'Date'[Date],
    "06/30"
)
```

## Related Functions

- `TOTALQTD` — quarter-to-date
- `TOTALMTD` — month-to-date
- `SAMEPERIODLASTYEAR` — prior year equivalent period
- `YEAR` — extracts the year from a date
- `LASTDATE` — used as end date in manual YTD patterns

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

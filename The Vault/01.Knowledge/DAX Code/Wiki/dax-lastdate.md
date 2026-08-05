---


title: "LASTDATE"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, time-intelligence]
note_type: pattern
description: "LASTDATE — returns the last date in the current filter context. Used with TOTALYTD and other time-intelligence functions. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# LASTDATE

Returns the last (maximum) date in the current filter context for a date column.

## Syntax

```
LASTDATE( <date_column> )
```

## Behavior

- Returns a single-column table containing one value — the last date
- Commonly used as the end date in a TOTALYTD or SAMEPERIODLASTYEAR calculation
- Respects filter context: if a month is filtered, returns the last day of that month

## Common Pattern

```dax
-- Year-to-date sales ending on the last visible date
SalesYTD :=
TOTALYTD(
    SUM( 'Sales'[Amount] ),
    'Date'[Date],
    LASTDATE( 'Date'[Date] )
)
```

## Related Functions

- `FIRSTDATE` — opposite of LASTDATE
- `TOTALYTD` — year-to-date using a year-end date parameter
- `SAMEPERIODLASTYEAR` — same period shifted one year back
- `ENDOFMONTH` / `ENDOFYEAR` — similar but returns the actual last date

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

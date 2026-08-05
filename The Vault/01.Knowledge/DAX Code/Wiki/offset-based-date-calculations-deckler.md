---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dates, offsets, time-intelligence, fiscal-calendar, no-calculate]
---

# Offset-Based Date Calculations (Deckler)

Integer offset columns on a date table as a replacement for all DAX time intelligence functions. Offsets are future-positive, present-is-zero, past-negative — like a number line for time.

> **Extends:** [offset-based-date-calculations](/wiki/offset-based-date-calculations.md) — this variant covers the No CALCULATE offset approach from DAX for Humans.

## Purpose

DAX built-in time intelligence functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`, `PREVIOUSQUARTER`, etc.) assume a standard Gregorian calendar. They fail for fiscal calendars (e.g., fiscal year starting June 1), 445/454 week-based quarters, or single-table models without a separate date table.

Offset columns solve all of these by representing time relationships as integers rather than relying on calendar-aware built-in functions. The present period is always `0`; past periods are negative; future periods are positive.

## Components

- **`CurrYearOffset`**: integer offset of each date's year from the current year (or fiscal year)
- **`CurrQuarterOffset`**: integer offset of each date's quarter from the current quarter
- **`CurrMonthOffset`**: integer offset of each date's month from the current month
- **`CurrWeekOffset`**: integer offset of each date's week from the current week
- **`CurrDayOffset`**: integer offset of each date's day from today

These are created as calculated columns in the date table (ideally in Power Query / M, not DAX).

## Structure

**Year Offset column:**
```dax
Year Offset =
VAR __Current = YEAR( TODAY() )
VAR __Result = [Year] - __Current
RETURN
    __Result
```
Returns `-1` for last year, `0` for current year, `1` for next year.

**General Month Offset column (handles fiscal calendars):**
```dax
Month Offset =
VAR __Today = TODAY()
VAR __Current = YEAR( __Today ) * 100 + MONTH( __Today )
VAR __Table =
    SUMMARIZE(
        ADDCOLUMNS(
            'Dates',
            "__Value", YEAR( [Date] ) * 100 + MONTH( [Date] )
        ),
        [__Value]
    )
VAR __Row = YEAR( [Date] ) * 100 + MONTH( [Date] )
VAR __Result =
    IF(
        __Row < __Current,
        COUNTROWS(
            FILTER(
                __Table,
                [__Value] >= __Row && [__Value] < __Current
            )
        ) * -1,
        COUNTROWS(
            FILTER(
                __Table,
                [__Value] >= __Current && [__Value] < __Row
            )
        ) + 0
    )
RETURN
    __Result
```

The same pattern works for `WEEKNUM`-based offsets by replacing `MONTH` with `WEEKNUM(..., 2)`.

## Why Offsets Beat Time Intelligence Functions

| Requirement | Time Intelligence | Offset Approach |
|-------------|-----------------|-----------------|
| Standard calendar | ✅ | ✅ |
| Fiscal year calendars | ❌ (only `TOTALYTD` supports FY start) | ✅ (use `Fiscal CurrYearOffset`) |
| 445/454 week quarters | ❌ | ✅ |
| Single-table models (no date table) | ❌ | ✅ (dynamic offsets via YEAR()*100+MONTH()) |
| Year-over-year on same partial period | ❌ (inconsistent) | ✅ (use `TODATE()` logic) |
| Week-level calculations | ❌ (no support) | ✅ |
| Debugging | Opaque | ✅ (offset values are visible in the date table) |

## Sources

The calendar table with offset columns can be created in DAX (for learning) but is best built in Power Query using Melissa de Korte's `fnDateTable` function, which produces 60 columns including all standard offsets, ISO offsets, and a `Fiscal CurrYearOffset` column.

## Related

- [Period-to-Date Offset Pattern](/wiki/period-to-date-offset-pattern.md) — using offsets for YTD/QTD/MTD/WTD
- [Rolling Periods](/wiki/rolling-periods-in-dax.md) — rolling averages using offset arithmetic
- [Calendar Table Creation](/wiki/date-table-calendar-addcolumns.md) — building the date table
- [TOTALYTD](/wiki/totalytd.md) — the time intelligence function being replaced

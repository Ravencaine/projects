---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dates, calendar, date-table, calendar, addcolumns, power-query]
---

# Calendar Table Creation: CALENDAR and ADDCOLUMNS

Creating a complete date/calendar table in DAX using `CALENDAR()`, `CALENDARAUTO()`, and `ADDCOLUMNS()` to add Year, Month, Quarter, Week, and Day columns.

> **Note:** Calendar tables are best created in Power Query (M) or at the data source level, not in DAX. DAX is used here for learning purposes. Melissa de Korte's `fnDateTable` (Power Query M) is the recommended production approach.

## Purpose

Nearly every Power BI semantic model needs a calendar table to support date-based analysis. The calendar table provides the row structure (one row per date) and lookup columns for grouping (Year, Month, Quarter, Week) and sorting (MonthSort, WeekdaySort).

## Components

- **`CALENDAR( start, end )`**: generates a single-column table of dates between two dates
- **`CALENDARAUTO( fiscal_year_start_month )`**: auto-detects the date range from the model and generates dates
- **`ADDCOLUMNS( table, "name", expression, ... )`**: adds calculated columns to any table

## Structure

**Basic DAX calendar:**
```dax
Dates =
CALENDAR(
    DATE( 2020, 1, 1 ),
    DATE( 2030, 12, 31 )
)
```
Creates a single-column `Date` table.

**Full calendar with lookup columns:**
```dax
Dates =
ADDCOLUMNS(
    CALENDAR( DATE( 2020, 1, 1 ), DATE( 2030, 12, 31 ) ),
    "Year",          YEAR( [Date] ),
    "Month",         FORMAT( [Date], "mmmm" ),
    "MonthSort",     MONTH( [Date] ),
    "Quarter",       "Q" & FORMAT( [Date], "Q" ),
    "QuarterSort",   FORMAT( [Date], "Q" ),
    "Weekday",       FORMAT( [Date], "dddd" ),
    "WeekdaySort",   WEEKDAY( [Date], 2 ),
    "Weeknum",       WEEKNUM( [Date], 2 ),
    "Day",           DAY( [Date] )
)
```

**Marking the table as a date table:**
Right-click the table in the Data pane → Mark as date table → toggle On → select the `Date` column. This enables DAX time intelligence functions to work correctly (though offset-based measures don't require this).

## Key Format Strings

| Format | Returns | Example |
|--------|---------|---------|
| `"mmmm"` | Full month name | "January" |
| `"dddd"` | Full weekday name | "Monday" |
| `"Q"` | Quarter number as text | "Q1" |
| `WEEKDAY(date, 2)` | Weekday number (1=Mon, 7=Sun) | `2` = Monday |
| `WEEKNUM(date, 2)` | Week number (week starts Monday) | `1`–`53` |

## Sort-by-Column Setup

Text columns (Month, Weekday) sort alphabetically by default. Override with Sort by column:
1. Select the text column (e.g., Month)
2. Column tools tab → Sort by column → pick the numeric sort column (MonthSort)
This ensures "January" sorts before "December," not alphabetically.

> **Gotcha (Brian Julius):** Adding a Sort-by column brings that sort column into filter context. Clearing filters requires removing both the original column and its sort column.

## Production Recommendation

Use Melissa de Korte's Power Query `fnDateTable` function (available at Enterprise DNA forum). It creates 60 columns including all offset columns (CurrYearOffset, CurrQuarterOffset, CurrMonthOffset, CurrWeekOffset, CurrDayOffset), ISO variants, and Fiscal offsets — far more complete than any basic DAX calendar.

## Related

- [Offset-Based Date Calculations](/wiki/offset-based-date-calculations-deckler.md) — the offset columns added to a full calendar table
- [Period-to-Date Offset Pattern](/wiki/period-to-date-offset-pattern.md) — using the calendar for PTD calculations
- [CALENDAR / CALENDARAUTO](/wiki/calendar-and-calendarauto.md) — the DAX date generation functions
- [ADDCOLUMNS](/wiki/addcolumns.md) — the column-adding function
- [Date Table Creation in DAX](/wiki/date-table-creation-in-dax.md) — existing KB note on this topic

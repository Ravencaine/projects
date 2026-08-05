---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [period-to-date, ytd, qtd, mtd, wtd, offsets, no-calculate]
---

# Period-to-Date Offset Pattern

Using `CurrYearOffset`/`CurrQuarterOffset`/`CurrMonthOffset`/`CurrWeekOffset` columns to compute YTD/QTD/MTD/WTD without DAX time intelligence functions.

## Purpose

`TOTALYTD`, `TOTALQTD`, `TOTALMTD`, and `TOTALWTD` are limited to standard calendars, cannot do fiscal calendars (except `TOTALYTD` with a FY start month), and offer no week-level support at all. The offset-based PTD pattern works with any calendar structure — fiscal years, 445 quarters, and weeks — in both multi-table and single-table models.

## Core Structure

All PTD measures follow the same 4-VAR skeleton:

```dax
Period To Date =
VAR __Offset =                     -- detect current period offset
    IF(
        HASONEVALUE( 'Calendar'[Year] ) && HASONEVALUE( 'Calendar'[Period] ),
        MAX( 'Calendar'[CurrPeriodOffset] ),
        0
    )
VAR __Today = TODAY()             -- anchor to today's date
VAR __MaxDate =                    -- compute the cutoff date for the period
    IF( __Offset = 0, __Today, MAX( 'Calendar'[Date] ) )
VAR __Table =
    SUMMARIZE(
        FILTER(
            'Calendar',
            [Date] <= __MaxDate
            && [CurrPeriodOffset] = __Offset
        ),
        [Date],
        "__Value", SUM( 'Table'[Value] )
    )
VAR __Result = SUMX( __Table, [__Value] )
RETURN
    __Result
```

The `__Offset` variable detects whether the visual is showing a single period (one year) or multiple periods (table). `HASONEVALUE` is the key guard: single period → use that period's offset; multiple periods → default to current period (offset 0).

## Year-to-Date (YTD)

```dax
Year To Date =
VAR __Today = TODAY()
VAR __Table =
    SUMMARIZE(
        FILTER(
            'Calendar',
            [Date] <= __Today
            && [CurrYearOffset] = 0
        ),
        [Date],
        "__Value", SUM( 'Table'[Value] )
    )
VAR __Result = SUMX( __Table, [__Value] )
RETURN
    __Result
```

Compare with `TOTALYTD`:
```dax
YTD = TOTALYTD( SUM('Table'[Value]), 'Calendar'[Date] )
```

The offset version can easily exclude today's partial day by changing `<=` to `<` — `TOTALYTD` cannot do this.

## Quarter-to-Date (QTD)

```dax
Quarter To Date 3 =
VAR __Offset =
    IF(
        HASONEVALUE( 'Calendar'[Year] ) && HASONEVALUE( 'Calendar'[Quarter] ),
        MAX( 'Calendar'[CurrQuarterOffset] ),
        0
    )
VAR __Today = TODAY()
VAR __MaxDate = IF( __Offset = 0, __Today, MAX( 'Calendar'[Date] ) )
VAR __Table =
    SUMMARIZE(
        FILTER(
            'Calendar',
            [Date] <= __MaxDate
            && [CurrQuarterOffset] = __Offset
        ),
        [Date],
        "__Value", SUM( 'Table'[Value] )
    )
VAR __Result = SUMX( __Table, [__Value] )
RETURN
    __Result
```

Note: `TOTALQTD` lacks the fiscal year parameter that `TOTALYTD` has — the offset approach is strictly more capable here.

## Month-to-Date (MTD)

```dax
Month To Date 3 =
VAR __Offset =
    IF(
        HASONEVALUE( 'Calendar'[Year] ) && HASONEVALUE( 'Calendar'[Month] ),
        MAX( 'Calendar'[CurrMonthOffset] ),
        0
    )
VAR __Today = TODAY()
VAR __MaxDate = IF( __Offset = 0, __Today, MAX( 'Calendar'[Date] ) )
VAR __Table =
    SUMMARIZE(
        FILTER(
            'Calendar',
            [Date] <= __MaxDate
            && [CurrMonthOffset] = __Offset
        ),
        [Date],
        "__Value", SUM( 'Table'[Value] )
    )
VAR __Result = SUMX( __Table, [__Value] )
RETURN
    __Result
```

## Week-to-Date (WTD)

```dax
Week To Date =
VAR __Offset =
    IF(
        HASONEVALUE( 'Calendar'[Year] ) && HASONEVALUE( 'Calendar'[Week Number] ),
        MAX( 'Calendar'[CurrWeekOffset] ),
        0
    )
VAR __Today = TODAY()
VAR __MaxDate = IF( __Offset = 0, __Today, MAX( 'Calendar'[Date] ) )
VAR __Table =
    SUMMARIZE(
        FILTER(
            'Calendar',
            [Date] <= __MaxDate
            && [CurrWeekOffset] = __Offset
        ),
        [Date],
        "__Value", SUM( 'Table'[Value] )
    )
VAR __Result = SUMX( __Table, [__Value] )
RETURN
    __Result
```

Note: **DAX has no built-in week time intelligence functions.** The offset approach is the only native DAX solution for WTD.

## Fiscal Year-to-Date

```dax
FY To Date =
VAR __Offset =
    IF(
        HASONEVALUE( 'Calendar'[Year] ),
        MAX( 'Calendar'[Fiscal CurrYearOffset] ),
        0
    )
VAR __Today = TODAY()
VAR __MaxDate =
    IF(
        __Offset = 0,
        __Today,
        MAXX(
            FILTER( ALL( 'Calendar' ), [Fiscal CurrYearOffset] = __Offset ),
            [Date]
        )
    )
VAR __Table =
    SUMMARIZE(
        FILTER(
            ALL('Calendar'),
            [Date] <= __MaxDate
            && [Fiscal CurrYearOffset] = __Offset
        ),
        [Date],
        "__Value", SUM( 'Table'[Value] )
    )
VAR __Result = SUMX( __Table, [__Value] )
RETURN
    __Result
```

Uses `ALL('Calendar')` because fiscal year boundaries don't align with the standard Year column used in visuals.

## Single-Table PTD (No Separate Date Table)

The offset approach works without any date table by computing offsets dynamically:

```dax
Month To Date =
VAR __Offset =
    IF(
        HASONEVALUE( 'Table'[Year] ) && HASONEVALUE( 'Table'[Month] ),
        YEAR( MAX( 'Table'[Date] ) ) * 100 + MONTH( MAX( 'Table'[Date] ) ),
        YEAR( TODAY() ) * 100 + MONTH( TODAY() )
    )
VAR __Table =
    SUMMARIZE(
        ADDCOLUMNS(
            'Table',
            "__Offset", YEAR( [Date] ) * 100 + MONTH( [Date] )
        ),
        [__Offset],
        "__Value", SUM( 'Table'[Value] )
    )
VAR __Result =
    SUMX(
        FILTER(
            __Table,
            [__Offset] <= __Offset
        ),
        [__Value]
    )
RETURN
    __Result
```

DAX time intelligence functions **cannot** work with single-table models — this pattern can.

## Related

- [Offset-Based Date Calculations](/wiki/offset-based-date-calculations-deckler.md) — the offset column definitions
- [Rolling Periods in DAX](/wiki/rolling-periods-in-dax.md) — rolling averages using offset arithmetic
- [TOTALYTD](/wiki/totalytd.md) — the time intelligence function being replaced
- [DATESYTD](/wiki/datesmtd-datesqtd-datesytd.md) — the underlying time intelligence filter functions

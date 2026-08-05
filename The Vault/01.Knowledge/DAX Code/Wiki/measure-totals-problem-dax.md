---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: reference
tags: [totals, grand-total, hasonevalue, isinscope, semi-additive, measure-totals]
---

# Measure Totals Problem in DAX

Grand totals in matrix visuals don't always equal the sum of the visible row values — because the total row operates under a different (or no) filter context than the detail rows.

## The Problem

A measure computes correctly for each row in a matrix visual but shows a wrong value in the total/grand total row. This is one of the most common DAX confusion points and arises from how DAX evaluates measures across different filter contexts.

Common causes:

1. **Semi-additive measures**: measures like inventory balances, account balances, or exchange rates that shouldn't be summed across time periods
2. **HASONEVALUE guard missing**: the total row has no single-value filter, so `MAX(...)` returns a table-wide aggregate instead of the period-specific value
3. **Missing ISINSCOPE/ISFILTERED check**: the measure doesn't distinguish between a total row and a detail row

## Detection Patterns

| Function | What it detects |
|----------|----------------|
| `HASONEVALUE(column)` | True when exactly one distinct value is selected for the column |
| `ISINSCOPE(column)` | True when the column is in the current subtotal/total context |
| `ISFILTERED(column)` | True when the column has an active filter |
| `ISONORAFTER(...)` | Used in calculation groups to detect sort position |

## Example: Fixing a Totals Problem with HASONEVALUE

```dax
Year To Date 2 =
VAR __Offset =
    IF(
        HASONEVALUE( 'Calendar'[Year] ),
        MAX( 'Calendar'[CurrYearOffset] ),
        0          -- fallback for total row: use current year offset
    )
VAR __Today = TODAY()
VAR __MaxDate =
    DATE(
        YEAR( __Today ) + __Offset,
        MONTH( __Today ),
        DAY( __Today )
    )
VAR __Table =
    SUMMARIZE(
        FILTER(
            'Calendar',
            [Date] <= __MaxDate
            && [CurrYearOffset] = __Offset
        ),
        [Date],
        "__Value", SUM( 'Table'[Value] )
    )
VAR __Result = SUMX( __Table, [__Value] )
RETURN
    __Result
```

Without the `HASONEVALUE` check, the `MAX('Calendar'[CurrYearOffset])` in the total row would return an ambiguous result (multiple rows have different offsets), causing incorrect totals.

## Standard Guard Pattern

```dax
Safe Measure =
VAR __IsTotal = NOT HASONEVALUE( 'Table'[Category] )
VAR __Result =
    IF(
        __IsTotal,
        <total-row calculation>,
        <detail-row calculation>
    )
RETURN
    __Result
```

## From TOCSV Debugging (Ch2 Reference)

In the TOCSV section, Deckler demonstrates that the total row in a Table visual has no Item filter — it shows the average of ALL rows. Each detail row filters to its own Item. The total row is simply a different context, not a sum of the rows.

## Related

- [HASONEVALUE](/wiki/hasonevalue.md) — detecting single-value filter context
- [ISINSCOPE](/wiki/isinscope.md) — detecting whether a column is in the current scope
- [The Measure Totals Problem in DAX](/wiki/the-measure-totals-problem-in-dax.md) — existing KB note on this topic
- [Why Totals Look Wrong in DAX](/wiki/why-totals-look-wrong-in-dax.md) — existing KB note
- [Semi-Additive Measures](/wiki/time-intelligence-ytd-pattern.md) — balance-type measures that require special total handling

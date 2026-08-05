---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [lookup, filter, maxx, minx, no-calculate, pattern]
---

# LOOKUP without CALCULATE: FILTER + MAXX/MINX

Using `FILTER` + `MAXX`/`MINX` as a row-by-row lookup pattern — finding the value in one column for the row that maximizes (or minimizes) another column.

## Purpose

DAX "thinks in tables, rows, and columns," not cells. But you often need to look up a specific cell value based on a condition — e.g., "what is the Price of the most expensive item?" The No CALCULATE approach uses `FILTER` + `MAXX`/`MINX` to find that row and return its value.

## Structure

```dax
<Measure> =
VAR __Table = FILTER( <source table>, <condition> )
VAR __Result = MAXX( __Table, <value column> )
RETURN
    __Result
```

## Examples

**Find the minimum Total Cost for Pickle rows:**
```dax
Pickle Total Cost Min/Max =
VAR __Item = "Pickle"
VAR __Table = FILTER( 'Table', 'Table'[Item] = __Item )
VAR __Result = MINX( __Table, [Total Cost] )
RETURN
    __Result
```
Result: **7.98** (the lower Pickle value). Swap `MINX` → `MAXX` for the upper value: **15.96**.

**Find the most expensive Banana or Grapefruit row where Quantity is 3:**
```dax
Banana or Grapefruit Qty 3 =
VAR __Table =
    FILTER(
        'Table',
        ( 'Table'[Item] = "Banana" | 'Table'[Item] = "Grapefruit" )
        && 'Table'[Quantity] = 3
    )
VAR __Result = MAXX( __Table, [Total Cost] )
RETURN
    __Result
```
Result: **14.97**. Parentheses group the OR condition separately from the Quantity filter.

**Double Lookup — find the Total Cost on the most recent date:**
```dax
Double Lookup =
VAR __MaxDate = MAX( 'Table'[Date] )
VAR __Table = FILTER( 'Table', 'Table'[Date] = __MaxDate )
VAR __Result = MAXX( __Table, [Total Cost] )
RETURN
    __Result
```
This pattern "chains" two lookups: first finding the max date, then finding the max cost among rows on that date. Placed in a table visual, it shows the most-expensive-row-on-max-date for each Item group.

## Comparison with LOOKUPVALUE

`LOOKUPVALUE` returns a value if exactly one distinct row matches the criteria. `FILTER` + `MAXX`/`MINX` does the same thing but is more explicit and composable. Deckler's No CALCULATE philosophy prefers the latter because it uses the smallest number of base DAX functions and the intermediate table is inspectable.

```dax
-- LOOKUPVALUE equivalent (less preferred in No CALCULATE philosophy)
Price of Most Expensive Pickle =
LOOKUPVALUE(
    'Table'[Total Cost],
    'Table'[Item], "Pickle",
    'Table'[Total Cost], MAXX( FILTER('Table', 'Table'[Item]="Pickle"), [Total Cost] )
)
```

## Related

- [No CALCULATE Banana Pattern](/wiki/no-calculate-banana-pattern.md) — the parent pattern
- [TOCSV Debugging Pattern](/wiki/dax-debugging-tocsv.md) — inspect intermediate tables in this pattern
- [LOOKUPVALUE](/wiki/lookupvalue.md) — the dedicated lookup function and when to prefer it
- [X Aggregators](/wiki/x-aggregators-sumx-minx-maxx.md) — MAXX/MINX are the aggregation half of this pattern

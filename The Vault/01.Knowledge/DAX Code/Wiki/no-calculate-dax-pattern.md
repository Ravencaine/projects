---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "no-calculate", "filter-context"]
note_type: pattern

---

# No CALCULATE DAX Pattern

A DAX pattern that solves the majority of calculation problems without ever using CALCULATE. Instead, it uses FILTER + iterator functions to make filter logic explicit.

## Purpose

Avoid the cognitive overhead of CALCULATE by expressing filtering as an explicit table transformation followed by an iterator. This makes the code self-documenting: you can see exactly what rows are included.

## Components

- `VAR` / `RETURN` — variable declaration for readability
- `FILTER()` — explicit row-by-row filtering
- Iterator function: `SUMX`, `AVERAGEX`, `MAXX`, `MINX`, `COUNTX`, etc.

## Structure

```dax
Measure Name =
VAR __ExcludeItem = "Pickle"
VAR __Table = FILTER( 'Table', 'Table'[Item] <> __ExcludeItem )
VAR __Result = SUMX( __Table, [Total Cost] )
RETURN
__Result
```

The pattern:
1. Declare filter criteria as variables
2. Build the filtered table with `FILTER()`
3. Pass the filtered table to an iterator (`SUMX`, etc.)
4. Return the result

## Variations

- **Multiple filters:** nest `FILTER()` calls or use `&&` inside a single `FILTER()`
- **Keep-all filter:** use `REMOVEFILTERS()` to clear existing filters before applying new ones
- **Cross-table filter:** extend the filter expression to reference related columns

## Related

- [[CALCUHATE]]
- [[no-calculate-vs-calculate-comparison]]
- [[calculate]]

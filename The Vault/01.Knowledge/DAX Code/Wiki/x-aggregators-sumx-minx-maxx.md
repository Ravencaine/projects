---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [x-aggregators, iterators, sumx, minx, maxx, filtering]
---

# X Aggregators: SUMX, MINX, MAXX, AVERAGEX

Iterator functions that take a table (or table expression) as their first argument and a scalar expression as their second, then evaluate that expression across every row of the table and aggregate the results.

## Purpose

Basic aggregators (`SUM`, `MIN`, `MAX`, `AVERAGE`) accept only a single column reference. X aggregators accept a **table expression** as the first argument, which means they can iterate over a filtered set of rows — making filtering and aggregation a single unified operation.

## Components

- **Table expression** (arg 1): can be a table name, `VAR`, or any DAX expression returning a table (e.g. `FILTER(...)`, `SUMMARIZE(...)`)
- **Scalar expression** (arg 2): any DAX expression evaluated once per row in the table context — typically a column reference like `[Total Cost]`

## Structure

```dax
XAGG(
    <table expression>,
    <scalar expression>
)
```

## SUM vs SUMX Equivalence

`SUM` is syntactic sugar for `SUMX` — they are functionally identical:

```dax
SUM( 'Table'[Price] )
SUMX( 'Table', 'Table'[Price] )
```

Both sum every row of the `Price` column. The difference is that `SUMX` lets you pass a filtered table instead of the whole table.

## Conditional Aggregation with FILTER

The canonical No CALCULATE pattern: filter first, then aggregate.

```dax
Min Total Cost Not Pickle =
MINX(
    FILTER( 'Table', 'Table'[Item] <> "Pickle" ),
    [Total Cost]
)
```

This finds the minimum `Total Cost` for all rows where Item is not "Pickle" (result: **8.97**).

```dax
Max Total Cost Not Pickle =
MAXX(
    FILTER( 'Table', 'Table'[Item] <> "Pickle" ),
    [Total Cost]
)
```

Same pattern, different aggregator (result: **15.96**).

## X Aggregator Family

| Function | Returns | Notes |
|----------|---------|-------|
| `SUMX` | Sum | Most commonly used |
| `MINX` | Minimum | Often paired with `FILTER` for conditional lookups |
| `MAXX` | Maximum | Often paired with `FILTER` for conditional lookups |
| `AVERAGEX` | Arithmetic mean | Iterates; unlike `AVERAGE`, works with filtered tables |
| `COUNTX` | Count of non-blank rows | Iterator equivalent of `COUNT` |
| `COUNTAX` | Count including TRUE/FALSE | Iterator equivalent of `COUNTA` |
| `PRODUCTX` | Product of expression | Iterator equivalent of `PRODUCT` |

## Variations

**Compound filter (multiple conditions):**
```dax
AVERAGEX(
    FILTER(
        'Table',
        'Table'[Item] = "Banana" && 'Table'[Quantity] >= 2
    ),
    [Total Cost]
)
```

**Nested table building with SUMMARIZE:**
```dax
SUMX(
    SUMMARIZE(
        'Table',
        'Table'[Item],
        "__Total", SUM( 'Table'[Total Cost] )
    ),
    [__Total]
)
```

## Related

- [No CALCULATE Banana Pattern](/wiki/no-calculate-banana-pattern.md) — the pattern that combines FILTER + X aggregator
- [DAX Variables](/wiki/dax-variables-var-return.md) — typically used to store the table expression in a VAR
- [FILTER](/wiki/filter.md) — the function used to create the table argument
- [DAX Context](/wiki/dax-context-row-filter.md) — row context and filter context in iterator functions

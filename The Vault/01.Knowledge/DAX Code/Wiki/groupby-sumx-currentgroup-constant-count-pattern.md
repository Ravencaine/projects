---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
note_type: pattern
tags: [dax, pattern, groupby, currentgroup, sumx, count, variable-table]
---

# GROUPBY + SUMX(CURRENTGROUP(), 1) — Counting Rows by Variable Table

`GROUPBY` does not accept aggregators directly — it requires iterating over `CURRENTGROUP()` with an iterator. To count rows per group of a *variable* (non-model) table, use `SUMX(CURRENTGROUP(), 1)` to sum a constant 1.

## Purpose

Count the number of rows per group when the source table is a `VAR` (not a model table) and the counting logic must apply per group — a common need when computing "how many times did X appear in Y" over a virtual table built earlier in the same measure.

## The Problem

`GROUPBY`'s aggregation expressions must be iterators over `CURRENTGROUP()`. The aggregator set is fixed: `AVERAGEX`, `COUNTAX`, `COUNTX`, `GEOMEANX`, `MAXX`, `MINX`, `PRODUCTX`, `STDEVX.S`, `STDEVX.P`, `SUMX`, `VARX.S`, `VARX.P`.

`COUNTROWS` is *not* in that list. So this fails:

```dax
-- ❌ Error: COUNTROWS cannot be used directly as an aggregation in GROUPBY
GROUPBY (
    YearsAndTop10,
    'Product'[ProductKey],
    "NumOfYears", COUNTROWS ( CURRENTGROUP () )    -- not allowed
)
```

`SUMX` is the workhorse — it iterates over its table argument and sums the result of an expression evaluated per row.

## Components

- `GROUPBY(<table>, <groupBy_columns>, [<name>, <expression>]…)` — group a virtual table by columns
- `CURRENTGROUP()` — returns the subset of rows for the current group (only valid inside `GROUPBY`'s aggregation expressions)
- `SUMX(CURRENTGROUP(), 1)` — iterate over the group, evaluate a constant `1` per row, sum the results → row count

## Structure

```dax
VAR SourceTable = ...   -- some virtual table built earlier in the measure
VAR Grouped =
    GROUPBY (
        SourceTable,
        SourceTable[KeyColumn],
        "RowCount", SUMX ( CURRENTGROUP (), 1 )
    )
RETURN
    Grouped
```

`SUMX(CURRENTGROUP(), 1)` sums `1` for each row in the current group → produces the row count for that group.

## Example

In the evergreen-top-N-products pattern, the source table is `(Year, ProductKey)` pairs built by `GENERATE(Years, TOPN(...))`. We want to count how many years each product appears in:

```dax
VAR YearsAndTop10 =
    CALCULATETABLE (
        GENERATE (
            CALCULATETABLE (
                SUMMARIZE ( Sales, 'Date'[Year] ),
                ALLSELECTED ()
            ),
            TOPN (
                10,
                VALUES ( 'Product'[ProductKey] ),
                [Sales Amount]
            )
        ),
        ALLSELECTED ()
    )
VAR ProdsAndCount =
    GROUPBY (
        YearsAndTop10,
        'Product'[ProductKey],
        "NumOfYears", SUMX ( CURRENTGROUP (), 1 )    -- counts how many years per product
    )
```

The resulting table has one row per product with `NumOfYears` equal to the count of years that product appeared in the top 10.

## Variations

| Need | Aggregation expression |
|---|---|
| Count rows | `"Count", SUMX ( CURRENTGROUP (), 1 )` |
| Sum a column | `"Total", SUMX ( CURRENTGROUP (), SourceTable[Amount] )` |
| Average | `"Avg", AVERAGEX ( CURRENTGROUP (), SourceTable[Amount] )` |
| Min / Max per group | `"Min", MINX ( CURRENTGROUP (), SourceTable[Amount] )` |
| Standard deviation | `"StDev", STDEVX.S ( CURRENTGROUP (), SourceTable[Amount] )` |

For non-constant counts (e.g., conditional: count only rows where amount > 0), use `SUMX(CURRENTGROUP(), IF(<condition>, 1, 0))` — same idiom, conditional constant.

## Why Not SUMMARIZE?

`SUMMARIZE` would also work for simple aggregations:

```dax
VAR ProdsAndCount =
    SUMMARIZE (
        YearsAndTop10,
        'Product'[ProductKey],
        "NumOfYears", COUNTROWS ( YearsAndTop10 )   -- ❌ wrong: counts total, not per group
    )
```

`COUNTROWS(YearsAndTop10)` returns the *total* row count, not per-group. To get per-group, you'd need either:

- `SUMMARIZECOLUMNS` with `FILTER` inside the aggregation (often harder to read)
- A calculated column on a physical table (not applicable to a virtual VAR)
- `GROUPBY` + `CURRENTGROUP()` — the only clean idiom for per-group aggregation over a variable table

The official Microsoft Learn distinction is documented in SQLBI's "[Differences between GROUPBY and SUMMARIZE](https://www.sqlbi.com/articles/differences-between-groupby-and-summarize/)" — `GROUPBY` is for situations where you need iterator-based aggregation over a virtual table.

## Why Not ADDCOLUMNS + COUNTROWS?

```dax
VAR ProdsAndCount =
    ADDCOLUMNS (
        VALUES ( 'Product'[ProductKey] ),
        "NumOfYears",
        VAR __Rows =
            FILTER ( YearsAndTop10, 'Product'[ProductKey] = ... )
        RETURN
            COUNTROWS ( __Rows )
    )
```

Works, but iterates `VALUES('Product'[ProductKey])` — every product in the dimension, not just the ones that appear in `YearsAndTop10`. For a sparse dimension (millions of products) this is wasteful. `GROUPBY` only creates one row per *existing* group in the source table.

## Common Pitfalls

- Using `COUNTROWS(CURRENTGROUP())` directly — runtime error
- Using `COUNTROWS(SourceTable)` inside `GROUPBY`'s aggregation — counts the *whole* source table, not the current group
- Forgetting that `CURRENTGROUP()` is only valid inside a `GROUPBY` aggregation expression
- Using `GROUPBY` on a model table when `SUMMARIZECOLUMNS` would suffice — `GROUPBY` has no `IGNORE`/`ROLLUPGROUP` support, less flexibility

## Related

- [[currentgroup]] — function reference (and the only aggregator set)
- [[groupby]] — function reference
- [[summarize]] — when SUMMARIZE is the better choice
- [[grouping-rows-in-dax]] — overview of grouping idioms
- [[evergreen-top-n-products-pattern]] — pattern that uses this idiom
- [[Author-Marco-Russo-Alberto-Ferrari]] — SQLBI co-founders
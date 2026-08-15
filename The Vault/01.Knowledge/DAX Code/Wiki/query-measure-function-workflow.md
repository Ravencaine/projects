---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
note_type: workflow
tags: [dax, workflow, measure-development, udf, query-first, sqlbi]
---

# Query → Measure → Function Workflow for Non-Trivial DAX

A three-stage authoring protocol for DAX measures that manipulate tables: prototype in a query, then move into a measure to handle filter context, then extract into a function once the logic stabilises.

## Prerequisites

- A clear business question that requires table manipulation (top-N, ranking, period-by-period, etc.)
- DAX Studio, Power BI Desktop DAX query view, or Tabular Editor — for running queries against the model
- A test report with the target matrix/visual layout — to verify filter-context behaviour

## Steps

### 1. Prototype the logic in a DAX query

Write the business logic as a standalone `EVALUATE` query with `VAR` blocks. Run it in DAX Studio or the Power BI DAX query view.

Why first:

- A query has **no outer filter context:** easier to reason about the table transformations in isolation
- You can inspect intermediate `VAR` results by changing the `RETURN` clause (e.g., `RETURN YearsAndTop10` to see the year-by-top-N table)
- Debugging is faster — you see the raw rows, not a confusing aggregate number
- No risk of accidentally shipping a broken measure into production reports

```dax
EVALUATE
VAR NumOfTop = 10
VAR Coverage = 0.8
VAR Years =
    SUMMARIZE ( Sales, 'Date'[Year] )
VAR NumOfYears =
    COUNTROWS ( Years )
VAR YearsAndTop10 =
    GENERATE (
        Years,
        TOPN ( NumOfTop, VALUES ( 'Product'[ProductKey] ), [Sales Amount] )
    )
VAR ProdsAndCount =
    GROUPBY (
        YearsAndTop10,
        'Product'[ProductKey],
        "NumOfYears", SUMX ( CURRENTGROUP (), 1 )
    )
VAR MinYears = NumOfYears * Coverage
VAR BestProds =
    FILTER ( ProdsAndCount, [NumOfYears] >= MinYears )
RETURN
    BestProds
```

Iterate until the final table is correct.

### 2. Move the code into a measure — fix filter-context issues

Copy the `VAR` block into a measure. The first run will almost certainly produce wrong numbers because of the outer filter context (matrix row, slicer selection, etc.).

Common filter-context leaks:

- `SUMMARIZE(Sales, 'Date'[Year])` only sees the currently-filtered years → wrap in `CALCULATETABLE(... ALLSELECTED())`
- `TOPN(...)` evaluates `[Sales Amount]` in the deeply-filtered context → wrap the whole `GENERATE(...TOPN(...))` in `CALCULATETABLE(... ALLSELECTED())`
- The final filter table (`BestProds`) uses `Product[ProductKey]` — applying via `CALCULATE(<expr>, BestProds)` will *overwrite* any matrix filter on `Product[ProductKey]` → wrap in `KEEPFILTERS(BestProds)`

```dax
Num Best Prods :=
VAR NumOfTop = 10
VAR Coverage = 0.8
VAR Years =
    CALCULATETABLE (
        SUMMARIZE ( Sales, 'Date'[Year] ),
        ALLSELECTED ()
    )
VAR NumOfYears = COUNTROWS ( Years )
VAR YearsAndTop10 =
    CALCULATETABLE (
        GENERATE (
            Years,
            TOPN ( NumOfTop, VALUES ( 'Product'[ProductKey] ), [Sales Amount] )
        ),
        ALLSELECTED ()
    )
VAR ProdsAndCount =
    GROUPBY (
        YearsAndTop10,
        'Product'[ProductKey],
        "NumOfYears", SUMX ( CURRENTGROUP (), 1 )
    )
VAR MinYears = NumOfYears * Coverage
VAR BestProds =
    FILTER ( ProdsAndCount, [NumOfYears] >= MinYears )
VAR Result =
    CALCULATE ( COUNTROWS ( 'Product' ), KEEPFILTERS ( BestProds ) )
RETURN
    Result
```

Test in the target matrix/visual. For each row, column, and total — verify the numbers match expectations.

### 3. Extract a UDF once the logic is reused

If the same top-N-then-frequency-then-filter chain will be applied to more than one measure (e.g., `Num Best Prods` and `Sales Best Prods`), extract it into a UDF.

```dax
DEFINE
FUNCTION Local.ComputeForBestProds ( computeExpr : EXPR, sortExpr : EXPR ) =>
    -- ... same VAR chain ...
    CALCULATE ( computeExpr, KEEPFILTERS ( BestProds ) )
EVALUATE
```

Then the measures become one-liners:

```dax
Num Best Prods   := Local.ComputeForBestProds ( COUNTROWS ( 'Product' ), [Sales Amount] )
Sales Best Prods := Local.ComputeForBestProds ( [Sales Amount], [Sales Amount] )
```

When promoting to a UDF, wrap the sort expression in `CALCULATE(sortExpr)` inside `TOPN` — this ensures the expression evaluates in the right context regardless of the argument's form (measure, column, literal).

## Variations

| Situation | Skip to step |
|---|---|
| The "measure" is purely a calculated table on the model | Step 1 only — write the query, save as a calculated table. No filter-context issues. |
| Only one measure needs the logic | Stop after step 2 — don't extract a UDF for a single caller |
| The table logic produces a static list (no filter context issues) | Step 1 + step 2 in one pass — measure directly from query, no `ALLSELECTED` or `KEEPFILTERS` needed |
| The logic is itself parameter-dependent (different N, different threshold) | Add a parameter table or `SELECTEDVALUE` from the start — step 2 may need to handle parameter changes |

## Common Errors

- [[TopN-ProductKey-Override-Gotcha]] — BestProds filter replaces outer ProductKey filter without KEEPFILTERS
- [[filter-functions-allexcept-keepfilters]] — KEEPFILTERS intersects; the default CALCULATE filter argument replaces. Wrong choice silently produces wrong numbers.
- [[auto-exist-and-all-gotchas]] — `SUMMARIZE` is affected by auto-exist; if your year list collapses unexpectedly, that's why
- [[avoid-using-filter-as-filter-argument]] — `CALCULATE(<expr>, FILTER(...))` is the slower form; use direct filters where possible

## Related

- [[dax-queries]] — DAX query syntax basics
- [[dax-user-defined-functions-udf]] — UDF authoring
- [[Local-Wrapper-UDF-Pattern]] — `Local.*` prefix convention for model-dependent wrappers
- [[dax-udf-define-function-pattern]] — full DEFINE FUNCTION syntax
- [[UDF-Generalization-Workflow]] — three-stage refactor for any working pattern into a reusable library
- [[Evergreen-Top-N-Products]] — worked example of this workflow
- [[Virtual-Table-Debugging-via-Calculated-Tables]] — debugging virtual tables via physical calculated tables
- [[Author-Marco-Russo-Alberto-Ferrari]] — originators of the protocol
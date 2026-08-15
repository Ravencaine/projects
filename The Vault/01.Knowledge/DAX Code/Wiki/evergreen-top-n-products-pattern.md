---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
note_type: pattern
tags: [dax, pattern, top-n, ranking, evergreen, generate, topn, groupby, currentgroup, allselected, keepfilters, coverage]
---

# Evergreen Top-N Products Pattern

Find the products that consistently rank in the top N across multiple time periods — "evergreen" SKUs that survive year after year.

## Purpose

Standard Top-N rankings show the best sellers *in the current filter context*. This pattern answers a different business question: which products *persistently* rank in the top N across years, quarters, or any other time dimension? Useful for:

- Identifying evergreen SKUs (vs. fads that spike one year)
- Supplier consolidation (negotiate long-term contracts on products that stay best-sellers)
- Inventory strategy (stock levels for products with sustained demand)
- Product portfolio review (which products have stable demand vs. which need promotion)

## Components

- `SUMMARIZE` — enumerate the period dimension (e.g., distinct years)
- `GENERATE` — crossjoin each period with its top N rows
- `TOPN` — extract the top N within each group's filter context
- `GROUPBY` + `SUMX(CURRENTGROUP(), 1)` — count how often each product appears
- `CALCULATETABLE(... ALLSELECTED())` — decouple the top-N logic from outer filter context
- `FILTER` with `Coverage` threshold (e.g., 0.8) — keep only products that appear in ≥80% of periods
- `CALCULATE(... KEEPFILTERS(BestProds))` — apply the resulting product list without overwriting report filters

## Structure

```dax
Evergreen Prods :=
VAR NumOfTop   = 10
VAR Coverage   = 0.8
VAR Years =
    CALCULATETABLE (
        SUMMARIZE ( Sales, 'Date'[Year] ),
        ALLSELECTED ()
    )
VAR NumOfYears =
    COUNTROWS ( Years )
VAR YearsAndTop10 =
    CALCULATETABLE (
        GENERATE (
            Years,
            TOPN (
                NumOfTop,
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
        "NumOfYears", SUMX ( CURRENTGROUP (), 1 )
    )
VAR MinYears =
    NumOfYears * Coverage
VAR BestProds =
    FILTER ( ProdsAndCount, [NumOfYears] >= MinYears )
RETURN
    BestProds
```

Then apply the list via `CALCULATE` with `KEEPFILTERS`:

```dax
Num Best Prods :=
CALCULATE (
    COUNTROWS ( 'Product' ),
    KEEPFILTERS ( [Evergreen Prods] )
)
```

## Example

In Russo & Ferrari's demo, with 5 years of data and `NumOfTop = 10`, the algorithm:

1. Produces a 50-row table of `(Year, ProductKey)` — 10 products per year
2. Groups by product, counts how many years each product appears
3. Filters to products appearing in ≥4 of 5 years (Coverage = 0.8)
4. Returns 5 "evergreen" products, 1 of which is in all 5 years

The resulting product list is dynamic — it reacts to slicer selections on year ranges, product categories, or any other dimension that flows through `ALLSELECTED()`.

## Variations

| Variation | Change | Use when |
|---|---|---|
| Top N by a different metric | Swap `[Sales Amount]` for `[Units Sold]`, `[Margin]`, etc. | You want the evergreen list *by a criterion other than revenue* |
| Top N per quarter / month | Change `SUMMARIZE (Sales, 'Date'[Year])` to `'Date'[Quarter]` or `'Date'[Month]` | The "period" dimension is finer than year |
| Per category | Add `'Product'[Category]` to the `SUMMARIZE` group-by | You want category-specific evergreen lists (then add Category to the final filter) |
| Threshold-based instead of coverage | Replace `NumOfYears * Coverage` with a fixed integer like `>= 4` | The period count is unstable (e.g., partial first/last year) |
| Parameterised N | Read `NumOfTop` from a slicer via `SELECTEDVALUE` | Power users want to explore 5/10/20 |

### Function form (preferred when reused across measures)

When multiple measures need the same evergreen product list, extract it into a UDF:

```dax
DEFINE
FUNCTION Local.ComputeForBestProds ( computeExpr : EXPR, sortExpr : EXPR ) =>
    VAR NumOfTop   = 10
    VAR Coverage   = 0.8
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
                TOPN (
                    NumOfTop,
                    VALUES ( 'Product'[ProductKey] ),
                    CALCULATE ( sortExpr )
                )
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
        CALCULATE ( computeExpr, KEEPFILTERS ( BestProds ) )
    RETURN
        Result
EVALUATE
```

Then call from multiple measures:

```dax
Num Best Prods := Local.ComputeForBestProds ( COUNTROWS ( 'Product' ), [Sales Amount] )
Sales Best Prods := Local.ComputeForBestProds ( [Sales Amount], [Sales Amount] )
```

Note the `CALCULATE(sortExpr)` wrapping inside `TOPN` — this is the UDF evaluation-mode idiom that ensures the sort expression evaluates correctly regardless of argument type.

## Why This Pattern Works

1. **`GENERATE` runs `TOPN` per period row.** For each year in `Years`, `TOPN` evaluates against the filter context of that year, returning the 10 best products. The result is the crossjoin of years × their top products.
2. **`GROUPBY` + `SUMX(CURRENTGROUP(), 1)` counts appearances.** `COUNTROWS` cannot be used directly inside `GROUPBY` — the function requires iterating over `CURRENTGROUP()` via an iterator. Summing a constant 1 across the group produces the count.
3. **`CALCULATETABLE(... ALLSELECTED())` keeps the logic slicer-aware.** Without it, the `TOPN` would be computed in the deeply-filtered matrix context (per row) instead of the user's chosen selection (e.g., the year range they picked).
4. **`KEEPFILTERS(BestProds)` avoids overwriting report filters.** By default, `CALCULATE(<expr>, T)` *replaces* filters on columns in `T` with the filter from `T`. If the report uses `Product[ProductKey]` as a row label, the matrix filter would be replaced by the product list — wrong. `KEEPFILTERS` intersects instead.
5. **`Coverage` threshold makes "evergreen" definable.** A fixed number of years (e.g., `>= 4`) breaks when the data spans a non-integer number of years. Using `NumOfYears * Coverage` (e.g., 0.8) scales naturally.

## Common Pitfalls

- **Forgetting `ALLSELECTED`** → the top-N list shrinks to per-cell rows and the measure returns 1 everywhere
- **Using `CALCULATE(computeExpr, BestProds)` without `KEEPFILTERS`** → the product filter overrides any matrix column on `Product[ProductKey]`, returning incorrect counts
- **Using `COUNTROWS` inside `GROUPBY`** → runtime error; must wrap in `SUMX(CURRENTGROUP(), 1)` or similar iterator
- **Missing `CALCULATE` around UDF argument inside `TOPN`** → sort expression may not evaluate in the expected filter context when called from a UDF

## Related

- [[topn]] — TOPN function reference and idioms
- [[generate]] — GENERATE / GENERATEALL semantics
- [[groupby]] — GROUPBY function (article pattern uses GROUPBY + CURRENTGROUP)
- [[currentgroup]] — COUNTROWS-inside-GROUPBY workaround via `SUMX(CURRENTGROUP(), 1)`
- [[allselected]] — decouples measure logic from slicer selection
- [[keepfilters]] — intersect-vs-replace filter semantics
- [[dax-user-defined-functions-udf]] — UDF extraction of this pattern
- [[Local-Wrapper-UDF-Pattern]] — `Local.*` prefix convention for model-dependent wrappers
- [[Author-Marco-Russo-Alberto-Ferrari]] — SQLBI co-founders
- [[TopN-ProductKey-Override-Gotcha]] — BestProds filter overrides outer ProductKey filter without KEEPFILTERS
- [[Source-SQLBI-Top-10-Every-Year]] — full source from SQLBI (Nov 2025)
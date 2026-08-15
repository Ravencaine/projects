---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
note_type: function
tags: [dax, udf, top-n, evergreen, sqlbi]
---

# Local.ComputeForBestProds

A DAX user-defined function that evaluates an expression only for products appearing in the top-N across a coverage fraction of the visible years.

## Signature

```dax
Local.ComputeForBestProds ( computeExpr : EXPR, sortExpr : EXPR )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `computeExpr` | EXPR | The expression to evaluate — e.g. `[Sales Amount]` or `COUNTROWS('Product')`. The result is returned only for evergreen top-N products. |
| `sortExpr` | EXPR | The measure or column used to rank products in TOPN — typically the same measure as `computeExpr` when ranking by value (e.g. `[Sales Amount]`). Can be any ranking expression. |

## Returns

The value of `computeExpr` filtered to only products that appear in the top-N in at least `Coverage × TotalYears` years.

Returns BLANK if no product qualifies.

## Algorithm

```
1. Enumerate visible years via SUMMARIZE(Sales, 'Date'[Year]) wrapped in CALCULATETABLE(... ALLSELECTED())
2. For each year, produce top-N products via GENERATE + TOPN — wrapped in CALCULATETABLE(... ALLSELECTED())
3. GROUPBY to count appearances per product: NumOfYears = SUMX(CURRENTGROUP(), 1)
4. FILTER to products where NumOfYears >= NumOfYears × Coverage (coverage default = 0.8)
5. Apply BestProds as KEEPFILTERS(computeExpr) — intersects with outer filter context
```

## Examples

```dax
-- Count of evergreen top-10 products
Num Best Prods :=
    Local.ComputeForBestProds ( COUNTROWS ( 'Product' ), [Sales Amount] )

-- Sum of sales for evergreen top-10 products
Sales Best Prods :=
    Local.ComputeForBestProds ( [Sales Amount], [Sales Amount] )
```

## Notes

- **Model dependency:** this function references `Sales`, `'Date'[Year]`, and `'Product'[ProductKey]` directly. It is a `Local.*` model-dependent wrapper UDF — do not move it to a model-independent library without parameterising those columns.
- **Coverage:** hard-coded to 0.8 (80%) internally. To make it a parameter, add a third `EXPR` argument.
- **NumOfTop:** hard-coded to 10. To make it configurable, add a parameter.
- **sortExpr wrapping:** `sortExpr` is wrapped in `CALCULATE(sortExpr)` inside `TOPN`. This ensures correct evaluation regardless of the expression type passed (measure reference, column reference, or literal).
- **`GROUPBY` + `SUMX(CURRENTGROUP(), 1)`:** `COUNTROWS(CURRENTGROUP())` does not work inside `GROUPBY` — `SUMX(CURRENTGROUP(), 1)` is the correct replacement.

## Related

- [[Evergreen-Top-N-Products]] — the atomic concept this function implements
- [[query-measure-function-workflow]] — the three-stage workflow that produced this function
- [[Local-Wrapper-UDF-Pattern]] — Local.* naming convention for model-dependent wrappers
- [[UDF-Generalization-Workflow]] — how to extract model objects as parameters to generalize this function
- [[TopN-ProductKey-Override-Gotcha]] — the gotcha that motivated the `KEEPFILTERS` wrapper
- [[Source-SQLBI-Top-10-Every-Year]] — primary source from SQLBI

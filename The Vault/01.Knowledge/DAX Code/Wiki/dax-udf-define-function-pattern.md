---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: pattern
tags: [dax, user-defined-function, pattern, syntax, boilerplate, tmdl]
---

# DEFINE FUNCTION Syntax Pattern

The canonical pattern for defining a DAX user-defined function with a doc comment, typed parameters, and an explicit evaluation mode.

## Purpose

Provide a reusable, readable, first-class function object in the semantic model. The function lives in Model Explorer, is version-controlled via TMDL, and is callable from measures, columns, visual calculations, and other functions.

## Components

- Triple-slash doc comment (`///`) — Model Explorer description
- Namespace-prefixed function name (PascalCase with dot separator)
- Typed parameter list with optional evaluation mode (`VAL` or `EXPR`)
- Arrow (`=>`) introducing the function body
- DAX expression body

## Structure

```dax
DEFINE
/// <one-sentence description of what the function does>
/// <optional: edge case, parameter description, or usage note>
FUNCTION <Namespace>.<FunctionName> = (
    <paramName> : <Type> [VAL | EXPR],
    <paramName> : <Type> [VAL | EXPR]
) =>
    <DAX expression>

-- Example usage:
MEASURE <Table>[<MeasureName>] = <Namespace>.<FunctionName> ( <args> )
```

## Example

```dax
DEFINE
/// Calculates net amount after applying the specified discount rate
/// Falls back to 0 when amount is blank or zero
FUNCTION Finance.ApplyDiscount = (
    amount : CURRENCY VAL,
    discountRate : DECIMAL VAL
) =>
    DIVIDE (
        amount * (1 - discountRate),
        1,
        0
    )

EVALUATE { Finance.ApplyDiscount ( 1000, 0.15 ) }   // Returns 850
```

## Variations

### With EXPR Parameter (Context-Deferred)

```dax
DEFINE
/// Sums baseAmount applying the intercompany exclusion filter
FUNCTION Finance.NetRevenue = (
    baseAmount : CURRENCY EXPR
) =>
    CALCULATE (
        baseAmount,
        REMOVEFILTERS ( 'Date' ),
        'Fiscal Settings'[IncludeInterco] = TRUE ()
    )

-- Usage:
MEASURE Sales[NetRev] = Finance.NetRevenue( SUM(Sales[Amount]) )
```

### With Multiple Parameters and Mixed Modes

```dax
DEFINE
/// Returns the proportion of total sales for the given amount expression
FUNCTION Analytics.SalesRatio = (
    amountExpr : CURRENCY EXPR,
    totalAmount : CURRENCY EXPR
) =>
    DIVIDE (
        amountExpr,
        totalAmount,
        0
    )

MEASURE Sales[SalesPct] = Analytics.SalesRatio(
    SUM(Sales[Amount]),
    CALCULATE( SUM(Sales[Amount]), REMOVEFILTERS() )
)
```

### Safe Divide Pattern

```dax
DEFINE
/// Safely divides numerator by denominator, returning defaultValue when denominator is 0
FUNCTION Math.SafeDivide = (
    numerator : NUMERIC VAL,
    denominator : NUMERIC VAL,
    defaultValue : NUMERIC VAL
) =>
    DIVIDE ( numerator, denominator, defaultValue )
```

## PBIP File Location

In a Power BI Project (.pbip), functions live in:

```
model/
  functions.tmdl
```

This makes functions first-class version-controlled objects — a structural change from the copy-paste era.

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[val-vs-expr-parameter-evaluation]] — gotcha
- [[dax-udf-adoption-workflow]] — workflow

---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: snippet
tags: [dax, user-defined-function, boilerplate, syntax, template]
---

# DAX UDF Boilerplate (DEFINE FUNCTION)

Ready-to-use function definition boilerplates for common UDF scenarios.

## Minimal Function (VAL parameters)

```dax
DEFINE
/// <description: what this returns>
FUNCTION <Namespace>.<FunctionName> = (
    <param> : <Type> VAL
) =>
    <expression>
```

## Function with EXPR Parameter (Deferred Evaluation)

```dax
DEFINE
/// <description: what this returns, including any context dependency>
FUNCTION <Namespace>.<FunctionName> = (
    <paramExpr> : <Type> EXPR
) =>
    CALCULATE(
        <paramExpr>,
        <filter1>,
        <filter2>
    )
```

## Safe Divide with Default

```dax
DEFINE
/// <description: safely divides numerator by denominator>
FUNCTION Math.SafeDivide = (
    numerator     : NUMERIC VAL,
    denominator  : NUMERIC VAL,
    defaultValue : NUMERIC VAL
) =>
    DIVIDE ( numerator, denominator, defaultValue )
```

## Business Logic: Apply Discount Rate

```dax
DEFINE
/// <description: returns amount after applying discount rate>
FUNCTION Finance.ApplyDiscount = (
    amount      : CURRENCY VAL,
    discountRate: DECIMAL  VAL
) =>
    amount * (1 - discountRate)
```

## Tax Application with Business Logic

```dax
DEFINE
/// <description: applies tax rate to amount, returns 0 if amount is blank>
FUNCTION Finance.AddTax = (
    amount  : CURRENCY VAL,
    taxRate : DECIMAL  VAL
) =>
    VAR _amount = IF ( ISBLANK(amount), 0, amount )
    RETURN
        _amount * (1 + taxRate)
```

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[dax-udf-define-function-pattern]] — pattern
- [[val-vs-expr-parameter-evaluation]] — gotcha

---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: gotcha
tags: [dax, user-defined-function, val, expr, evaluation-mode, context-transition, bug]
---

# VAL vs EXPR Parameter Evaluation Modes

Every UDF parameter has an evaluation mode. Choosing the wrong one silently produces wrong numbers — no error, no warning.

## Expected Behaviour

A function parameter receives the expression you passed to it, evaluates correctly, and returns the right answer.

## Actual Behaviour

With `VAL` (the default), the argument is evaluated **immediately** in the outer filter context before the function runs. The resulting value — not the expression — is passed in.

With `EXPR`, the unevaluated expression is passed in, and the function decides when and in what filter context to evaluate it.

```dax
-- VAL (default): the FILTER result is evaluated here, in the outer context,
-- before SafeDivide runs. The table is already filtered.
FUNCTION Math.SafeDivide = (
    numerator : NUMERIC VAL,
    denominator : NUMERIC VAL
) =>
    DIVIDE ( numerator, denominator )

-- The numerator and denominator arrive as VALUES, not expressions.
-- The function CANNOT re-evaluate them under a different context.
```

## Why It Happens

DAX evaluation timing is the entire game. Filter context and context transition determine what a DAX expression returns. When the caller passes an expression to a function:

- **VAL:** the expression is evaluated first. The function receives a scalar value. If the function then tries to run CALCULATE or change context, the original expression is gone — it's just a number.
- **EXPR:** the function receives the expression object. It can choose when to evaluate it — in the outer context, in an altered context, or multiple times with different filters.

## The Silent Failure

A function using VAL parameters on an expression like `CALCULATE(SUM(Sales[Amount]), FILTER(Product, Product[Color]="Red"))` will silently evaluate the FILTER in the outer context before the function body runs. If the function then tries to apply its own CALCULATE, the FILTER has already fired — the wrong set of rows may have been selected.

Result: a plausible-looking wrong number. No error message. Only visible when reconciled against the source system.

## How to Handle It

1. **Decide VAL or EXPR explicitly for every parameter**: the default is a deferral, not a decision
2. Use `EXPR` when the function body calls `CALCULATE`, changes filter context, or iterates
3. Use `VAL` for simple scalar inputs where context is not relevant
4. **Test every function from at least two calling contexts** before trusting it:
   - As a measure
   - As a calculated column
   - As an iterator (if applicable)
5. The VAL/EXPR class of bug only surfaces when the calling context changes — so change it yourself before production does

```dax
-- Correct EXPR usage: the function owns the CALCULATE context
FUNCTION Finance.NetRevenue = (
    baseAmount : CURRENCY EXPR
) =>
    CALCULATE (
        baseAmount,
        REMOVEFILTERS ( 'Date' ),
        'Fiscal Settings'[IncludeInterco] = TRUE ()
    )
```

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[context-transition-with-calculate]] — DAX Code KB

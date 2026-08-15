---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: function
tags: [dax, udf, currency, growth, anyref, expression, context-transition, parameter]
---

# dwp.CurrencyAwareGrowth — AnyRef Expression Parameter UDF

Demonstrates the correct use of an `AnyRef` expression parameter for context-correct growth% calculation. The key worked example that taught why parameter types matter.

## The Problem with Value Parameters

The original growth% measure needed to reference a different measure depending on the calling context (gross sales vs. net sales). Passing the measure as a `NUMERIC` (value) parameter evaluated it too early — in the caller's filter context — and silently returned the wrong number. The total row showed incorrect values with no error.

## The Fix: AnyRef Expression Parameter

Switching the parameter to `AnyRef` (expression type) passes the measure expression unevaluated. The UDF wraps the internal call in an explicit `CALCULATE`, controlling the evaluation context from inside the function body.

```dax
DEFINE
    /// Returns the % growth of the given expression vs the same expression
    /// in the previous period. Uses AnyRef so the function controls context.
    /// @param {AnyRef} MeasureExpr — the measure to compute growth% for
    /// @param {NUMERIC} PriorPeriodValue — the prior period value (passed as NUMERIC)
    FUNCTION dwp.CurrencyAwareGrowth = (
        MeasureExpr: AnyRef,
        PriorPeriodValue: NUMERIC
    ) =>
        VAR _current = CALCULATE ( MeasureExpr )   -- CALCULATE needed: controls context
        VAR _growth = DIVIDE ( _current - PriorPeriodValue, PriorPeriodValue )
        RETURN
            IF ( ISBLANK ( _growth ), BLANK(), _growth )
```

## Key Lesson

`CALCULATE ( MeasureExpr )` inside the UDF only works correctly when `MeasureExpr` is declared as `AnyRef`. If declared as `NUMERIC`, the measure is evaluated before `CALCULATE` can act on it — the context transition never fires.

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[Value-vs-Expression-Parameter-Types]] — explains the two parameter modes
- [[AnyRef-Expression-Parameter-Bug]] — gotcha: what goes wrong with the wrong type

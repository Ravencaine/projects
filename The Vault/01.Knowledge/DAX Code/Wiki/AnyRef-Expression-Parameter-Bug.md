---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: gotcha
tags: [dax, udf, anyref, expression, parameter, context-transition, silent-bug]
---

# AnyRef Expression Parameter Bug — Wrong Type Causes Silent Context Failure

Passing a measure as a value parameter (NUMERIC) instead of an expression parameter (AnyRef) causes the measure to be evaluated too early — in the caller's filter context. The result is silently wrong with no error or warning.

## The Bug in Practice

```dax
-- WRONG: measure passed as NUMERIC (value type)
DEFINE
    FUNCTION dwp.CurrencyAwareGrowth = (
        MeasureExpr: NUMERIC,      -- WRONG: value type
        PriorPeriodValue: NUMERIC
    ) =>
        VAR _current = CALCULATE(MeasureExpr)   -- CALCULATE here has no effect
        RETURN DIVIDE(_current - PriorPeriodValue, PriorPeriodValue)

-- Calling it:
dwp.CurrencyAwareGrowth([Total Sales], 100000)
-- Measure evaluated BEFORE CALCULATE wraps it → wrong context, wrong total
```

## Why It's Silent

The measure returns a number. `CALCULATE` doesn't throw an error when applied to an already-evaluated scalar — it just returns the same number. There is no error, no warning, no indication that the context transition never fired. Visuals just show the wrong total.

## The Fix

```dax
-- CORRECT: measure passed as AnyRef (expression type)
DEFINE
    FUNCTION dwp.CurrencyAwareGrowth = (
        MeasureExpr: AnyRef,        -- CORRECT: expression type
        PriorPeriodValue: NUMERIC
    ) =>
        VAR _current = CALCULATE(MeasureExpr)   -- NOW CALCULATE controls context
        RETURN DIVIDE(_current - PriorPeriodValue, PriorPeriodValue)
```

## How to Detect

1. Create a matrix with subtotals
2. Call the UDF with a measure
3. Compare the UDF total against the raw measure total — if they differ, the parameter type is wrong

## Rule

If the UDF body needs to control the evaluation context of a parameter — wrap it in CALCULATE, CALCULATETABLE, or any context-modifying function — the parameter must be an **expression type** (`AnyRef` or `CalendarRef`), not a value type.

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[Value-vs-Expression-Parameter-Types]] — atomic: full explanation of the two modes
- [[dwp.CurrencyAwareGrowth]] — worked example

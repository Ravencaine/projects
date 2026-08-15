---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: atomic
tags: [dax, udf, parameters, expression, anyref, context-transition, parameter-types]
---

# Value vs Expression Parameter Types

DAX UDFs have two fundamentally different parameter-passing modes. Choosing the wrong one causes silent bugs.

## Value Types (NUMERIC, TABLE, AnyVal, etc.)

- Evaluate **eagerly:** the argument is fully evaluated the moment the function is called
- The value is captured and passed into the function body
- Appropriate for: constants, column references, table expressions that don't need context transition

## Expression Types (AnyRef, CalendarRef)

- Pass an **unevaluated expression:** the function receives the expression tree and controls when/where to evaluate it
- The function can wrap the expression in its own `CALCULATE` to control context transition
- Required when the parameter needs to reference a measure and have the UDF control the measure's filter context

## The Silent Bug

Passing a measure as a `NUMERIC` value parameter evaluates it **too early:** in the caller's filter context — and returns the wrong result. The total row silently shows the wrong number with no error.

The fix: declare the parameter as `AnyRef` (expression type) and wrap the internal call in an explicit `CALCULATE`. The expression is now evaluated lazily under the function's controlled context.

## When to Use Each

| Use Case | Parameter Type |
|----------|---------------|
| Divide two numbers | `NUMERIC` (value) |
| Reference a column | `NUMERIC` (value — column evaluates in row context) |
| Reference a measure and control its context | `AnyRef` (expression) |
| Pass a date reference for the function to manipulate | `CalendarRef` (expression) |
| Pass a table expression | `TABLE` (value) |

## Rule of Thumb

If the UDF body needs to wrap the parameter in `CALCULATE`, `CALCULATETABLE`, or any context-modifying function — the parameter must be an expression type (`AnyRef` or `CalendarRef`), not a value type.

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[dwp.CurrencyAwareGrowth]] — worked example of AnyRef parameter
- [[AnyRef-Expression-Parameter-Bug]] — gotcha: wrong type causes silent context bug

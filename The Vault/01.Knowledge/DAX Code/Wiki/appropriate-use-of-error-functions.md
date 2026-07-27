---
created: 2026-07-26
source: dax.pdf
note_type: pattern
tags: [dax, pattern, error-handling]
---

# Appropriate Use of Error Functions

ISERROR and IFERROR help handle evaluation-time errors, but misuse degrades performance.

## Purpose

When a DAX expression might raise an error (e.g., division by zero, invalid conversion), error functions can return a safe fallback value. However, wrapping everything in IFERROR hides real problems and slows queries.

## Components

- `ISERROR` — returns TRUE if the expression results in an error
- `IFERROR` — returns the second expression if the first results in an error (optimised form of ISERROR nested in IF)

## Structure

```dax
-- Pattern 1: ISERROR + IF
IF(
    ISERROR([Sales] / [Quantity]),
    BLANK(),
    [Sales] / [Quantity]
)

-- Pattern 2: IFERROR (preferred over ISERROR + IF)
IFERROR([Sales] / [Quantity], BLANK())
```

## When to Use Error Handling

Use error handling when:
- A denominator could be zero and you want BLANK
- An expression involves type conversion that could fail
- You are testing for edge cases in business logic

Avoid error handling when:
- The error signals a real data or model problem (let it surface)
- The same result can be achieved with DIVIDE or other safe functions

## Example

```dax
-- Safe division: use DIVIDE instead of IFERROR
Sales Ratio := DIVIDE([Sales], [Target])

-- When you need a specific fallback value
Conversion Rate := IFERROR(
    [Orders] / [Visits],
    0  -- return 0 when denominator is 0/BLANK
)
```

## Performance Warning

Error handling adds evaluation overhead. Use `DIVIDE` when possible (it already handles division-by-zero safely).

## Related

- [[iferror]] — function
- [[iserror]] — function
- [[divide-function-vs-divide-operator]] — gotcha
- [[blank]] — function

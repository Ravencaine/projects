---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: function
tags: [conditional-logic, branching, color-coding, formatting]
related: [IF, SELECTEDVALUE, CALCULATE]
---

# SWITCH

Evaluates a list of expressions and returns one of multiple possible results. The idiomatic DAX pattern uses `SWITCH(TRUE(), ...)` for a series of boolean conditions.

## Signature

```dax
SWITCH(
    <expression>,
    <value>, <result>[,
    <value>, <result>]...,
    [<else>]
)
```

Or the boolean form (most common in practice):
```dax
SWITCH(
    TRUE(),
    <condition1>, <result1>,
    <condition2>, <result2>,
    ...
    [<else>]
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `expression` | Any | Value to match against listed values (in value-result form) |
| `value` | Scalar | One of the possible values for `expression` |
| `result` | Scalar | Result returned when the corresponding `value` matches |
| `else` | Scalar (optional) | Returned when no value matches |

## Examples

**Color assignment via boolean conditions (Bittar pattern):**
```dax
Vacancy Rate Color =
VAR _No1 = CALCULATE([No.1 Ranking], ALL(...))
VAR _No2 = CALCULATE([No.2 Ranking], ALL(...))
VAR _No3 = CALCULATE([No.3 Ranking], ALL(...))
VAR _Color =
    SWITCH(
        TRUE(),
        SELECTEDVALUE(...) = _No1, [Color Red],
        SELECTEDVALUE(...) = _No2, [Color Red],
        SELECTEDVALUE(...) = _No3, [Color Red],
        [Color Green]
    )
RETURN _Color
```

**Process step fill color:**
```dax
Job Posting Fill Color =
    SWITCH(
        TRUE(),
        [Selected Stage Order] > 1, [_const Color Blue],
        [Selected Stage Order] = 1, [_const Color Orange],
        [_const Color Light Grey]
    )
```

**Alert icon via SWITCH:**
```dax
Alert Icon =
    SWITCH(
        TRUE(),
        [Alert Exists] = "Yes", [_const Icon Alert],
        [_const Icon No Alert]
    )
```

**Dynamic measure selection (Field Parameters pattern):**
```dax
Selected KPI =
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Field Parameter'[Fields]) = "Revenue", [Revenue],
        SELECTEDVALUE('Field Parameter'[Fields]) = "Units Sold", [Units Sold],
        SELECTEDVALUE('Field Parameter'[Fields]) = "Average Price", [Average Price]
    )
```

## Notes

- `SWITCH(TRUE(), ...)` is the DAX equivalent of `IF-THEN-ELSE IF`. It is preferred over nested `IF`s for readability and performance.
- Every color-coding pattern in Isabelle Bittar's articles uses `SWITCH(TRUE(), ...)` — it is the core building block of all conditional formatting in her techniques.
- In the boolean form, conditions are evaluated top-to-bottom; the first `TRUE` wins.
- Always include a final `TRUE()` condition as an `else` to guarantee a result when no condition matches.
- When used with CALCULATE inside `ALL(...)`, SWITCH can force evaluation in a modified filter context (e.g., `ALL(dim[column])` removes a slicer filter).
- Performance: SWITCH with many conditions can be slower than lookup tables, but for <20 branches it is negligible.

## Related

- [[IF]] — simpler two-branch conditional
- [[SELECTEDVALUE]] — read the current slicer value to drive SWITCH conditions
- [[CALCULATE]] — modify filter context inside SWITCH conditions

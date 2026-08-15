---
created: 2026-08-09
updated: 2026-08-09
source: "DAX IF.EAGER Function in Power BI.md"
source_url: https://databear.com/dax-if-eager-function-in-power-bi/
note_type: function
tags: [dax, function, conditional, if.eager, eager, evaluation, performance, databear, boniface-muchendu]
---

# IF.EAGER

Evaluates both branch expressions regardless of the condition result. Eager evaluation ensures each measure in the branches is computed exactly once — unlike IF which evaluates ResultIfFalse twice (once for the condition, once as the return value).

## Syntax

```dax
IF.EAGER(<LogicalTest>, <ResultIfTrue> [, <ResultIfFalse>])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `LogicalTest` | Any expression returning TRUE or FALSE |
| `ResultIfTrue` | Returned when LogicalTest is TRUE |
| `ResultIfFalse` | Returned when LogicalTest is FALSE |

## Returns

One of the two result values depending on the condition.

## IF vs IF.EAGER

| Function | TRUE branch evaluation | FALSE branch evaluation |
|----------|----------------------|----------------------|
| `IF` | Evaluates ResultIfTrue once | Evaluates ResultIfFalse twice (condition + return) |
| `IF.EAGER` | Evaluates ResultIfTrue once | Evaluates ResultIfFalse once |

## Example

```dax
Bigger each month =
IF.EAGER(
    [Last month] > [This month],
    [Last month],
    [This month]
)
```

## When to Use IF.EAGER

- Both branches contain measure references that are expensive to compute
- The same measure appears in both branches
- Branch evaluation cost is comparable to the condition overhead
- Measure references are complex enough that double evaluation is measurable

## When NOT to Use IF.EAGER

- Branches contain simple arithmetic or column references (negligible cost)
- Using variables captures branch values cleanly (IF with VAR):

```dax
Bigger and better =
VAR ThisMonth = [This month]
VAR LastMonth  = [Last month]
RETURN
    IF(
        LastMonth > ThisMonth,
        LastMonth,
        ThisMonth
    )
```

The VAR approach evaluates each measure exactly once and makes the intent explicit. Prefer this pattern for clarity unless profiling shows IF.EAGER is necessary.

## Related

- [[if]] — standard IF (lazy evaluation)
- [[dax-performance-patterns]] — broader performance considerations

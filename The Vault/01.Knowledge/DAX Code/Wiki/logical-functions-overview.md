---
created: 2026-07-26
source: dax.pdf
note_type: concept
tags: [dax, logical-functions, if, switch, and, or, not]
---

# Logical Functions in DAX

Logical functions test a condition and return a value based on the result.

## Core Logical Functions

### IF

```dax
IF(<logical_test>, <value_if_true>[, <value_if_false>])
```

Returns one value if the condition is TRUE, another if FALSE. The third argument (value_if_false) is optional — returns BLANK if omitted.

```dax
Grade = IF([Score] >= 90, "A", IF([Score] >= 80, "B", "C"))
```

### IF.EAGER

```dax
IF.EAGER(<logical_test>, <value_if_true>[, <value_if_false>])
```

Same as IF but evaluates both branches eagerly (both branches are computed). Use when the branches may cause errors if not evaluated.

```dax
-- Safe division with error handling
Safe Ratio = IF.EAGER([Denominator] = 0, BLANK(), [Numerator] / [Denominator])
```

### SWITCH

```dax
SWITCH(<expression>, <value1>, <result1>[, <value2>, <result2>][..., <else>])
```

Evaluates an expression against a list of values and returns corresponding results.

```dax
Day Type = SWITCH(
    WEEKDAY([Date]),
    1, "Sunday",
    7, "Saturday",
    "Weekday"
)
```

### AND / OR

```dax
AND(<logical1>, <logical2>)
OR(<logical1>, <logical2>)
```

Both take exactly two arguments. For multiple conditions, use && and || instead:

```dax
-- AND equivalent
[Qty] > 10 && [Price] < 100

-- OR equivalent
[Status] = "Active" || [Status] = "Trial"
```

### NOT

```dax
NOT(<logical>)
```

Returns the opposite Boolean value.

```dax
NOT [IsActive]
[Status] <> "Deleted"
```

### TRUE / FALSE

Return the constant Boolean values.

```dax
Is Active = TRUE()
Is Deleted = FALSE()
```

## Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&&` | AND | `[A] > 0 && [B] > 0` |
| `||` | OR | `[A] > 0 || [B] > 0` |
| `IN` | Set membership | `[Color] IN {"Red", "Blue"}` |

## NOT IN Pattern

DAX does not have a `NOT IN` operator. Use NOT with IN:

```dax
-- NOT IN pattern
NOT [Color] IN {"Red", "Blue"}
```

## Common Patterns

### Nested IF (use SWITCH instead)
```dax
-- Avoid:
IF([X] = "A", 1, IF([X] = "B", 2, IF([X] = "C", 3, 0)))

-- Prefer:
SWITCH(
    [X],
    "A", 1,
    "B", 2,
    "C", 3,
    0
)
```

### Conditional SUM
```dax
Total Red = SUMX(
    FILTER('Sales', 'Product'[Color] = "Red"),
    'Sales'[Amount]
)
```

## Related

- [[if]]
- [[switch]]
- [[iferror]]

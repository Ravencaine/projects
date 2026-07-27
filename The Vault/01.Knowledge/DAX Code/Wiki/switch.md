---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, logical]
---

# SWITCH

## Signature

```dax
SWITCH(<expression>, <value1>, <result1>[, <value2>, <result2>][, …][, <else>])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `expression` | The expression to evaluate and compare against each value |
| `value1, value2, …` | Values to compare against `expression` |
| `result1, result2, …` | Result returned when the corresponding value matches |
| `else` | *(optional)* Result returned when no value matches; defaults to `BLANK()` |

## Returns

The `result` corresponding to the **first matching value**, or `else` if no match is found.

## Examples

```dax
-- Map status strings to numeric codes
SWITCH([Status], "Active", 1, "Inactive", 0, -1)

-- Multiple conditional branches using SWITCH(TRUE(), ...)
SWITCH(TRUE(),
    [Sales] > 10000, "High",
    [Sales] > 5000,  "Medium",
    "Low"
)
```

## Notes

- Cleaner than nested `IF`s for multiple conditions.
- Common pattern: `SWITCH(TRUE(), condition1, result1, condition2, result2, ...)` for multiple conditional branches.
- `else` result defaults to `BLANK()` if omitted.

## Related

- [[if]]
- [[calculate]]

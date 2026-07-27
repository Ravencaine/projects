---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, logical]
---

# IF / IF.EAGER

## Signature

```dax
IF(<logical_test>, <value_if_true>[, <value_if_false>])
IF.EAGER(<logical_test>, <value_if_true>[, <value_if_false>])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `logical_test` | An expression that returns `TRUE` or `FALSE` |
| `value_if_true` | Value returned when `logical_test` is `TRUE` |
| `value_if_false` | *(optional)* Value returned when `logical_test` is `FALSE`; defaults to `BLANK()` |

## Returns

`value_if_true`, `value_if_false`, or `BLANK()`.

## Examples

```dax
-- Classify sales as High or Low
IF([Sales] > 1000, "High", "Low")

-- IF.EAGER always evaluates both branches before returning
IF.EAGER([Sales] > 1000, [Sales] * 1.1, [Sales])
```

## Notes

- `IF` can return a **variant type** if the true/false branches have different data types.
- `IF.EAGER` executes **both branches** regardless of condition — useful when both branches are referenced elsewhere (e.g., by measures or tools).
- Prefer `SWITCH` for multiple conditions.

## Related

- [[switch]]
- [[coalesce]]
- [[iferror]]

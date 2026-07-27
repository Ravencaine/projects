---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, error]
---

# IFERROR

## Signature

```dax
IFERROR(<value>, <value_if_error>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `value` | The value or expression to evaluate |
| `value_if_error` | The value to return if the first argument results in an error |

## Returns

`value`, or `value_if_error` if the first argument results in an error.

## Examples

```dax
-- Return BLANK() on division or calculation errors
IFERROR([Sales] / [Quantity], BLANK())

-- Return 0 on division by zero
IFERROR(DIVIDE([A], [B]), 0)
```

## Notes

- Optimised form of `ISERROR` nested in `IF`.
- Use for graceful error handling.
- Prefer `DIVIDE` over `IFERROR` for division by zero.
- Avoid wrapping everything in `IFERROR` — let real errors surface during development.

## Related

- [[iserror]]
- [[divide]]
- [[appropriate-use-of-error-functions]]

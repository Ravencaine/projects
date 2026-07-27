---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter]
---

# SELECTEDVALUE

## Signature

```dax
SELECTEDVALUE(<column>[, <alternateResult>])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `column` | A column reference |
| `alternateResult` | *(optional)* Value to return when there is no selection or multiple selections |

## Returns

The **single selected value** if exactly one value is in the current filter context; otherwise `alternateResult` or `BLANK()`.

## Examples

```dax
-- Return the selected year, defaulting to 2020
SELECTEDVALUE('Date'[Year], 2020)

-- Apply a 10% markup to sales of red products only
IF(SELECTEDVALUE(Product[Color]) = "Red", [Sales] * 1.1, [Sales])
```

## Notes

- Returns `BLANK()` when zero or multiple values are selected.
- Preferred over the `HASONEVALUE` + `VALUES` pattern.
- `alternateResult` is returned when there are multiple **or** no selections.

## Related

- [[hasonevalue]]
- [[values]]
- [[use-selectedvalue-instead-of-values]]

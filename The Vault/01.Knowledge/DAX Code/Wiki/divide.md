---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# DIVIDE

## Signature

```dax
DIVIDE(<numerator>, <denominator>[, <alternateResult>])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `<numerator>` | The value to be divided. |
| `<denominator>` | The value to divide by. |
| `<alternateResult>` | *(Optional)* Value returned when denominator is zero or blank. Defaults to `BLANK`. |

## Returns

The quotient of numerator divided by denominator. Returns `<alternateResult>` (or `BLANK` if not provided) when the denominator is zero or blank.

## Examples

```dax
-- Simple division (returns BLANK on divide-by-zero)
DIVIDE([Profit], [Sales])

-- Return 0 instead of BLANK when denominator is zero
DIVIDE([Sales], [Target], 0)
```

## Notes

- Handles **divide-by-zero gracefully** — returns `BLANK` instead of an error.
- More **efficient** than `IF(ISBLANK(...), ..., ...)` or `IF(d=0, ..., n/d)`.
- For **measures**: prefer **not** using the 3rd alternate result argument — let `BLANK` propagate naturally so the visual renders empty rather than showing a zero that can be misinterpreted.
- For **constant denominators**: use the `/` operator directly for better performance (e.g., `SUM('Sales'[Profit]) / 100`).
- The optional 3rd argument is most useful in calculated columns or fixed-threshold scenarios.

## Related

- [[divide-function-vs-divide-operator]] — when to use DIVIDE vs. the `/` operator
- [[iferror]] — general-purpose error handling (less efficient for divide-by-zero)
- [[avoid-converting-blanks-to-values]] — guidance on letting BLANK propagate

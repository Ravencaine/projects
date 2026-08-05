---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, filter-modifier]
---

# KEEPFILTERS

## Signature
```
KEEPFILTERS(<expression>)
```

## Parameters

| # | Parameter | Type | Description |
|---|-----------|------|-------------|
| 1 | `expression` | filter | A filter expression (Boolean or table) |

## Returns

**table of values**: the filter expression, evaluated with both the new and existing filters combined (ANDed)

## Examples

```dax
-- AND the new filter with existing filters (don't replace)
Red Sales in Current Year :=
CALCULATE(
    [Sales],
    KEEPFILTERS('Product'[Color] = "Red")
)

-- KEEPFILTERS inside a range condition
Sales 100-500 :=
CALCULATE(
    [Sales],
    KEEPFILTERS('Sales'[Amount] >= 100),
    KEEPFILTERS('Sales'[Amount] <= 500)
)
```

## Notes

- By default, `CALCULATE` **replaces** existing filters on a column with the new filter argument. If a visual is already filtered to `"Blue"` and you add `'Product'[Color] = "Red"`, the result is **empty** because a column cannot be both Blue and Red simultaneously.
- `KEEPFILTERS` **changes this behavior**: it ANDs the new filter with the existing filters on the same column instead of replacing them.
- Use `KEEPFILTERS` when you want to **narrow** the filter (intersection) rather than **replace** it.
- Contrast with the default behavior, which is an OR-like replacement — `KEEPFILTERS` makes the filter more restrictive.
- Commonly used in **band/range measures** and when nesting `CALCULATE` calls that risk overwriting each other's intent.

## Related

- [[calculate]] — the context where KEEPFILTERS is used
- [[calculate-table]] — KEEPFILTERS works there too

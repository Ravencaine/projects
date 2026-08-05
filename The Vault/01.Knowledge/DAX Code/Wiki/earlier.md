---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, context]
---

# EARLIER

## Signature

```dax
EARLIER(<column>[, <number>])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `column` | The column to return the current value from |
| `number` | *(optional)* Outer evaluation pass level; defaults to `1` |

## Returns

The **current value** of the column at the specified outer row context.

## Examples

```dax
-- Reference the current row context of the column
EARLIER('Table'[Column])

-- Reference two levels of outer row context
EARLIER('Table'[Sales], 2)
```

## Notes

- Used in **calculated columns** for nested row context calculations.
- `EARLIEST` is equivalent to `EARLIER` with `number = 1`.
- Can be **slow**: consider using variables instead.
- **Not supported** in DirectQuery mode for calculated columns or RLS rules.

## Related

- [[calculate]]
- [[dax-context]]
- [[use-variables-in-dax-formulas]]

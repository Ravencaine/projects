---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# DISTINCT

## Signature

```dax
DISTINCT(<column>)
DISTINCT(<table>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `column` | A column reference |
| `table` | A table reference |

## Returns

A **table** of distinct values (column form) or distinct rows (table form) visible in the current filter context.

## Examples

```dax
-- Count distinct customers in the current filter context
COUNTROWS(DISTINCT('Sales'[CustomerKey]))
```

## Notes

- DISTINCT **removes the blank row**; VALUES includes it.
- Both functions return values visible in the current filter context.
- Column form returns a single-column table; table form returns distinct rows.

## Related

- [[values]]
- [[selectedvalue]]

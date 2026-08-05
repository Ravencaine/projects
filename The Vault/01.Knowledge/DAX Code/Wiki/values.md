---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# VALUES

## Signature

```dax
VALUES(<TableNameOrColumn>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `TableNameOrColumn` | A table name or a column reference |

## Returns

A **table** of distinct values from a column (or all rows from a table) in the current filter context. Always returns a single-column table when given a column.

## Examples

```dax
-- Count distinct years visible in the current filter context
COUNTROWS(VALUES('Date'[Year]))

-- Return the distinct colors for the current filter
VALUES('Product'[Color])
```

## Notes

- Returns **distinct values** from a column (or all rows from a table) in the current filter context.
- **Includes the blank row**: if a row with BLANK exists in the source, VALUES preserves it.
- For single-value detection, prefer `SELECTEDVALUE` instead.

## Related

- [[distinct]]
- [[selectedvalue]]
- [[hasonevalue]]

---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "filter-context", "removefilters"]
note_type: function

---

# REMOVEFILTERS

Removes all filters from a table or column, restoring the full context.

## Signature

```dax
REMOVEFILTERS( [TableOrColumn] )
```

- If no argument is supplied, removes all filters from all tables
- Returns a full table / column (not a scalar) — must be used inside an iterator

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| TableOrColumn | Table/Column | The table or column whose filters to remove. Optional. |

## Returns

A full table or column — all rows / values, unrestricted by current filter context.

## Examples

```dax
-- Remove all filters, then sum everything
Total All Items = SUMX( REMOVEFILTERS(), [Sales Amount] )

-- Remove filters on one column only
Filtered Total = SUMX( REMOVEFILTERS( 'Table'[Item] ), [Total Cost] )
```

## Notes

- `REMOVEFILTERS()` is equivalent to `ALL()` in iterator context
- Unlike `ALL()`, it cannot take a column list — it accepts a single table or column
- Useful as the first step in a No CALCULATE measure that needs to rebuild filters from scratch

## Related

- [[no-calculate-dax-pattern]]
- [[function]] — similar purpose, different syntax

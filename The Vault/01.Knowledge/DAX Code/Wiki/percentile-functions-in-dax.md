---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, statistics, percentile, percentilex, quantile]
note_type: function

---

# PERCENTILEX — Iterator-based Percentile

Returns the value at a given percentile from an iterator expression.

## Signatures

```dax
PERCENTILEX.EXC( <Table>, <Expression>, <K> )
PERCENTILEX.INC( <Table>, <Expression>, <K> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Table | Table | Table or table expression to iterate. |
| Expression | Number | Numeric expression evaluated per row. |
| K | Number | Percentile (0-1). |

## Returns

The value at the specified percentile.

## Examples

```dax
P90 Sales := PERCENTILEX.INC( 'Sales', 'Sales'[Amount], 0.9 )
P50 (Median) := PERCENTILEX.INC( 'Sales', 'Sales'[Amount], 0.5 )
```

## Notes

- **EXC:** Excludes endpoints. K must be between 0 and 1 exclusively. Requires at least 3 rows.
- **INC:** Includes endpoints. K must be between 0 and 1.
- Use INC for most business analytics (P50, P90, P99)

## Related

- [[better-median-workaround-in-dax]]
- [[stdevx.p]]

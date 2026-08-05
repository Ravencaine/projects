---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "table", "series", "number-sequence"]
note_type: function

---

# GENERATESERIES — Number Sequences

Generates a single-column table of sequential numbers.

## Signature

```dax
GENERATESERIES( <Start>, <End>, [<Increment>] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Start | Number | Starting value. |
| End | Number | Ending value. |
| Increment | Number | Step size. Optional. Default: 1. |

## Returns

A single-column table with column named `Value`.

## Examples

```dax
Numbers 1-100 := GENERATESERIES( 1, 100 )
Decimals 0-1 by 0.1 := GENERATESERIES( 0, 1, 0.1 )
Even Numbers 2-20 := GENERATESERIES( 2, 20, 2 )
```

## Notes

- The output column is always named `Value`
- Useful for creating supporting tables, bins, and axis scales
- Combine with SELECTCOLUMNS() to rename the column

## Related

- [[SELECTCOLUMNS]]
- [[ADDCOLUMNS]]

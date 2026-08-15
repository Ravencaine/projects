---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.RemoveRowsWithErrors

Returns a table with the rows removed from the input table that contain an error in at least one of the cells. If a columns list is specified, then only the cells in the specified columns are inspected for errors.

## Signature

```m
Table.RemoveRowsWithErrors(table as table, optional columns as nullable list) as
table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| optional columns | nullable list | |

## Returns

table

### Example 1

Remove error value from first row.

```m
Table.RemoveRowsWithErrors(
Table.FromRecords({
[Column1 = ...],
[Column1 = 2],
[Column1 = 3]
})
)
```

// Output
```
Table.FromRecords({
[Column1 = 2],
[Column1 = 3]
})
```


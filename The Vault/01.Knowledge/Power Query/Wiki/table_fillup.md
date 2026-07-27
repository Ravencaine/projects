---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.FillUp

Returns a table from the table specified where the value of the next cell is propagated to the null-valued cells above in the columns specified.

## Signature

```m
Table.FillUp(table as table, columns as list) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| columns | list | |

## Returns

table

### Example 1

Return a table with the null values in column [Column2] filled with the value below them from the table.

```m
Table.FillUp(
Table.FromRecords({
[Column1 = 1, Column2 = 2],
[Column1 = 3, Column2 = null],
[Column1 = 5, Column2 = 3]
}),
{"Column2"}
)
```

// Output
```
Table.FromRecords({
[Column1 = 1, Column2 = 2],
[Column1 = 3, Column2 = 3],
[Column1 = 5, Column2 = 3]
})
```


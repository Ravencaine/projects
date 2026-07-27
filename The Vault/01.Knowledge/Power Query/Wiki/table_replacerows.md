---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ReplaceRows

Replaces a specified number of rows, count, in the input table with the specified rows, beginning after the offset. The rows parameter is a list of records. table: The table where the replacement is performed. offset: The number of rows to skip before making the replacement. count: The number of rows to replace. rows: The list of row records to insert into the table at the location specified by the offset.

## Signature

```m
Table.ReplaceRows(
table as table,
offset as number,
count as number,
rows as list
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| offset | number | |
| count | number | |
| rows | list | |

## Returns

table

### Example 1

Starting at position 1, replace 3 rows.

```m
Table.ReplaceRows(
Table.FromRecords({
[Column1 = 1],
[Column1 = 2],
[Column1 = 3],
[Column1 = 4],
[Column1 = 5]
}),
1,
3,
{[Column1 = 6], [Column1 = 7]}
)
```

// Output
```
Table.FromRecords({
[Column1 = 1],
[Column1 = 6],
[Column1 = 7],
[Column1 = 5]
})
```


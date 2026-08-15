---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.Partition

Partitions the table into a list of groups number of tables, based on the value of the column and a hash function. The hash function is applied to the value of the column row to obtain a hash value for the row. The hash value modulo groups determines in which of the returned tables the row will be placed. table: The table to partition. column: The column to hash to determine which returned table the row is in. groups: The number of tables the input table will be partitioned into. hash: The function applied to obtain a hash value.

## Signature

```m
Table.Partition(
table as table,
column as text,
groups as number,
hash as function
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| column | text | |
| groups | number | |
| hash | function | |

## Returns

list

### Example 1

Partition the table ({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]}) into 2 tables on column [a], using the value of the columns as the hash function.

```m
Table.Partition(
Table.FromRecords({
[a = 2, b = 4],
[a = 1, b = 4],
[a = 2, b = 4],
[a = 1, b = 4]
}),
"a",
2,
each _
)
```

// Output
```
{
Table.FromRecords({
[a = 2, b = 4],
[a = 2, b = 4]
}),
Table.FromRecords({
[a = 1, b = 4],
[a = 1, b = 4]
})
}
```


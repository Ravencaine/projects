---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.FromPartitions

Returns a table that is the result of combining a set of partitioned tables, partitions. partitionColumn is the name of the column to add. The type of the column defaults to any, but can be specified by partitionColumnType.

## Signature

```m
Table.FromPartitions(
partitionColumn as text,
partitions as list,
optional partitionColumnType as nullable type
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| partitionColumn | text | |
| partitions | list | |
| optional partitionColumnType | nullable type | |

## Returns

table

### Example 1

Find item type from the list {number}.

```m
Table.FromPartitions(
"Year",
{
{
1994,
Table.FromPartitions(
"Month",
{
{
"Jan",
Table.FromPartitions(
"Day",
{
{1, #table({"Foo"}, {{"Bar"}})},
{2, #table({"Foo"}, {{"Bar"}})}
}
)
},
{
"Feb",
Table.FromPartitions(
"Day",
{
{3, #table({"Foo"}, {{"Bar"}})},
{4, #table({"Foo"}, {{"Bar"}})}
}
)
}
}
)
}
}
)
```

// Output
```
Table.FromRecords({
[
Foo = "Bar",
Day = 1,
Month = "Jan",
Year = 1994
],
[
Foo = "Bar",
Day = 2,
Month = "Jan",
Year = 1994
],
[
Foo = "Bar",
Day = 3,
Month = "Feb",
Year = 1994
],
[
Foo = "Bar",
Day = 4,
Month = "Feb",
Year = 1994
]
})
```

## Related

[[type_functions]]


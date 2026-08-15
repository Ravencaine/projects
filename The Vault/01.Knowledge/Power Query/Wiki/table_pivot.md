---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.Pivot

Given a pair of columns representing attribute-value pairs, rotates the data in the attribute column into a column headings.

## Signature

```m
Table.Pivot(
table as table,
pivotValues as list,
attributeColumn as text,
valueColumn as text,
optional aggregationFunction as nullable function
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| pivotValues | list | |
| attributeColumn | text | |
| valueColumn | text | |
| optional aggregationFunction | nullable function | |

## Returns

table

### Example 1

Take the values "a", "b", and "c" in the attribute column of table ({ [ key = "x", attribute = "a", value = 1 ], [ key = "x", attribute = "c", value = 3 ], [ key = "y", attribute = "a", value = 2 ], [ key = "y", attribute = "b", value = 4 ] }) and pivot them into their own column.

```m
Table.Pivot(
Table.FromRecords({
[key = "x", attribute = "a", value = 1],
[key = "x", attribute = "c", value = 3],
[key = "y", attribute = "a", value = 2],
[key = "y", attribute = "b", value = 4]
}),
{"a", "b", "c"},
"attribute",
"value"
)
```

// Output
```
Power Query M
Table.FromRecords({
[key = "x", a = 1, b = null, c = 3],
[key = "y", a = 2, b = 4, c = null]
})
```

### Example 2

Take the values "a", "b", and "c" in the attribute column of table ({ [ key = "x", attribute = "a", value = 1 ], [ key = "x", attribute = "c", value = 3 ], [ key = "x", attribute = "c", value = 5 ], [ key = "y", attribute = "a", value = 2 ], [ key = "y", attribute = "b", value = 4 ] }) and pivot them into their own column. The attribute "c" for key "x" has multiple values associated with it, so use the function List.Max to resolve the conflict.

```m
Table.Pivot(
Table.FromRecords({
[key = "x", attribute = "a", value = 1],
[key = "x", attribute = "c", value = 3],
[key = "x", attribute = "c", value = 5],
[key = "y", attribute = "a", value = 2],
[key = "y", attribute = "b", value = 4]
}),
{"a", "b", "c"},
"attribute",
"value",
List.Max
)
```

// Output
```
Table.FromRecords({
[key = "x", a = 1, b = null, c = 5],
[key = "y", a = 2, b = 4, c = null]
})
```


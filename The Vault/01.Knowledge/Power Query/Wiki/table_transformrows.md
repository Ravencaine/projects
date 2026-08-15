---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.TransformRows

Creates a list by applying the transform operation to each row in table.

## Signature

```m
Table.TransformRows(table as table, transform as function) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| transform | function | |

## Returns

list

### Example 1

Transform the rows of a table into a list of numbers.

```m
Table.TransformRows(
Table.FromRecords({
[a = 1],
[a = 2],
[a = 3],
[a = 4],
[a = 5]
}),
each [a]
)
```

// Output
```
{1, 2, 3, 4, 5}
```

### Example 2

Transform the rows of a numeric table into textual records.

```m
Table.TransformRows(
Table.FromRecords({
[a = 1],
[a = 2],
[a = 3],
[a = 4],
[a = 5]
}),
(row) as record => [B = Number.ToText(row[a])]
)
```

// Output
```
{
[B = "1"],
[B = "2"],
[B = "3"],
[B = "4"],
[B = "5"]
}
```


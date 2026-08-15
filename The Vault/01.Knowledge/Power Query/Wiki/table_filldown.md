---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.FillDown

Returns a table from the table specified where the value of a previous cell is propagated to the null-valued cells below in the columns specified.

## Signature

```m
Table.FillDown(table as table, columns as list) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| columns | list | |

## Returns

table

### Example 1

Return a table with the null values in column [Place] filled with the value above them from the table.

```m
Table.FillDown(
Table.FromRecords({
[Place = 1, Name = "Bob"],
[Place = null, Name = "John"],
[Place = 2, Name = "Brad"],
[Place = 3, Name = "Mark"],
[Place = null, Name = "Tom"],
[Place = null, Name = "Adam"]
}),
{"Place"}
)
```

// Output
```
Table.FromRecords({
[Place = 1, Name = "Bob"],
[Place = 1, Name = "John"],
[Place = 2, Name = "Brad"],
[Place = 3, Name = "Mark"],
[Place = 3, Name = "Tom"],
[Place = 3, Name = "Adam"]
})
```


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.InsertRows

Returns a table with the list of rows, rows, inserted into the table at the given position, offset. Each column in the row to insert must match the column types of the table.

## Signature

```m
Table.InsertRows(
table as table,
offset as number,
rows as list
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| offset | number | |
| rows | list | |

## Returns

table

### Example 1

Insert the row into the table at position 1.

```m
Table.InsertRows(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"]
}),
1,
{[CustomerID = 3, Name = "Paul", Phone = "543-7890"]}
)
```

// Output
```
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"]
})
```

### Example 2

Insert two rows into the table at position 1.

```m
Table.InsertRows(
Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
1,
{
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
}
)
```

// Output
```
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```


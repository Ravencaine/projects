---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ToRows

Creates a list of nested lists from the table, table. Each list item is an inner list that contains the row values.

## Signature

```m
Table.ToRows(table as table) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

list

### Example 1

Create a list of the row values from the table.

```m
Table.ToRows(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
)
```

// Output
```
{
{1, "Bob", "123-4567"},
{2, "Jim", "987-6543"},
{3, "Paul", "543-7890"}
}
```


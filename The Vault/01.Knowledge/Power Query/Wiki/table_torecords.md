---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ToRecords

Converts a table, table, to a list of records.

## Signature

```m
Table.ToRecords(table as table) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

list

### Example 1

Convert the table to a list of records.

```m
Table.ToRecords(
Table.FromRows(
{
{1, "Bob", "123-4567"},
{2, "Jim", "987-6543"},
{3, "Paul", "543-7890"}
},
{"CustomerID", "Name", "Phone"}
)
)
```

// Output
```
{
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
}
```


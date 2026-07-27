---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.Column

Returns the column of data specified by column from the table table as a list.

## Signature

```m
Table.Column(table as table, column as text) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| column | text | |

## Returns

list

### Example 1

Returns the values from the [Name] column in the table.

```m
Table.Column(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
"Name"
)
```

// Output
```
{"Bob", "Jim", "Paul", "Ringo"}
```


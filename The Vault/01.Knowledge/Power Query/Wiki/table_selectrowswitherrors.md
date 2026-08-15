---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.SelectRowsWithErrors

Returns a table with only those rows of the input table that contain an error in at least one of the cells. If a columns list is specified, then only the cells in the specified columns are inspected for errors.

## Signature

```m
Table.SelectRowsWithErrors(table as table, optional columns as nullable list) as
table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| optional columns | nullable list | |

## Returns

table

### Example 1

Select names of customers with errors in their rows.

```m
Table.SelectRowsWithErrors(
Table.FromRecords({
[CustomerID = ..., Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
)[Name]
```

// Output
```
{"Bob"}
```


---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ReverseRows

Returns a table with the rows from the input table in reverse order. Example Reverse the rows in the table. Usage Power Query M Table.ReverseRows( Table.FromRecords({ [CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Ringo", Phone = "232-1550"] }) ) Output Power Query M Table.FromRecords({ [CustomerID = 4, Name = "Ringo", Phone = "232-1550"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 1, Name = "Bob", Phone = "123-4567"] }) Last updated on 03/24/2026 --- PAGE 1109 ---

## Signature

```m
Table.ReverseRows(table as table) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

table


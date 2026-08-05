---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ColumnCount

Returns the number of columns in the table table. Example Find the number of columns in the table. Usage Power Query M Table.ColumnCount( Table.FromRecords({ [CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"] }) ) Output 3 Last updated on 03/24/2026 --- PAGE 966 ---

## Signature

```m
Table.ColumnCount(table as table) as number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

number


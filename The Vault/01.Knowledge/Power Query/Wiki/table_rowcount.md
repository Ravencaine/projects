---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.RowCount

Returns the number of rows in the table. Example Find the number of rows in the table. Usage Power Query M Table.RowCount( Table.FromRecords({ [CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"] }) ) Output 3 Last updated on 03/24/2026 --- PAGE 1110 ---

## Signature

```m
Table.RowCount(table as table) as number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

number


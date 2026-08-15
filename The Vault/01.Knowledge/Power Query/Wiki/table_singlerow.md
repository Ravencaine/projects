---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.SingleRow

Returns the single row in the one row table. If the table has more than one row, an error is raised. Example Return the single row in the table. Usage Power Query M Table.SingleRow(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123- 4567"]})) Output [CustomerID = 1, Name = "Bob", Phone = "123-4567"] Last updated on 04/03/2026 --- PAGE 1119 ---

## Signature

```m
Table.SingleRow(table as table) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

record


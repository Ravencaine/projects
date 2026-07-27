---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.PrefixColumns

Returns a table where all the column names from the table provided are prefixed with the given text, prefix, plus a period in the form prefix.ColumnName. Example Prefix the columns with "MyTable" in the table. Usage Power Query M Table.PrefixColumns( Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}), "MyTable" ) Output Table.FromRecords({[MyTable.CustomerID = 1, MyTable.Name = "Bob", MyTable.Phone = "123- 4567"]}) Last updated on 04/03/2026 --- PAGE 1071 ---

## Signature

```m
Table.PrefixColumns(table as table, prefix as text) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| prefix | text | |

## Returns

table


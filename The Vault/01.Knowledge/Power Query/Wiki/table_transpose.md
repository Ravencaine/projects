---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.Transpose

Makes columns into rows and rows into columns. Example Make the rows of the table of name-value pairs into columns. Usage Power Query M Table.Transpose( Table.FromRecords({ [Name = "Full Name", Value = "Fred"], [Name = "Age", Value = 42], [Name = "Country", Value = "UK"] }) ) Output Power Query M Table.FromRecords({ [Column1 = "Full Name", Column2 = "Age", Column3 = "Country"], [Column1 = "Fred", Column2 = 42, Column3 = "UK"] }) Last updated on 03/24/2026 --- PAGE 1150 ---

## Signature

```m
Table.Transpose(table as table, optional columns as any) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| optional columns | any | |

## Returns

table


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.CombineColumns

Combines the specified columns into a new column using the specified combiner function. Example Combine the last and first names into a new column, separated by a comma. Usage Power Query M Table.CombineColumns( Table.FromRecords({[FirstName = "Bob", LastName = "Smith"]}), {"LastName", "FirstName"}, Combiner.CombineTextByDelimiter(",", QuoteStyle.None), "FullName" ) Output Table.FromRecords({[FullName = "Smith,Bob"]}) Last updated on 04/02/2026 --- PAGE 972 ---

## Signature

```m
Table.CombineColumns(
table as table,
sourceColumns as list,
combiner as function,
column as text
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| sourceColumns | list | |
| combiner | function | |
| column | text | |

## Returns

table


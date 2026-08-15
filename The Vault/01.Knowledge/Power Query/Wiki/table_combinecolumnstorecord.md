---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.CombineColumnsToRecord

Combines the specified columns of table into a new record-valued column named newColumnName where each record has field names and values corresponding to the column names and values of the columns that were combined. If a record is specified for options, the following options may be provided: DisplayNameColumn: When specified as text, indicates that the given column name should be treated as the display name of the record. This need not be one of the columns in the record itself. TypeName: When specified as text, supplies a logical type name for the resulting record which can be used during data load to drive behavior by the loading environment. Related content Types and type conversion --- PAGE 973 ---

## Signature

```m
Table.CombineColumnsToRecord(
table as table,
newColumnName as text,
sourceColumns as list,
optional options as nullable record
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| newColumnName | text | |
| sourceColumns | list | |
| optional options | nullable record | |

## Returns

table


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.DuplicateColumn

Duplicate the column named columnName to the table table. The values and type for the column newColumnName are copied from column columnName. Example Duplicate the column "a" to a column named "copied column" in the table ({[a = 1, b = 2], [a = 3, b = 4]}). Usage Power Query M Table.DuplicateColumn( Table.FromRecords({ [a = 1, b = 2], [a = 3, b = 4] }), "a", "copied column" ) Output Power Query M Table.FromRecords({ [a = 1, b = 2, #"copied column" = 1], --- PAGE 985 --- [a = 3, b = 4, #"copied column" = 3] }) Related content Types and type conversion --- PAGE 986 ---

## Signature

```m
Table.DuplicateColumn(
table as table,
columnName as text,
newColumnName as text,
optional columnType as nullable type
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| columnName | text | |
| newColumnName | text | |
| optional columnType | nullable type | |

## Returns

table


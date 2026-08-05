---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ColumnsOfType

Returns a list with the names of the columns from table table that match the types specified in listOfTypes. Example Return the names of columns of type Number.Type from the table. Usage Power Query M Table.ColumnsOfType( Table.FromRecords( {[a = 1, b = "hello"]}, type table[a = Number.Type, b = Text.Type] ), {type number} ) Output {"a"} Related content Types and type conversion Last updated on 03/24/2026 --- PAGE 968 ---

## Signature

```m
Table.ColumnsOfType(table as table, listOfTypes as list) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| listOfTypes | list | |

## Returns

list


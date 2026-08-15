---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.Repeat

Returns a table with the rows from the input table repeated the specified count times. Example Repeat the rows in the table two times. Usage Power Query M Table.Repeat( Table.FromRecords({ [a = 1, b = "hello"], [a = 3, b = "world"] }), 2 ) Output Power Query M Table.FromRecords({ [a = 1, b = "hello"], [a = 3, b = "world"], [a = 1, b = "hello"], [a = 3, b = "world"] }) Last updated on 03/24/2026 --- PAGE 1095 ---

## Signature

```m
Table.Repeat(table as table, count as number) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| count | number | |

## Returns

table


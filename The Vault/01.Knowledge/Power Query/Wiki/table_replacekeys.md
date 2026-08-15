---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.ReplaceKeys

Replaces the keys of the specified table. Example Replace the existing keys of a table. Usage Power Query M let table = Table.FromRecords({ [Id = 1, Name = "Hello There"], [Id = 2, Name = "Good Bye"] }), tableWithKeys = Table.AddKey(table, {"Id"}, true), resultTable = Table.ReplaceKeys(tableWithKeys, {[Columns = {"Id"}, Primary = false]}) in resultTable Output Power Query M Table.FromRecords({ [Id = 1, Name = "Hello There"], [Id = 2, Name = "Good Bye"] }) Last updated on 03/24/2026 --- PAGE 1098 ---

## Signature

```m
Table.ReplaceKeys(table as table, keys as list) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| keys | list | |

## Returns

table


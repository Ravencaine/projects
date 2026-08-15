---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.StopFolding

Prevents any downstream operations from being run against the original source of the data in table.

## Signature

```m
Table.StopFolding(table as table) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

table

### Example 1

Fetches data from a SQL table in a way that prevents any downstream operations from running as a query on the SQL server.

```m
let
Source = Sql.Database("SomeSQLServer", "MyDb"),
MyTable = Source{[Item="MyTable"]}[Data],
MyLocalTable = Table.StopFolding(MyTable)
in
MyLocalTable
```

// Output
```
table
```


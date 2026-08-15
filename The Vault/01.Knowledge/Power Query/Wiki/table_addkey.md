---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.AddKey

Adds a key to table, where columns is the list of column names that define the key, and isPrimary specifies whether the key is primary.

## Signature

```m
Table.AddKey(
table as table,
columns as list,
isPrimary as logical
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| columns | list | |
| isPrimary | logical | |

## Returns

table

### Example 1

Add a single-column primary key to a table.

```m
let
table = Table.FromRecords({
[Id = 1, Name = "Hello There"],
[Id = 2, Name = "Good Bye"]
}),
resultTable = Table.AddKey(table, {"Id"}, true)
in
resultTable
```

// Output
```
Table.FromRecords({
[Id = 1, Name = "Hello There"],
[Id = 2, Name = "Good Bye"]
})
```


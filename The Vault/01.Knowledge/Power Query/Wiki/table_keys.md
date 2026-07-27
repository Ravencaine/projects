---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.Keys

Returns the keys of the specified table.

## Signature

```m
Table.Keys(table as table) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

list

### Example 1

Get the list of keys for a table.

```m
let
table = Table.FromRecords({
[Id = 1, Name = "Hello There"],
[Id = 2, Name = "Good Bye"]
}),
tableWithKeys = Table.AddKey(table, {"Id"}, true),
keys = Table.Keys(tableWithKeys)
in
keys
```

// Output
```
{[Columns = {"Id"}, Primary = true]}
```


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["type", "m-function"]
---


# Type.TableKeys

Returns the possibly empty list of keys for the given table type. Each key is defined using a record in the following form: Columns: a list of the column names that define the key Primary: true if the key is the table's primary key; otherwise, false Example Return the key information for a table type. Usage Power Query M let BaseType = type table [ID = number, Name = text], AddKey = Type.AddTableKey(BaseType, {"ID"}, true), DetailsOfKeys = Type.TableKeys(AddKey) in DetailsOfKeys Output {[Columns = {"ID"}, Primary = true]} Last updated on 04/02/2026 --- PAGE 1284 ---

## Signature

```m
Type.TableKeys(tableType as type) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tableType | type | |

## Returns

list


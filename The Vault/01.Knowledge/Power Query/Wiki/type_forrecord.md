---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [type, m-function]
---


# Type.ForRecord

Returns a type that represents records with specific type constraints on fields.

## Signature

```m
Type.ForRecord(fields as record, open as logical) as type
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| fields | record | |
| open | logical | |

## Returns

type

### Example 1

Dynamically generate a table type.

```m
let
columnNames = {"Name", "Score"},
columnTypes = {type text, type number},
rowColumnTypes = List.Transform(columnTypes, (t) => [Type = t, Optional =
false]),
rowType = Type.ForRecord(Record.FromList(rowColumnTypes, columnNames), false)
in
#table(type table rowType, {{"Betty", 90.3}, {"Carl", 89.5}})
```

// Output
```
#table(
type table [Name = text, Score = number],
{{"Betty", 90.3}, {"Carl", 89.5}}
)
```


---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["type", "m-function"]
---


# Type.TableRow

Returns the row type of the specified table type. The result will always be a record type.

## Signature

```m
Type.TableRow(table as type) as type
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | type | |

## Returns

type

### Example 1

Return the row type information for a simple table.

```m
let
tableRowType = Type.TableRow(Value.Type(#table({"Column1"}, {})))
in
Type.RecordFields(tableRowType)
```

// Output
```
[Column1 = [Type = type any, Optional = false]]
```

## Related

[[type_functions]]


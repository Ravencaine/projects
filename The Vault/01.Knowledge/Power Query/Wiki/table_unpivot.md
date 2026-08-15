---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.Unpivot

Translates a set of columns in a table into attribute-value pairs, combined with the rest of the values in each row.

## Signature

```m
Table.Unpivot(
table as table,
pivotColumns as list,
attributeColumn as text,
valueColumn as text
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| pivotColumns | list | |
| attributeColumn | text | |
| valueColumn | text | |

## Returns

table

### Example 1

Take the columns "a", "b", and "c" in the table ({[ key = "x", a = 1, b = null, c = 3 ], [ key = "y", a = 2, b = 4, c = null ]}) and unpivot them into attribute-value pairs.

```m
Table.Unpivot(
Table.FromRecords({
[key = "x", a = 1, b = null, c = 3],
[key = "y", a = 2, b = 4, c = null]
}),
{"a", "b", "c"},
"attribute",
"value"
)
```

// Output
```
Table.FromRecords({
[key = "x", attribute = "a", value = 1],
[key = "x", attribute = "c", value = 3],
[key = "y", attribute = "a", value = 2],
[key = "y", attribute = "b", value = 4]
})
```


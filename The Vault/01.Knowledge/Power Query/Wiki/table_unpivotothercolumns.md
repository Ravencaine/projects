---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.UnpivotOtherColumns

Translates all columns other than a specified set into attribute-value pairs, combined with the rest of the values in each row.

## Signature

```m
Table.UnpivotOtherColumns(
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

Translates all columns other than a specified set into attribute-value pairs, combined with the rest of the values in each row.

```m
Table.UnpivotOtherColumns(
Table.FromRecords({
[key = "key1", attribute1 = 1, attribute2 = 2, attribute3 = 3],
[key = "key2", attribute1 = 4, attribute2 = 5, attribute3 = 6]
}),
{"key"},
"column1",
"column2"
)
```

// Output
```
Table.FromRecords({
[key = "key1", column1 = "attribute1", column2 = 1],
[key = "key1", column1 = "attribute2", column2 = 2],
[key = "key1", column1 = "attribute3", column2 = 3],
[key = "key2", column1 = "attribute1", column2 = 4],
[key = "key2", column1 = "attribute2", column2 = 5],
[key = "key2", column1 = "attribute3", column2 = 6]
})
```


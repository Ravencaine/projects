---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ReplaceMatchingRows

Replaces all the specified rows in the table with the provided ones. The rows to replace and the replacements are specified in replacements, using {old, new} formatting. An optional equationCriteria parameter may be specified to control comparison between the rows of the table.

## Signature

```m
Table.ReplaceMatchingRows(
table as table,
replacements as list,
optional equationCriteria as any
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| replacements | list | |
| optional equationCriteria | any | |

## Returns

table

### Example 1

Replace the rows [a = 1, b = 2] and [a = 2, b = 3] with [a = -1, b = -2],[a = -2, b = -3] in the table.

```m
Table.ReplaceMatchingRows(
Table.FromRecords({
[a = 1, b = 2],
[a = 2, b = 3],
[a = 3, b = 4],
[a = 1, b = 2]
}),
{
{[a = 1, b = 2], [a = -1, b = -2]},
{[a = 2, b = 3], [a = -2, b = -3]}
}
)
```

// Output
```
Power Query M
Table.FromRecords({
[a = -1, b = -2],
[a = -2, b = -3],
[a = 3, b = 4],
[a = -1, b = -2]
})
```

## Related

[[comparison_criteria]]
[[equation_criteria]]


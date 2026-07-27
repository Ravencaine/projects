---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.PositionOfAny

Returns the row(s) position(s) from the table of the first occurrence of the list of rows. Returns -1 if no occurrence is found. table: The input table. rows: The list of rows in the table to find the positions of. occurrence: (Optional) Specifies which occurrences of the row to return. equationCriteria: (Optional) Controls the comparison between the table rows.

## Signature

```m
Table.PositionOfAny(
table as table,
rows as list,
optional occurrence as nullable number,
optional equationCriteria as any
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| rows | list | |
| optional occurrence | nullable number | |
| optional equationCriteria | any | |

## Returns

any

### Example 1

Find the position of the first occurrence of [a = 2, b = 4] or [a = 6, b = 8] in the table ({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]}).

```m
Table.PositionOfAny(
Table.FromRecords({
[a = 2, b = 4],
[a = 1, b = 4],
[a = 2, b = 4],
[a = 1, b = 4]
}),
{
[a = 2, b = 4],
[a = 6, b = 8]
}
)
```

// Output
```
0
```

### Example 2

Find the position of all the occurrences of [a = 2, b = 4] or [a = 6, b = 8] in the table ({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]}.

```m
Table.PositionOfAny(
Table.FromRecords({
[a = 2, b = 4],
[a = 6, b = 8],
[a = 2, b = 4],
[a = 1, b = 4]
}),
{
[a = 2, b = 4],
[a = 6, b = 8]
},
Occurrence.All
)
```

// Output
```
{0, 1, 2}
```

## Related

[[occurrence]]
[[comparison_criteria]]
[[equation_criteria]]


---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.PositionOf

Returns the row position of the first occurrence of the row in the table specified. Returns -1 if no occurrence is found. table: The input table. row: The row in the table to find the position of. occurrence: (Optional) Specifies which occurrences of the row to return. equationCriteria: (Optional) Controls the comparison between the table rows.

## Signature

```m
Table.PositionOf(
table as table,
row as record,
optional occurrence as any,
optional equationCriteria as any
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| row | record | |
| optional occurrence | any | |
| optional equationCriteria | any | |

## Returns

any

### Example 1

Find the position of the first occurrence of [a = 2, b = 4] in the table ({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]}).

```m
Table.PositionOf(
Table.FromRecords({
[a = 2, b = 4],
[a = 1, b = 4],
[a = 2, b = 4],
[a = 1, b = 4]
}),
[a = 2, b = 4]
)
```

// Output
```
0
```

### Example 2

Find the position of the second occurrence of [a = 2, b = 4] in the table ({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]}).

```m
Table.PositionOf(
Table.FromRecords({
[a = 2, b = 4],
[a = 1, b = 4],
[a = 2, b = 4],
[a = 1, b = 4]
}),
[a = 2, b = 4],
1
)
```

// Output
```
2
```

### Example 3

Find the position of all the occurrences of [a = 2, b = 4] in the table ({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]}).

```m
Table.PositionOf(
Table.FromRecords({
[a = 2, b = 4],
[a = 1, b = 4],
[a = 2, b = 4],
[a = 1, b = 4]
}),
[a = 2, b = 4],
Occurrence.All
)
```

// Output
```
{0, 2}
```

## Related

[[occurrence]]
[[comparison_criteria]]
[[equation_criteria]]


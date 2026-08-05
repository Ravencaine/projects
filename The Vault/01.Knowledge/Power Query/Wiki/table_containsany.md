---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ContainsAny

Indicates whether any the specified records in the list of records rows, appear as rows in the table. An optional parameter equationCriteria may be specified to control comparison between the rows of the table.

## Signature

```m
Table.ContainsAny(
table as table,
rows as list,
optional equationCriteria as any
) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| rows | list | |
| optional equationCriteria | any | |

## Returns

logical

### Example 1

Determine if the table ({[a = 1, b = 2], [a = 3, b = 4]}) contains the rows [a = 1, b = 2] or [a = 3, b = 5].

```m
Table.ContainsAny(
Table.FromRecords({
[a = 1, b = 2],
[a = 3, b = 4]
}),
{
[a = 1, b = 2],
[a = 3, b = 5]
}
)
```

// Output
```
true
```

### Example 2

Determine if the table ({[a = 1, b = 2], [a = 3, b = 4]}) contains the rows [a = 1, b = 3] or [a = 3, b = 5].

```m
Table.ContainsAny(
Table.FromRecords({
[a = 1, b = 2],
[a = 3, b = 4]
}),
{
[a = 1, b = 3],
[a = 3, b = 5]
}
)
```

// Output
```
false
```

### Example 3

Determine if the table (Table.FromRecords({[a = 1, b = 2], [a = 3, b = 4]})) contains the rows [a = 1, b = 3] or [a = 3, b = 5] comparing only the column [a].

```m
Table.ContainsAny(
Table.FromRecords({
[a = 1, b = 2],
[a = 3, b = 4]
}),
{
[a = 1, b = 3],
[a = 3, b = 5]
},
"a"
)
```

// Output
```
true
```

## Related

[[comparison_criteria]]
[[equation_criteria]]


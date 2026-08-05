---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.Min

Returns the smallest row in the table, given the comparisonCriteria. If the table is empty, the optional default value is returned.

## Signature

```m
Table.Min(
table as table,
comparisonCriteria as any,
optional default as any
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| comparisonCriteria | any | |
| optional default | any | |

## Returns

any

### Example 1

Find the row with the smallest value in column [a] in the table.

```m
Table.Min(
Table.FromRecords({
[a = 2, b = 4],
[a = 6, b = 8]
}),
"a"
)
```

// Output
```
[a = 2, b = 4]
```

### Example 2

Find the row with the smallest value in column [a] in the table. Return -1 if empty.

```m
Power Query M
Table.Min(#table({"a"}, {}), "a", -1)
```

// Output
```
-1
```

## Related

[[comparison_criteria]]


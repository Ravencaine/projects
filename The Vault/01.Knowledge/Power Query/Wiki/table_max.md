---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.Max

Returns the largest row in the table, given the comparisonCriteria. If the table is empty, the optional default value is returned.

## Signature

```m
Table.Max(
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

Find the row with the largest value in column [a] in the table ({[a = 2, b = 4], [a = 6, b = 8]}).

```m
Table.Max(
Table.FromRecords({
[a = 2, b = 4],
[a = 6, b = 8]
}),
"a"
)
```

// Output
```
[a = 6, b = 8]
```

### Example 2

```m
Table.Max(#table({"a"}, {}), "a", -1)
```

// Output
```
-1
```

## Related

[[comparison_criteria]]


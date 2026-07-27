---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.MatchesAllRows

Indicates whether all the rows in the table match the given condition. Returns true if all of the rows match, false otherwise.

## Signature

```m
Table.MatchesAllRows(table as table, condition as function) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| condition | function | |

## Returns

logical

### Example 1

Determine whether all of the row values in column [a] are even in the table.

```m
Table.MatchesAllRows(
Table.FromRecords({
[a = 2, b = 4],
[a = 6, b = 8]
}),
each Number.Mod([a], 2) = 0
)
```

// Output
```
true
```

### Example 2

Find if all of the row values are [a = 1, b = 2], in the table ({[a = 1, b = 2], [a = 3, b = 4]}).

```m
Table.MatchesAllRows(
Table.FromRecords({
[a = 1, b = 2],
[a = -3, b = 4]
}),
each _ = [a = 1, b = 2]
)
```

// Output
```
false
```


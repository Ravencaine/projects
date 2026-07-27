---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.MatchesAnyRows

Indicates whether any the rows in the table match the given condition. Returns true if any of the rows match, false otherwise.

## Signature

```m
Table.MatchesAnyRows(table as table, condition as function) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| condition | function | |

## Returns

logical

### Example 1

Determine whether any of the row values in column [a] are even in the table ({[a = 2, b = 4], [a = 6, b = 8]}).

```m
Table.MatchesAnyRows(
Table.FromRecords({
[a = 1, b = 4],
[a = 3, b = 8]
}),
each Number.Mod([a], 2) = 0
)
```

// Output
```
false
```

### Example 2

Determine whether any of the row values are [a = 1, b = 2], in the table ({[a = 1, b = 2], [a = 3, b = 4]}).

```m
Power Query M
Table.MatchesAnyRows(
Table.FromRecords({
[a = 1, b = 2],
[a = -3, b = 4]
}),
each _ = [a = 1, b = 2]
)
```

// Output
```
true
```


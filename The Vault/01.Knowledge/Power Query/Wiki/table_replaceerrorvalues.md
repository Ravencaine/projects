---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ReplaceErrorValues

Replaces the error values in the specified columns of the table with the new values in the errorReplacement list. The format of the list is {{column1, value1}, ...}. There may only be one replacement value per column, specifying the column more than once will result in an error.

## Signature

```m
Table.ReplaceErrorValues(table as table, errorReplacement as list) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| errorReplacement | list | |

## Returns

table

### Example 1

Replace the error value with the text "world" in the table.

```m
Table.ReplaceErrorValues(
Table.FromRows({{1, "hello"}, {3, ...}}, {"A", "B"}),
{"B", "world"}
)
```

// Output
```
Table.FromRecords({
[A = 1, B = "hello"],
[A = 3, B = "world"]
})
```

### Example 2

Replace the error value in column A with the text "hello" and in column B with the text "world" in the table.

```m
Table.ReplaceErrorValues(
Table.FromRows({{..., ...}, {1, 2}}, {"A", "B"}),
{{"A", "hello"}, {"B", "world"}}
)
```

// Output
```
Table.FromRecords({
[A = "hello", B = "world"],
[A = 1, B = 2]
})
```


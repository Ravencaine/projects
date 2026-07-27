---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ToList

Converts a table into a list by applying the specified combining function to each row of values in the table.

## Signature

```m
Table.ToList(table as table, optional combiner as nullable function) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| optional combiner | nullable function | |

## Returns

list

### Example 1

Combine the text of each row with a comma.

```m
Table.ToList(
Table.FromRows({
{Number.ToText(1), "Bob", "123-4567"},
{Number.ToText(2), "Jim", "987-6543"},
{Number.ToText(3), "Paul", "543-7890"}
}),
Combiner.CombineTextByDelimiter(",")
)
```

// Output
```
{"1,Bob,123-4567", "2,Jim,987-6543", "3,Paul,543-7890"}
```

## Related

[[combiner_functions]]


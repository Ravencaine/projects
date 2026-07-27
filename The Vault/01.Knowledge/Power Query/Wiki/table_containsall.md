---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ContainsAll

Indicates whether all the specified records in the list of records rows, appear as rows in the table. An optional parameter equationCriteria may be specified to control comparison between the rows of the table.

## Signature

```m
Table.ContainsAll(
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

Determine if the table contains all the rows, comparing only the column [CustomerID].

```m
Table.ContainsAll(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
{
[CustomerID = 1, Name = "Bill"],
[CustomerID = 2, Name = "Fred"]
},
"CustomerID"
)
```

// Output
```
true
```

### Example 2

Determine if the table contains all the rows.

```m
Table.ContainsAll(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
{
[CustomerID = 1, Name = "Bill"],
[CustomerID = 2, Name = "Fred"]
}
)
```

// Output
```
false
```

## Related

[[comparison_criteria]]
[[equation_criteria]]


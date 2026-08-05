---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.Contains

Indicates whether the specified record, row, appears as a row in the table. An optional parameter equationCriteria may be specified to control comparison between the rows of the table.

## Signature

```m
Table.Contains(
table as table,
row as record,
optional equationCriteria as any
) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| row | record | |
| optional equationCriteria | any | |

## Returns

logical

### Example 1

Determine if the table contains the row.

```m
Table.Contains(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
[Name = "Bob"]
)
```

// Output
```
true
```

### Example 2

```m
Table.Contains(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
[Name = "Ted"]
)
```

// Output
```
false
```

### Example 3

Determine if the table contains the row comparing only the column [Name].

```m
Table.Contains(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
[CustomerID = 4, Name = "Bob"],
"Name"
)
```

// Output
```
true
```

## Related

[[comparison_criteria]]
[[equation_criteria]]


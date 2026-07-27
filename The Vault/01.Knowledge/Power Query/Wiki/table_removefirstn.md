---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.RemoveFirstN

Returns a table that does not contain the first specified number of rows, countOrCondition, of the table table. The number of rows removed depends on the optional parameter countOrCondition. If countOrCondition is omitted only the first row is removed. If countOrCondition is a number, that many rows (starting at the top) will be removed. If countOrCondition is a condition, the rows that meet the condition will be removed until a row does not meet the condition.

## Signature

```m
Table.RemoveFirstN(table as table, optional countOrCondition as any) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| optional countOrCondition | any | |

## Returns

table

### Example 1

Remove the first row of the table.

```m
Table.RemoveFirstN(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
1
)
```

// Output
```
Table.FromRecords({
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
```

### Example 2

Remove the first two rows of the table.

```m
Table.RemoveFirstN(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
2
)
```

// Output
```
Table.FromRecords({
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
```

### Example 3

Remove the first rows where [CustomerID] <=2 of the table.

```m
Table.RemoveFirstN(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,
[CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
each [CustomerID] <= 2
)
```

// Output
```
Table.FromRecords({
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
```


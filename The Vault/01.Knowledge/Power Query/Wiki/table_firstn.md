---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.FirstN

Returns the first row(s) of the table table, depending on the value of countOrCondition: If countOrCondition is a number, that many rows (starting at the top) will be returned. If countOrCondition is a condition, the rows that meet the condition will be returned until a row does not meet the condition.

## Signature

```m
Table.FirstN(table as table, countOrCondition as any) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| countOrCondition | any | |

## Returns

table

### Example 1

Find the first two rows of the table.

```m
Table.FirstN(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
}),
2
)
```

// Output
```
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"]
})
```

### Example 2

Find the first rows where [a] > 0 in the table.

```m
Table.FirstN(
Table.FromRecords({
[a = 1, b = 2],
[a = 3, b = 4],
[a = -5, b = -6]
}),
each [a] > 0
)
```

// Output
```
Table.FromRecords({
[a = 1, b = 2],
[a = 3, b = 4]
})
```


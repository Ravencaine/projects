---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.AlternateRows

Keeps the initial offset then alternates taking and skipping the following rows. table: The input table. offset: The number of rows to keep before starting iterations. skip: The number of rows to remove in each iteration. take: The number of rows to keep in each iteration.

## Signature

```m
Table.AlternateRows(
table as table,
offset as number,
skip as number,
take as number
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| offset | number | |
| skip | number | |
| take | number | |

## Returns

table

### Example 1

Return a table from the table that, starting at the first row, skips 1 value and then keeps 1 value.

```m
Table.AlternateRows(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
}),
1,
1,
1
)
```

// Output
```
Power Query M
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```


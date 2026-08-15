---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.Sort

Sorts the table using the list of one or more column names and optional comparisonCriteria in the form { { col1, comparisonCriteria }, {col2} }.

## Signature

```m
Table.Sort(table as table, comparisonCriteria as any) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| comparisonCriteria | any | |

## Returns

table

### Example 1

Sort the table on column "OrderID".

```m
Table.Sort(
Table.FromRecords({
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],
[OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],
[OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],
[OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
[OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
[OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],
[OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]
}),
{"OrderID"}
)
```

// Output
```
Table.FromRecords({
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25],
[OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200],
[OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2],
[OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20],
[OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
[OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100],
[OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]
})
```

### Example 2

Sort the table on column "OrderID" in descending order.

```m
Table.Sort(
Table.FromRecords({
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],
[OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],
[OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],
[OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
[OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
[OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],
[OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]
}),
{"OrderID", Order.Descending}
)
```

// Output
```
Table.FromRecords({
[OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25],
[OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100],
[OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
[OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20],
[OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2],
[OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5],
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100]
})
```

### Example 3

Sort the table on column "CustomerID" then "OrderID", with "CustomerID" being in ascending order.

```m
Table.Sort(
Table.FromRecords({
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],
[OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],
[OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],
[OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
[OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
[OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],
[OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]
}),
{
{"CustomerID", Order.Ascending},
"OrderID"
}
)
```

// Output
```
Table.FromRecords({
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5],
[OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25],
[OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200],
[OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2],
[OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
[OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100],
[OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]
})
```

## Related

[[comparison_criteria]]


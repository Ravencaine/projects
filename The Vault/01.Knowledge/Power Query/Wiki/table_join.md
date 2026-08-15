---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.Join

Joins the rows of table1 with the rows of table2 based on the equality of the values of the key columns selected by key1 (for table1) and key2 (for table2). By default, an inner join is performed, however an optional joinKind may be included to specify the type of join. Options include: JoinKind.Inner JoinKind.LeftOuter JoinKind.RightOuter JoinKind.FullOuter JoinKind.LeftAnti JoinKind.RightAnti JoinKind.LeftSemi JoinKind.RightSemi An optional set of keyEqualityComparers may be included to specify how to compare the key columns. This parameter is currently intended for internal use only.

## Signature

```m
Table.Join(
table1 as table,
key1 as any,
table2 as table,
key2 as any,
optional joinKind as nullable number,
optional joinAlgorithm as nullable number,
optional keyEqualityComparers as nullable list
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table1 | table | |
| key1 | any | |
| table2 | table | |
| key2 | any | |
| optional joinKind | nullable number | |
| optional joinAlgorithm | nullable number | |
| optional keyEqualityComparers | nullable list | |

## Returns

table

### Example 1

Join two tables using a single key column.

```m
Table.Join(
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"],
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
}),
"CustomerID",
Table.FromRecords({
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],
[OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],
[OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],
[OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
[OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25]
}),
"CustomerID"
)
```

// Output
```
Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567", OrderID = 1, Item = "Fishing
rod", Price = 100],
[CustomerID = 1, Name = "Bob", Phone = "123-4567", OrderID = 2, Item = "1 lb.
worms", Price = 5],
[CustomerID = 2, Name = "Jim", Phone = "987-6543", OrderID = 3, Item = "Fishing
net", Price = 25],
[CustomerID = 3, Name = "Paul", Phone = "543-7890", OrderID = 4, Item = "Fish
tazer", Price = 200],
[CustomerID = 3, Name = "Paul", Phone = "543-7890", OrderID = 5, Item =
"Bandaids", Price = 2],
[CustomerID = 1, Name = "Bob", Phone = "123-4567", OrderID = 6, Item = "Tackle
box", Price = 20]
})
```

### Example 2

Join two tables that have conflicting column names, using multiple key columns.

```m
let
customers = Table.FromRecords({
[TenantID = 1, CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[TenantID = 1, CustomerID = 2, Name = "Jim", Phone = "987-6543"]
}),
orders = Table.FromRecords({
[TenantID = 1, OrderID = 1, CustomerID = 1, Name = "Fishing rod", Price =
100.0],
[TenantID = 1, OrderID = 2, CustomerID = 1, Name = "1 lb. worms", Price =
5.0],
[TenantID = 1, OrderID = 3, CustomerID = 2, Name = "Fishing net", Price =
25.0]
})
in
Table.Join(
customers,
{"TenantID", "CustomerID"},
Table.PrefixColumns(orders, "Order"),
{"Order.TenantID", "Order.CustomerID"}
)
```

// Output
```
Table.FromRecords({
[TenantID = 1, CustomerID = 1, Name = "Bob", Phone = "123-4567", Order.TenantID
= 1, Order.OrderID = 1, Order.CustomerID = 1, Order.Name = "Fishing rod",
Order.Price = 100],
[TenantID = 1, CustomerID = 1, Name = "Bob", Phone = "123-4567", Order.TenantID
= 1, Order.OrderID = 2, Order.CustomerID = 1, Order.Name = "1 lb. worms",
Order.Price = 5],
[TenantID = 1, CustomerID = 2, Name = "Jim", Phone = "987-6543", Order.TenantID
= 1, Order.OrderID = 3, Order.CustomerID = 2, Order.Name = "Fishing net",
Order.Price = 25]
})
Last updated on 03/25/2026
```


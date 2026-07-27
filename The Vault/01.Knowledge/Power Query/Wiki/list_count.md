---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Count

Returns the number of items in the specified list. list: The list to examine.

## Signature

```m
List.Count(list as list) as number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |

## Returns

number

### Example 1

Find the number of values in the list {1, 2, 3}.

```m
List.Count({1, 2, 3})
```

// Output
```
3
```

### Example 2

Find the number of times red appears in a list of colors, ignoring case.

```m
let
colors = {"Red", "Blue", "GREEN", "red", "Yellow", "RED"},
redCount = List.Count(
List.Select(colors, each Text.Lower(_) = "red")
)
in
redCount
```

// Output
```
3
```

### Example 3

Find the number of customers in a list who purchased more than $100.

```m
let
customers = {
[CustomerID = 101, CustomerName = "Alice", AmountPurchased = 150],
[CustomerID = 102, CustomerName = "Bob", AmountPurchased = 75],
[CustomerID = 103, CustomerName = "Carol", AmountPurchased = 50],
[CustomerID = 104, CustomerName = "Dave", AmountPurchased = 90],
[CustomerID = 105, CustomerName = "Eve", AmountPurchased = 120]
},
highValueCustomerCount = List.Count(
List.Select(customers, each [AmountPurchased] > 100)
)
in
highValueCustomerCount
```

// Output
```
2
```


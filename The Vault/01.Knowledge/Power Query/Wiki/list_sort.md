---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Sort

Sorts a list of data, list, according to the optional criteria specified. An optional parameter, comparisonCriteria, can be specified as the comparison criterion. This can take the following values: To control the order, the comparison criterion can be an Order enum value. (Order.Descending, Order.Ascending). To compute a key to be used for sorting, a function of 1 argument can be used. To both select a key and control order, comparison criterion can be a list containing the key and order ({each 1 / _, Order.Descending}). To completely control the comparison, a function of 2 arguments can be used. This function will be passed two items from the list (any two items, in any order). The function should return one of the following values: -1: The first item is less than the second item. 0: The items are equal. 1: The first item is greater than the second item. Value.Compare is a method that can be used to delegate this logic.

## Signature

```m
List.Sort(list as list, optional comparisonCriteria as any) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional comparisonCriteria | any | |

## Returns

list

### Example 1

Sort the list {2, 3, 1}.

```m
List.Sort({2, 3, 1})
```

// Output
```
{1, 2, 3}
```

### Example 2

Sort the list {2, 3, 1} in descending order.

```m
List.Sort({2, 3, 1}, Order.Descending)
```

// Output
```
{3, 2, 1}
```

### Example 3

Sort the list {2, 3, 1} in descending order using the Value.Compare method.

```m
List.Sort({2, 3, 1}, (x, y) => Value.Compare(1/x, 1/y))
```

// Output
```
{3, 2, 1}
```


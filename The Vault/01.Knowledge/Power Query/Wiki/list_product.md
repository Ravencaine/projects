---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Product

Returns the product of the non-null numbers in the list, numbersList. Returns null if there are no non-null values in the list.

## Signature

```m
List.Product(numbersList as list, optional precision as nullable number) as
nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| numbersList | list | |
| optional precision | nullable number | |

## Returns

nullable number

### Example 1

Find the product of the numbers in the list {1, 2, 3, 3, 4, 5, 5}.

```m
List.Product({1, 2, 3, 3, 4, 5, 5})
```

// Output
```
1800
```


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Covariance

Returns the covariance between two lists, numberList1 and numberList2. numberList1 and numberList2 must contain the same number of number values.

## Signature

```m
List.Covariance(numberList1 as list, numberList2 as list) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| numberList1 | list | |
| numberList2 | list | |

## Returns

nullable number

### Example 1

Calculate the covariance between two lists.

```m
List.Covariance({1, 2, 3}, {1, 2, 3})
```

// Output
```
0.66666666666666607
```


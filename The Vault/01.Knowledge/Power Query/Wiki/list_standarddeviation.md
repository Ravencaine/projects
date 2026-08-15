---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.StandardDeviation

Returns a sample based estimate of the standard deviation of the values in the list, numbersList. If numbersList is a list of numbers, a number is returned. An error is raised on an empty list or a list of items that is not type number.

## Signature

```m
List.StandardDeviation(numbersList as list) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| numbersList | list | |

## Returns

nullable number

### Example 1

Find the standard deviation of the numbers 1 through 5.

```m
List.StandardDeviation({1..5})
Outut
1.5811388300841898
Last updated on 01/22/2026
```


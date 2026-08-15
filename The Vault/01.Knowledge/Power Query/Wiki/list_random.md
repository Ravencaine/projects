---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.Random

Returns a list of random numbers between 0 and 1, given the number of values to generate and an optional seed value. count: The number of random values to generate. seed: [Optional] A numeric value used to seed the random number generator. If omitted a unique list of random numbers is generated each time you call the function. If you specify the seed value with a number every call to the function generates the same list of random numbers.

## Signature

```m
List.Random(count as number, optional seed as nullable number) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| count | number | |
| optional seed | nullable number | |

## Returns

list

### Example 1

Create a list of 3 random numbers.

```m
List.Random(3)
```

// Output
```
{0.992332, 0.132334, 0.023592}
```

### Example 2

Create a list of 3 random numbers, specifying seed value.

```m
List.Random(3, 2)
```

// Output
```
{0.883002, 0.245344, 0.723212}
```


---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.Log

Returns the logarithm of a number, number, to the specified base base. If base is not specified, the default value is Number.E. If number is null Number.Log returns null.

## Signature

```m
Number.Log(number as nullable number, optional base as nullable number) as
nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |
| optional base | nullable number | |

## Returns

nullable number

### Example 1

Get the base 10 logarithm of 2.

```m
Number.Log(2, 10)
```

// Output
```
0.3010299956639812
```

### Example 2

Get the base e logarithm of 2.

```m
Number.Log(2)
```

// Output
```
0.69314718055994529
```


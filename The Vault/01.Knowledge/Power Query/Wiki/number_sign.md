---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.Sign

Returns 1 for if number is a positive number, -1 if it is a negative number, and 0 if it is zero. If number is null, Number.Sign returns null.

## Signature

```m
Number.Sign(number as nullable number) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |

## Returns

nullable number

### Example 1

Determine the sign of 182.

```m
Number.Sign(182)
```

// Output
```
1
```

### Example 2

Determine the sign of -182.

```m
Number.Sign(-182)
```

// Output
```
-1
```

### Example 3

Determine the sign of 0.

```m
Number.Sign(0)
```

// Output
```
0
```


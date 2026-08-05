---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["type", "m-function"]
---


# Type.FunctionRequiredParameters

Returns a number indicating the minimum number of parameters required to invoke the input type of function.

## Signature

```m
Type.FunctionRequiredParameters(type as type) as number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| type | type | |

## Returns

number

### Example 1

Find the number of required parameters to the function (x as number, optional y as text).

```m
Type.FunctionRequiredParameters(type function (x as number, optional y as text) as
any)
```

// Output
```
1
```


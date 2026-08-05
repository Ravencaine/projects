---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["type", "m-function"]
---


# Type.ForFunction

Creates a function type from signature, a record of ReturnType and Parameters, and min, the minimum number of arguments required to invoke the function.

## Signature

```m
Type.ForFunction(signature as record, min as number) as type
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| signature | record | |
| min | number | |

## Returns

type

### Example 1

Creates the type for a function that takes a number parameter named X and returns a number.

```m
Type.ForFunction([ReturnType = type number, Parameters = [X = type number]], 1)
```

// Output
```
type function (X as number) as number
```


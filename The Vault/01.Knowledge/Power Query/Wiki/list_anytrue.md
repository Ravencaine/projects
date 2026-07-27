---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.AnyTrue

Returns true if any expression in the list list is true.

## Signature

```m
List.AnyTrue(list as list) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |

## Returns

logical

### Example 1

Determine if any of the expressions in the list {true, false, 2 > 0} are true.

```m
List.AnyTrue({true, false, 2>0})
```

// Output
```
true
```

### Example 2

Determine if any of the expressions in the list {2 = 0, false, 2 < 0} are true.

```m
List.AnyTrue({2 = 0, false, 2 < 0})
```

// Output
```
false
```


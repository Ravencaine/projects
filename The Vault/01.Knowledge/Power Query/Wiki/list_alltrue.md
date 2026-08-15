---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.AllTrue

Returns true if all expressions in the list list are true.

## Signature

```m
List.AllTrue(list as list) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |

## Returns

logical

### Example 1

Determine if all the expressions in the list {true, true, 2 > 0} are true.

```m
List.AllTrue({true, true, 2 > 0})
```

// Output
```
true
```

### Example 2

Determine if all the expressions in the list {true, true, 2 < 0} are true.

```m
List.AllTrue({true, false, 2 < 0})
```

// Output
```
false
```


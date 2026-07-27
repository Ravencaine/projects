---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Buffer

Buffers the list list in memory. The result of this call is a stable list.

## Signature

```m
List.Buffer(list as list) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |

## Returns

list

### Example 1

Create a stable copy of the list {1..10}.

```m
List.Buffer({1..10})
```

// Output
```
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```


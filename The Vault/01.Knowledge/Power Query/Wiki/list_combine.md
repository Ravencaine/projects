---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Combine

Takes a list of lists, lists, and merges them into a single new list.

## Signature

```m
List.Combine(lists as list) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| lists | list | |

## Returns

list

### Example 1

Combine the two simple lists {1, 2} and {3, 4}.

```m
List.Combine({{1, 2}, {3, 4}})
```

// Output
```
{
1,
2,
3,
4
}
```

### Example 2

Combine the two lists, {1, 2} and {3, {4, 5}}, one of which contains a nested list.

```m
List.Combine({{1, 2}, {3, {4, 5}}})
```

// Output
```
{
1,
2,
3,
{4, 5}
}
```


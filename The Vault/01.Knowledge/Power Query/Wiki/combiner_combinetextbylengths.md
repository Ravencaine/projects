---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [combiner, m-function]
---


# Combiner.CombineTextByLengths

Returns a function that combines a list of text values into a single text value using the specified lengths.

## Signature

```m
Combiner.CombineTextByLengths(lengths as list, optional template as nullable text)
as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| lengths | list | |
| optional template | nullable text | |

## Returns

function

### Example 1

Combine a list of text values by extracting the specified numbers of characters from each input value.

```m
Combiner.CombineTextByLengths({1, 2, 3})({"aaa", "bbb", "ccc"})
```

// Output
```
"abbccc"
```

### Example 2

Combine a list of text values by extracting the specified numbers of characters, after first pre- filling the result with the template text.

```m
Combiner.CombineTextByLengths({1, 2, 3}, "*********")({"aaa", "bbb", "ccc"})
```

// Output
```
"abbccc***"
```


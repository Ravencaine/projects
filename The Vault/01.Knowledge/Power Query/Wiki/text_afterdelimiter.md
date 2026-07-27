---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.AfterDelimiter

Returns the portion of text after the specified delimiter. An optional numeric index indicates which occurrence of the delimiter should be considered. An optional list index indicates which occurrence of the delimiter should be considered, as well as whether indexing should be done from the start or end of the input.

## Signature

```m
Text.AfterDelimiter(
text as nullable text,
delimiter as text,
optional index as any
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| delimiter | text | |
| optional index | any | |

## Returns

any

### Example 1

Get the portion of "111-222-333" after the (first) hyphen.

```m
Text.AfterDelimiter("111-222-333", "-")
```

// Output
```
"222-333"
```

### Example 2

Get the portion of "111-222-333" after the second hyphen.

```m
Text.AfterDelimiter("111-222-333", "-", 1)
```

// Output
```
"333"
```

### Example 3

Get the portion of "111-222-333" after the second hyphen from the end.

```m
Text.AfterDelimiter("111-222-333", "-", {1, RelativePosition.FromEnd})
```

// Output
```
"222-333"
```


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [logical, m-function]
---


# Logical.FromText

Creates a logical value from the text value text, either "true" or "false". If text contains a different string, an error is raised. The text value text is case insensitive.

## Signature

```m
Logical.FromText(text as nullable text) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |

## Returns

nullable logical

### Example 1

Create a logical value from the text string "true".

```m
Logical.FromText("true")
```

// Output
```
true
```

### Example 2

Create a logical value from the text string "a".

```m
Logical.FromText("a")
```

// Output
```
[Expression.Error] Could not convert to a logical.
Last updated on 01/22/2026
```


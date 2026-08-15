---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.Repeat

Returns a text value composed of the input text text repeated count times.

## Signature

```m
Text.Repeat(text as nullable text, count as number) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| count | number | |

## Returns

nullable text

### Example 1

Repeat the text "a" five times.

```m
Text.Repeat("a", 5)
```

// Output
```
"aaaaa"
```

### Example 2

Repeat the text "helloworld" three times.

```m
Text.Repeat("helloworld.", 3)
```

// Output
```
"helloworld.helloworld.helloworld."
```


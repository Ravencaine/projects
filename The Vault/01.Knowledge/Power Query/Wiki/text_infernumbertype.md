---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.InferNumberType

Infers the granular number type (Int64.Type, Double.Type, and so on) of text. An error is raised if text is not a number. An optional culture may also be provided (for example, "en-US"). Related content How culture affects text formatting --- PAGE 1200 ---

## Signature

```m
Text.InferNumberType(text as text, optional culture as nullable text) as type
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | text | |
| optional culture | nullable text | |

## Returns

type


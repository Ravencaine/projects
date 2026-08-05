---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["fabricai", "m-function"]
---


# FabricAI.Prompt

Returns the result of passing the specified input to an AI model. An optional context value can be provided in order to specify additional data that's relevant to the request.

## Signature

```m
FabricAI.Prompt(input as text, optional context as any) as text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | text | |
| optional context | any | |

## Returns

text

### Example 1

Use an AI model to categorize a product review.

```m
FabricAI.Prompt(
"Categorize the review as positive, negative, or neutral, and extract a single
key word in parentheses.",
[Review = "This is a great product. It only broke four times before we had to
return it!"]
)
```

// Output
```
"Negative (broke)"
Last updated on 11/18/2025
```


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.SplitAny

Returns a list of text values resulting from the splitting of a text value based on any character specified in the delimiter. text: The text value to split. separator: The delimiter characters used to split the text.

## Signature

```m
Text.SplitAny(text as text, separators as text) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | text | |
| separators | text | |

## Returns

list

### Example 1

Create a list from the given text using the specified delimiter characters.

```m
Text.SplitAny("Name|Customer ID|Purchase|Month-Day-Year", "|-")
```

// Output
```
{
"Name",
"Customer ID",
"Purchase",
"Month",
"Day",
"Year"
}
```


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.TrimStart

Returns the result of removing all leadling characters from the specified text. By default, all the leading whitespace characters are removed. text: The text from which the leading characters are to be removed. trim: Overrides the whitespace characters that are trimmed by default. This parameter can either be a single character or a list of single characters. Each leading trim operation stops when a non-trimmed character is encountered.

## Signature

```m
Text.TrimStart(text as nullable text, optional trim as any) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| optional trim | any | |

## Returns

nullable text

### Example 1

Remove leading whitespace from " a b c d ". Usage**

// Output
```
"a b c d "
```

### Example 2

Remove leading zeroes from the text representation of a number.

```m
Text.TrimStart("0000056.420", "0")
```

// Output
```
"56.420"
```

### Example 3

Remove the leading padding characters from a fixed width account name.

```m
let
Source = #table(type table [Name = text, Account Name= text, Interest =
number],
{
{"Bob", "@****847263-US", 2.8410},
{"Leslie", "@******4648-FR", 3.8392},
{"Ringo", "@*****24679-DE", 12.6600}
}),
#"Trimmed Account" = Table.TransformColumns(Source, {"Account Name", each
Text.TrimStart(_, {"*", "@"})})
in
#"Trimmed Account"
```

// Output
```
#table(type table [Name = text, Account Name = text, Interest = number],
{
{"Bob", "847263-US", 2.841},
{"Leslie", "4648-FR", 3.8392},
{"Ringo", "2046790-DE", 12.66}
}),
```


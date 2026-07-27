---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.Start

Returns the first count characters of text as a text value.

## Signature

```m
Text.Start(text as nullable text, count as number) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| count | number | |

## Returns

nullable text

### Example 1

Get the first 5 characters of "Hello, World".

```m
Text.Start("Hello, World", 5)
```

// Output
```
"Hello"
```

### Example 2

Use the first four characters of the first name and the first three characters of the last name to create an individual's email address.

```m
let
Source = #table(type table [First Name = text, Last Name = text],
{
{"Douglas", "Elis"},
{"Ana", "Jorayew"},
{"Rada", "Mihaylova"}
}),
EmailAddress = Table.AddColumn(
Source,
"Email Address",
each Text.Combine({
Text.Start([First Name], 4),
Text.Start([Last Name], 3),
"@contoso.com"
})
)
in
EmailAddress
```

// Output
```
#table(type table [First Name = text, Last Name = text, Email Address = text],
{
{"Douglas", "Elis", "DougEli@contoso.com"},
{"Ana", "Jorayew", "AnaJor@contoso.com"},
{"Rada", "Mihaylova", "RadaMih@contoso.com"}
})
```


---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.Combine

Returns the result of combining the list of text values, texts, into a single text value. Any null values present in texts are ignored. An optional separator used in the final combined text can be specified.

## Signature

```m
Text.Combine(texts as list, optional separator as nullable text) as text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| texts | list | |
| optional separator | nullable text | |

## Returns

text

### Example 1

Combine text values "Seattle" and "WA".

```m
Text.Combine({"Seattle", "WA"})
```

// Output
```
"SeattleWA"
```

### Example 2

Combine text values "Seattle" and "WA", separated by a comma and a space.

```m
Text.Combine({"Seattle", "WA"}, ", ")
```

// Output
```
"Seattle, WA"
```

### Example 3

Combine the values "Seattle", null, and "WA", separated by a comma and a space. (Note that the null is ignored.)

```m
Text.Combine({"Seattle", null, "WA"}, ", ")
```

// Output
```
"Seattle, WA"
```

### Example 4

```m
Combine the first name, middle initial (if present), and last name into the individual’s full name.
Power Query M
let
Source = Table.FromRecords({
[First Name = "Doug", Middle Initial = "J", Last Name = "Elis"],
[First Name = "Anna", Middle Initial = "M", Last Name = "Jorayew"],
[First Name = "Rada", Middle Initial = null, Last Name = "Mihaylova"]
}),
FullName = Table.AddColumn(Source, "Full Name", each Text.Combine({[First
Name], [Middle Initial], [Last Name]}, " "))
in
FullName
```

// Output
```
Table.FromRecords({
[First Name = "Doug", Middle Initial = "J", Last Name = "Elis", Full Name =
"Doug J Elis"],
[First Name = "Anna", Middle Initial = "M", Last Name = "Jorayew", Full Name =
"Anna M Jorayew"],
[First Name = "Rada", Middle Initial = null, Last Name = "Mihaylova", Full
Name = "Rada Mihaylova"]
})
```


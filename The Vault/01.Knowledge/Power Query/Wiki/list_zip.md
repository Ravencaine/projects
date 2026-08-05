---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Zip

Takes a list of lists, lists, and returns a list of lists combining items at the same position.

## Signature

```m
List.Zip(lists as list) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| lists | list | |

## Returns

list

### Example 1

Zips the two simple lists {1, 2} and {3, 4}.

```m
List.Zip({{1, 2}, {3, 4}})
```

// Output
```
{
{1, 3},
{2, 4}
}
```

### Example 2

Zips the two simple lists of different lengths {1, 2} and {3}.

```m
List.Zip({{1, 2}, {3}})
```

// Output
```
{
{1, 3},
{2, null}
}
Logical functions
Article • 11/22/2024
These functions create and manipulate logical (that is, true or false) values.
ﾉ Expand table
Name Description
Logical.From Creates a logical from the given value.
Logical.FromText Creates a logical value from the text values "true" and "false".
Logical.ToText Returns the text "true" or "false" given a logical value.
Feedback
Was this page helpful?  Yes  No
Provide product feedback | Ask the community
```


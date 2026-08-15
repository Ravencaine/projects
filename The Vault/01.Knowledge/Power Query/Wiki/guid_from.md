---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [guid, m-function]
---


# Guid.From

Returns a Guid.Type value from the given value. If the given value is null, Guid.From returns null. A check will be performed to determine if the given value is in an acceptable format. Acceptable formats provided in the examples.

## Signature

```m
Guid.From(value as nullable text) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | nullable text | |

## Returns

nullable text

### Example 1

The Guid can be provided as 32 contiguous hexadecimal digits.

```m
Guid.From("05FE1DADC8C24F3BA4C2D194116B4967")
```

// Output
```
"05fe1dad-c8c2-4f3b-a4c2-d194116b4967"
```

### Example 2

The Guid can be provided as 32 hexadecimal digits separated by hyphens into blocks of 8-4-4- 4-12.

```m
Guid.From("05FE1DAD-C8C2-4F3B-A4C2-D194116B4967")
```

// Output
```
"05fe1dad-c8c2-4f3b-a4c2-d194116b4967"
```

### Example 3

The Guid can be provided as 32 hexadecimal digits separated by hyphens and enclosed in braces.

```m
Guid.From("{05FE1DAD-C8C2-4F3B-A4C2-D194116B4967}")
```

// Output
```
"05fe1dad-c8c2-4f3b-a4c2-d194116b4967"
```

### Example 4

The Guid can be provided as 32 hexadecimal digits separated by hyphens and enclosed by parentheses.

```m
Text.FromBinary(Json.FromValue([A = {1, true, "3"}, B = #date(2012, 3, 25)]))
```

// Output
```
"{""A"":[1,true,""3""],""B"":""2012-03-25""}"
Last updated on 03/24/2026
```


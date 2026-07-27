---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["comparer", "m-function"]
---


# Comparer.FromCulture

Returns a comparer function that uses the culture and the case-sensitivity specified by ignoreCase to perform comparisons. A comparer function accepts two arguments and returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second. The default value for ignoreCase is false. The culture should be one of the locales supported by the .NET framework (for example, "en-US").

## Signature

```m
Comparer.FromCulture(culture as text, optional ignoreCase as nullable logical) as
function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| culture | text | |
| optional ignoreCase | nullable logical | |

## Returns

function

### Example 1

Compare "a" and "A" using "en-US" locale to determine if the values are equal.

```m
Comparer.FromCulture("en-US")("a", "A")
```

// Output
```
-1
```

### Example 2

Compare "a" and "A" using "en-US" locale ignoring the case to determine if the values are equal.

```m
Power Query M
Comparer.FromCulture("en-US", true)("a", "A")
```

// Output
```
0
Last updated on 04/03/2026
```


---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# LEFT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the specified number of characters from the start of a text string.

## Syntax

```dax
LEFT(<text>, <num_chars>)
```

## Remarks

Whereas Microsoft Excel contains different functions for working with text in single-byte and double-byte character languages, DAX works with Unicode and stores all characters as the same length; therefore, a single function is enough. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules. This function returns different results depending on the UnicodeCharacterBehavior setting of your model.
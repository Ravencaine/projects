---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# RIGHT

Applies to: Calculated column Calculated table Measure Visual calculation RIGHT returns the last character or characters in a text string, based on the number of characters you specify.

## Syntax

```dax
RIGHT(<text>, <num_chars>)
```

## Remarks

This function returns different results depending on the UnicodeCharacterBehavior setting of your model. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.
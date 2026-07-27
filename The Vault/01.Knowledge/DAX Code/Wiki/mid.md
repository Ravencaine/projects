---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# MID

Applies to: Calculated column Calculated table Measure Visual calculation Returns a string of characters from the middle of a text string, given a starting position and length.

## Syntax

```dax
MID(<text>, <start_num>, <num_chars>)
```

## Remarks

Whereas Microsoft Excel has different functions for working with single-byte and double- byte characters languages, DAX uses Unicode and stores all characters with the same length. This function returns different results depending on the UnicodeCharacterBehavior setting of your model.
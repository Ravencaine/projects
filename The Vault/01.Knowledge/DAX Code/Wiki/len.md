---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# LEN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of characters in a text string.

## Syntax

```dax
LEN(<text>)
```

## Remarks

Whereas Microsoft Excel has different functions for working with single-byte and double- byte character languages, DAX uses Unicode and stores all characters with the same length. If you use LEN with a column that contains non-text values, such as dates or Booleans, the function implicitly casts the value to text, using the current column format. This function returns different results depending on the UnicodeCharacterBehavior setting of your model.
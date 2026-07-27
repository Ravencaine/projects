---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# UNICHAR

Applies to: Calculated column Calculated table Measure Visual calculation Returns the Unicode character referenced by the numeric value.

## Syntax

```dax
UNICHAR(number)
```

## Remarks

If XML characters are not invalid, UNICHAR returns an error. If Unicode numbers are partial surrogates and data types are not valid, UNICHAR returns an error. If numbers are numeric values that fall outside the allowable range, UNICHAR returns an error. If number is zero (0), UNICHAR returns an error. The Unicode character returned can be a string of characters, for
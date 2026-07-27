---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# TRIM

Applies to: Calculated column Calculated table Measure Visual calculation Removes all spaces from text except for single spaces between words.

## Syntax

```dax
TRIM(<text>)
```

## Remarks

Use TRIM on text that you have received from another application that may have irregular spacing. The TRIM function was originally designed to trim the 7-bit ASCII space character (value 32) from text. In the Unicode character set, there is an additional space character called the nonbreaking space character that has a decimal value of 160. This character is commonly used in Web pages as the HTML entity, &nbsp;. By itself, the TRIM function does not remove this nonbreaking space character. For an
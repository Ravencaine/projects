---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# REPLACE

Applies to: Calculated column Calculated table Measure Visual calculation REPLACE replaces part of a text string, based on the number of characters you specify, with a different text string.

## Syntax

```dax
REPLACE(<old_text>, <start_num>, <num_chars>, <new_text>)
```

## Remarks

Whereas Microsoft Excel has different functions for use with single-byte and double-byte character languages, DAX uses Unicode and therefore stores all characters as the same length.
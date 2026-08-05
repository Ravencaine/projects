---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# CONCATENATE

Applies to: Calculated column Calculated table Measure Visual calculation Joins two text strings into one text string.

## Syntax

```dax
CONCATENATE(<text1>, <text2>)
```

## Remarks

The CONCATENATE function joins two text strings into one text string. The joined items can be text, numbers, Boolean values represented as text, or a combination of those items. You can also use a column reference if the column contains appropriate values. The CONCATENATE function in DAX accepts only two arguments, whereas the Excel CONCATENATE function accepts up to 255 arguments. If you need to
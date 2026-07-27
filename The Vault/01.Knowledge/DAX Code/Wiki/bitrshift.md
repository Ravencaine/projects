---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# BITRSHIFT

Applies to: Calculated column Calculated table Measure Visual calculation Returns a number shifted right by the specified number of bits.

## Syntax

```dax
BITRSHIFT(<Number>, <Shift_Amount>)
```

## Remarks

Be sure to understand the nature of bitshift operations and overflow/underflow of integers before using DAX bitshift functions. If Shift_Amount is negative, it will shift in the opposite direction. If absolute value of Shift_Amount is larger than 64, there will be no error but will result in overflow/underflow. There’s no limit on Number, but the result may overflow/underflow.
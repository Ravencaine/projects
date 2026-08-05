---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# COTH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the hyperbolic cotangent of a hyperbolic angle.

## Syntax

```dax
COTH(N)
```

## Remarks

The hyperbolic cotangent is an analog of the ordinary (circular) cotangent. 227 The absolute value of number must be less than and cannot be 0. If number is outside its constraints, an error is returned If number is a non-numeric value, an error is returned. The following equation is used: 1 COSH(N) eN + e−N COTH(N) = = = TANH(N) SINH(N) eN − e−N
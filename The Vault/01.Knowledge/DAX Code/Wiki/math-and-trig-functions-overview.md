---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: concept
tags: [dax, math-functions, trig-functions, overview]
---

# Math and Trig Functions in DAX

DAX provides a comprehensive set of mathematical and trigonometric functions.

## Rounding Functions

| Function | Description |
|----------|-------------|
| ROUND | Round to specified decimal places |
| ROUNDDOWN | Round toward zero |
| ROUNDUP | Round away from zero |
| TRUNC | Truncate to integer (remove fractional part) |
| INT | Round down to nearest integer |
| MROUND | Round to nearest multiple |
| CEILING | Round up to nearest multiple |
| FLOOR | Round down to nearest multiple |

### CEILING vs ISO.CEILING

Both round up, but differ for negative numbers:
```dax
CEILING(-5, 3)    -- returns -3 (upward, toward zero)
ISO.CEILING(-5, 3) -- returns -6 (upward, away from zero)
```

### INT vs TRUNC
```dax
INT(-4.3)    -- -5 (rounds down to lower integer)
TRUNC(-4.3)  -- -4 (drops the fractional part)
```

## Trigonometric Functions

| Function | Description |
|----------|-------------|
| SIN, SINH | Sine, Hyperbolic sine |
| COS, COSH | Cosine, Hyperbolic cosine |
| TAN, TANH | Tangent, Hyperbolic tangent |
| COT, COTH | Cotangent, Hyperbolic cotangent |
| ASIN, ASINH | Arcsine, Hyperbolic arcsine |
| ACOS, ACOSH | Arccosine, Hyperbolic arccosine |
| ATAN, ATANH | Arctangent, Hyperbolic arctangent |

## Logarithmic and Exponential

| Function | Description |
|----------|-------------|
| EXP | e raised to a power |
| LN | Natural logarithm (use LOG(x, EXP(1))) |
| LOG | Logarithm to specified base |
| LOG10 | Base-10 logarithm |
| POWER | Raise to a power (or use ^) |

## Other Math Functions

| Function | Description |
|----------|-------------|
| ABS | Absolute value |
| SIGN | Returns 1 (positive), 0 (zero), -1 (negative) |
| SQRT | Square root |
| FACT | Factorial |
| MOD | Remainder after division |
| QUOTIENT | Integer portion of division |
| PI | Returns 3.14159... |
| RAND | Random number (0-1, recalculates each query) |
| RANDBETWEEN | Random integer between two values |
| GCD | Greatest common divisor |
| LCM | Least common multiple |
| ODD | Next odd integer (up if needed) |
| EVEN | Next even integer (up if needed) |
| CONVERT | Convert between data types |

## Data Type Conversions

```dax
CONVERT(<expression>, <type>)
-- Types: INTEGER, DOUBLE, CURRENCY, STRING, BOOLEAN, DATETIME
CONVERT([Amount], INTEGER)
```

## Bitwise Operations

| Function | Description |
|----------|-------------|
| BITAND | Bitwise AND |
| BITOR | Bitwise OR |
| BITXOR | Bitwise XOR |
| BITLSHIFT | Bitwise left shift |
| BITRSHIFT | Bitwise right shift |

## Related

- [[round-trunc-int]]
- [[power-log-exp]]
- [[sqrt]]

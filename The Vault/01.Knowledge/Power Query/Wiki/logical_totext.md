---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["logical", "m-function"]
---


# Logical.ToText

Creates a text value from the logical value logicalValue, either true or false. If logicalValue is not a logical value, an error is raised.

## Signature

```m
Logical.ToText(logicalValue as nullable logical) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| logicalValue | nullable logical | |

## Returns

nullable text

### Example 1

Create a text value from the logical true.

```m
Logical.ToText(true)
```

// Output
```
"true"
Last updated on 01/22/2026
Number functions
08/11/2025
These functions create and manipulate number values.
Information
ﾉ Expand table
Name Description
Number.IsEven Returns true if a value is an even number.
Number.IsNaN Returns true if a value is Number.NaN.
Number.IsOdd Returns true if a value is an odd number.
Conversion and formatting
ﾉ Expand table
Name Description
Byte.From Returns an 8-bit integer number value from the given value.
Currency.From Returns a currency value from the given value.
Decimal.From Returns a decimal number value from the given value.
Double.From Returns a Double number value from the given value.
Int8.From Returns a signed 8-bit integer number value from the given value.
Int16.From Returns a 16-bit integer number value from the given value.
Int32.From Returns a 32-bit integer number value from the given value.
Int64.From Returns a 64-bit integer number value from the given value.
Number.From Returns a number value from a value.
Number.FromText Returns a number value from a text value.
Number.ToText Converts the given number to text.
Percentage.From Returns a percentage value from the given value.
Name Description
Single.From Returns a Single number value from the given value.
Rounding
ﾉ Expand table
Name Description
Number.Round Returns a nullable number (n) if value is an integer.
Number.RoundAwayFromZero Returns Number.RoundUp(value) when value >= 0 and
Number.RoundDown(value) when value < 0.
Number.RoundDown Returns the largest integer less than or equal to a number value.
Number.RoundTowardZero Returns Number.RoundDown(x) when x >= 0 and Number.RoundUp(x)
when x < 0.
Number.RoundUp Returns the larger integer greater than or equal to a number value.
Operations
ﾉ Expand table
Name Description
Number.Abs Returns the absolute value of a number.
Number.Combinations Returns the number of combinations of a given number of items for the optional
combination size.
Number.Exp Returns a number representing e raised to a power.
Number.Factorial Returns the factorial of a number.
Number.IntegerDivide Divides two numbers and returns the whole part of the resulting number.
Number.Ln Returns the natural logarithm of a number.
Number.Log Returns the logarithm of a number to the base.
Number.Log10 Returns the base-10 logarithm of a number.
Number.Mod Divides two numbers and returns the remainder of the resulting number.
Name Description
Number.Permutations Returns the number of total permutations of a given number of items for the
optional permutation size.
Number.Power Returns a number raised by a power.
Number.Sign Returns 1 for positive numbers, -1 for negative numbers, or 0 for zero.
Number.Sqrt Returns the square root of a number.
Random
ﾉ Expand table
Name Description
Number.Random Returns a random fractional number between 0 and 1.
Number.RandomBetween Returns a random number between the two given number values.
Trigonometry
ﾉ Expand table
Name Description
Number.Acos Returns the arccosine of a number.
Number.Asin Returns the arcsine of a number.
Number.Atan Returns the arctangent of a number.
Number.Atan2 Returns the arctangent of the division of two numbers.
Number.Cos Returns the cosine of a number.
Number.Cosh Returns the hyperbolic cosine of a number.
Number.Sin Returns the sine of a number.
Number.Sinh Returns the hyperbolic sine of a number.
Number.Tan Returns the tangent of a number.
Number.Tanh Returns the hyperbolic tangent of a number.
Bytes
ﾉ Expand table
Name Description
Number.BitwiseAnd Returns the result of a bitwise AND operation on the provided operands.
Number.BitwiseNot Returns the result of a bitwise NOT operation on the provided operands.
Number.BitwiseOr Returns the result of a bitwise OR operation on the provided operands.
Number.BitwiseShiftLeft Returns the result of a bitwise shift left operation on the operands.
Number.BitwiseShiftRight Returns the result of a bitwise shift right operation on the operands.
Number.BitwiseXor Returns the result of a bitwise XOR operation on the provided operands.
```


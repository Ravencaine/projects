---
title: "Power Automate unlocked for Excel users (PART 3): Logical comparison and Math functions"
source: "https://medium.com/@javidautomates/power-automate-unlocked-for-excel-users-part-3-logical-comparison-and-math-functions-5c605f91013a"
author:
  - "[[Javid R.]]"
published: 2025-10-08
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZpW9CSS_yxk7gN_ss_YMNw.jpeg)

> *Let’s be real for a moment. If you are reading this, you have probably spent countless hours in Excel doing the same things over and over again. Well, most of us have been there struggling with manual work sucking the life out of us. And again most of us have been there thinking “But there has to be a better way!”. The good news is: there IS a better way.*

*To read the full story for free, click* [*here*](https://medium.com/@rzayevjavid/power-automate-unlocked-for-excel-users-part-3-logical-comparison-and-math-functions-5c605f91013a?sk=e6951257748f220e107dfe5690d0331b)*.*

If you have been following this series, you already know how to work on [strings](https://medium.com/@rzayevjavid/power-automate-unlocked-for-excel-users-string-functions-2dd27a0d2e2e) and [collections](https://medium.com/@rzayevjavid/power-automate-unlocked-for-excel-users-part-2-collection-functions-7cb477d51e51) in Power Automate. Today, we will unlock the door to something new: Logical Comparison and Math functions. As an Excel user, you have likely built complex IF statements and mathematical functions. Good news is, Power Automate have the similar functions - let’s start to learn those together.

### Part 1: Logical Comparison Functions

1\. **equals**

Power Automate:

Checks whether both values, expressions, or objects are equivalent and returns boolean value. Just don’t forget that this function is case-sensitive.

equals(object1, object2)

```c
equals(variables('Condition'), "Good")
```

Excel:

\= operator or EXACT(text1, text2)

2\. **greater**

Power Automate:

Checks whether the first value is greater than the second value and returns boolean value.

greater(value1, value2)

```c
greater(variables('Age'), 100)
```

Excel:

\> operator

3\. **greaterOrEquals**

Power Automate:

Checks whether the first value (number, date or string) is greater than or equal to the second value and returns boolean value.

greaterOrEquals(value1, value2)

```c
greaterOrEquals(variables('Age'), 100)
```

Excel:

\>= operator

4\. **less**

Power Automate:

Checks whether the first value is less than the second value. Returns true when the first value is less, or return false when the first value is more.

less(value1, value2)

```c
less(variables('DirectCosts'), variables('IndirectCosts'))
```

Excel:

< operator

5\. **lessOrEquals**

Power Automate:

Checks whether the first value is less than or equal to the second value. Returns true when the first value is less than or equal, or return false when the first value is more.

lessOrEquals(value1, value2)

```c
lessOrEquals(55000, variables('IndirectCosts'))
```

Excel:

<= operator

6\. **and**

Power Automate:

Checks whether all expressions are true and returns boolean value.

and(expression1, expression2, …)

```c
and(
  equals(triggerBody()?['PaidAmount'], 5000),
  equals(triggerBody()?['IfToday'], true)
)
```

Excel:

AND(logical1, logical2, …)

7\. **or**

Power Automate:

Checks whether at least one expression is true and returns boolean value.

or(expression1, expression2, …)

```c
or(
  equals(triggerBody()?['PaidAmount'], 5000),
  equals(triggerBody()?['IfToday'], true)
)
```

Excel:

OR(logical1, logical2, …)

8\. **not**

Power Automate:

Checks whether an expression is false and returns boolean value.

not(expression)

```c
not(empty(triggerBody()?['Reference']))
```

Excel:

NOT(logical)

9\. **if**

Power Automate:

Checks whether an expression is true or false and return boolean value accordingly.

if(expression, valueIfTrue, valueIfFalse)

```c
if(equals(variables('Age'), 100), "Old", "Young")
```

Excel:

IF(logical\_test, value\_if\_true, value\_if\_false)

10\. **isInt**

Power Automate:

Returns a boolean that indicates whether a string is an integer.

isInt(string)

```c
isInt("100")
```

Excel:

AND(ISNUMBER(A1), A1=INT(A1))

11\. **isFloat**

Power Automate:

Returns a boolean indicating whether a string is a floating-point number.

isFloat(string, locale)

```c
isFloat("22.000,00")
```

Excel:

AND(ISNUMBER(A1), A1<>INT(A1))

### Part 2: Math Functions

12\. **add**

Power Automate:

Returns the result from adding two numbers.

add(summand1, summand2)

```c
add(variables('Cost'), variables('Profit'))
```

Excel:

\+ operator or SUM()

13\. **sub**

Power Automate:

Returns the result from subtracting the second number from the first number.

sub(minuend, subtrahend)

```c
sub(variables('Revenue'), variables('Profit'))
```

Excel:

\- operator

14\. **mul**

Power Automate:

Returns the product from multiplying two numbers.

mul(multiplicand1, multiplicand2)

```c
mul(variables('Quantity'), variables('UnitCost'))
```

Excel:

\* operator or PRODUCT()

15\. **div**

Power Automate:

Returns the result from dividing two numbers.

div(dividend, divisor)

```c
div(variables('TotalCosts'), variables('Quantity'))
```

Excel:

/ operator

16\. **mod**

Power Automate:

Returns the remainder from dividing two numbers

mod(dividend, divisor)

```c
mod(variables('TotalCosts'), variables('Quantity'))
```

Excel:

MOD()

17\. **min**

Power Automate:

Returns the lowest value from a set of numbers or an array.

min(value1, value2, …) or min(array)

```c
min(100, variables('Age'))
```

Excel:

MIN()

18\. **max**

Power Automate:

Returns the highest value from a set of numbers or an array.

max(value1, value2, …) or max(array)

```c
max(100, variables('Age'))
```

Excel:

MAX()

19\. **range**

Power Automate:

Returns an integer array that starts from a specified integer.

range(startIndex, count)

```c
range(1, 7)
```

Excel:

SEQUENCE()

20\. **rand**

Power Automate:

Returns a random integer from a specified range, which is inclusive only at the starting end.

rand(minValue, maxValue)

```c
rand(1, 100)
```

Excel:

RANDBETWEEN()

Now as you have learned string, collection, logical comparison and math functions, you are ready to use them in flows. Start small and the rest will follow! Just remember, you are not learning from scratch — you are just translating skills which you already have.

*I will continue to show how to use Power Automate for your automation needs. If you found this post helpful, you can support this blog post with clapping and your comments. If you find this series interesting, next post will be about Date & Time functions.*
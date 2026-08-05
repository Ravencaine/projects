---
title: "DAX IF.EAGER Function in Power BI"
source: "https://databear.com/dax-if-eager-function-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2022-10-16
created: 2026-08-04
description: "IF.EAGER function checks a condition and returns one value when TRUE, otherwise it returns a second value. It uses an eager execution plan which always executes the branch expressions regardless of the condition expression."
Processed: "Unprocessed"
---
We have several conditional expressions, such as the IF and IF. EAGER function, in Power BI. The IF. EAGER function is a logical function whose primary role is to check if a condition in a set of data has been met or.. If the condition in question is true, then the logical expression will prompt the system to return one value.. If the condition is false, another value will.

## Syntax of the DAX IF.EAGER Function

1. EAGER( \<LogicalTest>, \<ResultIfTrue> \[, \<ResultIfFalse> \] )
- **LogicalTest**: Any value or expression can be evaluated as either a TRUE or False.
- **ResultIfTrue**: The result can only be returned if the outcome of the logical test is TRUE.
- **ResultIfFalse**: The return is only returned if the outcome of the logical test is FALSE.

For conditional expressions such as IF and IF. EAGER can be evaluated using two methods which are: strict and eager. Understanding how these two modes work plays a major role in tuning the performance measure.

## How DAX IF.EAGER Function works

1. IF.EAGER is an improvement of the old IF function, which was quite plain. When using the IF. EAGER function Power BI evaluates all the sections of the function regardless of whether the test condition is true or false; previously, it could only evaluate if the tested condition is TRUE.

### Let’s use an example to explain how this conditional statement works.

Suppose you are provided with the sales data for a previous and current month of a model, as shown below.

![IF.EAGER calculation](99.System/Attachments/IF.EAGER_calculation.gif)

I have introduced two measures in this case: last month and this month.

Without using the MAX function, it is possible to show the highest value for both this month and last month. This is done by creating a new measure, as illustrated below.

Bigger each month = IF.EAGER(

// the IF.EAGER function will evaluate the values for this month and last month once only

\[Last month\] > \[This month\],

\[Last month\],

\[This month\]

)

The image below would be a representation of the outcome after executing the above function.

![IF.Eager Function](99.System/Attachments/IF.Eager_Function.gif)

The introduced measure would make it easy to identify the highest value by comparing the two measures and selecting the highest one at the current period of time.

As stated above, what sets IF. EAGER, apart from The IF conditional expression, evaluates all the available measures without considering whether the condition being tested is true. In this case example, below is the number of times each measure would be evaluated if the test condition is true.

| Function | This Month | Last Month |
| --- | --- | --- |
| IF | 1 | 2 (1 for the condition and 1 for the second argument) |
| IF.EAGER | 1 | One only |

IF.Eager evaluation like the one in the example could save a lot of time and other resources though it makes you feel like you are experiencing redundancy. This is because it is possible to use standard variables in place of the IF.EAGER logical expression as shown in the snippet below.

Bigger and better =

// get the values of each measure

VAR ThisMonth = \[This month\]

VAR LastMonth = \[Last month\]

// return the higher

RETURN IF(

LastMonth > ThisMonth,

last month,

this month

)

I hope you found this helpful. Read more blogs from DataBear [here](https://databear.com/blog/).
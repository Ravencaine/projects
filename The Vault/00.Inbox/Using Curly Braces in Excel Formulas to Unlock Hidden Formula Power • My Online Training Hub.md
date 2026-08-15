---
title: "Using Curly Braces in Excel Formulas to Unlock Hidden Formula Power • My Online Training Hub"
source: "https://www.myonlinetraininghub.com/using-curly-braces-in-excel-formulas-to-unlock-hidden-formula-power"
author:
  - "[[Mynda Treacy]]"
published: 2026-02-17
created: 2026-08-09
description:
Processed: "Unprocessed"
---
Most Excel users are not aware that curly braces can be used inside functions like DATE, XLOOKUP, and SORT to name a few, to unlock behaviour that is otherwise hidden. **These are not tricks or edge cases. They are built into how Excel evaluates formulas.**

Just take the DATE function which most think returns a single date; you can see below I’ve used it to return the quarter start dates for 2026, and I’ll cover how and why it works in more detail shortly:

![How to use curly braces in Excel formulas?](https://d13ot9o61jdzpp.cloudfront.net/images/01-curly-brace-formulas.png)

How to use curly braces in Excel formulas?

In this article, you will learn how curly braces work, why they matter, and how to use them in practical formulas you can apply immediately.

## Watch the Step-by-step Video

![](https://www.youtube.com/watch?v=KaC0CGV8he8)

[![Subscribe YouTube](https://d13ot9o61jdzpp.cloudfront.net/images/subscribe.png)](https://www.youtube.com/c/MyOnlineTrainingHub?sub_confirmation=1)  
![](https://www.youtube.com/watch?v=subscribe_embed)

## Download the Practice File

Enter your email address below to download the free file.

By submitting your email address you agree that we can email you our Excel newsletter.

## What Are Curly Braces in Excel?

Curly braces define what Excel calls an array constant. You can think of an array constant as a small list of values that lives directly inside a formula.

For example:

{1,2,3}

This is a horizontal array of three values:

![Understanding what are curly braces in Excel formulas](https://d13ot9o61jdzpp.cloudfront.net/images/02-curly-brace-formulas.png)

Understanding what are curly braces in Excel formulas

> Many Excel functions can accept arrays as arguments, even though most users only ever pass a single value. Once you understand this, you start to see Excel functions very differently.

In Excel 365, formulas that return arrays will usually spill automatically into neighbouring cells. The curly braces are simply defining the input values.

There is one important rule to remember when working with array constants.

Semicolons separate rows.  
Commas separate columns.

This means:

{1;2;3}

creates a vertical list:

![how to spit out a vertical list using an Excel formula?](https://d13ot9o61jdzpp.cloudfront.net/images/03-curly-brace-formulas.png)

how to spit out a vertical list using an Excel formula?

While:

{1,2,3}

creates a horizontal list:

![how to spit out a horizontal array through an Excel formula?](https://d13ot9o61jdzpp.cloudfront.net/images/04-curly-brace-formulas.png)

how to spit out a horizontal array through an Excel formula?

With that foundation in place, let’s look at how curly braces work inside real Excel functions.

## Using Curly Braces With the DATE Function

The [DATE function](https://www.myonlinetraininghub.com/excel-date-function) normally takes a single year, month and day

```
=DATE(year, month, day)
```

Most users expect it to return a single date.

However, if you pass an array of months using curly braces, DATE will return multiple dates.

For example, to generate quarter start dates for 2026:

```
=DATE(2026,{1;4;7;10},1)
```

Because semicolons are used, the results spill vertically. This instantly produces a list of quarterly start dates:

![How to use Curly Braces With the DATE Function in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/05-curly-brace-formulas.png)

How to use Curly Braces With the DATE Function in Excel?

If you want the same dates to spill horizontally instead, use commas:

```
=DATE(2026,{1,4,7,10},1)
```

By changing nothing but the separators, you control the shape of the output:

![How to use Curly Braces With the DATE Function in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/06-curly-brace-formulas.png)

How to use Curly Braces With the DATE Function in Excel?

This technique is perfect for building reporting periods or schedules without typing month lists onto the worksheet.

## Filtering Specific Columns Using FILTER and CHOOSE

Suppose you have a table containing employee names, departments and salaries, and you want to return only HR and IT employees. That part is easy with the [FILTER function](https://www.myonlinetraininghub.com/excel-functions/excel-filter-function).

But what if you also want to control which columns are returned, or even rearrange them, without creating helper columns?

This is where the [CHOOSE function](https://www.myonlinetraininghub.com/excel-choose-function) and curly braces come in.

Here is the full formula:

```
=FILTER(
 CHOOSE({1,2}, C6:C13, E6:E13),
 (D6:D13="HR")+(D6:D13="IT")
)
```

And here’s the result:

![How to filter Specific Columns Using FILTER and CHOOSE in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/07-curly-brace-formulas.png)

How to filter Specific Columns Using FILTER and CHOOSE in Excel?

Let’s break this down.

The CHOOSE function is used to build a virtual table. By passing {1,2} as the index argument, you are telling Excel that you want two columns returned.

Next, you specify which columns those are. In this case, column C contains names and column E contains salaries. The department column in D is skipped entirely.

Finally, FILTER is used to return only rows where the department is HR or IT. The plus sign acts as OR logic.

This pattern is extremely powerful. You can use CHOOSE not only to select columns, but also to reorder them before they are filtered.

## Creating a Mini Summary Table With VSTACK

Curly braces are also useful for building small summary tables without PivotTables or helper ranges.

For example, we can use [VSTACK](https://www.myonlinetraininghub.com/excel-vstack-and-hstack-functions) with [COUNTIF](https://www.myonlinetraininghub.com/excel-countif-and-countifs-formulas-explained) to count how many employees are in IT and HR and display the result as a table:

```
=VSTACK(
 {"IT","HR"},
 COUNTIF(D6:D13,{"IT","HR"})
)
```

And here is the result:

![How to create a Mini Summary Table With VSTACK in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/08-curly-brace-formulas.png)

How to create a Mini Summary Table With VSTACK in Excel?

The first array constant: {"IT","HR"}, defines the labels. The COUNTIF function then accepts the same array constant as its criteria and returns both counts in one calculation.

VSTACK combines the labels and counts into a clean two-row table.

This is a simple but very practical reporting technique.

## Using Curly Braces in XLOOKUP for Smarter Fallback Results

Most users know that the [XLOOKUP function](https://www.myonlinetraininghub.com/excel-xlookup-function) can return multiple columns. What many people do not realise is that the if\_not\_found argument can also return multiple values when you use curly braces.

Here is an example:

```
=XLOOKUP(
 I8,
 C6:C13,
 D6:E13,
 {"Unknown Dept.","Unknown Salary"}
)
```

This formula looks up an employee name in cell I8. If the name is found, it returns the department and salary.

If the name is not found, instead of returning a generic error or message, it returns a tailored fallback message for each column.

![How to use Curly Braces in XLOOKUP for Smarter Fallback Results in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/09-curly-brace-formulas.png)

How to use Curly Braces in XLOOKUP for Smarter Fallback Results in Excel?

This results in much cleaner, more professional output, especially in reports or dashboards.

## Multi-Level Sorting With SORT and Curly Braces

The SORT function can perform multi-level sorting if you pass a list of sort keys using curly braces.

For example:

```
=SORT(C9:G17,{2,5},-1)
```

Here’s the result:

![How to perform Multi-Level Sorting With SORT and Curly Braces in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/10-curly-brace-formulas.png)

How to perform Multi-Level Sorting With SORT and Curly Braces in Excel?

Here, {2,5} tells Excel to sort first by the second column and then by the fifth column. The -1 specifies descending order.

This allows you to perform complex sorts without SORTBY or helper columns, simply by passing an array of sort keys.

## Cleaning Messy Text With TEXTSPLIT and Multiple Delimiters

The [TEXTSPLIT function](https://www.myonlinetraininghub.com/textsplit-textbefore-and-textafter-functions) becomes far more powerful when combined with curly braces.

If you have a text string that contains multiple delimiters such as commas, slashes and parentheses, you can split it in one go.

For example:

```
=TEXTSPLIT(D5,{",","/","("},")",TRUE)
```

Here it is applied to a practical example:

![How to clean Messy Text With TEXTSPLIT and Multiple Delimiters in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/11-curly-brace-formulas.png)

How to clean Messy Text With TEXTSPLIT and Multiple Delimiters in Excel?

In this formula:

- The array constant: {",","/","("} defines multiple column delimiters.
- The closing parenthesis is used as a row delimiter.
- TRUE tells Excel to ignore empty values.

With a single formula, a messy block of text is transformed into structured columns.

## Taking This Further With Advanced Excel Formulas

If you’re reading this and thinking, “I know Excel formulas, but clearly not like this,” that is exactly why I created my [**Advanced Excel Formulas** course](https://www.myonlinetraininghub.com/advanced-excel-formulas-course).

The course further into array logic, lookup patterns and modern formula techniques like the ones shown here, all grounded in real-world use cases.

You can find the course here: [Advanced Excel Formulas Course](https://www.myonlinetraininghub.com/advanced-excel-formulas-course)
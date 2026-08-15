---
title: "Mastering Excel LAMBDA Functions — Select Distinct"
source: "https://medium.com/@simon.harrison_Select_Distinct/mastering-excel-lambda-functions-select-distinct-2da159618dbb"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2024-05-10
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*9OYfTwIvWskuuGV0xQbHcg.png)

Creating powerful, custom functions in Excel got easier with Excel LAMBDA functions. These functions offer a dynamic way to create reusable formulas. These can simplify complex calculations, tailor your data manipulation, and enhance the efficiency of your workflows. Here’s an in-depth look at how to use LAMBDA functions, including some practical examples.

Excel LAMBDA functions were introduced by Microsoft in December 2020. Initially, they were released to users in the Beta Channel of the Microsoft Office Insider program. They have become generally available as part of Microsoft 365 (formerly Office 365).

## What are Excel LAMBDA Functions?

LAMBDA functions are a feature in Microsoft Excel that allow users to define their own custom functions using Excel’s formula. Essentially, they turn any formula into a named function that can be reused throughout your workbook. This not only saves time but also helps keep your spreadsheets clean and your calculations consistent.

## Benefits of Using LAMBDA Functions

1\. **Customization**: Tailor functions exactly to your needs without any VBA scripting or additional software.

2\. **Reusability**: Once created, these functions can be reused across your spreadsheets, just like any native Excel function.

3\. **Simplification**: Complex formulas can be broken down into simpler, understandable parts.

4\. **Maintenance**: Easier to update and maintain a single function than multiple complex formulas.

## Creating Your First LAMBDA Function

Let’s start with a basic example. Suppose you want a function to add two numbers:

```c
=LAMBDA(a, b, a + b)
```

To use this, you would enter it into a cell like so:

```c
=LAMBDA(a, b, a + b)(5, 3)
```

This would return \`8\`. But the true power comes from naming this function:

1\. Go to the Formulas tab.

2\. Click ‘Name Manager’.

3\. Create a new name, for example, \`AddNumbers\`.

4\. Define it as \`=LAMBDA(a, b, a + b)\`.

Now, you can use \`=AddNumbers(5, 3)\` anywhere in your workbook to get \`8\`.

## Advanced Example: Recursive LAMBDA Function

LAMBDA can also be recursively. For instance, let’s create a function to calculate the factorial of a number:

```c
=LAMBDA(n, IF(n=1, 1, n * Factorial(n-1)))
```

After naming this function \`Factorial\` using the Name Manager, you can calculate the factorial of 5 as follows:

```c
=Factorial(5)
```

This would return \`120\`.

![](https://miro.medium.com/v2/resize:fit:1184/format:webp/0*MsgwfgEgjzRVnjEX.png)

## Practical Uses in Real-world Scenarios

1\. **Financial Modelling**: Create bespoke functions for specific financial calculations. These could include calculations such as NPV or IRR. You can tailor these to your company’s methodologies.

2\. **Data Analysis**: Functions for statistical analysis or data cleaning. You can customize frequently used formulas as LAMBDA functions.

3\. **Educational Purposes**: Teachers can create functions that help students understand complex mathematical concepts. This can be through customized, simple functions.

## Best Practices for Using LAMBDA Functions

\- **Keep it simple**: While LAMBDA functions are powerful, they can also make your formulas very complex. Aim for clarity.

\- **Document your functions**: Document your LAMBDA function’s purpose, inputs, and outputs.

\- **Test thoroughly**: Like any function, testing is crucial. Ensure your LAMBDA functions behave as expected with a variety of inputs.

## Conclusion

Excel LAMBDA functions open up a world of possibilities for customizing your data manipulation and analysis. By mastering these functions, you can significantly enhance the power and efficiency of your spreadsheets. Start with simple functions and gradually explore more complex calculations as you become comfortable with the syntax and capabilities.

With practice, LAMBDA functions can be an invaluable addition to your Excel toolkit, transforming the way you handle data and calculations in your spreadsheets.

Or find other useful SQL, Power BI or other business analytics timesavers in our Blog

We select our Business Analytics Timesavers from our day-to-day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people. Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

Blog Posted by [David Laws](https://www.selectdistinct.co.uk/about-select-distinct-limited/about-david-laws/)
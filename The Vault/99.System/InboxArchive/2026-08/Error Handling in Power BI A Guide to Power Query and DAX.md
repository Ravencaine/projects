---
title: "Error Handling in Power BI: A Guide to Power Query and DAX"
source: "https://databear.com/handling-errors-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2023-07-16
created: 2026-08-04
description: "Enhance your Power BI skills with our guide on error handling. Learn how to use 'try', 'otherwise' in Power Query and 'if error' in DAX for smoother operations."
Processed: "Unprocessed"
---
## Understanding Error Handling in Power BI DAX

Welcome to another blog post where we share recovery tips, tricks, and best practices when working with Power BI. Today, we’ll focus on Error Handling in Power BI, a crucial aspect of maintaining seamless data analytics operations. We aim to demonstrate how you can effectively handle errors using Power Query’s try and otherwise expressions and DAX’s if-error function.

Error handling is a concept in data or programming in general, where we purposefully use code to ensure that when an error happens, it’s dealt with properly. It’s a pivotal aspect of Power BI as a single error in one line could be the root cause for issues like dashboard not refreshing or calculations not showing a value. Handling errors ensures that you can catch and fix these without breaking the whole report.

Power BI has some functions that already take this into account. For instance, the divide function where you have a third parameter that allows you to set the value in case the division returns an error.

In this article, we will explore error handling further using Power Query and DAX.

## Power Query: Using ‘Try’ and ‘Otherwise’

We are using a simple list of products, each with their unit price and quantity sold. Our goal is to create a new column to calculate the total sales for each of these products by multiplying the unit price against the quantity. This can be done by adding a custom column named “total sales”, and then using the following formula:

`[Unit Price] * [Quantity]`

But, what if one of the values errors out because we are trying to multiply a number value against a text value, say, “none”?

This is where the error handling in Power Query comes into play. We can amend our formula with the `try` and `otherwise` keywords:

`try [Unit Price] * [Quantity] otherwise null`

This essentially tries the expression that you wrote and if it returns an error (otherwise), it should be null or empty. You can change the otherwise value to be null, zero, or whatever you want, really.

## Diving Deeper: Handling Errors with Record Details

If you remove the `otherwise` part of your `try otherwise`, what it will do is change the result of your values into a record instead of a single value. This record is essentially a table for each of these rows, giving more details about the type of error that you got. This level of detail is useful when you’re trying to troubleshoot multiple errors caused by multiple reasons.

## Handling Errors in DAX

Now, moving to DAX, if we want to do the same calculation, which is calculating total sales, we face a similar problem. Without converting the column into a number type value, we won’t be able to create the calculation. Here’s where we can use the `if error` function which simply needs two parameters: the expression and the alternative results.

So, in our case, we use the convert function to change the quantity into an integer. We then wrap this inside the `if error` function, and provide an alternative value of zero in case of an error:

`IFERROR(CONVERT([Quantity], INTEGER), 0)`

As you can see, instead of erroring out the whole calculated column, it just returns a zero which is exactly what we want.

Finally, to finish it off, you just simply multiply it against the unit price:

`[Unit Price] * IFERROR(CONVERT([Quantity], INTEGER), 0)`

## Conclusion

Error handling in Power BI, either in Power Query or DAX measures, can help ensure your report continues to function smoothly. It ensures that you can catch and fix errors without breaking the whole report.

Thanks for reading! If you found this blog post useful.

You can visit the rest of our [blog](https://databear.com/blog/) posts for more insightful information on everything related to Power BI.

Learn more about Power BI by taking our training [course](https://databear.com/power-bi-training/).
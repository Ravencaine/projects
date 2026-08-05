---
title: "KEEPFILTERS DAX Function in Power BI"
source: "https://databear.com/keepfilters-dax-function-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2023-04-09
created: 2026-08-04
description: "Discover the power of KeepFilters DAX function in Power BI through our comprehensive guide. Learn to manage multiple filters and enhance your data models and measures for precise data analysis."
Processed: "Unprocessed"
---
## Introduction to DAX KeepFilters

Welcome to another insightful blog post where we dive deep into the world of Power BI! Today, we are going to explore the powerful KeepFilters DAX function, a game-changer when it comes to handling multiple filters on your data.

KeepFilters are necessary when you have arbitrarily shaped filters that you do not want to lose by applying additional filters on individual items. In other words, whenever you have one or more filters on a column and you want to apply some more filters without losing the previous filters, you can use KeepFilters.

## Using KeepFilters in Power BI

In this post, we are working with a Power BI file and a data model to demonstrate how to use the KeepFilters DAX function. We will calculate different measures using KeepFilters and other predicates, and then see where we would need the KeepFilters.

### Example: Calculating Total Sales for Product Color

we want to calculate total sales where the product color is black. We create a new measure called “Black Color Sales” and write the following expression:

**Black Color Sales = CALCULATE(Total Sales, ‘Product'\[Color\] = “Black”)**

![Keep filter ](99.System/Attachments/Keep_filter_.png)

Now, let’s say we only need the value for black color and don’t want other values to appear in other columns. We can use the KeepFilters to achieve this. We can either use the VALUES function or the KEEPFILTERS function to do this.

#### Using VALUES Function:

**Black Color Sales (Values) = CALCULATE(Total Sales, VALUES(‘Product'\[Color\]) = “Black”)**

![Keep filter](99.System/Attachments/Keep_filter.png)

#### Using KEEPFILTERS Function:

**Black Color Sales (Keep Filters) = CALCULATE(Total Sales, KEEPFILTERS(‘Product'\[Color\] = “Black”))**

![Keep filter 2](99.System/Attachments/Keep_filter_2.png)

Both of these expressions are equivalent and will give you the same result, without putting values in each and every cell.

### Understanding the Intersection of Multiple Filters

In our next example, we will demonstrate how the intersection of multiple filters works when using KeepFilters. Let’s say we have three different filters applied on the same column: black or blue, black, and black or red. We want to calculate the total sales for black and blue or black and red.

#### Applying Multiple Filters Simultaneously:

To apply both filters simultaneously, we can use nested CALCULATE functions:

**Total Sales (Black and Blue or Black and Red) = CALCULATE(CALCULATE(Total Sales, ‘Product'\[Color\] = “Black” || ‘Product'\[Color\] = “Blue”), ‘Product'\[Color\] = “Black” || ‘Product'\[Color\] = “Red”)**

#### Using KeepFilters with Intersection:

To get the intersection of the two filters using KeepFilters, we can modify our expression as follows:

**Total Sales (Intersection with KeepFilters) = CALCULATE(CALCULATE(Total Sales, KEEPFILTERS(‘Product'\[Color\] = “Black” || ‘Product'\[Color\] = “Blue”)), KEEPFILTERS(‘Product'\[Color\] = “Black” || ‘Product'\[Color\] = “Red”))**

With this expression, we can clearly see that the intersection of the two filters is the black color, and the result will be the total sales for the black-colored products.

In summary, using KeepFilters in Power BI modifies the default behavior of the CALCULATE function and adds an additional filter because the intersection of filters is used. By understanding and using the KeepFilters DAX function, we can effectively manage multiple filters applied to the same column without losing any existing filters. This allows us to achieve more accurate and precise results when working with Power BI data models and measures.

You can visit the rest of our [blog](https://databear.com/blog/) posts for more insightful information on everything related to Power BI.

Learn more about Power BI by taking our training [course](https://databear.com/power-bi-training/).
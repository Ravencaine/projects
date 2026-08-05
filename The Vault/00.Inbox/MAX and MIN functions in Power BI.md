---
title: "MAX and MIN functions in Power BI"
source: "https://databear.com/max-and-min-functions-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2022-11-19
created: 2026-08-04
description: "We are going to talk about MAX and MIN functions. The MAX and MIN functions have many variations, like MAX, MIN, MAXX, MINX, MINA, and MAXA."
Processed: "Unprocessed"
---
Today we are going to talk about MAX and MIN functions. The MAX and MIN functions have many variations, like MAX, MIN, MAXX, MINX, MINA, and MAXA.

We will check each variation in detail with an example.

## DAX MAX and MIN Functions

Let’s get started and explore MAX and MIN functions.

Here is our dataset.

![Min and Max Function ](99.System/Attachments/Min_and_Max_Function_.png)

Now, here I have different columns like region, Rep, Items, Total, Unit Cost, and Unit. Now, let’s explain how to use the MAX function. The Max function basically returns the maximum value from your data.

Here is the syntax for MAX

**MAX(\<column>)**

**MAX(\<expression1>, \<expression2>)**

Now let’s say, for example, we need maximum Unit Cost. For that, I need to create one measure.

![MAX and MIN functions](99.System/Attachments/MAX_and_MIN_functions-1.png)

We need to provide the column name. So, let’s provide our Unit Cost column. MAX also accepts the second parameter scalar. We will see that later. Also, we can see in the image above we have Max Unit Cost for each item. In the same way, if you just want to have a minimum Unit Sale, you just need to use MIN function MIN is obviously opposite from the MAX.

Here is the syntax for MIN

**MIN(\<column>)**

**MIN(\<expression1>, \<expression2>)**

## MAXX and MINX Functions with Filter Expression

Now, let’s look at MAXX and MINX expressions. That is MAXX and MINX are both iterator functions. What is the iterator function? Check our previous blog on SUM and SUMX. Let’s cover up those scenarios again over here. For example, if I just wanted to find out the maximum Unit cost for a particular region, then we need to use the MAXX function with a filter option.

Here is the syntax for MAXX

**MAXX(\<table>, \<expression>)**

![MAX and MIN functions](99.System/Attachments/MAX_and_MIN_functions.png)

So, I just created a measure MAXX for the central region. We need to provide a table and filter for the central region’s maximum Unit Sales. We will use the filter function inside that and provide our table Sale Orders region equal to central. And from this region, we need maximum Unit cost.

Similarly, we need to try the MINX function, we need to choose MINX, and will give us the minimum value by central region.

Here is the syntax

**MAXX(\<table>, \<expression>)**

## MAXX and MINX Functions as Iterator Function

Let’s look at MAXX as an iterator function used to iterate calculations row by row. Now in our dataset, we have Unit and Unit Cost columns. Now I need to find the maximum Total values, which is the summation of Unit and Unit Costs. The MAXX function will help to iterate row by row and store it in temporary storage. Now, let’s see how.

![MAXX and MINX functions](99.System/Attachments/MAXX_and_MINX_functions-1.png)

The best thing about the iterator function is that there is no need to create a separate column. We can use MINX by changing MAXX to MINX using the same syntax. MAX and MIN functions can also be used as scalar functions.

![MAXX and MINX functions](99.System/Attachments/MAXX_and_MINX_functions.png)

I have created two columns for calculating the Max Unit cost for the Central and East region. It is giving us the maximum Unit cost for both of these regions. Now, we can compare these values with each other, then we need to explore the MAX expression’s second parameter. MAX compares the two DAX expressions and returns the MAX for both.

![MAX and MIN functions](99.System/Attachments/MAX_and_MIN_functions-2.png)

**MAXA and MINA DAX function**

When MINA operates with a Boolean data type, it considers TRUE as 1 and FALSE as 0(Zero). If the value is not Boolean, the MINA function internally executes as MINX, without any performance difference. MAXA operates opposite of MINA in that MAXA returns the max value of the Boolean data type

**Read more about Apps in Power BI [here](https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps).**
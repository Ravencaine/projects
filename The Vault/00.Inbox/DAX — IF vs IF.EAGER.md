---
title: "DAX — IF vs IF.EAGER"
source: "https://medium.com/@michalmolka/dax-if-vs-if-eager-2465d1e47db2"
author:
  - "[[Michal Molka]]"
published: 2021-07-09
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

In March 2021 Power BI got a new IF.EAGER DAX function. What is the difference between the “new” and an “old” IF?

The **IF** function is strict evaluated which computes TRUE or FALSE result only when a condition is met.

For instance: **IF (5<2, 5+2, 7+1)**. An engine computes only the second part of T/F section (7+1), (5+2) isn’t computed.

The **IF.EAGER** function is eager evaluated. Computes TRUE and FALSE results regardless the condition is met or not.

An example: **IF(5<2, 5+2, 7+1)**. The engine computes the first and the second part of T/F section (5+2), (7+1).

Now, you can ask a question. Why we should use the second one?

In some cases it provides a better performance. E.g. when T/F values are computed values (like measures - for example).

Our example is an [Iowa Liquor Sales](http://data.iowa.gov/) dataset. It contains 21 million rows.

We have three measures: SUM, AVERAGE, COUNT, which are used in the IF function.

```c
DEFINE
    MEASURE Iowa_Liquor_Sales[SalesSum] =
        CALCULATE ( SUM ( Iowa_Liquor_Sales[Volume Sold (Liters)] ) )
    MEASURE Iowa_Liquor_Sales[SalesAverage] =
        CALCULATE ( AVERAGE ( Iowa_Liquor_Sales[Volume Sold (Liters)] ) )
    MEASURE Iowa_Liquor_Sales[SalesCount] =
        CALCULATE ( COUNTROWS ( Iowa_Liquor_Sales ) )
EVALUATE
SUMMARIZE (
    Iowa_Liquor_Sales,
    Iowa_Liquor_Sales[Category Name],
    "IF", IF ( [SalesCount] < 100000, [SalesSum], [SalesAverage] )
)
```
![](https://miro.medium.com/v2/resize:fit:1388/format:webp/1*FuRT1cf-mD_eG3tQxVAT1A.png)

Code for the IF.EAGER is almost identical besides the IF is changed to the IF.EAGER function.

```c
DEFINE
    MEASURE Iowa_Liquor_Sales[SalesSum] =
        CALCULATE ( SUM ( Iowa_Liquor_Sales[Volume Sold (Liters)] ) )
    MEASURE Iowa_Liquor_Sales[SalesAverage] =
        CALCULATE ( AVERAGE ( Iowa_Liquor_Sales[Volume Sold (Liters)] ) )
    MEASURE Iowa_Liquor_Sales[SalesCount] =
        CALCULATE ( COUNTROWS ( Iowa_Liquor_Sales ) )
EVALUATE
SUMMARIZE (
    Iowa_Liquor_Sales,
    Iowa_Liquor_Sales[Category Name],
    "IF", IF.EAGER ( [SalesCount] < 100000, [SalesSum], [SalesAverage] )
)
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*T0ruqn0RiWY6RCayjzcqZg.png)

As you noticed, the difference is evident.

Total: 94ms compared to 39ms. Scans: 4 compared to 2

In most cases when a dataset is small or there is no calculation in a TRUE/FALSE section the difference is invisible. When you face with conditions as an above, you can take an advantage of using the IF.EAGER function.
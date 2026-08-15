---
title: "DAX — KEEPFILTERS vs FILTER"
source: "https://medium.com/@michalmolka/dax-keepfilters-vs-filter-8f3fb519ccaf"
author:
  - "[[Michal Molka]]"
published: 2021-10-01
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Every now and then we need to create a calculation containing filtered values. Like on the picture bellow.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*0Dkr0Uuw3TUIaz8qVYitkQ.png)

As you can see, among others, we can use the **KEEPFILTERS()** or **FILTER()** function. What is the difference? Performance of course.

As an example, we use an Iowa Liquor Sales dataset. It contains 21 million records.

Source: [Iowa Liquor Sales | data.iowa.gov](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy)

When we go with the **KEEPFILTERS()** solution…

```c
DEFINE MEASURE
Iowa_Liquor_Sales[KeepFiltersMeasure] = 
    CALCULATE(
        SUM(Iowa_Liquor_Sales[Volume Sold (Liters)]), 
        KEEPFILTERS(
            Iowa_Liquor_Sales[City] in {"Aurelia", "Avoca", "Baxter"} &&
            AND(
              Iowa_Liquor_Sales[Sale (Dollars)]  >= 10, 
              Iowa_Liquor_Sales[Sale (Dollars)] < 55
              ) 
          )
        )

EVALUATE

SUMMARIZECOLUMNS(
    Iowa_Liquor_Sales[County], 
    Iowa_Liquor_Sales[City], 
    Iowa_Liquor_Sales, 
    "KeepFiltersMeasure", 
    Iowa_Liquor_Sales[KeepFiltersMeasure])
```

…we get following statistics and a plan.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cFwg5nLwxe3W7UVXQhS3CA.png)

Once you use the **FILTER()** function…

```c
DEFINE MEASURE
Iowa_Liquor_Sales[FilterMeasure] = 
    CALCULATE(
        SUM(Iowa_Liquor_Sales[Volume Sold (Liters)]), 
        FILTER(
            Iowa_Liquor_Sales, 
            Iowa_Liquor_Sales[City] in {"Aurelia", "Avoca", "Baxter"} &&
            AND(
              Iowa_Liquor_Sales[Sale (Dollars)]  >= 10, 
              Iowa_Liquor_Sales[Sale (Dollars)] < 55
              ) 
          )
        )

EVALUATE

SUMMARIZECOLUMNS(
    Iowa_Liquor_Sales[County], 
    Iowa_Liquor_Sales[City], 
    Iowa_Liquor_Sales, 
    "FilterMeasure", 
    Iowa_Liquor_Sales[FilterMeasure]
    )
```

…you get this result.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PKtt1_Z3rUyu4ndUvClPLw.png)

As you can see, here is the performance difference for the benefit of the **KEEPFILTERS()** function.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*--MtXNNb3GbqP7GPOlcQ8g.png)

In this case the **KEEPFILTERS()** function is faster than the **FILTER()** calculation. Total time is 15 ms in comparison to 30 ms. The **FILTER()** uses two queries as opposed to the **KEEPFILTERS()** which uses only one query.

How the **KEEPFILTERS()** works? It keeps an existing context and compares context filters to function’s arguments. In other words, a query result is a combination of a filtered context and values from the function’s arguments.

How the **CALCULATE()** + **FILTER()** works? The **FILTER()** is an iterator. So, placed inside the **CALCUALTE()** function it evaluates every row of a provided table (by function arguments) inside a particular filter context.
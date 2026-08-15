---
title: "Power BI — Time Intelligence"
source: "https://medium.com/@michalmolka/power-bi-time-intelligence-a3b46ef74d45"
author:
  - "[[Michal Molka]]"
published: 2020-09-05
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Today’s post is about time intelligence DAX formulas. I want to show you a few examples.

At first I imported a \[**Users**\] table from the Stack Overflow database and a \[**Date**\] table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*o6LOqH96csJJ7_ZfRm5_Qg.png)

I created relationships between tables and marked the \[**Date**\] table as a date table type.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VJQrI4HJeCLSwJE0LdmeTA.png)

The first example, we want to show an account creation cumulative quantity by year, quarter, month.

![](https://miro.medium.com/v2/resize:fit:1130/format:webp/1*Wahd-vKTVru6pr97xdS1Jg.png)

```c
Quantity Total = 
  SWITCH(
    TRUE(),
    Parameter[Parameter Value] = 1,
    TOTALYTD([Quantity], 'Date'[Date]),
    Parameter[Parameter Value] = 2,
    TOTALQTD([Quantity], 'Date'[Date]),
    Parameter[Parameter Value] = 3,
    TOTALMTD([Quantity], 'Date'[Date]),
    BLANK()
  )
```

But, what we should do when we want to use the cumulative total from another point in time. Let’s assume that we want to start from the half of the year. We can use the **DATESYTD()** function with an optional parameter **\[TearEndDate\]** or the **TOTALYTD()** function which had been used earlier.

```c
Quantity Half Year = 
  CALCULATE(
    [Quantity], 
    DATESYTD(
      'Date'[Date], 
      "06-30"
    )
  )
// OR
Quantity Half Year = 
  TOTALYTD(
    [Quantity], 
    'Date'[Date], 
    "06-30"
  )
```

As you can see, our calculation window starts in July and ends in June.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*FvJsmlJWPnZxaxSH1BNyuw.png)

Th next example.

1. I want to compare the current value to last year and the same period quantity.
2. Compare the current value to the last month value.

We can use two measures to reach the goal.

```c
Quantity Last Year Period = 
  CALCULATE(
    [Quantity], 
    SAMEPERIODLASTYEAR('Date'[Date])
    )
  
// AND

Quantity Last Month Period = 
  CALCULATE(
    [Quantity], 
    PARALLELPERIOD(
      'Date'[Date], 
      -1, 
      MONTH
    )
  )
```
![](https://miro.medium.com/v2/resize:fit:1344/format:webp/1*TcZUaRKi91uU1RSCKCJPVQ.png)

What if we want to compute a moving sum, let’s say for the last two months?

```c
Quantity Two Last Month = 
  CALCULATE(
    [Quantity],
    DATESINPERIOD(
      'Date'[Date], 
      LASTDATE('Date'[Date]), 
      -2, 
      MONTH
    )
  )
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*YSsz9tSQhEOC0EcmBgRsHQ.png)

At the end, let’s check how much new accounts quantity changed year to year.

```c
% Change = DIVIDE([Quantity] - [Quantity Last Year Period],[Quantity Last Year Period])
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GgDt2k6zCWpGPg12B56Vrg.png)
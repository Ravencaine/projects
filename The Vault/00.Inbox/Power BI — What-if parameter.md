---
title: "Power BI — What-if parameter"
source: "https://medium.com/@michalmolka/power-bi-what-if-parameter-d5212001ec4c"
author:
  - "[[Michal Molka]]"
published: 2021-04-30
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

In many cases, when you share a report with your users. You want to allow them to enter parameters which influence on measures or indicators.

The perfect solution is a What-if parameter.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yKcElrAx6DgOgkYveCqgJw.png)

Let’s assume that we want to give a user a possibility to manipulate a value of following measure.

```c
Quantity = COUNTROWS(Posts)
```

User wants to get the measure value after he had added an additional specified percentage value of this measure. An example is worth more than thousand words, so let’s go to a real case.

Firstly, you need to create a parameter and its properties.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*TWU137HlO-xFW2dHbusgBQ.png)

Power BI created a table with a calculated column and a measure.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*NIhYG1T1-9szcdG5tpMW-w.png)

```c
Percentage Change = GENERATESERIES(0, 1, 0.01)
Percentage Change Value = SELECTEDVALUE('Percentage Change'[Percentage Change], 0)
```

The column includes all values between 0 and 1 with 0.01 step. It provides values to a slicer.

![](https://miro.medium.com/v2/resize:fit:1214/format:webp/1*0WFDFMxX7HsBGzYWvStGhQ.png)

The measure stores a selected value from the slicer above.

And this is a place where the magic happens.

```c
'Percentage Change'
```

The measure result is calculated taking into an account the **Percentage Change Value** parameter.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*v28WwdTWgd_aZ7z9489b7A.gif)
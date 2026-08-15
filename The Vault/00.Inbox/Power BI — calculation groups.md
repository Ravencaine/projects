---
title: "Power BI — calculation groups"
source: "https://medium.com/@michalmolka/power-bi-calculation-groups-d2e92539f776"
author:
  - "[[Michal Molka]]"
published: 2026-03-01
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SntLpROllbFfaV6OqQTaVA.png)

**Calculation groups** are one of the topics that are all over the internet. I can’t count how many posts and tutorials are available. It looks like everyone knows them; they are obvious for developers, and there is nothing more to say about them. But still, during my work with clients, I see some monstrous models containing way too many measures. I won’t write anything new about this topic. This also isn’t a deep dive. Without further ado, let’s start with an example.

The **calculation group** can be added in the Model view, inside the **Calculation groups** section.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*COmueaN0omfq7tvAzMAQtQ.png)

Rename the Calculation group column. This object will be used in slicers or as columns in visualizations.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Ms-GsGzjsBRU6PWtLOSSmA.png)

Then create calculation items with the following measures.

```c
Current = SELECTEDMEASURE()
PD = CALCULATE(SELECTEDMEASURE(), PREVIOUSDAY(iowa_date[CalendarDate]))
PM = CALCULATE(SELECTEDMEASURE(), PREVIOUSMONTH(iowa_date[CalendarDate]))
PQ = CALCULATE(SELECTEDMEASURE(), PREVIOUSQUARTER(iowa_date[CalendarDate]))
PY = CALCULATE(SELECTEDMEASURE(), PREVIOUSYEAR(iowa_date[CalendarDate]))
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*73YkQ5vm8j_e2TgwkCTszQ.png)

We need some arguments for the created measures. SELECTEDMEASURE() will call them during calculations, depending on a context.

```c
AvgOfSales = CALCULATE(SUM(iowa_sale[SaleDollars]))
CountOfSales = CALCULATE(COUNTROWS(iowa_sale))
SumOfSales = CALCULATE(AVERAGE(iowa_sale[SaleDollars]))
```

OK, everything is ready; it’s time for check them out in practice.

Place the \[**CalculationType**\] column into a slicer and into the column pane on the matrix. Then, some other measures you want to calculate. For example, place \[**SumOfSales**\] into the values pane and a chosen column from the Date dimension.

Here, the calculation group column on a slicer works like a filter for columns.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oK3Uc-0Qj4q8BNSupXsYew.png)

We can add more measures to the table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0RNjHkXnFTwD3awxDsMh5Q.png)

With one or two period types, it is readable. But, we can go wild and select everything.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Ntog23l77y5NhxV5kSVKBw.png)

We aren’t restricted only to the matrix visual. It look pretty good as well on a chart.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ApVxnHq_Z-lgldylnEHBDA.png)

Creating and editing calculation groups weren’t supported by Power BI Desktop for a long time. To avoid this inconvenience, developers were using Tabular Editor. So, we can compare how it looks in TE.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*89090k01iwmi4XXOJYv9pw.png)

Why calculation groups, you may ask. In this case, we have three measures and five calculation items. With these objects, we can create fifteen combinations of calculations. When we need more combinations, let’s say 10 calculation items and 10 measures. Then, instead of 20 objects, we would need to create 100 measures.
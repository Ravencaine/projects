---
title: "How to Sort Dates in Power BI"
source: "https://medium.com/microsoft-power-bi/how-to-sort-dates-in-power-bi-0926ba6bb5c6"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-10-25
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Sorting Months in the correct order

![How to sort dates correctly in Power BI, showing months sorted alphabetically on the left, then sorted in chronological order on the right](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*7nvGdPidPVhFo3EH.jpg)

How to sort dates correctly in Power BI, showing months sorted alphabetically on the left, then sorted in chronological order on the right

Working with dates can sometimes be a little challenging, this quick guide shows you how to sort dates in Power BI

Its not always obvious how to do simple things like sort months in calendar order

Here we show some simple tips using a date dimension table

If you want to know how to create a date dimension table in Power BI so you can follow this example

[Add a date dimension table in Power BI](https://www.selectdistinct.co.uk/2022/12/28/add-a-date-dimension-table-in-power-bi/)

## Sorting Dates Properly (sort dates chronologically in Power BI)

We usually want to sort dates chronologically

This causes issues when we want to use them in reports

In this example the default sort order is alphabetical, which is not what we want

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*6SgbPOQnCEdvuX5E.png)

Months by default sort alphabetically

## How to sort one column by another column in Power BI

In Power BI Desktop, go to the data tab and select the column that you want to change the sort order of.

In this case we are selecting the ‘MonthNameLong’ column, as by default it is sorting alphabetically

So, to sort dates in Power BI we need to sort the alphabetical fields such as month name, by an associated value based field such as month number

To do this, Click the ‘MonthNameLong’ field heading to select it

On the ribbon, select sort by column and choose ‘MonthNumber’

Sorting the date by month number gives use the effect of sorting the date chronologically

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*jB26vra59JU2vQmn.png)

Now all of the visuals using this field now use the Month Number to sort the values throughout the report

example

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*pBxEW_TUJfMjg3jAeG_Gpg.png)

## Suggested date sorting settings in Power BI

Whilst we are looking at dates, we should do similar for the Day names too as these are also stored as text and will sort alphabetically

If you have used our date dimension table or similar, then you should apply these settings to other fields

![](https://miro.medium.com/v2/resize:fit:1240/format:webp/0*RhXL1m6xWVdlMcZZ.jpg)

## How to sort dates in Power BI: a Conclusion

You now know how to sort dates in Power BI.

Many users are initially frustrated by these date sorting challenges in Power BI, and often they decide to use a date formatted field as a quick work around

But at the expense of readability, showing a chart with month number ’10’ does solve the sorting problem, but the user has to think what it means.

It is much more user friendly to show ‘October’ or ‘OCT’

Now that you have learned that a column can be sorted by a different column this is a very convenient way of sorting date related columns the correct way

It can also be applied to types of data too, e.g. if you have an ‘Ordinal’ data type such as Gold, Silver, Bronze, you could add a sort order column to that with values such as 1,2,3 which can be sorted

Watch our YouTube video on how to sort dates in Power BI

Subscribe to our channel to see more Timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

This post originally appeared in our Blog

[How to sort dates in Power BI — Select Distinct](https://www.selectdistinct.co.uk/2023/01/24/how-to-sort-dates-in-power-bi/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
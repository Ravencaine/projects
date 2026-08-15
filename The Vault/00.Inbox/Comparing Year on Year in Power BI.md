---
title: "Comparing Year on Year in Power BI"
source: "https://medium.com/microsoft-power-bi/comparing-year-on-year-in-power-bi-30d36afeed2c"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2024-04-16
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_dfaUhT-kmW4-xHCWf7tmQ.png)

In an earlier post we showed you how to use [SAMEPERIODLASTYEAR](https://www.selectdistinct.co.uk/2023/06/08/sameperiodlastyear-in-power-bi/) in power BI to compare data to the prior year

The major shortfall of this is that the built in function matches the day of month and month, and does not properly reflect the day of the week

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*pha7A3yCGKG11ISa.png)

If we show these with the day of the week the problem becomes apparent

We can see that this does not suit us if we need to report daily data against the ssame

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*jPOVHURsv1L1eSfK.png)

The solution is to use a matching date from 364 days earlier or 52 weeks

This particular year was also a leap year which has caused the comparison to become out of sync by two days

The solution will need to use these dates

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*j9jYt_4DKODRDmHr.png)

## Use Case for matching weekdays in Power BI

A very good example of where this is a problem is where the data has an obvious difference betweeen weekdays and weekends

Here is an example using our website homepage impressions data by date from Google Search Console Data

You can see the dips at weekends when traffic dips, so it is really important that we match weekdays

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*BLP4-EXIrZZP60i5.png)

## Step by Step to comparing year on year in Power BI

The first thing we will do is show what happens when we use the same period last year function

We create a measure to return the Impressions for the previous year using the SAMEPERIODLASTYEAR function

```c
Impressions LY = 
CALCULATE(sum('Sample GSC Data'[Impressions])
, SAMEPERIODLASTYEAR('Sample GSC Data'[Date]))
```

Then we can easily add the result into a simple table to see the result

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*T84Sp1CVgO0d_15N.png)

At first glance this looks OK

But validation the data back to prior year we can that SAMEPERIODLASTYEAR is not working as we would like it to

The stand out number for last year is the 13 showing against the 13th of April being compared to Saturday the 13th of April 2024

Looking back at the 13th of April 2023 we can see it was a Thursday

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*sY9DMUvUISOYw31t.png)

## Create a measure to return the correct year on year data

We know that if we compare to 364 days ago we will always match the weekday. So we create a filtered measure that does this

```c
Impressions LY2 
= CALCULATE(sum('Sample GSC Data'[Impressions])
, DATEADD('Sample GSC Data'[Date],-364,DAY))
```

We use the DATEADD function, with a minus 364 days value to match to the correct dates

Now when we add this to the same table we can that it correctly aligns last years dates to this year by weekday, and the data for Thursday the 13th April is matched to the Thursday the 11th April

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Deedy3yy74qLYkvE.png)

## Conclusion

In general, Comparing Year on Year in Power BI can be achieved using the same period last year function when the requirement to have matching week days is not important. For example of you are reporting data that is aggregated into months already

But if you need to have comparison of year on year performance where the data is by day, then you need to use this technique or similar

Alternative ways to achieve this could be via a date dimension table in which you could define the previous period in that table. This would be good for periods such as school holidays which can move around at some points in the year

You can also easily amend the number of days to offset to give other comparisons too. such last week (-7 days), or 2 years ago ( -728 days)

Subscribe to our channel to see more tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful SQL, Power BI or other business analytics timesavers in our Blog

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

By [Simon Harrison](https://www.selectdistinct.co.uk/about-select-distinct-limited/simon-harrison-select-distinct/)
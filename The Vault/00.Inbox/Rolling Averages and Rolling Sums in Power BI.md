---
title: "Rolling Averages and Rolling Sums in Power BI"
source: "https://medium.com/microsoft-power-bi/rolling-averages-and-rolling-sums-in-power-bi-c2aae4a20c2f"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-09-11
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Why they are useful and how to create them

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*C6ORh6YnLWsZU06S.png)

## Why are rolling averages useful

Rolling averages and Rolling totals are used when analysing data over time

Rolling averages smooth out fluctuations across the number of periods

Both of these are possible in Power BI if you know the steps involved

![](https://miro.medium.com/v2/resize:fit:1326/format:webp/0*mClLJSsXxN2C1Z-2.png)

## How to create rolling averages in Power BI

Power BI has a really helpful feature called quick measures

Quick measures are a commonly used set of calculations, which simplify the DAX coding when you need to create some of the more complex measures

Click on the Quick measures icon

In calculations, scroll down to

‘Rolling Average’

Add the value to measure and the date

Then in periods, set your period interval from days, months quarters or years

Then set the number of periods before and after

Click OK

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*3WN8G1ZO3dWAAoYf.png)

After you click ok the DAX code is generated for you and the new measure is created

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*XzJjBI35DRSjvp2b.png)

You can now use this field on your visuals

![](https://miro.medium.com/v2/resize:fit:1326/format:webp/0*swwwSnK_K2MMT0YL.png)

## How to create rolling sums in Power BI

By default, Power BI does not have a quick measure for the rolling sum, but to save time, just create a rolling average, then edit the DAX code

Change the highlighted fields

The first one is the name of the measure, so change it from Average to Sum

The second one needs to change the AVERAGEX function to use a SUMX

The press enter

![](https://miro.medium.com/v2/resize:fit:1116/format:webp/0*69DU9Q-Ek-MbZEPe.png)

You now have a rolling SUM measure in Power BI

![](https://miro.medium.com/v2/resize:fit:1384/format:webp/0*K4GUX6Qdn12Eqyqs.png)

A word of caution though, you can see on the chart that the first periods don’t contain the three periods, so you may need to exclude those from the chart

## Conclusion

Having the ability to add a rolling average or rolling sum to Power BI reports helps to smooth out fluctuations and present a more stable result set

This post originally featured on our blog  
[Rolling Averages and Rolling Sums in Power BI — (selectdistinct.co.uk)](https://www.selectdistinct.co.uk/2023/04/27/rolling-averages-and-rolling-sums-in-power-bi/)

Subscribe to our channel to see more Power BI tips and timesavers

[https://www.youtube.com/channel/UC\_DiGjuhpRbv6fE8cqD4QBg](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful Power BI timesavers in our Blog

## [Business Analytics Blog - Select Distinct](https://www.selectdistinct.co.uk/business-analytics-blog/?source=post_page-----c2aae4a20c2f---------------------------------------)

### Business Analytics Blog with tips and Timesavers for Microsoft Power BI, SQL and Excel. Practical tips for Business…

www.selectdistinct.co.uk

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
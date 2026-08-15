---
title: "Power BI KPIs"
source: "https://medium.com/microsoft-power-bi/power-bi-kpis-41b9404763e3"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-11-27
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Power BI KPIs can be a very powerful way to draw attention to specific key performance indicators

![](https://miro.medium.com/v2/resize:fit:1338/format:webp/0*uO-mrRrhx2mIdeyB.png)

## What is a KPI?

a KPI (Key Performance Indicator) is a way to measure performance against a target, these targets can be financial, strategic, operational or simply functional. The important point is in the first word ‘KEY’. To be a KPI the thing being measured must be an important part of the success of the organisation

## Examples of KPIs

Using a retailer as an example, common KPIs could include some of the following

**Sales**  
Gross Sales could be measured against a Budget and progress monitored to ensure that the business remains on track to meet its expected performance

**Marketing**

A Marketing return on investment could be tracked to ensure that marketing spend is delivering sufficient increase in sales revenue (after deducting the marketing cost)

**(Sales revenue — Marketing cost) / Marketing cost = ROI**

**Customer Satisfaction**

Collecting customer feedback and using ordinal measures such as a 1 to 5 scale could be compared against a target or against a year on year comparative

## Using KPIs in Power BI

Power BI can be very helpful with its built in KPI visuals, you can easily add the KPI visual to a dashboard to highlight very quickly areas that need to made prominent

For example

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*rd_zxiU3r06kILVr.png)

The KPI visual shows a comparison to a target, in this case the sales last year are defined as the target with a value of $42.29M and we can clearly see that the sales this year are over 2% higher at $43.15M

It also shows the trend in the background to give more visual context, as well as a colour scheme which shows the value and the trend in green denoting a good performance

## How to create a KPI visual in Power BI

a step by step guide

We will start with a sample dataset which we used the Google Public Dataset for IOWA liquor sales, the reason we sue this is because it is a large dataset and is real data

If you want to do the same we suggest reading this first

[Connect Power BI to Google Big Query — Select Distinct](https://www.selectdistinct.co.uk/2023/09/07/connect-power-bi-to-google-big-query/)

Alternatively just follow along using your own data

## Step 1

Starting with a Power BI workbook in Power BI desktop, select the KPI visual and drag it onto your canvas

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*ccHOfjnWSczc1PEQ.png)

You can see that there are three standard pieces of information that we need in a KPI visual

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*jZdJr2hkna0h0659.png)

Value is the data to be measured, in our example we use the Sales in Dollars

Trend Axis is the time period to be measured across, we will use the date

Target is optional, but we will come back to this

We can now see the visual begin to take shape

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*ai-wvNZ0Lz3CVj0o.png)

The value shown on the KPI card returns the sum of the sales for the last date in the data set by default, at this stage there are no filters applied, we can also see the trend in the background but it has no colour until we give it context

At this point without the target being set Power BI has no way to determine whether this value is good or bad

## Step 2

Our data set has two years of data and contains over five million rows of data, but this data does not have any useful date grouping, so we created a data dimension table to return all of the dates relevant to this data set

If you want to see how to do this read this blog and grab the DAX code to create your own

[How to add a date dimension table in Power BI (selectdistinct.co.uk)](https://www.selectdistinct.co.uk/2022/12/28/add-a-date-dimension-table-in-power-bi/)

We now have a calendar table which will give us better options for reporting

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*sJZmWTwoBCDYS6W6.png)

Now set the relationship between the sales data and the calendar table

![](https://miro.medium.com/v2/resize:fit:1248/format:webp/0*k4qa9oiMSaWfddQ8.png)

Now can can amend the KPI to show the monthly trend using the Year and month number field

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*8aUODX58akXOUWrh.png)

The trend is now changed to display the monthly data in the background

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*yliqNiRxAp-Z9N_S.png)

But you can see that is still lacks the context of a target

Usually you would have a sales budget to measure against, but in this case we will use the next best thing, last year as a comparative

In the sales table, create a new measure using SAMEPERIODLASTYEAR

```c
Sales $ LY = CALCULATE(SUM(sales[sale_dollars]), SAMEPERIODLASTYEAR('Calendar table'[Date]))
```

For more information on using SAMEPERIODLASTYEAR read this post

[How to use SAMEPERIODLASTYEAR in Power BI — (selectdistinct.co.uk)](https://www.selectdistinct.co.uk/2023/06/08/sameperiodlastyear-in-power-bi/)

## Step 3

Add the target value to the KPI card, drag the new measure for sales last year into the target field for the KPI visual

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*v53KumMp4VkvlRF2.png)

Finally, set the title to something more readable such as Sales v Last Year

## Formatting Options for Power BI KPIs

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*g45WbQT0K63eaWfv.png)

**Callout value** is used to set the font and font size as well as horizontal and vertical alignment options for the main value being measured. You can also change the display units as Thousands, Millions, Billions or even Trillions

**Icons** allows you turn them on or off, you might notice a small green tick beside the $43.15M sales value which denotes the performance relative to the target, you can also change the size of the icon

**Trend Axis** allows you to enable the background trend chart behind the main number, there are also options to change the colour using conditional formatting, reverse the logic so that low is good (in the case of overheads for example) and amend the level of transparency

**Target Label** allows you to turn the target and the target value on or off, as well as change the title from the default ‘goal’ to a word of your choice such as target or last year. You can also amend the font, font size and colour. One other option is to show the distance to goal either on or off, this relates to the +2.02% in our example, with options to show as a percentage, a value difference or both and again to change the direction to decreasing is positive

**Date** allows you to show the date, in our example it shows the year month number as ‘2022/12’ which could be helpful, again with the usual font, size and colour options

## Some Limitations of Power BI KPIs

Although the KPI cards can be very useful, its worth trying to keep the focus on the relative performance of the key indicators, too many visual elements can actually detract from the impact so choose items carefully

The axis of the trend line can be misleading at times as it defaults to a maximum and minimum value, this can cause confusion as the low points in the trend tend to look like zero

Unlike other visuals there is no interactivity on the objects so no way to drill through, you would need to add other visuals to the page to allow this

## Conclusion

The main purposes of KPIs and the KPI visuals in Power BI are to draw your attention to the relevant performance

Think of using them to highlight the most important points on a page but keep things to a minimum

## Further reading

Choosing relevant and measurable goals and making sure they align with business objectives is a very broad topic, to learn more we recommend you take a look at the Made to Measure KPIs website, by Bernie Smith, He shares some really insightful guides to their use and how to avoid common pitfalls

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*KOKBd6vtcT6sqSZ0.png)

[Made to Measure KPIs | Practical help with KPIs, measures and reporting](https://madetomeasurekpis.com/)

Subscribe to our channel to see more tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

This article was originally published in our Blog

[Power BI KPIs — Select Distinct](https://www.selectdistinct.co.uk/2023/10/18/power-bi-kpis/)

Find other useful SQL, Power BI or other business analytics timesavers in our Blog

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
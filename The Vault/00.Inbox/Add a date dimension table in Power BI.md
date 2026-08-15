---
title: "Add a date dimension table in Power BI"
source: "https://medium.com/microsoft-power-bi/add-a-date-dimension-table-in-power-bi-347b3a32d5f2"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-06-08
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
## How to easily add a date dimension table in Power BI in 1 minute

![How to easily create a date dimension table in Power BI](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*TV6S1vZPaJUM6AkQ.jpg)

How to easily create a date dimension table in Power BI

A date dimension table allows you to work with dates more easily, Having a date dimension table can eliminate the need for complex DAX expressions.

Creating a date dimension table in Power BI is straightforward, you can just copy this DAX code into a new table, then customize as needed.

```c
Calendar table =

ADDCOLUMNS(
CALENDAR(DATE( 2020, 1, 1 ), DATE( 2021, 12, 31 ) ), "DateAsInteger", FORMAT ( [Date], "YYYYMMDD" ),
"Year", YEAR( [Date] ),
"Monthnumber", FORMAT ( [Date], "MM" ),
"YearMonthnumber", FORMAT ( [Date], "YYYY/MM" ),
"YearMonthShort", FORMAT ( [Date], "YYYY/mmm" ),
"MonthNameShort", FORMAT ( [Date], "mmm" ),
"MonthNameLong", FORMAT ( [Date], "mmmm" ),
"DayOfWeekNumber", WEEKDAY ( [Date] ),
"DayOfWeek", FORMAT ( [Date], "dddd" ),
"DayOfWeekShort", FORMAT ( [Date], "ddd" ),
"Quarter", "Q" & FORMAT ( [Date], "Q" ),
"YearQuarter", FORMAT ( [Date], "YYYY" ) & "/Q" & FORMAT ( [Date], "Q" ) )
```

The CALENDAR function above generates a list of all of the dates between the two date values entered, which you easily customise or substitute for a dynamic date range the references another dataset, we often use this with a maximum and minimum date from a fact table to make the date dimension fully dynamic

Once you have added the date dimension table you can set the relationships to it and use any of the extra date fields in your dashboards

Try out different options and see what works best for you.

## Watch the video to see it in action, its only just over 1 minute long

Subscribe to our channel to see more Power BI Timesavers

[https://www.youtube.com/channel/UC\_DiGjuhpRbv6fE8cqD4QBg](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
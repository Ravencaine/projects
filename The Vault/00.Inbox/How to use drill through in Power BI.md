---
title: "How to use drill through in Power BI"
source: "https://medium.com/microsoft-power-bi/how-to-use-drill-through-in-power-bi-ee9197913392"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2022-06-10
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Our latest business intelligence tip, is how easy it is to set up drill through in power BI

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KOOq01PkyxLZD_QtdRVf8w.png)

## Lets start with why you should

Allowing your report users to drill through from a summary chart through to a detail page showing what is contained is a really strong way to build engagement and trust in the information

By allowing users to see exactly what is behind the headlines helps users to understand in much greater detail why the numbers are what they are

In this example we walk through a simple scenario showing how it could be used in a **retail report**

## First Step

The first thing we need to do is to create the detail page that we want users to be able to drill to

Here we have created a very simple Top 20 product models by sales amount

![](https://miro.medium.com/v2/resize:fit:1256/format:webp/1*6XUT06KNc9Snl9LyzBuMcQ.png)

Top 20 Best Sellers

Now set up the filters to pass through from the source chart objects

We want to keep all applied filters, in the **Drillthrough** section of the **Visualizations** pane, set **Keep all filters** to **On**.

Now set the filter fields you want to pass from the other report pages to filter down your best sellers

Here we will select Category, Sub Category and Country

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*UBjQBfHHMSFbpOl9PiNzsA.png)

Now we can go back to other pages and any chart that has the relevant fields

We can see a drill through option showing where the relevant Category, Sub Category or Country fields are used in the visual

You can right-click to select the drill through option

## Drill through from a sub category

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KOOq01PkyxLZD_QtdRVf8w.png)

## Drill through from a country summary

![](https://miro.medium.com/v2/resize:fit:1202/format:webp/1*znklHLnvqmkNjhq5aUG2Mg.png)

Click below to see the under 1 minute guide

Subscribe to our channel to see more SQL tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)
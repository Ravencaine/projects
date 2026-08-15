---
title: "How to Sync Slicers in Power BI — Select Distinct"
source: "https://medium.com/@simon.harrison_Select_Distinct/how-to-sync-slicers-in-power-bi-select-distinct-d807b84ddea0"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2024-03-12
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XTiCz8Z6BrDutxgz9KJZfg.png)

This post explains how to sync slicers in Power BI, without any complex code

Slicers are an excellent way to give your users the ability to explore data, allowing users to use the slicers to filter the data down to particular information of interest. But, if your data has different data sets with common values e.g. a week number, you would need to either

1\. Create a relationship between the data sets  
or  
2\. Enable Sync Slicers to keep different data sets aligned

In our example here we will show how you can use the sync slicers across three different data sets

1\. A Sales Budget  
2\. A Weekly Sales Summary  
3\. A Daily Sales Data Set

Each of these have a common field called week number

If you want to follow the step by step guide, you can download this Excel file with sample data  
[Sync Slicers Data](https://www.selectdistinct.co.uk/wp-content/uploads/2024/03/Sync-Slicers-Data-1.xlsx)

## Step By Step Guide to Sync Slicers in Power BI

## Step 1 — Download the data

Download the Excel file above.  
It contains three tables

Products  
A list of product IDs with fictional Sell Prices and Costs

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*FXPBWyJkGDpXuFCU.png)

Budget  
A simple list of weekly budgets by product, with five products and just four weeks for our example

![](https://miro.medium.com/v2/resize:fit:1282/format:webp/0*GK26Gu2hPbuUErXQ.png)

Actuals  
A randomised fictional data set with the same five products and four weeks but with daily sales being calculated with a random factor applied to the Sales Units

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*CbrbI6NNov2hTlPK.png)

## Step 2 — Load the data into Power BI Desktop

Open Power BI Desktop  
Click Get Data and select your excel file, wherever you saved it

The data sets in the file are formatted as tables already, so select the bottom three options, then click load

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*g-209l9ATpe7kLYX.png)

## Step 3 — Add a weekly summary table using DAX SUMMARIZE

Go to the table view, and click new table, then use the DAX code to create the new table

```c
Actuals Summary = 
SUMMARIZE ( Actuals 
            , Actuals[Week]
            , Actuals[Product ID] 
            , "Sales Units", Sum(Actuals[Sales Units]) 
            , "Sales Value", Sum(Actuals[Sales]) 
            , "Gross Profit", Sum(Actuals[GP]) 
            )
```

The DAX SUMMARIZE function is a great way to create a table of sub totals. In this example our budgets are at a by product by week level. So it makes sense to compare our actual sales to the same level of granularity

How SUMMARIZE Works in this example

Actuals Summary is the name for the new table

SUMMARIZE( is the starting point for the function

Actuals tells the SUMMARIZE function which table we want to summarise

, Actuals\[Week\], Actuals\[Product ID\], This tells the SUMMARIZE function to summarise by the week and product id fields, in our example we want a by week, by product total for sales, units and gross profit

“Sales Units”, Sum(Actuals\[Sales Units\]), “Sales Value”, Sum(Actuals\[Sales\]), “Gross Profit”, Sum(Actuals\[GP\]). These are the fields that we want to create the aggregated values for. Here we set each column and name as well as tell it to use the SUM function

When you press enter the DAX runs and creates the new table

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*aFIUwTUlgB-nH_FQ.png)

## Step 4 — Add the tables and slicers to the Power BI canvas

Create three simple tables from the Budget, Actuals Summary and the Actuals data sets

For the budget we used the Week, Product ID and Sum of Sales Budget

Then for the Actuals Summary, we used the same with Week, Product ID and Sum of Sales Value

and finally to show the sales by day, we used the Week, the Date and the Sum of Sales

Then for each of those add a seperate slicer for each of the three data sets, using the Week field

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*2pQBBgiL82M6tbhw.png)

At this point the slicers all operate independently of each other

## Final Step — Sync Slicers

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*rfH1ZYi27kmtUu65.png)

To get the slicers to stay in Sync, go to the View ribbon

On the right hand side in the Show Panes section, select the Sync Slicers button

The Sync Slicers Panel appears

With the first slicer selected, looks for the advanced options and hit the chevron

Then, in the group name box type the name ‘Week’

Ensure both the options below are also ticked

We have created a group called Week, and we will use this to group the other slicers into the same group

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*4ajx_Hmz3nCPkiM3.png)

Now select the next slicer and enter the same group name in the Sync Slicers panel.

And repeat it for the third Slicer too

Now when you select any of the weeks on any of the slicers all three of them are kept in sync

Here is the dashboard embedded in this page so you can see how it works

## Conclusion

Having the ability to sync slicers across different data sets when the data is at a different level of granularity is really useful

We find that users find this very convenient and it is fairly simple to set up

Subscribe to our channel to see more tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful SQL, Power BI or other business analytics timesavers in our Blog

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

By [Simon Harrison](https://www.selectdistinct.co.uk/about-select-distinct-limited/simon-harrison-select-distinct/)
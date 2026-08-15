---
title: "Conditional Format a Line Chart in Power BI"
source: "https://medium.com/@simon.harrison_Select_Distinct/conditional-format-a-line-chart-in-power-bi-61e25a70e431"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-06-12
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
**This is a workaround to show you how you can conditional format a line chart in Power BI.**

Power BI does not at first seem to have an option to add conditional formatting to a line chart, but, there is a way to make it work, although it takes a few simple steps to do it

here is of the summary of the steps required

1. Create a bar chart
2. Apply conditional formatting to the bar chart
3. Change the bar chart to a line chart and the conditional format remains
![](https://miro.medium.com/v2/resize:fit:1142/format:webp/1*OjHPhR36rPOYiGj7Xv2bOQ.jpeg)

***Because this a workaround it may mean that at some point Microsoft stops this working, but there will hopefully be an official method to ensure that we can still apply conditional formatting to a line chart***

## Step 1

The first step is to create a normal bar chart, in this example we use a stacked column bar chart

Here we can see Gross Sales by Month across a year of data

![](https://miro.medium.com/v2/resize:fit:1206/format:webp/1*s-5S3tWtKh_dgUxqHvNNJQ.png)

## Step 2

Next, we apply the normal conditional formatting rules

to do this in the formatting area, select the ‘fx’ icon next to the default colour option

we have defined fixed bands with blue representing low sales, red for medium and green for high

![](https://miro.medium.com/v2/resize:fit:1322/format:webp/1*7SabxoAnXcAdKwNxQX4DRw.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aknl8E-g1Fi4V-LOlvAD6w.png)

## Step 3

Finally we just need to change it to a line chart, and the conditional formatting we defined earlier is preserved

With the bar chart selected, go over to the visualisations pane and click the line chart icon, the chart is changed to a line chart and the conditional formatting is preserved

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*r-IeM9-8v5V11hOGdfACIA.png)

And there you have it, how to conditional format a line chart in Power BI

Here is a short video which explains these steps in a little more detail

This post was originally posted in our blog  
[Conditional Format a line chart in Power BI (selectdistinct.co.uk)](https://www.selectdistinct.co.uk/2022/12/29/conditional-format-a-line-chart-in-power-bi/)

Find other useful Power BI timesavers in our Blog

[Blog — Select Distinct](https://www.selectdistinct.co.uk/business-analytics-blog/)
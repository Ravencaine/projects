---
title: "Toggle Measures in Power BI"
source: "https://medium.com/microsoft-power-bi/toggle-measures-in-power-bi-3ef8c00bd607"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-09-20
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*ShQExKe5a2mVlgV6.png)

## Space on your dashboards is a limiting factor

Setting up toggle measures in Power BI helps to use the space better

One of the key challenges with dashboard building is finding the balance between detail and available space

This article shows you how to combine a couple of features to create the ability to toggle measures in Power BI

You may want to show sales amount, units sold or profit depending on the selection of a slicer.

We want to give the user an easy option to switch between measures using a slicer

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*1Mn9JNtr1yFsTCMn.png)

This will allow the users to toggle between measures to see which of these measures they choose without having to squeeze all of the data on screen at the same time

**How can you achieve this in Power BI?**

One way to do this is to use the SWITCH function, which is a kind of logical function, similar to CASE statements in SQL or nested IF statements, that evaluates an expression against a list of values and returns one of multiple possible result expressions.

## The syntax of the SWITCH function is:

```c
SWITCH(<expression>, <value>, <result> [, <value>, <result>]… [, <else>])
```

The parameters of a SWITCH function are:

- **expression**: Any DAX expression that returns a single value
- **value**: A target value
- **result**: The output to be calculated if the target value is met
- **else**: An alternative value if none of the target values are met

Let’s see how we can use the SWITCH function to toggle measures in Power BI.

## Step 1: Create a slicer with three options

First, we need to create a slicer that will allow us to choose between three options: Sales, Units Sold and Profit.

## Create the list of options for the slicer

Begin by adding a new table to store the names of each measure you want to select from

On the data pane, click enter data

Double click the first column name and edit it to ‘Measure Name’

and add a second column to define the sort order you want the rows to appear on a slicer, we want Sales to appear first so we have set that as option number one

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*jKfMi6oxn8kQJLSO.png)

Then name this table ‘Measure List’ and click load

## Step 2. Add the slicer for the toggle switch

Click on the slicer icon and a slicer is added to the canvas

Drag the newly created field ‘Measure Name’ to the slicer

By default the Measure names will be sorted in value order, but we want to sort by the Order column

To resolve this, go to the data pane, select the measure names field and set it to sort by the order column

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*tLWAinF-dR5lLAnZ.png)

Your slicer should look like this

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Scp3CK5Az_39xP7j.png)

The slicer now has the options in the correct order, but it does not have any purpose as yet

## Step 3: Define the rules for the SWITCH

We added a new measure for the chart which is controlled by the slicer

Add a new measure and insert this DAX code

```c
Dynamic Measure =

SWITCH (

TRUE (),

SELECTEDVALUE('Measure List'[Measure Name]) = "Sales", sum('Sales Summary'[ Sales]),

SELECTEDVALUE('Measure List'[Measure Name]) = "Units Sold", sum('Sales Summary'[Units Sold]),

SELECTEDVALUE('Measure List'[Measure Name]) = "Profit", sum('Sales Summary'[Profit]),

0

)
```

The formula does the following:

- It creates a variable called SelectedValue that stores the value of the selected option in the slicer using the SELECTEDVALUE function.
- It uses the SWITCH function to return either sales amount, units sold or profit based on the value of SelectedValue.
- if the SelectedValue does not match any of the options then the ELSE case at the end is set to return a zero

## Now we can use the measure in a visual

Add the Dynamic Measure field to the Y axis on a column chart, just as you would if you wanted to chart sales by month

If we select Units Sold, the measure presents units sold

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*qMNyAf2JNJ4BUAhJ.png)

If we toggle it to Sales, we can see the sales

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*8cUsEm12qneErhxa.png)

The column chart presents this quite well,

but you can use this with any visual that supports measures instead

## Conclusion

In this blog post, we learned how to use the SWITCH function to toggle measures in Power BI.

We saw how we can combine this with a slicer with three options and use it as a toggle for the SWITCH function.

Our experience of using this for our clients has often been met with great feedback such as “I love that toggle button!” or “I never realised you could switch between measures”

[(17) Power BI Tips Switch Measures — YouTube](https://www.youtube.com/watch?v=cHMYwdXx1nU)

Subscribe to our channel to see more Power BI tips and timesavers

[https://www.youtube.com/channel/UC\_DiGjuhpRbv6fE8cqD4QBg](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful Power BI timesavers in our Blog

[https://www.selectdistinct.co.uk/business-analytics-blog/](https://www.selectdistinct.co.uk/business-analytics-blog/)

This article was originally published in our blog  
[Toggle Measures in Power BI — Select Distinct](https://www.selectdistinct.co.uk/2023/05/10/toggle-measures-in-power-bi/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
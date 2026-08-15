---
title: "Dropdown Lists in Excel — Select Distinct"
source: "https://medium.com/@simon.harrison_Select_Distinct/dropdown-lists-in-excel-select-distinct-a5d8adb629a8"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2024-01-02
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*IfEyyrayAlwBahEN.png)

Dropdown lists in Excel are a useful feature that allow users to select an item from a list of options.

They are commonly used in data entry to control what data is entered. And to ensure that users do not enter incorrect data, preventing some errors

## Creating a drop down list in Excel

step by step guide to creating a drop down list in Excel

We will use an example of creating a master list of stores for a fictional retailer, we want to control three key inputs

Nearest City, we want to have no misspellings, no abbreviations and consistent names

Location Type, we want to limit to High Street, Shopping Centre or Retail Park

Brand, select the brand from a list, avoiding typo’s

## Step 1, create the control lists

![](https://miro.medium.com/v2/resize:fit:1160/format:webp/0*R879y5johDy6FdTg.png)

We list the allowed values in a worksheet as simple columns. It is also a good idea to create these as Excel tables

[Why you should be using tables in Excel](https://www.selectdistinct.co.uk/2022/12/28/why-you-should-be-using-tables-in-excel/)

To make these into tables select the range of data and press Ctrl+T

## Step 2 — set up data validation

Next, go to the page where you want to add the drop down list and select the cell or range

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Os94QtzLD7QP-u_b.png)

Then on the ribbon, go to Data, Data Validation and select the data validation option

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*pP77WW17Twa81xN4.png)

The data validation dialogue box appears.

## Step 3 — Define the Source Data

In the Allow section, scroll down to select list. Make sure to tick the option for in-cell dropdown, this is what enables the dropdown list

For the source, select the range of cells that you want to appear in the dropdown list

than click OK

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*KikvOad0V8-Ygw61.png)

## Creating a dynamic drop down list in Excel

So far, we have used a fixed range to define the allowed data entry. But you can build some future expansion in by allowing the lists to grow

We will now do this for the brand

The steps are the same as the fixed lists, but with one key difference

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*qGK7sSifR4RdbPYA.png)

\=INDIRECT(“Brands\[Brand\]”)

This command tells the system to look for values within the Brand column, in the Brands table

This is better than a fixed list because if we add a new Brand to the list it is automatically included in the validation range

## How to edit a drop down list in Excel

To edit a dropdown list, simply select one of the cells with the validation, and select data validation on the data ribbon

You are then presented with the data validation dialogue box. From there you can edit the settings or other controls as you need to

Add an input message to a drop down list

To make things easier to understand for your users, you have the option to add an input message. This message can pop up to prompt the user to select a value from the drop down list

You can enter your own text in this message

To do this, select the cell with the validation, then when the data validation box appears, select the Input message tab

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*P5aNXe8Bjc1YYOYf.png)

When a cell with an input message is selected this message is displayed

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*ergVflmlb73PP90q.png)

## Add an error alert to a drop down list

It is also a good idea to add an error message to guide users when data validation is enabled.

To add an error message, select the cell with the validation settings. Click data validation on the ribbon and then go to the Error Alert tab

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*gJDVHn4I8a4VSHbF.png)

There are three styles, by default the stop option prevents any values being entered that are not in the list

The other two are warning and information, these both allow data to be entered that is not in the list. But it does notify the user for a more flexible solution

We will leave it as a Stop option to prevent inconsistencies

## Conclusion

Using drop down lists in excel is a really simple yet powerful way to begin to control data quality, preventing errors at source whilst giving you control over what users see

Subscribe to our channel to see more tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful SQL, Power BI or other business analytics timesavers in our Blog

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

By [Simon Harrison](https://www.selectdistinct.co.uk/about-select-distinct-limited/simon-harrison-select-distinct/)
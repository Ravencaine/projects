---
title: "NETWORKDAYS DAX function"
source: "https://databear.com/networkdays-dax-function/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-04-20
created: 2026-08-04
description: "Power BI is launching new features and functions to improve its functionality. The NETWORKDAYS is a new DAX function that serves the same purpose as the NETWORKDAYS work function in excel. When presented with two dates (the Start and end dates), NETWORKDAYS function returns an integer of the work days available between the two dates."
Processed: "Unprocessed"
---
Like any other power app, Power BI is launching new features and functions to improve its functionality. The NETWORKDAYS is a new DAX function that serves the same purpose as the NETWORKDAYS work function in excel. When presented with two dates (the Start and end dates), NETWORKDAYS function returns an integer of the work days available between the two dates. This function comprises four parameters, as shown in the syntax below.

**NETWORKDAYS(<start\_date>, <end\_date>\[, \<weekend>, \<holidays>\])**

Two of these parameters the start\_date and the end\_date are mandatory, while the holidays and weekends are optional. When the DAX function optional parameter is declared it becomes mandatory and will return an error if they are not incorporated.

## How it works NETWORKDAYS Function

To illustrate how the NETWORKDAYS DAX function works, we will use a function whose syntax is equivalent to that of the NETWORKDAYS work function in excel.

The function is made of four parameters the first three parameters function like the excel function. The fourth parameter allows room for altering the day the week will start.

These parameters are:

1. Start as date
2. End as date
3. Holidays
4. An optional number will adjust the Start of the week (from Monday to any other desired day).

The NETWORKDAYS DAX function has an inbuilt user interface that allows users to select the holiday table and the column with the holiday dates, as illustrated below.

![](99.System/Attachments/Picture1.png)

The table below shows the NETWORKDAYS function UI for the holiday table. This is not the only option, as the user can manually add the holiday list to the UI. Consequently, you can always leave the optional parameter blank and edit it later to make your desired adjustments to the start\_date.

![](99.System/Attachments/Picture21.png)

In this case, we can add the date to the list containing the 3 <sup>rd</sup> parameter using the NETWORKDAYS DAX function as illustrated below.

**fnNETWORKDAYS ( StartDate, EndDate, {#date(2020, 1, 1) {#date(2020,12,25)} )**

The code for this function is:

> ![](99.System/Attachments/data.png)

If the holidays are not in the dedicated column, you should reference that table and filter the holidays. The SUMMARIZE COLUMNS DAX function can be implemented to create a single-column table that will only contain the holiday dates. The syntax for this is illustrated below.

**HolidayTable = SUMMARIZECOLUMNS(‘Holiday Table'\[Dates\])**

[check out this Power BI training resource](https://databear.com/power-bi-training/)
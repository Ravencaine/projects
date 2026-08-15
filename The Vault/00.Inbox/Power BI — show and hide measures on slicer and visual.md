---
title: "Power BI — show and hide measures on slicer and visual"
source: "https://medium.com/@michalmolka/power-bi-show-and-hide-measures-on-slicer-3b9609434466"
author:
  - "[[Michal Molka]]"
published: 2022-06-24
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

UPDATE: Microsoft published a baked in functionality. A Field Parameter, you can check it out in this article: [A field parameter](https://michalmolka.medium.com/power-bi-a-field-parameter-afd2f24c2dcb).

In some cases you want to see all measures on your visualizations. In some instances you want to manipulate a visibility of your calculations. Today I tell you how you can show or hide measures depending on your needs.

The first step is to create standard measures:

```c
Sum of sales = SUM(Iowa_Liquor_Sales[Volume Sold (Liters)])
Avg of sales = AVERAGE(Iowa_Liquor_Sales[Volume Sold (Liters)])
Count of sales = COUNTROWS(Iowa_Liquor_Sales)
Max of sales = MAX(Iowa_Liquor_Sales[Volume Sold (Liters)])
Min of sales = MIN(Iowa_Liquor_Sales[Volume Sold (Liters)])
```

The next step, we need to create a table containing measures names. This table (column) is used to integrate values into a slicer. And to establish a column values on visualizations.

```c
Sales select measure = 
DATATABLE(
    "Measure Name", STRING,
    {
        {"Sum of sales"},
        {"Avg of sales"},
        {"Count of sales"},
        {"Max of sales"},
        {"Min of sales"}
    }
)
```

Moving forward we have to create the measure, which is responsible for showing or hiding selected measures.

```c
Select measure = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Sales select measure'[Measure Name]) = "Sum of sales", [Sum of sales],
        SELECTEDVALUE('Sales select measure'[Measure Name]) = "Avg of sales", [Avg of sales],
        SELECTEDVALUE('Sales select measure'[Measure Name]) = "Count of sales", [Count of sales],
        SELECTEDVALUE('Sales select measure'[Measure Name]) = "Max of sales", [Max of sales],
        SELECTEDVALUE('Sales select measure'[Measure Name]) = "Min of sales", [Min of sales],
        BLANK()
    )
```

Once we have everything ready. We can create visualizations: a matrix and a line chart.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GQkNuitGedmZ3yfS8qJhog.png)

Put a chosen category label into the rows (matrix) and axis (line chart) section.

Locate a \[**Measure name**\] column from the previously created the \[**Sales select measure**\]table, place into the columns (matrix) and columns (line chart) section.

Insert the \[**Select measure**\] measure into the values field (in both cases).

A matrix setup:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Qg_XFegk7BGItAQW8q4Oag.png)

A line chart settings:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VBwTKT2jUtCWoDpceYEPEQ.png)

And here is a demo.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2yTp89ZQFR8TO05sQU1ujA.gif)
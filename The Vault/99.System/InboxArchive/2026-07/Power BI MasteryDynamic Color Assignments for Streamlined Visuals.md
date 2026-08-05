---
title: "Power BI Mastery:Dynamic Color Assignments for Streamlined Visuals"
source: "https://medium.com/microsoft-power-bi/power-bi-mastery-dynamic-color-assignments-for-streamlined-visuals-bc1b59ec29d2"
author:
  - "[[Isabelle Bittar]]"
published: 2023-10-12
created: 2026-07-29
description: "Assigning Bar Chart Colors to Field Values in Power BI Using DAX"
Processed: "Unprocessed"
---
## Assigning Bar Chart Colors to Field Values in Power BI Using DAX

![](99.System/Attachments/1!whvLrKCBIV5YQGlQPTlWDw.png.webp)

By KI Data Science

In the process of developing a comprehensive dashboard to monitor the progression of the COVID-19 situation, I found it necessary to depict the data in various manners to account for the individual circumstances across the different WHO Regions. One of the challenges I faced was ensuring the consistency of bar chart colors across multiple visuals. Manually selecting the colors for each bar in every graph would have been cumbersome and inefficient. Thus, to streamline the process and ensure visual consistency, I employed a DAX measure to dynamically assign the colors based on the respective WHO Region.

### Here’s how the DAX measure works:

The measure, named `Bar chart color`, uses the SWITCH function. The SWITCH function in DAX evaluates a list of conditions and returns one of the multiple possible result expressions. In this case, we're checking which region is selected and assigning a specific color to it.

The `SELECTEDVALUE` function returns the value when there’s only one value in the specified column; otherwise, it returns an alternative or default result. In our scenario, it checks for the currently selected WHO Region and matches it with the predefined color codes.

```c
Bar chart color = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE('WHO Regions'[WHO Region]) = "Europe", "#C8D65B",
        SELECTEDVALUE('WHO Regions'[WHO Region]) = "Western Pacific", "#C12592",
        SELECTEDVALUE('WHO Regions'[WHO Region]) = "Americas", "#FFBB30",
        SELECTEDVALUE('WHO Regions'[WHO Region]) = "South-East Asia", "#5200AE",
        SELECTEDVALUE('WHO Regions'[WHO Region]) = "Eastern Mediterranean", "#00AE8F",
        SELECTEDVALUE('WHO Regions'[WHO Region]) = "Africa", "#0A71D5",
        SELECTEDVALUE('WHO Regions'[WHO Region]) = "Other", "#EFF1F4"
    )
```

### Implementing the DAX Measure in Power BI Visuals:

To utilize this dynamic color assignment in your bar charts:

1. Access the Visual: For the intended bar chart, navigate to the *Visual* tab.
2. Bars Section: Under this section, locate and click on the `fx` symbol adjacent to *Colors*.
3. Field Value: In the dropdown, choose the *Field value* option.
4. Retrieve Measure: From the available options, select the `Bar chart color` measure that you've created.

### This approach is advantageous because:

1. Consistency: The colors remain consistent across multiple visuals, making the dashboard user-friendly and easy to interpret.
2. Efficiency: Eliminating the need for manual color assignment reduces the chances of errors and saves time.
3. Flexibility: In the future, if there’s a need to change the color for a particular region, one would simply need to update this measure, and the change will reflect across all relevant visuals in the report.

By harnessing the power of DAX, the task of assigning consistent colors to bars in a graph based on their categories becomes both streamlined and dynamically adaptable.

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
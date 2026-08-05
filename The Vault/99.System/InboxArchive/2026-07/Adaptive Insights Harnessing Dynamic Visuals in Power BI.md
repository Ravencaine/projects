---
title: "Adaptive Insights: Harnessing Dynamic Visuals in Power BI"
source: "https://medium.com/microsoft-power-bi/adaptive-insights-harnessing-dynamic-visuals-in-power-bi-45847609ab8c"
author:
  - "[[Isabelle Bittar]]"
published: 2023-10-22
created: 2026-07-29
description: "Elevate Data Confidentiality and User Experience with Context-Sensitive Visualizations"
Processed: "Unprocessed"
---
## Elevate Data Confidentiality and User Experience with Context-Sensitive Visualizations

![](99.System/Attachments/1!Up7Q5HQncmCbQr0O8Nm9zA.png.webp)

By KI Data Science

*PBIX file available for download at the end of this article.*

### Introduction

Here is a cool tip inspired from Guy in Cube (view their tutorial [here](https://www.youtube.com/watch?v=sXn-QZqLD-8) ), that allows for the dynamic rendering of diverse visualizations in Power BI, tailored according to specific criteria or parameters you set. This technique is particularly beneficial in fields like HR, where data sensitivity demands prudent handling.

### Contextual Scenario

In HR, the sensitive nature of data often necessitates aggregate results, especially when the subset of employees — determined via filters or row-level security — is small enough to risk individual identification. Consider scenarios like sharing employee survey outcomes or data related to equity, diversity, and inclusion. Such information, if not handled correctly, could lead to privacy issues if report viewers manage to pinpoint individual employees through extensive data manipulation.

### Implementation in Power BI

We’ll explore this concept through a Power BI visualization displaying employee survey responses. The objective is to allow detailed data breakdown (e.g., by job levels: employee, manager, executive) only when the respondent count exceeds 15, ensuring anonymity. Conversely, if the count is under 15, only aggregated data is viewable, maintaining confidentiality.

![](99.System/Attachments/1!nVC-LLpOCYRTojb6v0xLWg.png.webp)

Target Visualization if Over 15 Respondents are Selected

![](99.System/Attachments/1!TlBo-_3HHAJHhwupOGz1sA.png.webp)

Target Visualization if Less Than 15 Respondents are Selected

Our starting point is the following dummy dataset loaded in Power BI:

![](99.System/Attachments/1!GPSuPYk5Bi6vHdJjXP5vbQ.png.webp)

### 1\. Establishing Base DAX Measures for Bar Charts

The initial measures that need to be created are `Overall Score` and `Survey Respondents`

- `Overall Score` calculates the average survey value, normalized by 10 to obtain a percentage.
- `Survey Respondents` counts distinct employee entries.
```c
Overall Score = 
    DIVIDE(
        AVERAGE('Survey Results'[Value]),
        10
    )

Survey Respondents = DISTINCTCOUNT('Survey Results'[Employee Name])
```

Use the card visual to display the `Survey Respondents` measure.

Following this, we will create the measures for the Overall Score per Job Levels:

```c
Overall Score Employees = 
    CALCULATE(
        [Overall Score],
        FILTER(
            'Survey Results',
            'Survey Results'[Job Level] = "Employee"
        )
    )

Overall Score Managers = 
    CALCULATE(
        [Overall Score],
        FILTER(
            'Survey Results',
            'Survey Results'[Job Level] = "Manager"
        )
    )

Overall Score Executives = 
    CALCULATE(
        [Overall Score],
        FILTER(
            'Survey Results',
            'Survey Results'[Job Level] = "Executive"
        )
    )
```

### 2\. Determining Visual Display with a DAX Measure

The goal of this measure: `Total Respondents More or Equal to 15` is to determine which chart will be displayed. If the result of the IF statement is 1, the chart with the detailed decomposition should be displayed. If the result is 0, the chart with the aggregated scores should be displayed.

```c
Total Respondents More or Equal to 15 = 
    IF(
        [Survey Respondents]>=15,
        1,
        0
    )
```

### 3\. Crafting Individual Charts

For the first chart showing the detailed job level composition, select the Clustered column chart and drop the fields as follow:

- The column `Attribute` under the X-axis.
- The measures `Overall Score Employees`, `Overall Score Managers` and `Overall Score Executives` under the Y-axis.
- You can update the names under the Y-axis by removing the “Overall Score” text to lighten the legend.
![](99.System/Attachments/1!cxzTdeEWpskgR8z8GmVw4A.png.webp)

Fields for the First Visual

For the second chart, use the same chart type but replace the Y-axis measures by the `Overall Score` measure.

![](99.System/Attachments/1!fK46Vi3ENnkOBNeUfd7Myw.png.webp)

Fields for the Second Visual

You should now have the following 2 side-by-side charts:

![](99.System/Attachments/1!FMkFD1flAX6ciWxfpG9xqw.png.webp)

The Two Visuals At This Point

### 4\. Incorporating DAX Measure into Visual Filters

We will now add the `Total Respondents More or Equal to 15` measure in the filter pane to each visual and set their target values.

For the chart with the detailed decomposition, set the value as 1.

![](99.System/Attachments/1!9h-fTndicvhweNfr3h9BqA.png.webp)

Set the Value to 1 for the Detailed Decomposition Chart

For the chart with the aggregated results, set the value as 0.

![](99.System/Attachments/1!KGh6fbnP9lamBwZdx8_Aig.png.webp)

Set the Value to 1 for the Detailed Decomposition Chart

For each instance, make sure you click on “Apply filter” at the bottom.

Now add a slicer to your report page and drop the ‘Country’ field to test. If you select the country ‘Canada’, you should have a total of 34 respondents and therefore the chart with the detailed decomposition should be displayed.

![](99.System/Attachments/1!IKvb6J6SJW1AQN8FTFVK5Q.png.webp)

What Should Appear if Over 15 Survey Respondents are Selected

If you select the country US, the aggregated chart should be displayed as the number of respondents is inferior to 15.

![](99.System/Attachments/1!ww29tyuDnZZC46ZuANT-LQ.png.webp)

What Should Appear if Less Than 15 Survey Respondents are Selected

### 5\. Refining Chart Aesthetics

For each chart, make sure to:

- Remove the **Chart Title**
- Remove the **Axis** and **Axis Titles**
- Remove the **white background**
- Add **data labels**

You can also add additionnal formatting like I did. See the detail in the file available for download at the end of this article.

### 6\. Merging Visuals for User Experience

The final step is to place the charts one on top of the other to give your users the feel like it’s only one chart, but rendering different results based on user selections.

### Conclusion

As you can see, this trick can be very practical when you want to render different visuals or simply hide some depending on set criteria. The previous example showed how it could be accomplished in the context of rendering employee data on survey results, but there are multiple use cases where this could be relevant. For example, you can decide to display different visuals based on selected field parameters if there is a more logical or cleaner way of showcasing results, like in the below example on showcasing a line chart if data is selected to be viewed daily, vs. abar chart if data is selected to be viewed monthly or weekly.

![](99.System/Attachments/1!uUWSqzZQSf-g5y674yVynw.png.webp)

Displaying a Line Chart VS. Bar Chart Based on User Selections

Learn more about the possibilities in using field parameters in this [article](https://medium.com/microsoft-power-bi/more-power-to-your-users-with-field-parameters-in-power-bi-bfa948a315b2).

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/1dJJX4h5YseiFOjVo-6Z8PTOzUaQy0K0F?usp=share_link)**.**

Your feedback fuels my content! Engage through comments, and if you find value in such insights, your claps encourage more of this content. Thank you for your readership!

### Sources

*Happy dynamic visualizing in Power BI!*

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
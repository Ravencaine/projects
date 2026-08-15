---
title: "Conditionally Color-Coding Line Charts in Power BI 📈"
source: "https://medium.com/the-bi-corner/conditionally-color-coding-line-charts-in-power-bi-3978fd93a2cc"
author:
  - "[[Isabelle Bittar]]"
published: 2025-04-26
created: 2026-08-04
description: "Step-by-step walkthrough (PBIX included!)"
Processed: "Unprocessed"
---
## Step-by-step walkthrough (PBIX included!)

![](99.System/Attachments/1!51xK6OUgW8hlWjrEGFnKUA.png.webp)

By Isabelle Bittar for KI Data Science

*🎁PBIX available for download at the end of this article!*

### Introduction

So, I’ve written about this before, but I recently figured out a better workaround for conditionally color-coding line charts in Power BI 😅. It’s actually pretty simple, and I’ve been using it a lot lately on my current projects.

Unlike bar/column charts — where we can conditionally set the color using the **fx** — line charts only let us select a single, static color. That can be a big limitation when you want the line color to change based on certain scenarios. In this case, I wanted it to be **green** if the price of Bitcoin increased and **red** if it decreased, based on the selected timeframe.

In this article, I’ll walk you through how I built a line chart that dynamically changes color based on Bitcoin’s price variation.

![](99.System/Attachments/1!zYmSebuQidEi7EQMQSRHzQ.png.webp)

Conditionally Formatting Option Not Available for Line Charts vs. Bar Charts in Power BI

### Step 1: Getting Started

For the data, I’ve loaded a **Bitcoin** table in Power BI with historical prices I retrieved from [Investing.com](https://www.investing.com/).

![](99.System/Attachments/1!rblBJSnbhiks2jrnccznTQ.png.webp)

Then I created a few measures under my **Dates** folder to calculate the date range based on the user’s selection from a custom **DateSelection** table. This slicer drives the selected timeframe.

![](99.System/Attachments/1!hfWf_ZgSK4_gbGpMo9dU5g.png.webp)

Initial Dates Measures Created in Power BI

I won’t spend too much time on this part here. You can view the details in the PBIX file. But if you’re interested in learning more about integrating timeframe selection into your reports, I cover that in detail in this article:

## [Using Time Periods as Slicers to Enhance Power BI Line or Area Charts’ Range](https://medium.com/microsoft-power-bi/using-time-periods-as-slicers-to-enhance-power-bi-line-or-area-charts-range-de1abe76c6c3?source=post_page-----3978fd93a2cc---------------------------------------)

### Enhancing Data Visualization: Mastering Time Frame Selection in Power BI Reports

medium.com

Next, I created the following four measures to calculate the current price, last price, and price variation:

```c
Price = SUM(Bitcoin[Price])

Current Price = 
VAR _MaxDate = [Max Date]
RETURN
    CALCULATE(
        [Price],
        FILTER(
            Bitcoin,
            Bitcoin[Date]= _MaxDate
        )
    )

Last Price = 
VAR _MinDate = [Min Date]
RETURN
    CALCULATE(
        [Price],
        FILTER(
            Bitcoin,
            Bitcoin[Date] = _MinDate
        )
    )

Price Variation = [Current Price] - [Last Price]
```

I’ll be using the **Price Variation** measure to determine whether the line should be green (for a positive change) or red (for a negative one).

### Step 2: Building the Line Chart

To create the line chart that shows price over the selected timeframe, I started by creating a **Calendar** table in Power Query. This table includes all the dates between the min and max dates of the Bitcoin table. I **did not** connect this table to the model.

```c
let
    GetMinDate = Date.StartOfMonth(List.Min(#"Bitcoin"[#"Date"])),
    GetMaxDate = Date.EndOfMonth(List.Max(#"Bitcoin"[#"Date"])),
    Source = #table({"MinDate", "MaxDate"}, {{GetMinDate, GetMaxDate}}),
    AddDateColumn = Table.AddColumn(Source, "Date", each {Number.From([MinDate])..Number.From([MaxDate])}),
    ExpandDates = Table.ExpandListColumn(AddDateColumn, "Date"),
    #"Changed Type" = Table.TransformColumnTypes(ExpandDates,{{"Date", type date}}),
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"MinDate", "MaxDate"})
in
    #"Removed Columns"
```
![](99.System/Attachments/1!Oy7uNesBBj9aJbsEyMs3gw.png.webp)

Calendar Table in Power BI

➡️ *This Calendar table contains only one column: Date.*

Next, I created a new measure called **Price for Graph**:

```c
Price for Graph = 
VAR _SelectedDate = SELECTEDVALUE('Calendar'[Date])
RETURN
    CALCULATE(
        [Price],
        FILTER(
            Bitcoin,
            Bitcoin[Date] = _SelectedDate
        )
    )
```

Then, I built the line chart by:

- Using the Power BI **Line chart** visual
- Dropping the **Date** field from the Calendar table into the X-axis
- Dropping the **Price for Graph** measure into the Y-axis
![](99.System/Attachments/1!GRLmAJ4PLhfz_1mD1fcwlw.png.webp)

Building the Line Chart in Power BI

I also made sure to:

- Set the **X-axis** to “Continuous”
- Set its **Minimum Range** to reflect the \[Min Date\] based on user selection
![](99.System/Attachments/1!UEs2lKFLeqxFMQteRqgyug.png.webp)

Setting up the X-Axis of the Line Chart in Power BI

✅ At this point, the line chart is ready for conditional color-coding.

### Step 3: Conditionally Color-Coding the Line Chart

Next, I created two measures. At first, they both return the same result — just bear with me, we’ll adjust them shortly 😅:

```c
Price - Green Line = 
    IF(
        [Price Variation] >= 0 ,
        [Price for Graph],
        [Price for Graph]
    )

Price - Red Line = 
    IF(
        [Price Variation] < 0 ,
        [Price for Graph], 
        [Price for Graph]
    )
```

Then, I **replaced** the **Price for Graph** measure in the Y-axis with these two new measures.

![](99.System/Attachments/1!wbhFa1phcbtNbo5BE10xGA.png.webp)

Changing the Fields Under the Y-Axis of the Line Chart in Power BI

🟢🔴 At this point, both series overlap in the chart. I then manually set the color of:

- **Price — Green Line** to green
- **Price — Red Line** to red
![](99.System/Attachments/1!vX8GUlBJ_NPlk_wqnpIfuA.png.webp)

Setting the Color of Each Series of the Line Chart in Power BI

Now that the colors are set, I adjusted the measures to only show the appropriate series based on the price variation:

```c
Price - Green Line = 
    IF(
        [Price Variation] >= 0 ,
        [Price for Graph]
    )

Price - Red Line = 
    IF(
        [Price Variation] < 0 ,
        [Price for Graph]
    )
```

📌 *Why do we set the colors first, then change the logic?*  
Because if the condition hides a series (e.g. red line on a price increase), it won’t appear in the visual, and you won’t be able to set its color from the Format pane.

![](99.System/Attachments/1!A8wmj3Bjjdhh7pE-CDG7ww.png.webp)

Adjusting the Measures in Power BI

### Step 4: Final Touches

Just a few clean-up steps to polish the visual:

- I **turned off the legend**
- I **renamed both Y-axis fields** to “Price” so that tooltips don’t display “Price — Green Line” or “Price — Red Line” — just a clean “Price”
![](99.System/Attachments/1!nUiWFCHzW9o4tl_wSsPrCw.png.webp)

Turning Off Legend and Renaming Fields in Power BI

![](99.System/Attachments/1!BMhVONnRjCQQTDER_OrJjQ.png.webp)

Final Result in Power BI

✨ **And voilà!** The result is a line chart in Power BI that dynamically changes color based on Bitcoin price variation.

### Wrapping Up

While line charts in Power BI don’t natively support conditional formatting like bar or column charts do, this workaround can provide that flexibility.

I hope this article gives you some ideas for how to level up your own line chart visuals — and maybe even encourages you to experiment with techniques that go beyond the out-of-the-box options.

Let me know if you try this out — I’d love to hear how you adapt it to your own data! 😊

**🎁 You can download the PBIX file with the final chart and all the formatting used in this article** [**here**](https://drive.google.com/drive/folders/183qJmC0egq0asRKJfE1kKiCRL6GvxTJW?usp=sharing)**.**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)
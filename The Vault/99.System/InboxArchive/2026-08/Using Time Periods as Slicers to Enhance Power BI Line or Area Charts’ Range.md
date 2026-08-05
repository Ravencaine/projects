---
title: "Using Time Periods as Slicers to Enhance Power BI Line or Area Charts’ Range"
source: "https://medium.com/microsoft-power-bi/using-time-periods-as-slicers-to-enhance-power-bi-line-or-area-charts-range-de1abe76c6c3"
author:
  - "[[Isabelle Bittar]]"
published: 2023-12-13
created: 2026-08-02
description: "Enhancing Data Visualization: Mastering Time Frame Selection in Power BI Reports"
Processed: "Unprocessed"
---
## Enhancing Data Visualization: Mastering Time Frame Selection in Power BI Reports

![](99.System/Attachments/1!P7MUfRtm7-l_auwfXiFv8Q.png.webp)

By Isabelle Bittar for KI Data Science

*PBIX file available for download at the end of this article.*

### Introduction

The flexibility to choose a specific time frame for data visualization can be very helpful, especially in domains like stock/asset data analysis. This feature, commonly seen in platforms like Google Finance and CoinMarketCap, allows users to tailor their data analysis to specific periods, offering more targeted insights.

![](99.System/Attachments/1!DTfyJWt1jr8sJZMs-Fzvzg.png.webp)

Examples From Google Finance and CoinMarketCap

In this article, I’ve utilized data from Investing.Com to create the visuals showcased in the cover image. I will guide you through the detailed steps to replicate these visuals in Power BI. Below is a glimpse of the `Stock Data` table loaded into Power BI, which forms the basis of our analysis:

![](99.System/Attachments/1!2AVtKTULyQQE-4h98qT5OA.png.webp)

Excerpt of the Stock Data Table in Power BI

You can view the data extracts and steps applied in Power Query in the project folder available for download at the end of this article.

### 1\. Building a Date Period Slicer

The first step is to build a date period table where the period column can be used as a slicer in your Power BI report. In my case, I built the following `Period` table in Excel and loaded it to Power BI.

![](99.System/Attachments/1!ZiCvGZYdHyDErjzisK-88w.png.webp)

Period Table Loaded in Power BI

To ensure that the periods appeared in the right order in the slicer, I sorted the `Period` column by the `Order` column.

![](99.System/Attachments/1!fijJXEnH-fOiEOdf62NiGw.png.webp)

Sorting Columns by Another Column in Power BI

Once this period table was ready, I added a new slicer to the report and add the `Period` column under `Field`.

![](99.System/Attachments/1!pJEaBXWnWblemcOhCVeiwQ.png.webp)

Adding a New Slicer in Power BI

I applied a few formatting steps to the slicer to give it my desired look and feel to it.

![](99.System/Attachments/1!VfRXOrzCdq5enkLqF5jONg.png.webp)

Slicer Added to Power BI Report

If you would like to learn more on the different formatting options you can apply to Power BI’s new slicer, you can check out this article:

## [How To Use Power BI’s New Slicer: Building a Market Watch Dashboard](https://isabittar.medium.com/how-to-use-power-bis-new-slicer-building-a-market-watch-dashboard-1326853731d8?source=post_page-----de1abe76c6c3---------------------------------------)

### Unlocking Enhanced Customization and Interactivity for Dynamic Data Analysis

isabittar.medium.com

### 2\. Calculating Minimum and Maximum Dates

To define the period range for all calculations (such as stock price, variation, percentage variation), it’s essential to calculate the minimum and maximum dates.

The easiest is the `Maximum Date`. We basically need to calculated the latest date available in our dataset. Here is the DAX calculation:

```c
Maximum Date = MAX('Stock Data'[Date])
```

The `Minimum Date` depends on the user’s selection in the slicer. Using the `Maximum Date`, the calculation involves subtracting time based on the selected period. In my case, here were the requirements:

- `1W`: subtract 7 days from the `Maximum Date`
- `1M`: subtract 1 month from the `Maximum Date`
- `6M`: subtract 6 months from the `Maximum Date`
- `1Y`: subtract 1 year from the `Maximum Date`

Here is the DAX measure that was created to achieve this:

```c
Minimum Date = 
VAR _MaxDate = [Maximum Date]
VAR _SelectedPeriod = SELECTEDVALUE(Period[Period])
VAR _MinimumDate = 
    SWITCH(
        TRUE(),
        _SelectedPeriod = "1W", _MaxDate-7,
        _SelectedPeriod = "1M", EDATE(_MaxDate,-1),
        _SelectedPeriod = "6M", EDATE(_MaxDate,-6),
        _SelectedPeriod = "1Y", EDATE(_MaxDate,-12)
    )
RETURN _MinimumDate
```

### 3\. Setting the Minimum Axis to the Line Chart

The final step involves setting the `Minimum Date` measure as the X-axis minimum range in the line or area chart.

In my case, the following area chart was built using the `Date` column as X-axis and `Price` column as Y-axis from the `Stock Data` table.

![](99.System/Attachments/1!NB3gChbRwyb3Ur7zxobDQA.png.webp)

Building the Area Chart

Then I set the minimum X-axis as follow:

![](99.System/Attachments/1!-n2YbpIzdWgQJi3q19JRKw.png.webp)

Setting the Minimum X-Axis of an Area or Line Chart in Power BI

Once this step is completed, the line/area chart range will dynamically change as you select different values from the slicer:

![](99.System/Attachments/1!08zfLAfT-dTV9UsZ_kXk7Q.png.webp)

Dynamically Changing Power BI Chart Range

### Conclusion

Implementing time period slicers in Power BI line or area charts significantly enhances data visualization, particularly in stock data analysis. This approach offers users the flexibility to view data over various time frames, thereby providing deeper insights and a more interactive experience. The combination of calculated minimum and maximum dates, along with dynamic chart ranges, transforms data analysis into a more tailored and insightful process. As we continue to explore the vast capabilities of Power BI, it’s clear that such customization options are not just advantageous but essential for efficient and effective data analysis.

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/1hVQPElEb7I992J_MtY3EcK_lErEe7oF_?usp=drive_link)**.**

Your feedback fuels my content! Engage through comments, and if you find value in such insights, your claps encourage more of this content. Thank you for your readership!

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

In my next article, I will be covering how to dynamically change the color of line and area charts in Power BI, like in the example below.

![](99.System/Attachments/1!jimigRPojMTTjWNWQ2qWJg.png.webp)

Next Article: How To Dynamically Change Area/Line Chart Color in Power BI

In the meantime, here are other articles you might enjoy on data visualization in Power BI.

## [Unlock the Power of Data: Crafting Advanced KPI Cards in Power BI](https://medium.com/microsoft-power-bi/unlock-the-power-of-data-crafting-advanced-kpi-cards-in-power-bi-9d464ea01a37?source=post_page-----de1abe76c6c3---------------------------------------)

### Transforming Data into Stories: Crafting Visually Engaging and Insightful Dashboards

medium.com

## [Enhance Your Power BI Reports: 4 Dynamic Color Coding Techniques](https://medium.com/microsoft-power-bi/enhance-your-power-bi-reports-4-dynamic-color-coding-techniques-4873ef5d18c1?source=post_page-----de1abe76c6c3---------------------------------------)

### Unlock the full potential of your Power BI bar charts with these innovative color coding strategies.

medium.com

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X (Formerly Twitter)***](https://twitter.com/KI_Datascience)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
---
title: "How To Use Power BI’s New Slicer: Building a Market Watch Dashboard"
source: "https://medium.com/microsoft-power-bi/how-to-use-power-bis-new-slicer-building-a-market-watch-dashboard-1326853731d8"
author:
  - "[[Isabelle Bittar]]"
published: 2023-12-10
created: 2026-07-29
description: "Unlocking Enhanced Customization and Interactivity for Dynamic Data Analysis"
Processed: "Unprocessed"
---
## Unlocking Enhanced Customization and Interactivity for Dynamic Data Analysis

![](99.System/Attachments/1!HOPKqddTdFc6QyxDi651nA.png.webp)

By Isabelle Bittar for KI Data Science

*PBIX file available for download at the end of this article.*

### Introduction

The new Power BI slicer became available in November 2023 and I tested it out in the following Market Watch section of a dashboard I am working on. I was really excited by all the customization options and wanted to start experimenting.

The big difference with the new slicer (compared to the old one), are all these customization options. Here are some of the highlights from my experimentation. You can:

- Add images and descriptions to callout values.
- Modify the callout values’ shapes.
- Specify the desired layout (number of rows and columns)
- Apply all the formatting options of buttons to the slicers (e.g.: specify background, border and font colors to values depending on their `State: Default, Hover, Press and Selected`).

In this article, I will share how I leveraged these features to build this slicer of the Market Watch dashboard.

![](99.System/Attachments/1!03QmZ9ofD1S6g5jrKCbGcA.png.webp)

Watch List Leveraging Power BI’s New Slicer

### Case Study: Market Watch Dashboard

![](99.System/Attachments/1!ELLDTSFx0jqRJhRTz3vCOA.png.webp)

By Isabelle Bittar for KI Data Science

I am developing a dashboard using [Investing.com](https://ca.investing.com/crypto/bitcoin) data to track selected stocks and currencies. This ‘Market Watch’ section offers a dynamic view of assets over different time frames (1 week, 1 month, 6 months, 1 year) and detailed asset information. The dashboard integrates two slicers: one for time periods and another for watch list assets, both utilizing the new Power BI slicer.

### How to Use Power BI’s New Slicer

Power BI’s new slicer is available on the visualizations pane. You can select it and drag the fields you wish to use (like with the old slicer).

![](99.System/Attachments/1!qNzTsBjCPk_yDxeZmV0a2Q.png.webp)

Using Power BI’s New Slicer

For this slicer, I used the `Abbr` column from the dimension table `Key` created in Excel to help navigate the transaction data exported from [Investing.Com](https://ca.investing.com/). You can view the detailed extracts in the folder available for download at the end of this article.

![](99.System/Attachments/1!mhj1XE5Qil8Q5jDYr7HgFQ.png.webp)

Key Table

The `Image` column was generated using public web links to images (with no backgrounds) that represented each asset. To be able to use the image information, it is important that the `Data category` of this column be `Image URL`

![](99.System/Attachments/1!d355GOgZL0xAbhteXx4Ttg.png.webp)

Changing Data Category to Image URL in Power BI

Here was the starting point of the slicer before applying the different formatting options:

![](99.System/Attachments/1!sCUST_GMKE1vL075s7JbTg.png.webp)

Slicer Starting Point Before Applying Formatting Options

Below are the steps that were taken to achieve the final version of the formatted slicer.

### 1\. Layout Adjustment

I started by setting the slicer to display 6 rows and 1 column.

![](99.System/Attachments/1!c1N-XMHB0fj7_JLBE0zDFg.png.webp)

Changing Power BI’s New Slicer Layout

### 2\. Title Removal

I turned `Off` the title in the `General` tab for a cleaner look.

![](99.System/Attachments/1!Ya9HsR3yKRESk2ftl6WJxA.png.webp)

Removing Power BI’s New Slicer Title

### 3\. Changing the Callout Values’ Font

I changed the callout values’ font style to `Segeo UI Semibold` and applied size `10`.

### 4\. Adding the Callout Values’ Description

I created the following DAX measure called `Description` that I added to the callout values’ `Label`. This measure renders each asset’s full name and their description.

```c
Description = SELECTEDVALUE('Key'[Full Name]) & " - " & SELECTEDVALUE('Key'[Description])
```

To assign in to the callout values’ `Label`, we first need to turn it `On` and add it to the `Field` value.

![](99.System/Attachments/1!HdZS1sPdfEw0rcq9MHCiZA.png.webp)

Adding a Label To Power BI’s New Slicer

### 5\. Incorporating Images

Under `Image`, I added the `Image` column from the `Key` table and made the following changes to the available options:

- Changed the `Image fit` to `Normal`
- Changed the `Position` to `Left`
- Decreased the `Image area size` to `10%`
- Decreased the `Space between image and callout` to `10 px`
- Switched `Off` the `Ignore padding` option
![](99.System/Attachments/1!OcBu7Q5SYZOLt_AVO9CQ1A.png.webp)

Adding and Formatting Images to Power BI’s New Slicer

### 6\. Formatting the Button Options

Finally, for the slicer to fit the theme of my dashboard, I made these last changes under the `Default State` of the `Button` tab.

- Turned `Off` the `Border`
- Changed the `Fill Color` to `Black (#000000)`
![](99.System/Attachments/1!Q6sspwy6zyOQIwb1_jA7-g.png.webp)

Formatting the Button Options of Power BI’s New Slicer

### Conclusion

So, there you have it! Playing around with Power BI’s new slicer has been a game-changer for my Market Watch dashboard. It’s amazing how a few tweaks in formatting can turn dull data into something that’s not just informative but also pretty cool to look at.

Whether you’re a data geek like me or just someone trying to make sense of all those numbers, these new features are a total win. They say the devil is in the details, and in this case, those details are what make your dashboard stand out. So go ahead, give these tricks a try on your own dashboard and watch the magic happen. Happy slicing!

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/1g4JGjTzNHIzx3qBKPUxiEI8KV0BAk5Zn?usp=sharing)**.**

### Engage with Me

What are your experiences with Power BI’s new slicer? Do you have tips or challenges to share? Join the conversation in the comments below.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

In the meantime, here are other articles you might enjoy on data visualization in Power BI.

## [Unlock the Power of Data: Crafting Advanced KPI Cards in Power BI](https://medium.com/microsoft-power-bi/unlock-the-power-of-data-crafting-advanced-kpi-cards-in-power-bi-9d464ea01a37?source=post_page-----1326853731d8---------------------------------------)

### Transforming Data into Stories: Crafting Visually Engaging and Insightful Dashboards

medium.com

## [Enhance Your Power BI Reports: 4 Dynamic Color Coding Techniques](https://medium.com/microsoft-power-bi/enhance-your-power-bi-reports-4-dynamic-color-coding-techniques-4873ef5d18c1?source=post_page-----1326853731d8---------------------------------------)

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
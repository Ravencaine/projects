---
title: "Unlock the Power of Data: Crafting Advanced KPI Cards in Power BI"
source: "https://medium.com/microsoft-power-bi/unlock-the-power-of-data-crafting-advanced-kpi-cards-in-power-bi-9d464ea01a37"
author:
  - "[[Isabelle Bittar]]"
published: 2023-11-01
created: 2026-07-29
description: "Transforming Data into Stories: Crafting Visually Engaging and Insightful Dashboards"
Processed: "Unprocessed"
---
## Transforming Data into Stories: Crafting Visually Engaging and Insightful Dashboards

![](99.System/Attachments/1!_WK9Yws1w6PWCDwV-OdPkg.png.webp)

By Isabelle Bittar for KI Data Science

*PBIX file available for download at the end of this article.*

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

KPI cards are a staple in dashboard development, frequently used for their efficiency in conveying critical metrics. Power BI offers robust visualization tools for enhancing KPIs, but in this article, I aim to take you a bit further. I will guide you through creating your own KPI cards, similar to the ones in our cover image, that go beyond displaying just a single metric. We’ll dive into how to incorporate trends, variations, and even the latest data update details. By the end of this tutorial, you’ll be able to construct KPI cards that offer a richer, more comprehensive data narrative.

### Anatomy of the KPI Card

Let’s start by breaking down the composition of one of the KPI cards I created.

![](99.System/Attachments/1!yuYUoCZSOElR6zqv2azJ2w.png.webp)

Composition of a KPI Card

### Steps to Develop a KPI Card

### 1\. Crafting the Background of the KPI Card

![](99.System/Attachments/1!tLRprOZdtM1TeyGCldyksQ.png.webp)

Crafting the Background of the KPI Card

The first step is to prepare the KPI card background. Here are the three steps to integrate the white background, logo and title:

a) **White Background**: Begin by inserting a rounded rectangle shape from the Insert tab. You can customize this shape in the Format tab — I chose to paint it white and soften the edges by setting the corner rounding to 5%.

![](99.System/Attachments/1!WZ9QAcFPaGCjelL_8FYBSA.png.webp)

Rouding Corners to 5%

b) **Logo**: Next, add another rounded rectangle shape to serve as the foundation for your logo. From the same Insert tab, upload your logo image. For optimal results, I recommend using an image with a transparent background. In my experience, SVG format images tend to render more crisply in Power BI reports.

c) **Title**: Finally, add a text box for the card’s title. You have the freedom to style the text to suit your design — in my design, I opted for a bold main title complemented by a subtler, smaller-font subtitle to provide additional context.

### 2\. Embedding the Main KPI into the Card

![](99.System/Attachments/1!oWSnBBPw9-EFFchSL-X6ZQ.png.webp)

Embedding the Main KPI into the Card

The next step involves incorporating the main KPI into your card. For this example, I used data sourced from [Investing.com](https://ca.investing.com/crypto/bitcoin/historical-data). The data, once loaded, is structured as follows in my table:

*You can view the CSV extracts and Power Query transformation steps in my file available for download at the end of this article.*

![](99.System/Attachments/1!71tKP3kcEzmTypOmsD5FfQ.png.webp)

Data Table

To calculate the current Bitcoin price, I formulated two initial measures:

```c
Maximum Date = MAX('Stock Data'[Date])

Bitcoin Current Price = 
VAR _Date = [Maximum Date]
VAR _Price = 
    CALCULATE(
        MAX('Stock Data'[Price]),
        FILTER(
            'Stock Data',
            'Stock Data'[Source.Name] = "Bitcoin" &&
            'Stock Data'[Date] = _Date
        )
    )
RETURN _Price
```

After setting up these measures, incorporate them into a card visual sourced from the Visualizations pane. This visual is then positioned on the KPI card background to highlight the current Bitcoin price effectively.

![](99.System/Attachments/1!WCqKUd4mGwdSyC4FMKiHcg.png.webp)

Card Visual with KPI Measure

### 3\. Incorporating Variation Data into the KPI

![](99.System/Attachments/1!6T80GXOyfcAq0znQtMteAw.png.webp)

Incorporating Variation Data into the KPI

The subsequent stage involves enriching your KPI card with variation data. This data not only shows the current state but also contextualizes it with past performance. The process begins by crafting measures to dynamically update the content within shapes and text boxes on the card.

Start with the variation text displayed in the green rounded rectangle:

**Bitcoin Price Yesterday**: This measure captures the Bitcoin price from the previous day. It’s calculated using the following DAX formula:

```c
Date 1 Day Before = [Maximum Date] - 1

Bitcoin Price Yesterday = 
VAR _Date = [Date 1 Day Before]
VAR _Price = 
    CALCULATE(
        MAX('Stock Data'[Price]),
        FILTER(
            'Stock Data',
            'Stock Data'[Source.Name] = "Bitcoin" &&
            'Stock Data'[Date] = _Date
        )
    )
RETURN _Price
```

**Bitcoin Price Variation**: This is the difference between today’s price and yesterday’s, calculated simply as:

```c
Bitcoin Price Variation = [Bitcoin Current Price] - [Bitcoin Price Yesterday]
```

**Bitcoin Percentage Variation**: To express this variation as a percentage, use the formula:

```c
Bitcoin Percentage Variation = 
    DIVIDE(
        [Bitcoin Price Variation],
        [Bitcoin Price Yesterday]
    )
```

**Visual Indicators (Arrows)**: Represent upward and downward trends with Unicode characters: `UNICHAR(8599)` for up (↗) and `UNICHAR(8600)` for down (↘).

```c
Arrow Down = UNICHAR(8600) 

Arrow Up = UNICHAR(8599)
```

**Bitcoin Text Variation**: Combining the above elements, this measure creates a dynamic text showing price change and its direction:

```c
Bitcoin Text Variation = 
VAR _VariationText = FORMAT([Bitcoin Price Variation], "$0.00") & " (" & FORMAT([Bitcoin Percentage Variation], "0.0%") & ") " 
VAR _TextToReturn = 
    SWITCH(
        TRUE(),
        [Bitcoin Price Variation]>0, _VariationText & [Arrow Up],
        [Bitcoin Price Variation]<0, _VariationText & [Arrow Down]
    )
RETURN _TextToReturn
```

Next, define the aesthetic elements — the font and background colors for the variation data, based on its nature (positive or negative):

**Colors Defined in DAX**:

```c
Color Dark Green = "#018B77"

Color Dark Red = "#CC426B"

Color Light Green = "#DCFFFB"

Color Light Red = "#F8E3E9"

Color Transparent = "#FFFFFF00"
```

**Conditional Formatting Measures:**

`Bitcoin Font Color` and `Bitcoin Background Color` are set using SWITCH statements, changing colors based on whether the price variation is positive or negative.

```c
Bitcoin Font Color = 
    SWITCH(
        TRUE(),
        [Bitcoin Price Variation]>0, [Color Dark Green],
        [Bitcoin Price Variation]<0, [Color Dark Red],
        [Color Transparent]
        )

Bitcoin Background Color = 
    SWITCH(
        TRUE(),
        [Bitcoin Price Variation]>0, [Color Light Green],
        [Bitcoin Price Variation]<0, [Color Light Red],
        [Color Transparent]
        )
```

After establishing these measures, integrate another rounded rectangle shape into your KPI card. Utilize the ‘Format’ tab to dynamically apply the `Bitcoin Text Variation`, `Bitcoin Font Color`, and `Bitcoin Background Color` to the shape's fill, text, and font color settings. Here is an example for the Bitcoin Text Variation:

![](99.System/Attachments/1!fxbiMYNiDbGQ8-y6piyUXg.png.webp)

Adding the Dynamic Text to a Shape

Finally, to add the information on the last data update, start by creating the DAX measure, as follow:

```c
Last data update text = "24H, updated: " & FORMAT([Maximum Date], "YYYY-MM-DD")
```

Incorporate this measure into a text box (or a custom HTML visual, if preferred). By adding the measure to the text box and saving it, you enable dynamic updates of the last data refresh time.

![](99.System/Attachments/1!1kK_1cry2GP4bkAGSyZTCg.png.webp)

Adding a Dynamic Value to a Text Box

Complete the process by formatting the text font to match the overall design and positioning it aptly on the KPI card background.

### 4\. Integrating the Graph with Historical Prices

![](99.System/Attachments/1!AIEtPUsYc00NhTdWdmDiFg.png.webp)

Integrating the Graph with Historical Prices

The final enhancement to our KPI card involves adding a graph that displays historical price trends. To accomplish this, follow these steps:

- **Selection and Setup**: Begin by choosing an area chart from your toolkit. Assign the `Date` column as the X-axis and the measure `Bitcoin Current Price` as the Y-axis. This forms the basic structure of your graph.
![](99.System/Attachments/1!xtuwTWP3YsU9at2wBZ-IpA.png.webp)

Area Chart Creation

- **Graph Customization for a Trend-Focused Look**: To create a visually appealing and trend-focused graph, implement the following formatting modifications:

a) **Y-Axis Modifications**: Eliminate the Y-axis and its title to simplify the graph. This keeps the focus on price trends over time.

![](99.System/Attachments/1!YfHOtYqqHRWbkuc6SWSYtg.png.webp)

Removing Y-axis

b) **X-Axis Adjustments**: Remove the title from the X-axis. This minimalistic approach aids in highlighting the data itself rather than the chart’s components.

![](99.System/Attachments/1!n7gHfn9FB4BztPoLfksumQ.png.webp)

Removing X-axis’ Title

c) **Line Aesthetics**: Alter the stroke width of the line chart. Reducing it from 3 to 2 creates a sleeker, more refined appearance.

![](99.System/Attachments/1!n0INVvDJ5jy_XhdK5aMo_w.png.webp)

Changing Line Stroke Width

d) **Area Transparency**: Adjust the chart’s area transparency to 90%. This change allows for a better focus on the line graph while maintaining the context provided by the area shading.

![](99.System/Attachments/1!2F90s3UjL0ERJlxKhLOlHQ.png.webp)

Changing Area transparency

e) **Adding a Title**: Conclude by incorporating a title to the graph. This guides the viewer’s understanding and reinforces the graph’s purpose.

![](99.System/Attachments/1!YBAT1TbhnZsPua-AutIVHg.png.webp)

Adding a Title

### Conclusion: Beyond Basic Visualization

In conclusion, this tutorial demonstrates the intricate process of creating dynamic and visually engaging KPI cards using Power BI. In a world where data is abundant but insights are scarce, mastering such customizations in Power BI paves the way for more informed decisions and a stronger grasp of business dynamics.

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/1ddfSR0Tmn51ZIgCnInzj7s0NJabTiMh5?usp=sharing)**.**

Your feedback fuels my content! Engage through comments, and if you find value in such insights, your claps encourage more of this content. Thank you for your readership!

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

Connect or follow me here:

- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***Twitter***](https://twitter.com/KI_Datascience)

Enjoying tips and tricks in advanced data visualization in Power BI? Here are a few recommended reads:

## [Unlocking Potential: 7 Features to Elevate User Experience in Your Power BI Dashboards](https://medium.com/microsoft-power-bi/unlocking-potential-7-features-to-elevate-user-experience-in-your-power-bi-dashboards-a882877d68c3?source=post_page-----9d464ea01a37---------------------------------------)

### Transforming Data Interpretation: Enhancing Engagement, Insight, and Accessibility in Power BI Dashboards

medium.com

## [Adaptive Insights: Harnessing Dynamic Visuals in Power BI](https://medium.com/microsoft-power-bi/adaptive-insights-harnessing-dynamic-visuals-in-power-bi-45847609ab8c?source=post_page-----9d464ea01a37---------------------------------------)

### Elevate Data Confidentiality and User Experience with Context-Sensitive Visualizations

medium.com

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-end) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----9d464ea01a37---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy
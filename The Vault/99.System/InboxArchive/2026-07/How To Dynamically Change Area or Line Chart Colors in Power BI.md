---
title: "How To Dynamically Change Area or Line Chart Colors in Power BI"
source: "https://medium.com/microsoft-power-bi/how-to-dynamically-change-area-or-line-chart-colors-in-power-bi-3a4ad89e58b5"
author:
  - "[[Isabelle Bittar]]"
published: 2023-12-17
created: 2026-07-29
description: "Mastering Visual Insights: A Step-by-Step Guide to Custom Color Dynamics in Power BI Charts"
Processed: "Unprocessed"
---
## Mastering Visual Insights: A Step-by-Step Guide to Custom Color Dynamics in Power BI Charts

![](99.System/Attachments/1!9qMPiG8H8s_bmCybSAXMgA.png.webp)

By Isabelle Bittar for KI Data Science

*PBIX file available for download at the end of this article.*

### Introduction

In my last article, [**Using Time Periods as Slicers to Enhance Power BI Line and Area Charts’ Range**](https://isabittar.medium.com/using-time-periods-as-slicers-to-enhance-power-bi-line-or-area-charts-range-de1abe76c6c3), I showed how to dynamically adjust line or area chart axes using a time period slicer. A notable feature in the accompanying images was the color transition of my charts — shifting from green to red based on the stock/asset price fluctuation. This color change effectively represented positive (green) and negative (red) variations.

![](99.System/Attachments/0!BOHGkwfhhWy72wv4.png.webp)

By Isabelle Bittar for KI Data Science

This technique can be very useful, especially since Power BI does not offer the option to dynamically change the color of lines/areas, unlike its capability with bar charts.

![](99.System/Attachments/1!-oVDxxJ-Fxs9dh83vrlVjA.png.webp)

No Native Option to Dynamically Change Line Colors in Power BI Area or Line Charts

### How To Achieve This in Power BI

To achieve this, I basically used two charts: 1 green chart and 1 red chart. Both charts were exactly the same, except for their line colors.

![](99.System/Attachments/1!27W5kXciwrNr8STxoztfvg.png.webp)

Starting Point: Two Area Charts With Different Line Colors

I then created a measure, applied to each chart’s filter pane, that was used to hide or display the area chart. The result of the following measure gave a 0 or 1 depending if the asset’s price variation was null or positive (1) or negative (0).

```c
Chart Variation Display = 
    IF(
        CALCULATE([Price Variation], ALL('Stock Data'[Date]))>=0,
        1,
        0
    )
```

For the green chart, I set this measure in its filter pane to equal **1** …

![](99.System/Attachments/1!xcFWNqft-kODUSi4OH2DiQ.png.webp)

Applying 1 to the Chart Variation Display Filter Measure to the Green Chart

… while for the red chart, I assigned it a value of **0**.

![](99.System/Attachments/1!0k05L6J0z3g0dYlRuwXPjQ.png.webp)

Applying 0 to the Chart Variation Display Filter Measure to the Red Chart

Once I clicked on the `Apply Filter` for the red chart, the chart disappeared as expected (since the variation was positive).

![](99.System/Attachments/1!vMU6XnlvljRLDfupO1SGdQ.png.webp)

As a final step, I overlayed the charts one on top of each other. I also made sure that the background of both chart was turned off, ensuring that the appropriate color chart was visible depending on the price variation.

![](99.System/Attachments/1!dtBd0K8eoyKhnBz8lhdG_Q.png.webp)

Turning Off the Charts’ Background

### Limitation

One constraint of this approach is the inability to hover over the secondary chart for detailed values. For instance, if the red chart overlays the green, only the red chart’s values are accessible.

![](99.System/Attachments/1!ZRyVrItQtHkWEUUFpXSVPA.png.webp)

Limitation: Cannot Hover Over The Values of The Green Chart

### Other Use Cases for This Technique

This method of toggling chart visibility based on filter pane measures is versatile and applicable in various scenarios. For instance, I applied a similar technique in the following article to safeguard confidential information through context-sensitive visualizations.

## [Adaptive Insights: Harnessing Dynamic Visuals in Power BI](https://medium.com/microsoft-power-bi/adaptive-insights-harnessing-dynamic-visuals-in-power-bi-45847609ab8c?source=post_page-----3a4ad89e58b5---------------------------------------)

### Elevate Data Confidentiality and User Experience with Context-Sensitive Visualizations

medium.com

### Color-Coding Area or Line Charts’ Data Markers

Additionally, an alternative approach involves color-coding data markers of line or area charts, rather than the lines or areas themselves. This method, detailed in the following article, offers another avenue for enriching Power BI reports.

## [Enhancing Data Visualization in Power BI: Color-Coded Markers and Target Lines for Impactful Area…](https://medium.com/microsoft-power-bi/enhancing-data-visualization-in-power-bi-color-coded-markers-and-target-lines-for-impactful-area-c773ad4a12e7?source=post_page-----3a4ad89e58b5---------------------------------------)

### Unlocking Advanced Charting Techniques: A Step-by-Step Guide to Elevating Your Power BI Reports

medium.com

### Conclusion

In sum, while Power BI may not inherently support dynamic color changes in line or area charts, creative solutions like overlaying charts with conditional visibility can effectively achieve this goal. Such techniques not only enhance the visual appeal of data representations but also add a layer of dynamic interactivity to reports. The ability to apply these methods across different scenarios, from data confidentiality to advanced charting techniques, underscores the versatility and power of custom solutions in Power BI.

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/1hVQPElEb7I992J_MtY3EcK_lErEe7oF_?usp=sharing)**.**

Your feedback fuels my content! Engage through comments, and if you find value in such insights, your claps encourage more of this content. Thank you for your readership!

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

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
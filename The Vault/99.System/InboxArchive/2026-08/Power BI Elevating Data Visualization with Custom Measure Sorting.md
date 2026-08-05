---
title: "Power BI: Elevating Data Visualization with Custom Measure Sorting"
source: "https://medium.com/microsoft-power-bi/power-bi-elevating-data-visualization-with-custom-measure-sorting-b368fd382917"
author:
  - "[[Isabelle Bittar]]"
published: 2023-09-04
created: 2026-08-02
description: "How to Implement Custom Sorting for Measures in a Power BI Visualization Table"
Processed: "Unprocessed"
---
## How to Implement Custom Sorting for Measures in a Power BI Visualization Table

![](99.System/Attachments/1!OyFzGmFpqRierN5Zp7d2kQ.png.webp)

By KI Data Science

### Introduction

In Power BI, the flexibility and power of data representation are undeniably vast. For professionals who often deal with large sets of data, the platform offers intuitive solutions to streamline their analyses. One such feature is the ability to easily customize sorting for table values that originate from columns. By employing a custom sort order table and linking it to one’s data model, users can swiftly arrange their data in a manner that best suits their needs.

However, as with any robust tool, there are complexities and unique scenarios to consider. Sometimes, the focus shifts from columns to measures, presenting a distinct set of challenges. Instead of the conventional column values, there might be occasions where the necessity arises to apply a custom sorting mechanism specifically to measures. This divergence from the norm demands a deeper understanding of the platform’s capabilities and, at times, a sprinkle of creativity to derive the best possible outcomes.

### Custom Sorting for Measures

Consider the following scenario: you wish to sort the “Overall Progress” column differently from the standard alphabetical order. Ideally, you’d want a sequence that mirrors progress statuses such as “Ahead of schedule”, “On schedule”, “Slightly behind schedule”, and “Behind schedule”.

![](99.System/Attachments/1!-JQIGXt-I-3K30pkEbqHTg.png.webp)

By KI Data Science

Here’s the original DAX measure for reference:

```c
Overall progress = 
    SWITCH(
        TRUE(),
        [Cumulative completion]>[Cumulative planned completion], "Ahead of schedule",
        [Cumulative completion]=[Cumulative planned completion], "On schedule",
        [Cumulative completion]+0.05>=[Cumulative planned completion], "Slightly behind schedule",
        "Behind schedule"
    )
```

In Power BI tables, measure results can only be sorted alphabetically or numerically by default. To circumvent this, we need a technique that facilitates the desired sort order while adhering to the alphabetical constraints. One way is by integrating invisible Unicode characters that remain hidden in the rendered visual.

The `UNICHAR(8203)` provides a "Zero width space" solution. Although this character is invisible in the visualization table, DAX recognizes it as valid. When sorting, spaces are prioritized before letters. Hence, the more spaces a term has, the earlier it will appear. By pairing with the `REPT()` function, we can append multiple spaces to each result of the switch statement to establish our intended sort order.

Here’s an improved DAX measure using this method:

```c
Overall progress = 
    SWITCH(
        TRUE(),
        [Cumulative completion]>[Cumulative planned completion], REPT(UNICHAR(8203),4) & "Ahead of schedule",
        [Cumulative completion]=[Cumulative planned completion], REPT(UNICHAR(8203),3) &"On schedule",
        [Cumulative completion]+0.05>=[Cumulative planned completion], REPT(UNICHAR(8203),2) &"Slightly behind schedule",
        REPT(UNICHAR(8203),1) &"Behind schedule"
    )
```

Now, by sorting the “Overall Progress” column in the visualization table, the result aligns with our desired sequence.

![](99.System/Attachments/1!HT2KUaNmJIU5SvzXwTiENg.png.webp)

By KI Data Science

### Conclusion

In Power BI, while the platform offers intuitive tools for a myriad of data visualization tasks, certain nuances like custom sorting for measures can pose a challenge. However, with innovative techniques such as utilizing the zero-width space character in DAX, we can overcome these challenges. The example provided underscores the importance of understanding both the out-of-the-box capabilities of Power BI and the creative workarounds that can be employed. As always, the key is to adapt and utilize available tools to make data visualization as insightful and meaningful as possible.

Click [here](https://www.ki-datascience.com/product-page/m-a-execution-dashboard) to see the full Power BI project.

### Sources

## [Custom Sort Order Within a DAX Measure -](https://powerbi.tips/2019/09/custom-sort-order-within-a-dax-measure/?source=post_page-----b368fd382917---------------------------------------)

### Learn how to use DAX to create a custom TEXT column sort order. This tutorial explains a simple solution to ordering…

powerbi.tips

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)
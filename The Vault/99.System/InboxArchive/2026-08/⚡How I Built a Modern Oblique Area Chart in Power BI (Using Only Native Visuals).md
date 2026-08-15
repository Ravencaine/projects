---
title: "⚡How I Built a Modern Oblique Area Chart in Power BI (Using Only Native Visuals)"
source: "https://medium.com/the-bi-corner/how-i-built-a-modern-oblique-area-chart-in-power-bi-using-only-native-visuals-c0986d0c6753"
author:
  - "[[Isabelle Bittar]]"
published: 2025-07-23
created: 2026-08-09
description: "A step‑by‑step guide to designing stylish, custom‑looking area charts without custom visuals"
Processed: "Unprocessed"
---
## A step‑by‑step guide to designing stylish, custom‑looking area charts without custom visuals

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZRXJCfxRehTvpoBCPP8ZmA.png)

By Isabelle Bittar for KI Data Science

🎁 **PBIX available at the end of this article!**

### Introduction

Power BI’s native visuals can produce so many cool and powerful visualizations — and they’re often our go‑to choices because of their great performance and easier maintenance.  
But let’s be honest: sometimes the default visuals don’t quite match the style of the report or dashboard we’re designing… or they just don’t look that great right out of the box. 😅

![](https://miro.medium.com/v2/resize:fit:1332/format:webp/1*l1Ll2KLKfAy0CrMVpqxRvA.png)

Power BI’s Default Area Chart Style

In a recent project, I came across a healthcare app that featured some really modern‑looking area charts, with a slanted, oblique pattern — like the one you see in the cover image of this article. We all know the default Power BI area chart doesn’t exactly look that slick, but after some experimentation, I managed to recreate the look using a native Power BI **line chart** combined with a few workarounds.

Here’s a short demo video of what it looks like in action:

In this article, I’ll walk you through how I built it — it was actually simpler than I was expecting, hope you find it too! 😎

### Step 1: Setting Up the Line Chart

In my data model, there are multiple tables, but the main table containing all the vital measurements is called **“Vital Stats.”** This table stores the average, minimum, and maximum values for all patient vitals being monitored.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*s3x2lTuFGKFNzHticgyhSg.png)

Vital Stats Table Loaded in Power BI

Once the **Vital Stats** table was loaded into Power BI, I created the following three measures to calculate the average, maximum, and minimum values for the selected vital:

```c
Average Vital = 
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER(
            'Vital Stats',
            'Vital Stats'[Measure Type] = "Average"
        )
    )

Max Vital = 
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER(
            'Vital Stats',
            'Vital Stats'[Measure Type] = "Max"
        )
    )

Min Vital = 
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER(
            'Vital Stats',
            'Vital Stats'[Measure Type] = "Min"
        )
    )
```

I then added these three measures to a line chart along with the **Date** field on the axis. To make the chart interactive, I also included a single‑select slicer with a drop‑down list of vitals so users can choose which vital to view.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tLNVBLVWUBkw8DUEHOm47A.png)

Initial Line Chart Set Up in Power BI

### Step 2: Designing the Oblique Background

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3-Bx1EnpLAk7lHf-FoeV9w.png)

Oblique Background Designed in Figma and Exported in PNG

I created the oblique background in **Figma**, which I planned to use behind my Power BI chart. After finalizing the design, I exported it as a **PNG**.

Of course, you could also use background images found online if you prefer a different style. But if you’re interested in learning how to integrate Figma into your Power BI workflow, here’s an introductory article I wrote on the topic:

## [Figma Meets Power BI: Revolutionizing Report Design](https://medium.com/microsoft-power-bi/figma-meets-power-bi-revolutionizing-report-design-420cce760aa7?source=post_page-----c0986d0c6753---------------------------------------)

### Unleashing Creativity and Efficiency in Data Visualization

medium.com

I then added the background as an image in Power BI.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ftHJh45fcJsoVE2w7cHieA.png)

Adding an Image in Power BI

After that, I resized both the chart and the background image so that the background covered the entire plot area, placing it behind the chart. I also made sure to turn off the chart’s own background.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LBQYJtz82KmJ2gTgMa8H_Q.png)

Resizing Background Image and Turning Off Chart Background in Power BI

### Step 3: Creating the White Areas Between the Top and Bottom of the Graph

The goal here was to color in white the areas of the chart above the maximum vital line and below the minimum vital line. To achieve this, I created the following measures that calculate the maximum and minimum heights the line chart should allow:

```c
Max Graph Area = 
VAR _MaxVital = 
    CALCULATE(
        MAXX(
            ALL('Vital Stats'[Date]),
            [Max Vital]
        )
    )
RETURN _MaxVital + 0.05* _MaxVital

Min Graph Area = 
VAR _MinVital = 
    CALCULATE(
        MINX(
            ALL('Vital Stats'[Date]),
            [Min Vital]
        )
    )
RETURN _MinVital - 0.05 * _MinVital
```

I then added these measures to the chart and set the chart’s Y‑axis minimum and maximum to these measures.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*giEwYyz1-Ut7J_8uXYBcaQ.png)

Adding Min and Max Graph Area Measures to Y‑Axis Fields and Setting the Y‑Axis Range in Power BI

At this point, my line chart looked like this:

![](https://miro.medium.com/v2/resize:fit:1326/format:webp/1*LQ7ZbAgQZVQCRRnnuKD_eg.png)

State of the Line Chart After Completing the Previous Steps in Power BI

Now the fun part starts! 🤓

In the **Analytics** pane of the visualization, I created error bars.

- For the **Max Vital** series, I set the **Upper Bound** to `Max Graph Area` and the **Lower Bound** to `Max Vital`.
- I enabled only the **Error Band** option, set the style to **Fill**, changed the band color to **white**, and set Transparency to **0**.

I then repeated the same process for the **Min Vital** series, setting the **Upper Bound** to `Min Vital` and the **Lower Bound** to `Min Graph Area`.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fQSv9b_BbjbTaMgI6S1ymg.png)

Setting the Error Bands to Create White Areas in Power BI

Finally, I set both the **Min Graph Area** and **Max Graph Area** line colors to white.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8mdI_5gO52mD5xkBGc4ilA.png)

Setting the Min and Max Graph Area Line Colors to White in Power BI

### Step 4: Adding the Final Formatting Touches

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BTKX9UfxY3RSM5bPGgDuqQ.png)

Final Formatting Touches to the Line Chart in Power BI

I added some final formatting touches, such as:

- Setting the **Average Vital** line to a darker blue and increasing its width to 4 px.
- Adding 6 px markers to the **Max Vital** and **Min Vital** series.
- Removing axis titles and updating the label font for a cleaner look.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rcuRHsgS90LF1lY0vfU5OQ.png)

Assigning a Custom Tooltip Page to the Line Chart in Power BI

Since there were measures in my chart (like `Max Graph Area` and `Min Graph Area`) that I didn’t want to appear in the default tooltip, I created a custom tooltip on a separate page and assigned it to the chart.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vtFSJiZVYLqCYm0rVT-B8g.png)

Setting a Dynamic Date Selection to the Line Chart in Power BI

Lastly, I wanted the date selection to be dynamic, so users could choose to view the last 7 days, 14 days, or month. To do this, I created a separate table for these time frames, added it to a drop‑down slicer, and used a measure to set the chart’s minimum X‑axis dynamically.

If you’d like to learn more about this dynamic date selection technique in Power BI, check out the article I wrote on the topic:

## [Using Time Periods as Slicers to Enhance Power BI Line or Area Charts’ Range](https://medium.com/microsoft-power-bi/using-time-periods-as-slicers-to-enhance-power-bi-line-or-area-charts-range-de1abe76c6c3?source=post_page-----c0986d0c6753---------------------------------------)

### Enhancing Data Visualization: Mastering Time Frame Selection in Power BI Reports

medium.com

You can explore all the details in the **PBIX** file available for download at the end of this article.

### Conclusion

And that’s it! 🎉 With just a few creative workarounds and some thoughtful formatting, you can push Power BI’s native visuals far beyond their default look. This modern oblique area chart not only gives your reports a fresh, custom design but also keeps everything lightweight and easy to maintain — no custom visuals or external tools required.

I hope this walkthrough sparks some ideas for your own dashboards and shows you how flexible Power BI can be when you experiment a little. If you try this technique (or adapt it to your own style), I’d love to hear about it — feel free to share your results or ask questions in the comments.

Happy building! 🚀✨

**👉As promised,** [**here**](https://drive.google.com/file/d/1fdXjkhegkbZLJhFo-nucHnzLMiiFMQRy/view?usp=sharing) **’s the PBIX file with the example visuals and tricks mentioned above.**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)
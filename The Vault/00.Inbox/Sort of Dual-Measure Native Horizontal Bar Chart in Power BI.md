---
title: "Sort of Dual-Measure Native Horizontal Bar Chart in Power BI"
source: "https://medium.com/microsoft-power-bi/sort-of-dual-measure-native-horizontal-bar-chart-in-power-bi-ce549387c86a"
author:
  - "[[Mateusz Mossakowski]]"
published: 2024-10-27
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*dNKLCWMma2Q6funBOgGrLg.gif)

**While it’s relatively easy to create a dual-axis vertical bar chart in Power BI — especially useful for measures of different types, like absolutes and percentages (using the Line and clustered column chart) — the challenge gets a bit bigger when attempting this with a native horizontal bar chart (Clustered bar chart).**

**Of course, you could use some custom visuals to achieve this, but I don’t always like taking shortcuts (or sometimes I just prefer making things harder for myself). That’s why I decided to experiment with the native Clustered bar chart to create a similar effect, combining an absolute measure (as bars) with a percentage measure (as markers).**

**If you’re not yet bored by this already too long intro, read on to learn the steps needed to meet these requirements!**

From a high-level perspective, we’ll need the following:

1\. A few variations to the percentage measure to properly align it with the absolute measure.  
2\. Several constant lines to simulate a secondary X-axis.  
3\. Error bars to display markers for the percentage measure.

These steps together help create the dual-axis effect within the horizontal bar chart.

**Data Model**

The data model here is intentionally oversimplified — otherwise, I’d risk losing your attention instantly (assuming I haven’t already!).

Metrics1 represents percentage values, while Metrics2 refers to absolute values.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*3VrrvXLEJtzksxVU6yTsCA.png)

Semantic Model — LOL 😁

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Ndk0gxNQ2ESLm2cJonatAw.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*2fSX1-T7Dnc3a7gdM9Ve1A.png)

**Chart Specific Measures**

For the chart-specific measures, we’ll begin with an adjusted percentage measure. This measure defines the “length” of the percentage bar in the chart (which will eventually be made fully transparent) by referencing the maximum value of the absolute measure. This way, 25% aligns with the first quarter of the longest absolute bar, 50% aligns with the midpoint, and so on.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NVe8TmHc48az2kQbDOtjDg.png)

Next, we’ll need a measure to set the X-axis maximum. This measure multiplies the final result by 1.1 to give some extra space right-hand-side for the longest bar (absolute measure) or the farthest marker (percentage measure).

The setup for this includes also:

\- A **percentage factor** variable, defined as the maximum of either 1 (when all percentage measures are below 100%) or the highest percentage value.  
\- An **absolute factor** variable, simply the overall maximum of the absolute measure.

The final X-axis maximum is the product of these three components.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*udpAqmWfzYy6Uc5AWlCKKA.png)

Last but not least, we add four constant lines (though they’re actually dynamic 😉) to simulate a secondary X-axis for the percentage measure. Each line follows a similar pattern: the overall maximum absolute measure is multiplied by 25%, 50%, 75%, or left as-is for 100%. This will help align the percentage markers along the axis.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HZ94X5zocuicQKfR9BFYbg.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*epcq5rPs3gRs6CyRElsc2w.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xCRVd7LqwrgKe9ghl4mgsQ.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TaICDNi-pjZ2uV_dhMAKlw.png)

**Implementation**

Now, let’s dive into the actual implementation. I’ll guide you through each step:

Once again, we’re using a **Clustered bar chart** with the following setup:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-E3OC-wa2oVVUKlt1zPd7Q.png)

The first step is to hide the “fake” percentage measure.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*GP_5x5o7zJeborxTP-9GHQ.png)

The second step is to enable data labels for the “fake” percentage measure and set the value to the “real” percentage measure. This ensures that report end users see meaningful values for each category.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*bBZIfBy1tEFxiYGILOApxw.png)

Next, we need to position the percentage measure markers correctly. To do this, we’ll move on to the error bars in the Further analyses section. For the “fake” percentage measure, we’ll use the measure itself as the upper bound.

Then, we should enable bars — this is just to control the color of the marker. Finally, turn on the markers and select the one that looks the most visually appealing 😁.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Ku-xM-aUm_L2HbF5xWWq9g.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Ft-1apuj8zIelD7Nj67xxw.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*qlKeU8Q-72BJ2T1b2za2AQ.png)

The last missing piece is adding the four constant lines that will help users visually reference the percentage measure marker values at 25%, 50%, 75%, and 100%.

To achieve this, we need to return to the Further Analyses section and create four constant lines that will actually be driven by measure values. Let’s make them dotted and position them behind the bars so they enhance readability without distracting from the chart.

Last but not least, we’ll turn on the data labels and position them above the constant lines to differentiate them from the original X-axis (which will still refer to the absolute measure).

The most crucial step here is to switch the style to **Name**. If we leave it as **Data Value**, the labels will display the overall maximum absolute value multiplied by 25%, 50%, 75%, and 100%, which would only confuse end users 🙃.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*jqkNcJOUQR3ZvBNSfGQymw.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*CRZ-9ZG93V9tSsI-YBbwuw.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*MmNDDF4voZNtI5bLke1icA.png)

**Summary**

As you can see from the above description, setting up a dual-measure horizontal bar chart in Power BI using native visuals is a walk in the park! NOT 😁

Regardless, it was a great logical exercise inspired by [Tomasz Wozniak](https://www.linkedin.com/in/twoznia/), who asked whether we could accomplish something like this in Power BI. It turns out we can, at least to some extent. However, it’s still not ideal and requires a tremendous amount of effort to achieve this suboptimal solution.

Most likely, it would be easier and more effective to use an SVG measure(s) or a Deneb visual to accomplish this. Unfortunately, I’m not yet proficient in those areas, so I haven’t been able to tackle the challenge from either perspective.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*dNKLCWMma2Q6funBOgGrLg.gif)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----ce549387c86a---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee
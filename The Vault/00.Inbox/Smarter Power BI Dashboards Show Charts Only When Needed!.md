---
title: "Smarter Power BI Dashboards: Show Charts Only When Needed!"
source: "https://datatraining.io/blog/chart-visibility-only-when-needed"
author:
  - "[[datatraining]]"
published:
created: 2026-08-13
description: "Have you ever wanted to show a chart in Power BI only when a specific item is selected in another visual? For example, display detailed metrics only when a region or employee is selected? Let's see ways to achieve it."
Processed: "Unprocessed"
---
Have you ever wanted to show a chart in Power BI only when a specific item is selected in another visual? For example, display detailed metrics only when a region or employee is selected? Let's see ways to achieve it.

power bi dax visual

This tutorial shows two ways to achieve the card visibility as required:  
  

1\. The old "card overlay trick"

2\. A smarter, modern method using **dynamic DAX logic** and even **custom placeholders**  

Let’s explore both.

![](https://lwfiles.mycourse.app/datatraining-public/f8fa8a1c24f7de55967e5a6baaf683c0.png) ![](https://lwfiles.mycourse.app/datatraining-public/55b3dcd43c26a843585a2b147995006a.png)

**Method 1: Card Overlay Trick (Quick & Dirty)**  
  
The idea: use a **card visual** on top of the main chart to block it. When a selection is made, the card becomes **transparent** using a DAX measure. It’s quick but has a big downside: **no tooltips**.

**Step-by-Step  
  
**

1\. Create a **card visual** and position it directly over your main chart.

![](https://lwfiles.mycourse.app/datatraining-public/a6161dc51398098ade9855b8c0377977.png)

2\. Add a **placeholder text measure** like:

![](https://lwfiles.mycourse.app/datatraining-public/5d8af5e1a39938b68e3d31dfb41074e9.png) 3. Add it to the card. Format the font, remove the border, center it, and adjust size/color.

4\. Create a **transparency color measure** using RGBA:

![](https://lwfiles.mycourse.app/datatraining-public/6701ccb861665ea4cd58de8f5f955b1b.png)

5\. Apply this measure as **conditional formatting** to:

- Card **text color**
- Card **background color  
	  
	**

Now, the card hides the chart unless a region is selected. **But tooltips won’t work due to the overlay.**

![](https://lwfiles.mycourse.app/datatraining-public/e5b24af700c58cf0aaaac96ef5d449c4.png)

**Method 2: The Smart Way – Dynamic Measures Only**  
  
To avoid overlays (and keep tooltips!), modify your **measures** to return blank when nothing is selected.

**Step-by-Step  
  
**

1\. Update every measure used in the chart, like this:

![](https://lwfiles.mycourse.app/datatraining-public/be9f8806b3edd60023e6f27e9b83fae1.png)

Repeat for Sales Max, Average, and any custom values.  

2\. The chart now **disappears** when nothing is selected, but it leaves a blank space. To make that more user-friendly, add a **visual placeholder.**

![](https://lwfiles.mycourse.app/datatraining-public/2649dd9148ea79a18c90d47fe649fd89.png)

**Optional: Custom Placeholder with SVG**  
  
Instead of using text or shapes, use a **PowerPoint-generated image.  
  
How to Add a Placeholder  
  
**

1. In PowerPoint, design a simple placeholder (e.g. “Please select a region”).
2. Export it as an **SVG image.**
3. In your visual, go to:  
	\- **Format → Plot area → Background image**  
	\- Upload the SVG and set fit to " **fit** " or " **fill** "
4. This image will only be visible **when the chart is blank** (i.e. when no region is selected).

![](https://lwfiles.mycourse.app/datatraining-public/531c63e5c2145d17829d2726f1cc42c1.png)

Now the visual looks polished even without interaction - and no overlay or shape tricks are needed.

**  
Benefits of the Dynamic Method**

Keeps **tooltips**

Works with **dynamic titles and subtitles**

Clean UX — no layering issues

Fully **DAX-driven logic**

Reusable in any report

![](https://lwfiles.mycourse.app/datatraining-public/05e6d445ef44bc0d1228eb42701903ad.png)

**Final Thoughts**

This pattern can be extended:

- Switch images for different selections
- Add animations with bookmarks (if desired)
- Combine with user-based filtering for personalized dashboards

**Hope you like it!**

Give it a try and see how it works for you! I’d love to hear what you think or see how you use this trick in your own reports.

How to Power BI

![](https://www.youtube.com/watch?v=Vo9R2OIYrZc)
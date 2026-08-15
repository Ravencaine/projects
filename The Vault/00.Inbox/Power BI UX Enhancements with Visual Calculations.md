---
title: "Power BI UX Enhancements with Visual Calculations"
source: "https://datatraining.io/blog/visual-calculations-ux-enhancements"
author:
  - "[[datatraining]]"
published:
created: 2026-08-13
description: "Improving the user experience of Power BI visuals through conditional formatting, dynamic titles, and custom reference lines is now significantly easier, thanks to visual calculations. This article walks you through what they are, how they work, and why they can simplify your report development workflow."
Processed: "Unprocessed"
---
Improving the user experience of Power BI visuals through conditional formatting, dynamic titles, and custom reference lines is now significantly easier, thanks to visual calculations. This article walks you through what they are, how they work, and why they can simplify your report development workflow.

power bi visual visual calculation ux

**What Are Visual Calculations?  
  
**

In the past, we often had to create a long list of DAX measures just to format a single chart highlighting the max value, customizing axis limits, or updating titles dynamically. This cluttered the data model and added complexity.

**Visual Calculations** solve that by allowing you to write *logic directly at the visual level*, without adding measures to your model. They are flexible, contextual, and intuitive.  
  
**Use Case 1: Conditional Formatting (Highlighting Max/Min)  
**  
Let’s say you want to highlight the maximum value in a column chart.  
1\. Select the visual.

![](https://lwfiles.mycourse.app/datatraining-public/e64c91514979b824d9d94553e4baf7e1.png)

2\. Go to the *Build* panel → *Tooltips* → **Add New Visual Calculation**.

![](https://lwfiles.mycourse.app/datatraining-public/7f0bc0f7e3e96c4f9fa1d50324c3f7c2.png) 3. Name it: cf max

4\. Use this expression:

![](https://lwfiles.mycourse.app/datatraining-public/63ec463ccfa700b2cf02b1da9974f8b2.png)

The keyword ROWS() dynamically references the current dimension on the x-axis, no need to hardcode fields.  
  

**To apply conditional formatting:**

Tweak the measure a bit:

![](https://lwfiles.mycourse.app/datatraining-public/366354c3fabcf017e62e23aa2de138fa.png)

Don’t forget to set the *data* format of the visual calculation to **Text** so that it can be used in the format pane.

![](https://lwfiles.mycourse.app/datatraining-public/62e5406c9c5f8aa3bbfdb372fa44247c.png)

Then go to Visual → *Columns* → Color fx → choose field value CF Max

![](https://lwfiles.mycourse.app/datatraining-public/378a23fb2872475bed599b5af6de90ea.png)

The big advantage? The **formula automatically adjusts** even if you switch from *Month to Product Subcategory* on the x-axis.

![](https://lwfiles.mycourse.app/datatraining-public/6a612e89c6f4c9006741bf1df86cb278.png)

**Use Case 2: Dynamic Y-Axis Scaling  
**  
Sometimes, we want extra headroom in a chart by pushing the y-axis max a bit higher.  
  

1. Add another visual calculation: Yaxis max
2. Use this expression:

To ensure this works at the **total level** (not just within a single context), wrap it in EXPANDALL:

![](https://lwfiles.mycourse.app/datatraining-public/aeef61777a52cce6ceff231d0a8e5262.png)

Apply this to the Y-axis via the formatting pane.

![](https://lwfiles.mycourse.app/datatraining-public/20664a747cf99482b99ecc7a8c4214a3.png) ![](https://lwfiles.mycourse.app/datatraining-public/70b126f0155424ee68f88656e9f33a84.png)

**Use Case 3: Highlight Points Above Moving Average**  
  
1. Create a line chart

![](https://lwfiles.mycourse.app/datatraining-public/36cd11adba2d69da141c12d4c67dfdda.png)

2\. Add a **moving average line** from a template visual calculation.

![](https://lwfiles.mycourse.app/datatraining-public/36464a62a0d5878cb42f36f24ee5feaa.png)

3\. Change its format to a **dotted black line.**

![](https://lwfiles.mycourse.app/datatraining-public/ac2914775dc1ff1b9fcf2d2352810b27.png)

4\. Create another visual calculation:

![](https://lwfiles.mycourse.app/datatraining-public/c8a5bcec3cf0b46fa38c1d9c063d2e8f.png)

Apply **markers** only to this calculation (disable them for others). This highlights only the points above the moving average.

![](https://lwfiles.mycourse.app/datatraining-public/4cce0ba5b8b36becdb685715efcd7cae.png)

**Use Case 4: Dynamic Subtitle Based on KPI**

Let’s dynamically show how many months had sales above the 3-month moving average.

1. Create a visual calculation returning 1 or 0:
2. Wrap it in a SUMX(ROWS(),...) to count total months.
3. Wrap that again in EXPANDALL() so it works at the total level.

![](https://lwfiles.mycourse.app/datatraining-public/13270cd68853d8f450fc36947fb39781.png)

4\. Create the subtitle:

![](https://lwfiles.mycourse.app/datatraining-public/c80b38cd631c6228c04c13a9d6d5b9ca.png)

Make sure to set this calculation to **Text** in the *Properties* panel.

![](https://lwfiles.mycourse.app/datatraining-public/12649c7d7a682f7ab5393a8265758847.png)

**Use Case 5: Reference Lines and Shaded Areas**

You can also use visual calculations to dynamically set reference lines and shaded bands in charts.  
  
1. Create min and max of the moving average using visual calculations.

![](https://lwfiles.mycourse.app/datatraining-public/85e7e76f78860e6c7934cffb01c5f1a4.png)

2\. Use these values in the constant line or shaded area options.  
3\. Apply color formatting to only the top area.

![](https://lwfiles.mycourse.app/datatraining-public/f80416c73eaf217635f8f28cb49c4cf7.png)

**Why Visual Calculations Are a Game-Changer**

- **No need to pollute your data model** with helper measures.
- Works across dynamic axes (ROWS() and COLUMNS()).
- Simpler syntax than traditional DAX measures.
- Easier to maintain and reuse.

**Summary**

Visual Calculations allow you to:

- Apply conditional formatting
- Set dynamic axis limits
- Highlight specific points
- Build dynamic titles and subtitles
- Customize reference lines and areas

All without writing cluttered DAX measures or modifying your data model.

**Hope you like it!**

Give it a try and see how it works for you! I’d love to hear what you think or see how you use this trick in your own reports.

How to Power BI

![](https://www.youtube.com/watch?v=zF7SOU8QlbA)
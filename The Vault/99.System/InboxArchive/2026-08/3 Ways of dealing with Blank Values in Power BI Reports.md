---
title: "3 Ways of dealing with Blank Values in Power BI Reports"
source: "https://databear.com/blank-values-in-power-bi-reports/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-03-03
created: 2026-08-04
description: "Power BI is an incredible tool for interactive data visualization, but the way it handles blank or missing values can sometimes leave your reports looking a little less than polished."
Processed: "Unprocessed"
---
### Introduction

Power BI is an incredible tool for interactive data visualization, but the way it handles blank or missing values can sometimes leave your reports looking a little less than polished. Those big “blank” values, especially in card visuals, can be jarring and even create the impression of broken reports.

![Blank Values](99.System/Attachments/Blank_Values.png)

While blank values can happen for totally legitimate reasons (for example, there might not be sales data for a particular month/category combination), you want a way to handle them elegantly in your reports. In this blog post, we’ll dive into several strategies to do just that.

### The Problem and Easiest Fix for Blank Values

If your goal is to ensure numerical measures always display a value, even when there’s no corresponding data, the simplest solution is to add “+ 0” to the end of your measure:

- **Original Measure:** Sales = SUMX(‘SalesTable’, ‘SalesTable'\[SalesAmount\])
- **Modified Measure:** Sales = SUMX(‘SalesTable’, ‘SalesTable'\[SalesAmount\]) + 0

![The Problem and Easiest Fix Blank Values](99.System/Attachments/The_Problem_and_Easiest_Fix_Blank_Values.png)

### Using the New Card Visual solve Blank Values

The New Card Visual offers a built-in solution for blank values, letting you customize them without any DAX code. Just toggle the “Show blank value as” option and replace “blank” with your preferred placeholder (e.g., “null”, “N/A”, “0”).

![New card Blank Values](99.System/Attachments/New_card_Blank_Values.png)

### DAX to the Rescue: Using the IF Statement to deal with Blank Values

For finer control or different display values, you can craft a DAX measure using the IF statement to handle blanks:

Sales No Blank = IF(ISBLANK(\[Sales\]), “N/A”, \[Sales\])

This checks if the Sales measure is blank. If it is, “N/A” is displayed, otherwise the original Sales value is returned.

**Understanding Implicit Measures**

You can write the above DAX code even more compactly because the IF statement can implicitly check if a measure is blank:

Sales No Blank = IF(\[Sales\], \[Sales\], “N/A”)

**Choosing the Right Method**

- **\+ 0 Solution:** Super quick, but be careful in charts, as it will force zero values to be displayed.
- **New Card Visual:** Easy and flexible for cards, giving you full control over the blank value display.
- **DAX (IF):** Versatile solution, offering customization for how you handle blanks in various visualizations and measures.

**Let’s Enhance Your Power BI Reports!**

Blank values don’t have to ruin the look and feel of your Power BI reports. Now you have the tools and knowledge to deal with them seamlessly.

Don’t forget to visit our [training page](https://databear.com/power-bi-training/) to learn all you can about Power BI. Also see our other blog posts [page](https://databear.com/blog/).
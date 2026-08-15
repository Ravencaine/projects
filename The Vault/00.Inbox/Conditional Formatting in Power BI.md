---
title: "Conditional Formatting in Power BI"
source: "https://medium.com/write-your-world/conditional-formatting-in-power-bi-ff9a60d908b7"
author:
  - "[[Anurodh Kumar]]"
published: 2025-06-27
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yONoP_df8QhMAVuappRXCQ.png)

image by Anurodh Kumar

Conditional Formatting in Power BI allows you to dynamically change the appearance of visuals (colors, icons, font styles, etc.) based on the data values. It enhances visual storytelling and draws attention to important insights.

## Where You Can Apply Conditional Formatting

### You can apply it to:

- Tables & Matrix visuals
- Card & KPI visuals
- Column & bar charts (using data colors)
- Gauge & multi-row cards (limited options)
- Slicers and buttons (via Field Value formatting)

## Types of Conditional Formatting

### 1\. Background Color

Apply different cell background colors based on numeric thresholds or field values.

### 2\. Font Color

Change text color based on values (e.g., negative numbers in red).

### 3\. Data Bars

Shows horizontal bars inside cells to represent relative size of values.

### 4\. Icons

Add icons like arrows, checkmarks, or traffic lights based on value rules.

## 5\. Field Value Formatting

Dynamically change color, font, or URL based on a column value (text-based hex color codes like #FF0000).

## How to Apply Conditional Formatting (Example: Table Visual)

1. Click on a Table or Matrix visual.
2. Hover over the field in Values, click the down arrow (▼).
3. Select Conditional formatting > \[Type\] (e.g., Background color).
4. Choose: Color by Rules (e.g., if value > 100, color = green) Gradient (from min to max value) Based on another field (e.g., use a % field to color a sales field)

## Example Use Case

### Sales Target Achievement (%):

- ≥ 90% → Green background
- 70–89% → Yellow background
- < 70% → Red background
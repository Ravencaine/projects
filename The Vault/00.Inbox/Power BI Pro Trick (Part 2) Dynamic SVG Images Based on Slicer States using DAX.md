---
title: "Power BI Pro Trick (Part 2): Dynamic SVG Images Based on Slicer States using DAX"
source: "https://medium.com/@ankan.ab21/power-bi-pro-trick-part-2-dynamic-svg-images-based-on-slicer-states-using-dax-c851ac95de9e"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2025-12-30
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
In my last blog post, [***Power BI Pro Trick: Use SVG Images in DAX to Create Smart Visual Indicators 🚀***](https://medium.com/learning-data/power-bi-pro-trick-use-svg-images-in-dax-to-create-smart-visual-indicators-5bd03c6fce6f)***,*** we learned how to convert any image into SVG, make it Power BI-compatible, and render it using the **new Image visual**. If you haven’t read it already, I would suggest you read it.

In this article, we’ll complete the story.

👉 **Goal:**  
Detect **different slicer states** using DAX and dynamically switch SVG images to act as a **visual indicator** for the end user.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4XTi2Oqd_vCe4ufu_dE77g.gif)

Video Demo: Showing different categories using the Image visual

This technique is extremely powerful for:

- Category selection indicators
- Smart legends
- Visual storytelling
- Executive-friendly dashboards

## Problem Statement Recap

We are working with **three categories**:

- Apparel
- Electronics
- Furniture

The slicer can have **7 possible logical states**:

State Selection  
1 Apparel  
2 Electronics  
3 Furniture  
4 Apparel + Electronics  
5 Apparel + Furniture  
6 Electronics + Furniture  
7 All selected OR nothing selected

Our task is to:

- Detect these states using DAX
- Return the **correct SVG image** for each state
- Render it using the **Image visual**

## Step 1: Base Table Assumption

We’ll assume the slicer is built on:

```c
SalesData[Category]
```

Values:

- Apparel
- Electronics
- Furniture

## Step 2: Detect Slicer State in DAX (Core Logic)

This is the **most important part** of the solution.

## Helper Measure — Count Selected Categories

```c
_Selected Category Count =
COUNTROWS(
    VALUES( SalesData[Category] )
)
```

This tells us:

- `1` → Single selection
- `2` → Two selections
- `3` → All selected
- Blank slicer also returns `3` (important!)

## Helper Measure — Check Individual Category Presence

```c
_Is Apparel Selected =
CONTAINS(
    VALUES( SalesData[Category] ),
    SalesData[Category], "Apparel"
)
```
```c
_Is Electronics Selected =
CONTAINS(
    VALUES( SalesData[Category] ),
    SalesData[Category], "Electronics"
)_Is Furniture Selected =
CONTAINS(
    VALUES( SalesData[Category] ),
    SalesData[Category], "Furniture"
)
```

These return `TRUE/FALSE` and make the logic **readable and scalable**.

## Step 3: Final SVG Selector Measure

This is the measure you will bind to the **Image visual**.

```c
Category_Select_Image =
VAR _count = [_Selected Category Count]
```
```c
VAR _apparel     = [_Is Apparel Selected]
VAR _electronics = [_Is Electronics Selected]
VAR _furniture   = [_Is Furniture Selected]RETURN
SWITCH(
    TRUE(),    /* ---------- SINGLE SELECTION ---------- */
    _count = 1 && _apparel,     [SVG_Apparel],
    _count = 1 && _electronics, [SVG_Electronics],
    _count = 1 && _furniture,   [SVG_Furniture],    /* ---------- TWO SELECTIONS ---------- */
    _count = 2 && _apparel && _electronics, [SVG_Apparel_Electronics],
    _count = 2 && _apparel && _furniture,   [SVG_Apparel_Furniture],
    _count = 2 && _electronics && _furniture, [SVG_Electronics_Furniture],    /* ---------- ALL OR NONE ---------- */
    _count >= 3, [SVG_All_Categories],    /* ---------- FALLBACK ---------- */
    [SVG_All_Categories]
)
```

✔ Handles **ALL edge cases**  
✔ No ambiguity  
✔ Easy to extend to more categories

## Step 4: Bind to the Image Visual

1. Insert **Image visual**
2. Image source → **Select from data**
3. Drop `Category_Select_Image`
4. Set **Apply settings to → All**
5. Adjust padding, background, and size

That’s it.  
Your slicer is now **self-explanatory**.

If you found this useful, please clap (***you can give me 50 claps👏 at a time***)

## About the Author:

Hi 👋 Thanks so much for reading! My name is **Ankan Bandyopadhyay,** a data visualization enthusiast/ Power BI Developer who believes that the best charts are the ones that disappear, leaving only the insights behind. Connect with me on **LinkedIn** to discuss data storytelling and visualization design.

☕ If you enjoy my articles and want to support me in writing more, you can [***buy me a coffee***](https://buymeacoffee.com/ankanbandyopadhyay) — every contribution means a lot and keeps this content going.

## Stay Tuned:

Make sure to [**follow me on Medium**](https://medium.com/@ankan.ab21) to access all my articles on advanced techniques in Power BI visualization.

## Connect or Follow Me Here:

- [***LinkedIn***](https://www.linkedin.com/in/bandyopadhyay-ankan/)

Now go build something amazing! 🚀
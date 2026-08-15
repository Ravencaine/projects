---
title: "The Power of Action Dots: Turning Numbers into Signals"
source: "https://medium.com/learning-data/the-power-of-action-dots-turning-numbers-into-signals-0a99152a6b80"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2025-10-10
created: 2026-08-12
description: "Featured"
Processed: "Unprocessed"
---
Featured

*How to make your* ***Matrices*** *come alive with intelligent “action dots,” color-coded direction cues, and dynamic context awareness*

— — — — — — — — — — — 🎁 PBIX included at the end — — — — — — — — — —

![](https://miro.medium.com/v2/resize:fit:1266/format:webp/1*OmXh_AI_jMqLkcVpIlJc-Q.png)

Action Dots in Action

Numbers tell stories, but sometimes they whisper. When you glance at a table or matrix in Power BI, you may see a region with sales of “15,000” and another with “22,000” next to it. But *how much worse is “15,000” compared to the average or to peers in that quarter*? That nuance often gets lost.

Enter **action dots** — tiny visual cues that do heavy interpretive lifting. They help the viewer instantly spot good vs. worrying, outliers, anomalies, and the lowest performers, **right inside the visual**. No extra legend, no side commentary.

In this post, I’ll walk through how to build your own action-dots in Power BI, embed them inside matrix or card visuals, and pair them with a custom KPI layout. By the end, your users will glance and immediately know not just how well a number is doing, *but how well it’s doing relative to its peers*.

## The Data

The dataset used for this presentation can be downloaded from [***here***](https://github.com/Ankan2508/Action-Dots-in-Action).

It is a simple flat table with quarterly sales data divided by region, around 4 years from 2016 to 2019.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*GxOAXX105VztxKX8SM11wA.png)

The Dataset

## The Setup: Sales by Region & Quarter

For this demonstration, we’ll use a simple dataset:

- Columns: `Year`, `Quarter`, `Region`, `Sales`
- Base measure:
```c
Total Sales = SUM('Sales'[Sales])
```

**Our goal:** For every region in every quarter, compare its sales against the **quarterly average** and flag the lowest region in that quarter.

1. **Relative deviation** from the quarterly average
2. **The lowest value in the quarter** gets a special icon
3. Display all this **inline** in a matrix or card, neatly

So far, so good. The magic lies in the custom DAX + formatting tricks.

## Step 1: The Foundation

We start by creating the reference points.

- **QuarterAverage**: average sales of all regions in that quarter
- **MinQuarterValue**: the minimum sales in that quarter
```c
QuarterAverage =
    CALCULATE(
        AVERAGE('Sales'[Sales]),
        ALLEXCEPT('Sales', 'Sales'[Year], 'Sales'[Quarter])
    )
```
```c
MinQuarterValue =
    CALCULATE(
        MIN('Sales'[Sales]),
        ALLEXCEPT('Sales', 'Sales'[Year], 'Sales'[Quarter])
    )
```

These give us the baseline (average) and the lowest performer in each quarter.

## Step 2: The Logic Behind the Dot

Now comes the fun part — the Action Dot logic.

```c
Action Dot = 
VAR Current = [Total Sales] 
VAR QuarterAvg = [QuarterAverage] 
VAR MinValue = [MinQuarterValue] 
VAR DiffPct = DIVIDE(Current - QuarterAvg, QuarterAvg, 0) 

RETURN 
  SWITCH( 
      TRUE(), 
      Current = MinValue, "⚠️", 
      DiffPct > 0.05, "🟢", 
      DiffPct < -0.05, "🔴", 
      "🟡" 
     )
```
- 🟢 = Above average
- 🟡 = Near average
- 🔴 = Below average
- ⚠️ = The lowest value in that quarter

This single emoji now carries meaning. It’s data storytelling in one character.

```c
Sales with Colored Dot (All) = 
VAR CurrentSales = [Total Sales]
VAR FormattedSales = FORMAT(CurrentSales, "#,##0")

-- Calculate quarter average
VAR QuarterAverage =
    CALCULATE(
        AVERAGE('Sales'[Sales]),
        ALLEXCEPT('Sales', 'Sales'[Year], 'Sales'[Quarter])
    )

-- % below average (positive number means below avg)
VAR PercentBelowAverage =
    DIVIDE(QuarterAverage - CurrentSales, QuarterAverage, 0)

-- Minimum sales in the same quarter
VAR MinSales =
    CALCULATE(
        MIN('Sales'[Sales]),
        ALLEXCEPT('Sales', 'Sales'[Year], 'Sales'[Quarter])
    )

-- Determine if this row is the minimum
VAR IsLowest = CurrentSales = MinSales

-- Choose dot based on how far below average
VAR Dot =
    SWITCH(
        TRUE(),
        IsLowest, "⚠️",
        PercentBelowAverage > 0.3, UNICHAR(128308),   // 🔴
        PercentBelowAverage > 0.15, UNICHAR(128992),  // 🟠
        PercentBelowAverage > 0.1, UNICHAR(128993),   // 🟡
        PercentBelowAverage < -0.15, UNICHAR(128994), // 🟢 Green (>15% above avg)
        ""
    )

RETURN
IF(
    ISBLANK(CurrentSales),
    BLANK(),
    FormattedSales & IF(Dot <> "", " " & Dot, "")
)
```

## Step 4: Building the Matrix Visual

Now assemble everything inside the Matrix

1. Place Year and Quarter in the Rows section
2. Place Region in the Columns section
3. Place the Measure “Sales with Colored Dot (All)” in the Values section

… And your basic Matrix visual is ready. Do some formatting to make it look great.

## Step 5: The on-hover HTML-based Tooltip

I have built an HTML-based KPI Card, which is used as a Tooltip on hover to give extra context to the numbers

![](https://miro.medium.com/v2/resize:fit:1284/format:webp/1*1X7F_O4L3zk_mxBjr0jLZQ.png)

On hover Tooltip

### Building the Tooltip:

We combine **DAX logic and HTML formatting** to design an elegant, **color-coded KPI card** that feels alive.

Each card shows:

- The Action Dot
- The main KPI (Total Sales)
- A status tag (“Above Avg” / “Below Avg”) inside a rounded box
- The difference and % difference below it
- A “vs Quarterly Avg” reference

The entire card uses a **monospace font (Consolas)** for perfect alignment.

```c
HTML KPI Card =
VAR CurrentSales = [Total Sales]
VAR QA = [QuarterAverage]
VAR MinQ = [MinQuarterValue]
VAR Diff = CurrentSales - QA
VAR Pct = DIVIDE(Diff, QA, 0)
VAR Direction =
    SWITCH(TRUE(),
        Pct > 0.05, "Above Avg",
        Pct < -0.05, "Below Avg",
        "Near Avg"
    )
VAR Dot =
    SWITCH(TRUE(),
        CurrentSales = MinQ, "⚠️",
        Pct > 0.05, "🟢",
        Pct < -0.05, "🔴",
        "🟡"
    )
VAR Arrow =
    SWITCH(TRUE(),
        Pct > 0, "↗", "↘"
    )
VAR DiffColor = IF(Diff >= 0, "#3FB950", "#F85149")
RETURN
"<div style='font-family:Consolas;padding:10px;width:250px;background:#FFFFFF;border-radius:12px;box-shadow:0 2px 6px rgba(0,0,0,0.08);'>
  <div style='font-size:18px;color:#080326;font-weight:bold;margin-bottom:6px;'>" & Dot & " ₹" & FORMAT(CurrentSales, "#,##0") & "</div>
  <div style='display:inline-block;padding:4px 10px;border-radius:12px;background-color:" &
        SWITCH(TRUE(),
            Pct > 0.05, "#D4EDDA",
            Pct < -0.05, "#F8D7DA",
            "#FFF3CD") &
        ";color:" &
        SWITCH(TRUE(),
            Pct > 0.05, "#155724",
            Pct < -0.05, "#721C24",
            "#856404") &
        ";font-size:12px;font-weight:bold;'>" & Direction & "</div>
  <div style='margin-top:8px;padding:6px 8px;border-radius:12px;background-color:" & DiffColor & ";color:white;font-size:12px;'>
    " & FORMAT(Diff, "+#,##0;−#,##0") & " (" & FORMAT(Pct, "0.0%") & ") " & Arrow & "
  </div>
  <div style='margin-top:6px;font-size:11px;color:#555;'>vs Quarterly Avg ₹" & FORMAT(QA, "#,##0") & "</div>
</div>"
```

And yes — the lowest region will *always* show ⚠️, no matter how close it is to average.  
Because sometimes, “lowest” is all that matters.

## Step 6: Display & legend

Once you use an HTML viewer visual, each card or cell displays:

```c
⚠️ 15,400 (Below Avg)
–3,200 (–17.2%) ↘
vs Quarterly Avg ₹18,600
```

Or:

```c
🟢 24,800 (Above Avg)
+2,100 (+9.2%) ↗
vs Quarterly Avg ₹22,700
```

To help users, you also include a simple legend (in a separate card or multi-row card):

```c
🟢 Above Quarterly Avg  
🟡 Near Quarterly Avg  
🔴 Below Quarterly Avg  
⚠️ Lowest in Quarter
```

## Why this technique wins

- **Inline intelligence**: Users don’t have to mentally compare numbers or hover — the icons do the work.
- **Layered insights**: A number + icon + direction label + diff % — all in one glanceable package.
- **Customizable thresholds**: You can adjust cutoffs (5%, 10%, 15%, etc).
- **Zero dependence on custom visuals**: Pure DAX + HTML viewer (or Power BI card with Rich text)
- **Scalable**: You can use this logic in matrices, cards, tooltips — anywhere.

## Tips, caveats & improvements

- Use **monospace font (Consolas / Courier)** so alignment of numbers + icons stays consistent.
- When the “lowest” dot (⚠️) appears, consider making it bold or tinted red to emphasize criticality.
- If many values are “near average”, think of an alternative icon like “⚖️” or omit the dot.
- For extremely negative values, you might want a more aggressive red shade.
- Test responsiveness — in small card widths (say 180px), trim padding or font sizes.
- Always include a legend or small hint — never assume users know your dot logic.

## Final thoughts

When you build these visual cues thoughtfully, you transform static tables into living dashboards. Rather than letting readers wrestle with numbers, you lead their eyes exactly where you want them.

Numbers remain the foundation, but *action dots* are the signposts. They break the rules of “just showing numbers” and deliver insight — fast, visual, and compelling.

Go ahead — add action dots to your next report. Your stakeholders will thank you for lighting the path through the data.

**Now, as promised, here is the link to the** [***PBIX file***](https://github.com/Ankan2508/Action-Dots-in-Action)

*What creative charting challenges are you facing? Drop a comment below — I’d love to help you break more rules and build better visuals!*

**About the Author**: Hi, I’m **Ankan Bandyopadhyay,** a data visualization enthusiast/ Power BI Developer who believes that the best charts are the ones that disappear, leaving only the insights behind. Connect with me on [**LinkedIn**](http://www.linkedin.com/in/bandyopadhyay-ankan) to discuss data storytelling and visualization design.

***If you like my work, then*** [***buy me a coffee***](https://buymeacoffee.com/ankanbandyopadhyay) ***💓***

*The contents of external submissions are not necessarily reflective of the opinions or work of* [*Maven Analytics*](http://mavenanalytics.io/) *or any of its team members.*

*We believe in fostering lifelong learning and our intent is to provide a platform for the data community to share their work and seek feedback from the Maven Analytics data fam.*

[*Submit your own writing here*](https://medium.com/learning-data/how-to-get-your-work-published-by-learning-data-with-maven-analytics-7df21e466a3e?sk=020dfac485597d602e218968d9ffb395) *if you’d like to become a contributor.*

*Happy learning!*

*\-Team Maven*
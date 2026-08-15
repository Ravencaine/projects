---
title: "Building Interactive Flip-Card KPIs in Power BI: The HTML DAX Technique That Makes Static Cards Obsolete"
source: "https://medium.com/microsoft-power-bi/building-interactive-flip-card-kpis-in-power-bi-the-html-dax-technique-that-makes-static-cards-2905d65a1666"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2026-03-02
created: 2026-08-12
description: "Featured"
Processed: "Unprocessed"
---
Featured

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*gK0PeF-0xi9WFaHt9baHmA.png)

*When Power BI’s native card visuals aren’t enough, we build our own. Here’s how to create stunning, interactive KPI cards with Apple-style flip animations — entirely from DAX.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*In18GuMAOo9XzIeplDtQXA.gif)

The HTML Cards

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## The Problem with Static KPI Cards

Let’s be honest: Power BI’s native card visuals are… fine. They show a number. Maybe a trend arrow. Perhaps a comparison to last year, if you’re feeling fancy.

But they’re static. Boring. They tell you **what,** but rarely **why**.

What if your KPI cards could do this instead:

- Show the headline number on the front
- Reveal period growth, CAGR, and YoY comparisons when you hover
- Animate with a smooth flip transition (like flipping a physical card)
- Display dynamic insights that change based on your filters
- All without leaving Power BI or installing custom visuals

**That’s exactly what we’re building today.**

## What We’re Creating

Four interactive KPI cards for a pharmacy analytics dashboard:

**💰 Total Revenue**

- Front: €8.6M with period context
- Back: Period Growth, CAGR, YoY analysis

**💚 Total Margin**

- Front: €2.4M with 28.0% margin rate
- Back: Margin health assessment and growth trends

**💸 Total Cost**

- Front: €6.2M with cost ratio
- Back: Cost efficiency and inflation pressure alerts

**📊 Transaction Volume**

- Front: 62.1K transactions with a daily average
- Back: Volume velocity and customer engagement insights

Each card:

- Flips on hover with CSS3 animations
- Calculates dynamic metrics (CAGR, YoY) from DAX
- Adapts text based on filter context
- Maintains your report’s color scheme
- Requires zero JavaScript

## Why This Technique Matters

**1\. Native limitations pushed aside**  
The HTML Content visual gives us full control over layout, styling, and interactions that standard visuals can’t match.

**2\. No custom visuals needed**  
Everything runs on the HTML Content visual (available in AppSource) — no organizational approval red tape.

**3\. Pure DAX logic**  
All calculations, text, and even the HTML structure are generated from DAX measures. Change your data model, and the cards adapt automatically.

**4\. Enterprise-ready**  
Once built, these cards work in Power BI Service, can be bookmarked, and respond to all filters and slicers like any native visual.

## Prerequisites

Before we start, you’ll need:

1. **Power BI Desktop** (March 2024 or later)
2. **HTML Content visual** from AppSource ([install here](https://marketplace.microsoft.com/en-us/product/WA200001930))
3. Basic understanding of DAX (you don’t need to be an expert)
4. A dataset with revenue/margin data (we’ll use a pharmacy dataset, but you can adapt to any domain)

**Our data model:**

- `FactSales` table with `RevenueEUR`, `MarginEUR`, `CostEUR`
- `DimDate` table with standard date intelligence columns
- Relationship: `FactSales[DateID]` → `DimDate[DateID]`

## Building the First Card: Total Revenue

I’ll walk you through building the revenue card in complete detail. Once you understand this pattern, you can build the other three yourself (or grab them from me — more on that at the end).

## Step 1: Create the Core Measures (TMDL-friendly)

First, we need the basic calculations:

```c
measure total_revenue = SUM(FactSales[RevenueEUR])

measure py_revenue = 
    CALCULATE(
        [total_revenue],
        SAMEPERIODLASTYEAR(DimDate[Date])
    )

measure yoy_revenue_growth = 
    DIVIDE([total_revenue] - [py_revenue], [py_revenue], 0)

measure revenue_cagr = 
    VAR Years = DISTINCTCOUNT(DimDate[Year])
    VAR StartValue = 
        CALCULATE(
            [total_revenue],
            FILTER(ALL(DimDate), DimDate[Year] = MIN(DimDate[Year]))
        )
    VAR EndValue = [total_revenue]
    RETURN
        IF(
            Years > 1,
            POWER(DIVIDE(EndValue, StartValue, 0), 1 / (Years - 1)) - 1,
            BLANK()
        )
```

## Step 2: Create the HTML Card Measure

Now comes the magic — a DAX measure that returns HTML:

```c
measure html_card_total_revenue = 
VAR Revenue = [total_revenue]
VAR PYRevenue = [py_revenue]
VAR YoYGrowth = [yoy_revenue_growth]
VAR CAGR = [revenue_cagr]

-- Calculate period growth (month-over-month by default)
VAR PeriodGrowth = 
    VAR PrevPeriod = 
        CALCULATE(
            [total_revenue],
            DATEADD(DimDate[Date], -1, MONTH)
        )
    RETURN
        DIVIDE(Revenue - PrevPeriod, PrevPeriod, 0)
-- Dynamic insight based on growth
VAR GrowthInsight = 
    SWITCH(
        TRUE(),
        YoYGrowth > 0.15, "Strong year-over-year momentum with " & FORMAT(YoYGrowth, "+0.0%") & " growth. Revenue trajectory significantly ahead of prior year.",
        YoYGrowth > 0.05, "Solid growth trajectory at " & FORMAT(YoYGrowth, "+0.0%") & " YoY. Performance tracking above market expectations.",
        YoYGrowth > -0.05, "Revenue relatively flat YoY (" & FORMAT(YoYGrowth, "0.0%") & "). Monitor for trend reversals and seasonal patterns.",
        "Revenue declining " & FORMAT(YoYGrowth, "0.0%") & " YoY. Immediate attention required to identify root causes and implement corrective measures."
    )
-- Period context (shows which time period we're looking at)
VAR MinDate = MIN(DimDate[Date])
VAR MaxDate = MAX(DimDate[Date])
VAR PeriodLabel = 
    IF(
        DATEDIFF(MinDate, MaxDate, DAY) <= 31,
        FORMAT(MinDate, "MMM YYYY"),
        FORMAT(MinDate, "MMM YYYY") & " – " & FORMAT(MaxDate, "MMM YYYY")
    )
RETURN
"<!DOCTYPE html>
<html>
<head>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
            background: transparent;
            overflow: hidden;
            width: 340px;
            height: 190px;
            perspective: 1000px;
        }
        .card-container {
            width: 100%;
            height: 100%;
            position: relative;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }
        body:hover .card-container {
            transform: rotateY(180deg);
        }
        .card-face {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.12);
            display: flex;
            flex-direction: column;
        }
        .card-front {
            background: linear-gradient(135deg, #0F766E 0%, #14B8A6 100%);
            color: white;
        }
        .card-back {
            background: linear-gradient(135deg, #134E4A 0%, #0F766E 100%);
            color: white;
            transform: rotateY(180deg);
        }
        .card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 16px;
        }
        .icon {
            font-size: 28px;
        }
        .card-label {
            font-size: 13px;
            font-weight: 600;
            letter-spacing: 0.5px;
            opacity: 0.95;
            text-transform: uppercase;
        }
        .main-value {
            font-size: 42px;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }
        .period-context {
            font-size: 12px;
            opacity: 0.85;
            margin-bottom: auto;
        }
        .footer-metrics {
            display: flex;
            gap: 16px;
            padding-top: 12px;
            border-top: 1px solid rgba(255,255,255,0.2);
        }
        .metric {
            flex: 1;
        }
        .metric-label {
            font-size: 9px;
            opacity: 0.75;
            margin-bottom: 3px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .metric-value {
            font-size: 15px;
            font-weight: 700;
        }
        .back-title {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
            opacity: 0.85;
            margin-bottom: 12px;
            text-transform: uppercase;
        }
        .insight-text {
            font-size: 11px;
            line-height: 1.6;
            opacity: 0.95;
            margin-bottom: auto;
        }
        .growth-positive { color: #A7F3D0; }
        .growth-negative { color: #FCA5A5; }
    </style>
</head>
<body>
    <div class='card-container'>
        <!-- FRONT -->
        <div class='card-face card-front'>
            <div class='card-header'>
                <div class='icon'>💰</div>
                <div class='card-label'>Total Revenue</div>
            </div>
            <div class='main-value'>" & FORMAT(Revenue / 1000000, "€0.0M") & "</div>
            <div class='period-context'>Total Sales (" & PeriodLabel & ")</div>
            <div class='footer-metrics'>
                <div class='metric'>
                    <div class='metric-label'>Period</div>
                    <div class='metric-value " & IF(PeriodGrowth >= 0, "growth-positive", "growth-negative") & "'>" & FORMAT(PeriodGrowth, "+0.0%;-0.0%") & "</div>
                </div>
                <div class='metric'>
                    <div class='metric-label'>CAGR</div>
                    <div class='metric-value'>" & FORMAT(CAGR, "0.0%") & "</div>
                </div>
                <div class='metric'>
                    <div class='metric-label'>YoY</div>
                    <div class='metric-value " & IF(YoYGrowth >= 0, "growth-positive", "growth-negative") & "'>" & FORMAT(YoYGrowth, "+0.0%;-0.0%") & "</div>
                </div>
            </div>
        </div>
        
        <!-- BACK -->
        <div class='card-face card-back'>
            <div class='back-title'>💡 Revenue Analysis</div>
            <div class='insight-text'>" & GrowthInsight & "</div>
            <div class='footer-metrics'>
                <div class='metric'>
                    <div class='metric-label'>This Period</div>
                    <div class='metric-value'>" & FORMAT(Revenue, "€#,##0") & "</div>
                </div>
                <div class='metric'>
                    <div class='metric-label'>Prior Year</div>
                    <div class='metric-value'>" & FORMAT(PYRevenue, "€#,##0") & "</div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"
```

**What’s happening here:**

1. **Variables** — We calculate all metrics first (Revenue, YoY, CAGR, etc.)
2. **Dynamic insight** — `GrowthInsight` uses SWITCH logic to generate contextual text based on performance
3. **HTML structure** — Two card faces: front (default view) and back (flip view)
4. **CSS animations** — `transform: rotateY(180deg)` On hover creates the flip effect
5. **Dynamic classes** — `.growth-positive` and `.growth-negative` apply green/red colors based on values

## Step 3: Add the Visual to Your Report

1. Insert the **HTML Content** visual onto your canvas
2. Drag `html_card_total_revenue` to the **Values** field
3. Resize to **340px width × 190px height** (exact dimensions matter for the design)
4. Format the visual:
- **Title:** OFF
- **Background:** Transparent
- **Border:** OFF

**That’s it.** Hover over the card, and watch it flip.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*KNLI2ndQ1W8VdqybeEcfPQ.gif)

The KPI Card

## Building the Other Three Cards

Now that you’ve mastered the Revenue card, the other three follow the same pattern. Here’s what they look like:

**💚 Card 2: Total Margin** (Green gradient)

- Front: €2.4M with 28.0% margin rate
- Back: Margin health assessment based on margin %
- Insight logic: “Exceptional/Strong/Solid/Pressure” based on thresholds

**💸 Card 3: Total Cost** (Amber gradient)

- Front: €6.2M with cost-to-revenue ratio
- Back: Cost efficiency analysis
- Insight logic: Flags when costs are compressing margins

**📊 Card 4: Transaction Volume** (Blue gradient)

- Front: 62.1K with daily average
- Back: Volume velocity and customer engagement insights
- Insight logic: Accelerating/Growing/Flat/Declining based on YoY

## Your Turn

The structure is identical for all four:

1. Calculate the metrics (value, YoY, CAGR, period growth)
2. Write SWITCH logic for dynamic insights
3. Build the HTML with front/back card faces
4. Change the gradient colors and icons

**Try building one yourself.** You’ve got the full template from the Revenue card — swap in your measures and adjust the colors.

## Want All Four Ready-Made?

If you’d rather not spend time adapting the code, **drop a comment below or DM me on** [**LinkedIn**](https://www.linkedin.com/in/bandyopadhyay-ankan/), and I’ll send you:

- All 4 complete HTML card measures
- The supporting DAX calculations (CAGR, YoY for each metric)
- The PBIX file with everything configured

I’m happy to share — but I promise you’ll learn more by building at least one yourself first.

## Quick Adaptation Guide

Want to use this for your own dataset? Here’s the 3-step formula:

**Step 1: Map Your Measures** Replace `[total_revenue]` with your equivalent (`[TotalSales]`, `[ARR]`, etc.)

**Step 2: Adjust Insight Thresholds.** The `SWITCH(TRUE(), ...)` statements need industry-specific thresholds:

- SaaS: 30%+ YoY = hypergrowth
- Retail: 10%+ YoY = strong
- Manufacturing: 5%+ YoY = solid

**Step 3: Change Colors** Update the CSS gradients to match your brand:

```c
.card-front {
    background: linear-gradient(135deg, #YourColor1 0%, #YourColor2 100%);
}
```

That’s it. The technique is universal — only the numbers and colors change.

## Common Issues (Quick Fixes)

**The card doesn’t flip smoothly**  
→ Resize visual to exactly 340×190px

**Insight text is cut off**  
→ Keep SWITCH text under 150 characters

**Animation doesn’t work on mobile**  
→ Expected — hover effects don’t work on touch devices

**Works in Desktop but not Service**  
→ Make sure HTML Content visual is installed in your tenant

## Get the Complete Package

Ready to add these to your reports?

**Comment below or DM me on** [**LinkedIn**](https://www.linkedin.com/in/bandyopadhyay-ankan/), and I’ll send you:

- ✅ All 4 HTML card measures (copy-paste ready)
- ✅ Supporting DAX calculations (YoY, CAGR for each metric)
- ✅ Complete PBIX file with sample data
- ✅ Color scheme variations (SaaS, retail, finance)

**But here’s my challenge to you:** Try building at least one card yourself first using the Revenue template above. You’ll learn 10x more by doing than by copying.

## Final Thoughts

Static KPI cards were fine in 2015. But in 2026, users expect more. They want context. They want insights. They want to **understand** the number, not just see it.

These flip-card KPIs deliver exactly that — simple on the front, insightful on the back.

And the best part? No custom visuals. No approval process. No waiting.

**Just DAX, HTML, and a willingness to push boundaries.**

*Enjoyed this? Follow me for more Power BI techniques that break the rules. Drop a comment if you build one of these — I’d love to see what you create!*

**#PowerBI #DAX #DataVisualization #HTML #BusinessIntelligence**

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----2905d65a1666---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization
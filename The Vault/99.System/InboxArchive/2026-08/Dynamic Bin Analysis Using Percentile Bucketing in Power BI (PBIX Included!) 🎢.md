---
title: "Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!) 🎢"
source: "https://medium.com/microsoft-power-bi/dynamic-bin-analysis-using-percentile-bucketing-in-power-bi-pbix-included-9109ec404b13"
author:
  - "[[Isabelle Bittar]]"
published: 2025-10-19
created: 2026-08-02
description: "How to build context-aware visuals that adapt to user filters — no static ranges, no loss of meaning."
Processed: "Unprocessed"
---
## How to build context-aware visuals that adapt to user filters — no static ranges, no loss of meaning.

![](99.System/Attachments/1!QnMeLrFabgOkSSvFXRFHyQ.png.webp)

By Isabelle Bittar for KI Data Science

*PBIX available at the end of this article! 🥳*

## 🧭 Introduction

I recently built an expense dashboard where one visual shows how invoices distribute across different amount ranges. The report was highly interactive — users could slice by **Department**, **Category**, **Period**, and more.

With **fixed bins** (“$0–10K”, “$10–25K”…), the ranges quickly became meaningless when users drilled into narrower slices. Some departments only had small invoices, while others had very large ones — so a static scale didn’t tell the real story anymore.

That’s why I explored **percentile-based bins** as an alternative. Instead of defining hardcoded ranges, the buckets are recalculated dynamically based on the actual distribution of the filtered data.

You can see in this short demo the visual in the cover image in action:

In the following article, I’ll walk you through how to build your own chart with **dynamic amount ranges** that automatically adjust to slicer selections. But before diving into the DAX details, let’s clarify what percentile bucketing means — and why it’s so useful for data analysis.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## 📊 What is Percentile Bucketing?

Percentile bucketing is a way of **dividing your dataset into equally sized groups based on data distribution** rather than fixed numerical thresholds.

For example, instead of splitting expenses into static bins like “$0–10K”, “$10K–25K”, and so on, you divide them into **percentiles**:

- The first 20% of transactions (the smallest invoices) form **Bin 1**
- The next 20% form **Bin 2**, and so on up to 100%

This means each bin represents **an equal portion of your data**, even if the actual dollar ranges vary.

In practice:

- A *20th percentile* value means *20% of the records are below that amount*.
- A *50th percentile* (median) is the value in the middle of your dataset.
- Higher percentiles (e.g., 80th, 90th, 95th) are often used to highlight outliers or top performers.

The advantage of percentile bucketing is that it adapts to your dataset’s **shape and scale**.  
When users filter data — say, to view only one department — the percentiles are **recomputed** for that subset, ensuring the bins always represent meaningful distribution ranges.

In other words, it’s a **context-aware approach** to categorization.  
No matter what filters are applied, each bar in your chart still represents *the same proportion* of the filtered dataset, giving users a fair way to compare segments across different contexts.

## 🗂️ Step 1: Getting Started — The Data at a Glance

![](99.System/Attachments/1!fT-VzGf3ue2SwV_r5YGSmw.png.webp)

Expenses Tables Loaded in Power BI

For this walkthrough I’m using a single fact table named **Expenses** with the following columns:

- `InvoiceID` (unique per invoice)
- `InvoiceDate` (date)
- `Department`, `Category`, `Region`, `Vendor`, `CostCenter` (text)
- `Amount` (currency)

Next, you need to create a disconnected “bucket” table. In my case, I created a quintiles calculated table (Modeling → New Table) that looked like the following:

![](99.System/Attachments/1!hB0Bza4NqC8kBsCbxU5-Nw.png.webp)

Calculated DAX Buckets Tables in Power BI

With these two tables, you can start computing the base measures that will support the computation of the percentile buckets.

## ⚙️ Step 2: Setting Up the Base DAX Measures

In our case, the dynamic bins are expense amounts. Here is the first core measure created:

```c
[Total Expense Amount] = SUM ( Expenses[Amount] )
```

Next, you can set up the dynamic percentile thresholds measures. These are recalculated after any filter (date, department, vendor…). They use **ALLSELECTED** so cross-filtering on the page still defines the distribution, but ignores the axis row.

```c
p20 Amount =
PERCENTILEX.INC (
    ALLSELECTED ( Invoices ),
    [Total Expense Amount],
    0.20
)

p40 Amount =
PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.40 )

p60 Amount =
PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.60 )

p80 Amount =
PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.80 )

p100 Amount =
PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 1.0 )

p0 Amount =
PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.0 )
```

### 🧠 Quick Note: Understanding PERCENTILE Functions in DAX

In Power BI, there are four percentile functions:

- `**PERCENTILE.INC**` **/** `**PERCENTILEX.INC**` → *Inclusive* percentile calculation.
- `**PERCENTILE.EXC**` **/** `**PERCENTILEX.EXC**` → *Exclusive* percentile calculation.

The key difference lies in **how the percentile is interpolated** at the boundaries of your data:

- **Inclusive (**`**INC**`**)** includes both the **0th** and **100th** percentiles — meaning the lowest and highest values in your data are considered valid percentile positions.
- **Exclusive (**`**EXC**`**)** excludes those extremes — so the 0th and 100th percentiles are undefined, and the calculation is based only on values between those limits.

For this dashboard, I used `**PERCENTILEX.INC**`, because I wanted the bins to always reflect the **entire range** of expense amounts — including the smallest and largest invoices. This ensures that when users apply filters or drill down, the percentile edges still adapt smoothly without clipping the extremes of the distribution.

Once the percentile amount measures are defined, you can create two additional measures to establish the **minimum and maximum values** of each range (for example: between 0–20%, 20–40%, 40–60%, etc.).

Here’s how these measures are defined:

```c
Bucket Min Amount = 
VAR idx = SELECTEDVALUE ( Buckets[BucketIndex] )
RETURN
SWITCH (
    TRUE(),
    idx = 1, [p0 Amount],
    idx = 2, [p20 Amount],
    idx = 3, [p40 Amount],
    idx = 4, [p60 Amount],
    idx = 5, [p80 Amount]
)

Bucket Max Amount = 
VAR idx = SELECTEDVALUE ( Buckets[BucketIndex] )
RETURN
SWITCH (
    TRUE(),
    idx = 1, [p20 Amount],
    idx = 2, [p40 Amount],
    idx = 3, [p60 Amount],
    idx = 4, [p80 Amount],
    idx = 5, [p100 Amount]
)
```

Once the ranges are set, you can calculate the **total number of invoices** and the **total amount** that fall within each bucket. These measures will feed the bar chart visual:

```c
Bucket Count (Invoices) :=
VAR lo = [Bucket Min Amount]
VAR hi = [Bucket Max Amount]
RETURN
COUNTROWS (
    FILTER (
        ALLSELECTED ( Invoices ),
        [Total Expense Amount] > lo && [Total Expense Amount] <= hi
    )
)

Bucket Total Amount ($) :=
VAR lo = [Bucket Min Amount]
VAR hi = [Bucket Max Amount]
RETURN
SUMX (
    FILTER (
        ALLSELECTED ( Invoices ),
        [Total Expense Amount] > lo && [Total Expense Amount] <= hi
    ),
    Invoices[Amount]
)
```

Finally, to display readable labels for each percentile range, create this measure:

```c
Bucket Label = 
VAR lo = FORMAT([Bucket Min Amount], "$#,0")
VAR hi = FORMAT([Bucket Max Amount], "$#,0")
RETURN 
lo & " – " & hi
```

With these measures ready, you now have everything you need to start building your **dynamic bar chart** — showing total invoice amounts (or counts) across **context-aware percentile buckets**.

## 🎨 Step 3: Building the Bar Chart Visual

Once all the measures are ready, you can move on to building the bar chart visual.  
This is where your percentile-based ranges come to life 🥳.

Start by inserting a **Bar Chart** visual (I used a **stacked bar chart**) and configuring it as follows:

- **X-axis:** `Buckets[BucketPct]`
- **Y-axis:** either
- `Bucket Total Amount ($)` — to show the total dollar value of invoices per range, or
- `Bucket Count (Invoices)` — to show how many invoices fall within each range.

At this stage, your chart will display something like this:

![](99.System/Attachments/1!1FoNG0khzqSkLQFYGp064Q.png.webp)

Inserting the Initial Stacked Bar Chart in Power BI

Next, you can turn off completely the Y-axis (values and title) and assign the `Bucket Label` measure to the data labels of the chart and the `Bucket Total Amount` measure to the Detail.

![](99.System/Attachments/1!66aSnN4fwIfMgckX2JbErQ.png.webp)

Changing the Display of the Percentile Buckets in the Bar Chart in Power BI

Finally, you can add any relevant slicers to test that the boundaries are recalculated each time a filter is applied.

![](99.System/Attachments/1!q7QkT41-iJNkrd9joMCgsA.png.webp)

This is the real strength 💪 of **percentile bucketing**: instead of defining one-size-fits-all intervals, your dashboard adapts dynamically to what users are looking at.

To make the visual even more polished, you can:

- Sort the bars by `Bucket Min Amount` to ensure they appear in the correct ascending order.
- Apply your **accent colors** to the **bars** using a measure. I created the measure `Bucket Color` that reads from different accent colors I had stored in other dax measures.
```c
_Color Primary = "#3631F9"

_Color Accent 1 = "#7285FE"

_Color Accent 2 = "#E3E9F0"

_Color Accent 3 = "#E9EDF2"

_Color Accent 4 = "#BCC7D9"

Bucket Color = 
SWITCH ( [Bucket Index],
    5, [_Color Primary],
    4, [_Color Accent 1],
    3, [_Color Accent 3],
    2, [_Color Accent 2],
    1, [_Color Accent 4]
)
```
- Change the `X-axis` for a **field parameter** to enable users to toggle between viewing invoices vs. amounts.
- Include **information** on **how the dynamic groupings work** to your users. In my case, I added in the style of an information tooltip:
![](99.System/Attachments/1!y4PEmNNjL1zC21tlrqr-Rg.png.webp)

Adding a Tooltip with Information on the Dynamic Groupings in Power BI

- In my case, I really wanted to recreated the **Y-Axis look**, so I added a table visual to the left of the bar chart and then hid the index column and table headers behind a shape.
![](99.System/Attachments/1!2i4fw11ohv24RrKIMAXrOw.png.webp)

Adding a Table Visual to Display the Bucket Labels on the Bar Chart Visual in Power BI

- I also integrate a periods selection (Last Week, Last Month, Last Year). You can view the detail of how I implemented this in my PBIX file. I also wrote the following article [**Power BI Time Hacks: Mastering Dynamic Date View**](https://medium.com/microsoft-power-bi/power-bi-time-hacks-mastering-dynamic-date-views-20c26275bd2e) where I describe in more detail how to implement this method:

## [Power BI Time Hacks: Mastering Dynamic Date Views](https://medium.com/microsoft-power-bi/power-bi-time-hacks-mastering-dynamic-date-views-20c26275bd2e?source=post_page-----9109ec404b13---------------------------------------)

### Unlock the Secrets to Flexible Daily, Weekly, Monthly Analysis in Your Dashboards

medium.com

Once formatted, the result is a clean, adaptive visual that summarizes invoice distributions across dynamic ranges — a powerful way to make financial data more intuitive.

## 💡 Ways You Can Take This Further

Once your percentile buckets are up and running, there are several ways you can make this visual even more powerful and interactive:

### 1\. Let users choose the number of buckets

You don’t have to stick with five fixed percentiles (0–20%, 20–40%, etc.). You can create a **dynamic selector** — for example, (another 😅) field parameter that lets users toggle between 5 or 10 buckets (using 0.1 increments instead of 0.2).

### 2\. Build rank-based tooltips

If you’re analyzing client revenue or project expenses, your tooltip could display where the current client ranks within the distribution (“Top 15% of spenders”) or how they compare to the median.  
This helps users interpret data at a glance without having to mentally calculate where something falls in the overall curve.

### 3\. Handle edge cases gracefully

Consider adding a “No Amount” or “Outlier” bucket to catch special cases — such as missing amounts, zero values, or extreme outliers.  
This ensures your chart always sums up to the total population and keeps the visual clean even when data quality issues or unusually large transactions occur.

### 4\. Combine percentile analysis with anomaly detection

If distribution analysis is central to your report, take it a step further by tracking **outliers and anomalies** directly within Power BI.  
I explored this approach in detail in a separate article — using Python’s Isolation Forest model to flag suspicious transactions without ever leaving Power Query:

## [🚨 How to Do Anomaly Detection in Power BI (No External Tools Needed!)](https://medium.com/the-bi-corner/how-to-do-anomaly-detection-in-power-bi-no-external-tools-needed-b12973e58b2b?source=post_page-----9109ec404b13---------------------------------------)

### A hands-on case study using Python and Isolation Forest — run entirely inside Power Query to flag suspicious employee…

medium.com

## 🎯 Conclusion

If you’ve ever built dashboards with fixed bins, you know how quickly they lose relevance once users start filtering the data.  
Dynamic percentile bucketing solves that — it keeps your visuals **context-aware**, so every range always makes sense for the slice you’re looking at.

With just a few DAX measures, you can turn a basic bar chart into an adaptive view of your data — one that helps users instantly see where values sit within their current selection.

As you build your own version, keep this in mind:

- 💡 **Flexibility = trust.** When charts respond to filters, users feel like the data reflects *their* questions.
- 📊 **Percentiles tell a story.** They highlight balance, spread, and extremes — without you having to explain the math.
- ✨ **Small touches go a long way.** Dynamic labels, adaptive colors, and intuitive tooltips make the visual feel alive.

Try it on your own dataset — whether it’s expenses, sales, or customer metrics — and see how much more meaningful your distributions become when they adapt to your users instead of forcing them to adapt to the chart.

**🎁 You can download my Power BI report with the visual from the cover picture of this article** [**here**](https://drive.google.com/file/d/1hTljtgjW2k0R78F5H5jvr8mDy3UK82gQ/view?usp=sharing)**.**

Thanks for sticking with me until the end 😅 — I hope you enjoyed this article and will get the opportunity to try this method on your projects! 🤓

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)

👏🏻 Clap 🔎 [Follow](https://isabittar.medium.com/) 📩 [Subscribe](https://isabittar.medium.com/subscribe) ✍🏻Comment

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----9109ec404b13---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualization, DAX

**Tags:** Tutorial, PBIX, Data Visualization, DAX
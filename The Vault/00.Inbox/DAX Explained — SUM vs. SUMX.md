---
title: "DAX Explained — SUM vs. SUMX"
source: "https://medium.com/microsoft-power-bi/dax-explained-sum-vs-sumx-c050fb6bb355"
author:
  - "[[Tomas Kutac]]"
published: 2025-12-14
created: 2026-08-12
description: "Why row context changes everything — and when iterators outperform simple aggregations"
Processed: "Unprocessed"
---
## Why row context changes everything — and when iterators outperform simple aggregations

Both functions **add up values**, but they work **very differently** — and knowing when to use which will save you hours of debugging and confusion.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xQEirKKoxkkj-MBBjVemyw.png)

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## SUM — Simple Aggregation

**SUM** just totals a column directly.

```c
Sales = 
SUM ( OrderItem[Sales] )
```

✅ **When to use:**

- You’re summing a **single column** of numeric values.
- You don’t need to do any row-by-row calculations.

💡 **Fastest and simplest** aggregation in DAX.

## SUMX — Row-by-Row Evaluation

**SUMX** is more powerful — it goes **row by row** through a table, performs a calculation for each row, then adds them up.

```c
Sales Net = 
SUMX (
    OrderItem,
    OrderItem[Sales]
        / (
            1 + RELATED ( Provisions[Provision] )
        )
)
```

✅ **When to use:**

- You need to **calculate something per row** before summing it up.
- The value you’re summing **isn’t stored directly** in a single column.

💡 Think of `SUMX()` as “Sum **expression** across rows.”

Both functions are explained in detail in this video:

## ⚡ Pro Tips:

✅ If your column is already a calculated value in the data, use `SUM()`.  
✅ If you need to multiply, divide, or apply conditions per row — use `SUMX()`.  
✅ `SUMX()` can work over **any table expression**, not just a table from your model.

> 👉 See the example Power BI report [**here**](https://app.powerbi.com/view?r=eyJrIjoiZjRhNDQyMmUtYzcxOS00MmUxLTk5NDUtYjIyOTQ5ZmEwYTk5IiwidCI6Ijk0N2I1YTllLTZmYjUtNDM1Yi04NGMxLTQwYjYyYTRkZGNlNyIsImMiOjl9&pageName=c976cb0ed457e744ba81).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ukhodGYpmff9qjX_G9znJw.png)

## [Tomas Kutac - Medium](https://tomaskutac.medium.com/subscribe?source=post_page-----c050fb6bb355---------------------------------------)

### Read writing from Tomas Kutac on Medium. IT Manager, Data Analyst, Power BI, and Personal Growth enthusiast…

tomaskutac.medium.com

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----c050fb6bb355---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX
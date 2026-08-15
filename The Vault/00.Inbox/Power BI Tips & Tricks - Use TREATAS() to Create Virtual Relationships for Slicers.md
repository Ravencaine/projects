---
title: "Power BI Tips & Tricks - Use TREATAS() to Create Virtual Relationships for Slicers"
source: "https://medium.com/@tomaskutac/power-bi-tips-tricks-use-treatas-to-create-virtual-relationships-for-slicers-699934b9f5ad"
author:
  - "[[Tomas Kutac]]"
published: 2026-03-28
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RNioZblK4o61ZYfhr_6upw.png)

You’ve got a disconnected table (maybe a “what-if” parameter table, a custom filter table, or a mapping table) and you want it to filter your visuals.

The common instinct is to create a relationship. But sometimes that breaks your model or creates ambiguity.

Enter TREATAS().

It lets you apply filter values from one column as if they came from another column — no physical relationship needed.

```c
Filtered Sales =
CALCULATE (
    [Total Sales],
    TREATAS (
        VALUES ( MyFilter[Year] ),
        Date[Year]
    )
)
```

When to use this:

- Disconnected slicer tables that need to filter your model
- “What-if” parameter scenarios
- When adding a relationship would create ambiguity or a many-to-many mess

When NOT to use it:

- If a clean, direct relationship is possible, always prefer that first TREATAS() is one of those functions that feels like a workaround until you realize it’s actually the cleanest solution for certain patterns.

👉 [**Learn more about TREATAS()**](https://chatgpt.com/g/g-68554431f9608191b9b40505c423fc6e-power-bi-coach-and-assistant?prompt=Explain+TREATAS)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----699934b9f5ad---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tips & Tricks, DAX
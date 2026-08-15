---
title: "UNION-based alternative to SWITCH in Power BI DAX"
source: "https://medium.com/microsoft-power-bi/union-based-alternative-to-switch-in-power-bi-dax-0c1658f137cd"
author:
  - "[[Mateusz Mossakowski]]"
published: 2026-03-05
created: 2026-08-12
description: "Today I wanted to showcase an alternative to the well-respected SWITCH approach. The new kid on the block is an on-the-fly UNIONed table that is FILTERed later. It is not the holy grail you should blindly use to replace any SWITCH use cases. Quite the opposite. You should use the new approach only in specific scenarios where this optimization technique really shines."
Processed: "Unprocessed"
---
## Today I wanted to showcase an alternative to the well-respected SWITCH approach. The new kid on the block is an on-the-fly UNIONed table that is FILTERed later. It is not the holy grail you should blindly use to replace any SWITCH use cases. Quite the opposite. You should use the new approach only in specific scenarios where this optimization technique really shines.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0H8Q44Xhfp6_boC_DOUmGg.png)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

### Background:

This is a quite common scenario. There is a need to present measures that are grouped. To some extent you can achieve it through fields parameters, but there is always a “but”. That’s why it’s usually better to stick with a good old disconnected helper table.

As a cherry on top, you can add a format string column to the helper table, so you don’t format the numbers themselves. Instead you use this extra column in the dynamic format string.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*WZ9jagtnQcMtADdF65Tcfg.png)

helper table

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*B5c02G1iNSWP0lXmjUV5ZQ.png)

dynamic format string

### SWITCH

The natural reaction to such a scenario for almost all Power BI developers would be to use the SWITCH function, but if you read a couple more paragraphs, you can learn an alternative approach 😊

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jk5sz94LoBzUMuVq7amGMg.png)

regular SWITCH approach

### UNION

The alternative is to

- build an on-the-fly UNIONed table,
- filter it to a specific measure from the context,
- for this record retrieve the value field of the dynamic table.
![](https://miro.medium.com/v2/format:webp/1*0H8Q44Xhfp6_boC_DOUmGg.png)

### When should you use the alternative, and when should you use the regular approach?

To answer this, I ran cold-cache DAX performance checks in six scenarios (the number of measures in our helper table). Each test used a different number of selected measures, from one to six (all). I ran the exact same tests on two semantic models: one with six million records in the fact table and another with one billion records. The findings were very consistent across both models.

The general rule of thumb is: consider the UNION approach when you need all measures from the helper table always visible in your matrix. If you allow end users to select specific measures or group of measures, you should stick with the regular SWITCH. The fewer measures we operate on, the more both the formula engine and the storage engine benefit from SWITCH optimizations.

Explanation: In the UNION approach, the engine needs to evaluate every measure before filtering a specific measure. This works really well when we truly need the whole set of measures (you can see that both the storage engine duration and the storage engine query count does not differ regardless of how many measures are selected). However, the fewer measures we query, the more unnecessary pre-processing there is for measures that we won’t ultimately use. The formula engine duration of the UNION approach decreases as the number of “queried” measures decreases, but the pace is immensely slower than the decrease in the case of the regular SWITCH approach.

Plain DAX definition of the Union measure making it easier for you to copy 🙃

```c
Union = 
VAR _measure = SELECTEDVALUE(helper_table[measure_name])
VAR _table =
UNION(
    ROW( "@measure", "Revenue", "@value", [Revenue]),
    ROW( "@measure","Revenue YA", "@value", [Revenue YA]),
    ROW( "@measure","Revenue YoY %", "@value", [Revenue YoY %]),
    ROW( "@measure","Tax Amt", "@value", [Tax Amt]),
    ROW( "@measure","Tax Amt YA", "@value", [Tax Amt YA]),
    ROW( "@measure","Tax Amt YoY %", "@value", [Tax Amt YoY %])
)
VAR _filtered_table = FILTER(_table, [@measure] = _measure)
VAR _result = MAXX(_filtered_table, [@value])
RETURN _result
```

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----0c1658f137cd---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** DAX

**Tags:** Tutorial, DAX
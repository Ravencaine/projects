---
title: "Power BI Tips & Tricks — Use KEEPFILTERS to Preserve Context in CALCULATE"
source: "https://medium.com/microsoft-power-bi/power-bi-tips-tricks-use-keepfilters-to-preserve-context-in-calculate-e8bac1eef120"
author:
  - "[[Tomas Kutac]]"
published: 2026-04-03
created: 2026-08-12
description: "How one DAX modifier fixes the most common CALCULATE misunderstanding — and why your slicers will thank you."
Processed: "Unprocessed"
---
## How one DAX modifier fixes the most common CALCULATE misunderstanding — and why your slicers will thank you.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KUUyQf_Pjm0FkaQYxesHNA.png)

If you’ve ever written a CALCULATE expression with a filter argument and wondered why your slicers seem to have no effect, you’ve run into one of DAX’s most misunderstood behaviors: filter replacement.

### The default behavior

When you write something like this:

```c
Sales Red =
CALCULATE (
    [Total Sales],
    Product[Color] = "Red"
)
```

CALCULATE doesn’t *add* the “Red” filter on top of whatever context already exists on Product\[Color\]. **It *replaces* it entirely**. If a user has selected “Blue” in a slicer, that selection gets overwritten. The measure returns Red sales no matter what.

For some use cases — like a **fixed benchmark** — that’s exactly what you want. But more often, it leads to confusing report behavior where slicers appear to be broken.

### Enter KEEPFILTERS

KEEPFILTERS is a modifier function that changes this behavior. Instead of replacing the existing filter context, it intersects with it:

```c
Sales Red =
CALCULATE (
    [Total Sales],
    KEEPFILTERS ( Product[Color] = "Red" )
)
```

Now the logic works differently. If the slicer is set to “Red,” the intersection produces “Red” — and you get Red sales. If the slicer is set to “Blue,” the intersection of “Blue” and “Red” **is empty** — and the measure returns **BLANK**. That’s almost always the more intuitive behavior.

### When to use it

A good rule of thumb: if your CALCULATE filter is on a column that’s also exposed to the user through a slicer or row/column header in a visual, consider wrapping it in KEEPFILTERS. It ensures your measure respects the user’s selections rather than silently overriding them.

The exception is when you **intentionally want to override context** — for example, creating an “All Products” benchmark measure that always returns the total regardless of selection. In that case, the default replacement behavior is correct.

### A quick mental model

Think of it this way: without KEEPFILTERS, CALCULATE says “ **forget what the user picked, use my filter instead**.”

With KEEPFILTERS, CALCULATE says “ **use my filter, but only where it agrees with what the user already picked.**”

That one-word addition can be the difference between a report that confuses stakeholders and one that behaves exactly as expected.

👉 [**Learn more about KEEPFILTERS() with our Power BI Coach and Assistant**](https://chatgpt.com/g/g-68554431f9608191b9b40505c423fc6e-power-bi-coach-and-assistant?prompt=Explain+KEEPFILTERS%28%29)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----e8bac1eef120---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tips & Tricks, DAX
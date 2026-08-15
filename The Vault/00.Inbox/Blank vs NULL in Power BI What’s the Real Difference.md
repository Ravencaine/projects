---
title: "Blank vs NULL in Power BI: What’s the Real Difference?"
source: "https://medium.com/write-a-catalyst/blank-vs-null-in-power-bi-whats-the-real-difference-2e9a601e794b"
author:
  - "[[Anurodh Kumar]]"
published: 2025-05-28
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WitHxR7x11F8LecoFQuWeQ.png)

image by Anurodh Kumar

If you’ve spent any time working with Power BI, you’ve likely come across Blank values in DAX and NULL values in Power Query or your data source. At a glance, they might seem like the same thing — both represent missing or empty data, right? Not quite.

Let’s dive into what sets them apart — and why it matters.

## What is NULL?

In the world of Power Query (or SQL databases), NULL simply means “no data” or “unknown.”

Think of it like an empty cell in an Excel sheet that hasn’t been filled out yet. It’s a placeholder for “nothing here.”

In Power Query, null is a primitive value that you can check or replace using M code. For example:

```c
= Table.ReplaceValue(Source, null, "Unknown", Replacer.ReplaceValue, {"CustomerName"})
```

## What is BLANK()?

When the data reaches the Power BI data model and you’re working with DAX, NULL values get converted to Blank.

In DAX, Blank is a special value returned by the BLANK() function. It plays a role in both logic and calculations.

**Example:**

```c
NewColumn = IF([Sales] = 0, BLANK(), [Sales])
```

Now your visuals won’t show 0s — they’ll show empty cells instead.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*LHg25ZLNWmENLtR0)

## Why It Matters

- In Power Query, you should clean and replace null values early to avoid downstream issues.
- In DAX, use BLANK() carefully — it can affect totals, averages, and logic in unexpected ways.
- Don’t assume BLANK() = 0 — they are not the same, though they can behave similarly in some math operations.

*Handling missing data correctly is critical to building reliable Power BI reports. Knowing when you’re dealing with a Blank or a NULL can help you choose the right function and avoid mysterious gaps or miscalculations in your visuals.*

*So next time you see an empty value in Power BI, take a second look. Is it a null, or is it BLANK()? The answer might just save you from a debugging headache.*
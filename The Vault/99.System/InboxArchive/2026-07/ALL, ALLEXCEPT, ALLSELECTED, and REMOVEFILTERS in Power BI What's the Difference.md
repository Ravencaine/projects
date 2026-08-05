---
title: "ALL, ALLEXCEPT, ALLSELECTED, and REMOVEFILTERS in Power BI: What’s the Difference?"
source: "https://medium.com/write-your-world/all-allexcept-allselected-and-removefilters-in-power-bi-whats-the-difference-9a088a60a95e"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2025-09-19
created: 2026-07-27
description: "These four DAX functions look similar but behave differently. Here’s a simple guide with examples and visuals to clear the confusion."
Processed: "Unprocessed"
---
## These four DAX functions look similar but behave differently. Here’s a simple guide with examples and visuals to clear the confusion.

## Introduction: Why These Functions Confuse Everyone

If you’ve ever tried to calculate **percent of total sales** or adjust filters in Power BI, you’ve likely used `ALL()`, `ALLEXCEPT()`, `ALLSELECTED()`, or `REMOVEFILTERS()`.

On the surface, they look similar:

- They all “remove” or “control” filters.
- They’re all used inside CALCULATE.

But in practice, they behave very differently — and choosing the wrong one can give you completely wrong numbers.

In this post, we’ll break them down with **examples, visuals, and practical use cases**.

## 1\. ALL()

**Definition:** Removes all filters from the specified column or table.

Example:

```c
All Sales = CALCULATE( SUM(Sales[Revenue]), ALL(Sales[Region]) )
```
- Ignores any slicer/filter on Region.
- Useful for **percent of total** calculations.
![](99.System/Attachments/1!6yZs9laM-rVrV80OOv9P2g.png.webp)

ALL removes filters from a column/table, returning values as if no filter existed.

## 2\. ALLEXCEPT()

**Definition:** Removes all filters *except* the ones you specify.

Example:

```c
Sales by Year = CALCULATE( SUM(Sales[Revenue]), ALLEXCEPT(Sales, Sales[Year]) )
```
- Removes all filters except Year.
- Keeps grouping by Year while ignoring others like Region/Product.
![](99.System/Attachments/1!faUep3aqYG0WLqaDl1tRtQ.png.webp)

ALLEXCEPT keeps one filter (like Year) while removing the rest.

## 3\. ALLSELECTED()

**Definition:** Removes filters from a column/table but keeps **report-level selections** (outer filters).

Example:

```c
Percent of Subtotal = 
DIVIDE( 
 SUM(Sales[Revenue]), 
 CALCULATE( SUM(Sales[Revenue]), ALLSELECTED(Sales[Region])) 
)
```
- Respects report selection but ignores inner filters.
- Useful for **percent of subtotal** (like showing “% of selected regions”).
![](99.System/Attachments/1!15yRaRpm7gDVEHGwbmIGLw.png.webp)

ALLSELECTED respects report-level filters but clears inner filters in visuals.

## 4\. REMOVEFILTERS()

**Definition:** Newer, cleaner way to remove filters from columns/tables.

Example:

```c
All Region Sales = CALCULATE( SUM(Sales[Revenue]), REMOVEFILTERS(Sales[Region]) )
```
- Equivalent to ALL, but simpler.
- Recommended for clarity in most cases.
![](99.System/Attachments/1!69DfZ7tohdjZIO6l0UeODQ.png.webp)

REMOVEFILTERS is a simpler alternative to ALL for clearing filters.

![](99.System/Attachments/1!zQ6QE5Qkb-kLpsNqqqiZrQ.png.webp)

comparison table for ALL vs ALLEXCEPT VS ALLSELECTED VS REMOVEFILTERS

## Best Practices

- ✅ Use `ALL` when you want percent of total.
- ✅ Use `ALLEXCEPT` when you want to keep one dimension (like Year).
- ✅ Use `ALLSELECTED` for percent of subtotal or cumulative totals.
- ✅ Use `REMOVEFILTERS` for modern, cleaner code.
- ⚠ Don’t mix them randomly — choose based on the business logic.

## Closing Thought

These four functions control how filters behave in your calculations.

The next time your DAX measure looks wrong, ask:  
👉 *“Do I need to remove all filters, keep some, respect selections, or just clear one column?”*

Mastering these will make your **percent of total, YTD, and custom KPIs** bulletproof.
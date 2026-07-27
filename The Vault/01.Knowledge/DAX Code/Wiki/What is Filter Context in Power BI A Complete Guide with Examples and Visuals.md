---
created: 2026-07-27
source: "What is Filter Context in Power BI? A Complete Guide with Examples and Visuals"
source_url: https://medium.com/write-your-world/what-is-filter-context-in-power-bi-a-complete-guide-with-examples-and-visuals-3cdab77a2c83
note_type: source
tags: [dax-code]
---

## Filter context controls every calculation in DAX. Here’s a simple, visual guide to mastering it with real-world examples in Power BI.

## Introduction: Why Filter Context Matters

If you’ve ever wondered why your measure in Power BI shows different results when you slice by Region, Date, or Product, the answer is **Filter Context**.

Filter context is what makes DAX powerful — but also what makes it confusing.

- Why does `SUM(Sales[Revenue])` give one value on the total line and different values per region?
- Why does CALCULATE change results even when you didn’t change the formula?
- Why do filters in visuals or slicers impact your measures?

Understanding **filter context** is the key to answering all of these questions.

## What is Filter Context?

At its core:

👉 **Filter context is the set of filters applied to evaluate a DAX expression.**

These filters can come from:

- Slicers in your report.
- Rows and columns in visuals.
- Relationships between tables.
- Functions like CALCULATE or FILTER.

## Example 1: Simple SUM

```c
Total Sales = SUM(Sales[Revenue])
```
- Without any slicer → returns total revenue.
- With Region slicer = “North” → only sums rows where Region = North.

## How Filter Context Works in Visuals

Imagine a table with Region and Total Sales.

- For Region = North → DAX sees a filter where Region = “North”.
- For Region = South → DAX sees Region = “South”.
- For the Total row → no filter, so it sums across all regions.

Filter context narrows down the rows before the calculation happens.

## CALCULATE: Changing the Filter Context

The most important function in DAX is **CALCULATE** — because it **modifies filter context**.

Example:

```c
North Sales = CALCULATE( SUM(Sales[Revenue]), Sales[Region] = “North” )
```
- No matter what slicer you use, this measure always returns Sales for North only.
- CALCULATE overrides the existing filter context.

CALCULATE doesn’t just sum — it rewrites the filter context before running the formula.

Example 2: Multiple Filters

```c
Sales 2024 = CALCULATE( SUM(Sales[Revenue]), Sales[Year] = 2024 )
```
- Adds a filter → Year = 2024.
- Works alongside slicers (e.g., Region = North).
- Final context = Region = North AND Year = 2024.

When multiple filters are applied (slicers + CALCULATE), they combine to form the final filter context.

## Filter Context vs Row Context

- **Row Context** = one row at a time (used in calculated columns).
- **Filter Context** = subset of rows defined by filters (used in measures).

👉 Key point: **Filter Context can exist without Row Context, but Row Context often becomes Filter Context via CALCULATE (context transition).**


Row context evaluates one row at a time, while filter context defines a subset of rows for evaluation.

## Why Filter Context Confuses Beginners

1. Visual totals don’t always equal sum of rows (because of different contexts).
2. CALCULATE changes context silently.
3. Multiple filters combine (like slicer + CALCULATE).

👉 Once you realize DAX always asks: *“What rows are in context right now?”* → it clicks.

## Key Takeaways (Scannable Section)

- ✅ Filter Context = the filters applied to evaluate a DAX expression.
- ✅ Comes from slicers, visuals, relationships, and DAX functions.
- ✅ CALCULATE changes filter context before evaluation.
- ✅ Understanding it is essential for building correct measures.

## Closing Thought

Every DAX calculation is simply:

👉 *“Take the current filter context, then run the formula.”*

Once you understand that, debugging DAX becomes far easier.

Next time your measure looks wrong, ask: **“What filter context is active right now?”**

Power BI, DAX, Business Intelligence, Data Analytics, Data Science

> See also [[all]] for reference.


> See also [[calculate]] for reference.


> See also [[context-transition-with-calculate]] for reference.


> See also [[dax-context]] for reference.


> See also [[filter-context-vs-row-context]] for reference.


> See also [[measures-vs-calculated-columns]] for reference.

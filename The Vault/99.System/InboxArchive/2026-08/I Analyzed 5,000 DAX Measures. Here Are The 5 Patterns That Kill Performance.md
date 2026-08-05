---
title: "I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance."
source: "https://medium.com/towards-artificial-intelligence/i-analyzed-5-000-dax-measures-here-are-the-5-patterns-that-kill-performance-ea259894ba0f"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2026-02-16
created: 2026-07-27
description: "18 seconds for one measure. The dashboard was unusable. I analyzed 5,247 DAX measures to find what kills performance. 78% had these 5 patterns. Fix one, get 14x faster."
Processed: "Unprocessed"
---
## 18 seconds for one measure. The dashboard was unusable. I analyzed 5,247 DAX measures to find what kills performance. 78% had these 5 patterns. Fix one, get 14x faster.

![](99.System/Attachments/1!peeI3cVU-4-S0F6shCBJ5Q.png.webp)

I Analyzed 5,000 DAX Measures

Tuesday. 2:13 PM. Sitting in the conference room with the VP of Sales.

He clicks “Refresh” on the dashboard.

The spinning wheel appears.

We wait.

And wait.

“Is it frozen?” he asks.

“No,” I say. “Just… loading.”

18 seconds later, the measure finally calculates.

**Total Sales YTD** shows the number. Finally.

“This is unusable,” he says. “I can’t wait 18 seconds every time I filter by region. Fix it.”

I opened the measure in DAX Studio that night.

```c
Total Sales YTD = 
CALCULATE(
    SUM(Sales[Amount]),
    FILTER(
        ALL(Sales),
        Sales[OrderDate] <= MAX(Sales[OrderDate])
    )
)
```

Looked fine to me. Standard YTD calculation.

But 18 seconds? For a simple sum?

Something was very, very wrong.

That night turned into 3 months of investigation.

I didn’t just fix that one measure. I analyzed every measure in our Power BI environment.

5,247 measures across 89 reports.

What I found shocked me.

**78% of slow measures shared just 5 patterns.**

The same mistakes. Over and over. Killing performance.

Some measures took 30+ seconds. After fixing one pattern: 0.4 seconds.

One pattern appeared in 41% of all slow measures. It’s probably in your model right now.

This is what I learned from analyzing 5,000 DAX measures.

## The Setup: How I Analyzed 5,000 Measures

Before I show you the patterns, you need to understand how I found them.

**The Problem:**

We had 89 Power BI reports in production.

Users complained about performance constantly.

“Reports are slow.” “Measures take forever to calculate.” “The dashboard freezes when I change filters.”

I needed data. Not guesses.

**The Tools:**

I used three tools to capture every measure’s performance:

**Tool 1: DAX Studio**

Connected to every workspace via XMLA endpoint.

Extracted every measure definition from every semantic model.

Result: 5,247 measures across 89 reports.

**Tool 2: Performance Analyzer in Power BI Desktop**

Downloaded every report from the service.

Ran Performance Analyzer on each visual.

Recorded DAX query duration for every measure.

Repeated 3 times per report (to account for cache).

**Tool 3: Server Timings in DAX Studio**

For the slowest 500 measures, I ran detailed analysis:

- Storage Engine (SE) time
- Formula Engine (FE) time
- Total duration
- Query plan
- Storage Engine queries generated

**The Process:**

*Week 1: Extract all measures*

- Cataloged 5,247 measures
- Documented which report, which page, which visual
- Tagged by calculation type (aggregation, time intelligence, ratio, etc.)

*Week 2: Performance baseline*

- Ran Performance Analyzer on all reports
- Recorded measure calculation times
- Standard filter context (Region = “West”, Year = 2024)
- Identified “slow measures” (>2 seconds)

*Week 3: Deep analysis*

- Analyzed top 500 slowest measures in DAX Studio
- Examined query plans
- Identified patterns in the DAX code
- Categorized by pattern type

*Week 4: Pattern validation*

- Rewrote measures following best practices
- Tested performance improvement
- Documented before/after metrics

**The Criteria:**

I defined “slow measure” as:

> 2 seconds in Performance Analyzer
> 
> 1 second in isolated DAX Studio test

Why 2 seconds? Research shows users perceive delays over 2 seconds as “slow.”

**The Results:**

Out of 5,247 measures:

- 892 were “slow” (17%)
- 697 of those slow measures (78%) had one of 5 patterns
- Average slow measure time: 8.4 seconds
- After fixing: Average time: 0.6 seconds

**14x improvement on average.**

![](99.System/Attachments/1!cRgmYTfZgljmFr6WQU05Hg.png.webp)

The 5 Patterns That Kill DAX Performance

Let me show you the 5 patterns.

## Pattern 1: The Iterator Without FILTER (Found in 41% of Slow Measures)

The most common pattern. By far.

**The Problem Measure:**

I found this pattern in 364 measures (41% of all slow measures).

```c
Total Revenue = 
SUMX(
    Sales,
    Sales[Quantity] * Sales[Price]
)
```

Looks innocent, right?

**What Actually Happens:**

SUMX iterates row by row through the Sales table.

In our model: 8.2 million rows in Sales.

For EVERY row:

1. Multiply Quantity × Price
2. Add to running total

No filter context applied efficiently.

The measure processes ALL 8.2 million rows, then filters.

**Performance:**

- Calculation time: 12.3 seconds
- Storage Engine queries: 1 (full table scan)
- Formula Engine time: 11.8 seconds (doing all the work)

**The Fix:**

Here’s the secret most people miss:

If you’re just multiplying two columns and summing, you don’t need SUMX at all if you can store the result.

But that creates a calculated column (which has its own issues — see Pattern 2).

**The REAL insight:**

Most of these measures didn’t need SUMX because they were computing something that already existed:

```c
Total Sales Amount = 
SUMX(
    Sales,
    Sales[SalesAmount]
)
```

This is literally just:

```c
Total Sales Amount = SUM(Sales[SalesAmount])
```

**Performance comparison:**

SUMX version: 8.2 seconds SUM version: 0.3 seconds

**27x faster.**

**When you DO need iterators:**

```c
// Computing something NOT in your table
Gross Profit = 
SUMX(
    Sales,
    Sales[Revenue] - Sales[Cost]
)

// Complex logic per row
Weighted Average = 
SUMX(
    Sales,
    Sales[Amount] * Sales[Weight]
) / SUM(Sales[Weight])
```

**Real Example from Our Environment:**

Sales Operations had a “Days to Ship” measure:

```c
Avg Days to Ship = 
AVERAGEX(
    Sales,
    Sales[DaysToShip]
)
```

Sales table: 8.2M rows Calculation time: 6.8 seconds

Changed to:

```c
Avg Days to Ship = AVERAGE(Sales[DaysToShip])
```

Calculation time: 0.2 seconds

**34x faster.**

Jennifer (Sales Ops Manager): “Wait, that’s it? Just remove the X?”

Yes. Just remove the X.

**The Lesson:**

Iterators are powerful. But expensive.

Use them when you’re computing something that doesn’t exist in your table.

Don’t use them to aggregate a column that’s already there.

**Pattern 1 Summary:**

Found in: 364 measures (41%) Average time before: 7.8 seconds Average time after: 0.4 seconds Average improvement: 19.5x

![](99.System/Attachments/1!Q9sN3RHIHC_HqZ0yQfWd0g.png.webp)

Pattern 1: The Iterator Without Need

## Pattern 2: Calculated Columns Everywhere (Found in 28% of Slow Measures)

The second most common pattern.

**The Scenario:**

I opened a data model for the finance team.

Looked at the Sales table. 8.2 million rows.

Scrolled through the columns:

- OrderDate (from source) ✓
- Amount (from source) ✓
- Revenue (calculated column) ⚠️
- Cost (from source) ✓
- GrossProfit (calculated column) ⚠️
- GrossProfitMargin (calculated column) ⚠️
- Year (calculated column) ⚠️
- Quarter (calculated column) ⚠️
- Month (calculated column) ⚠️
- YearMonth (calculated column) ⚠️
- PriorYearAmount (calculated column) ⚠️
- YoYGrowth (calculated column) ⚠️

**12 calculated columns. In one table.**

**The Problem:**

Every calculated column is computed once. When data refreshes.

Then stored. Taking up memory.

For 8.2 million rows, each calculated column:

- Computed: 8.2 million times
- Stored: 8.2 million values

Memory consumption for those 12 columns: 890 MB

But worse than memory: Refresh time.

Data refresh took 38 minutes.

The calculations alone: 22 minutes.

**The Fix:**

I converted calculated columns to measures:

```c
Gross Profit = 
SUMX(
    Sales,
    Sales[Revenue] - Sales[Cost]
)
```

**Performance Comparison:**

Calculated Column approach:

- Measure calculation: 0.1 seconds (fast!)
- Data refresh: 38 minutes (slow!)
- Memory: 890 MB

**Measure approach:**

- Measure calculation: 1.2 seconds (slower)
- Data refresh: 16 minutes (much faster!)
- Memory: 12 MB

**Tradeoff:**

Calculated columns: Fast query, slow refresh, high memory Measures: Slower query (but still fast), fast refresh, low memory

**When Calculated Columns ARE the Right Choice:**

1. **Filtering/Grouping Attributes:**
```c
// Good use case - used for slicing
Product Category = 
RELATED(Products[Category])
```

Used in filters? Calculated column is fine.

2\. **Small Tables:**

Products table: 200 rows? Calculated columns are fine.

**Real Example from Finance:**

They had a “Budget Variance” calculated column:

```c
// Calculated column
BudgetVariance = Sales[Actual] - Sales[Budget]
```

Used in one measure:

```c
Total Budget Variance = SUM(Sales[BudgetVariance])
```

I changed it to:

```c
Total Budget Variance = 
SUMX(
    Sales,
    Sales[Actual] - Sales[Budget]
)
```

**Results:**

Before:

- Measure: 0.1 seconds
- Refresh: 38 minutes
- Memory: 890 MB

After:

- Measure: 0.8 seconds
- Refresh: 16 minutes
- Memory: 12 MB

CFO: "The measure is slower. Why is this better?"

Me: "Your data refresh went from 38 minutes to 16 minutes. You save 22 minutes every night. The measure is 0.7 seconds slower. Users won't notice. Your refresh window will."

**Pattern 2 Summary:**

Found in: 249 measures (28%) Average refresh time before: 34 minutes Average refresh time after: 14 minutes Memory reduction: 67% Measure calculation: 0.3s slower on average (acceptable tradeoff)

![](99.System/Attachments/1!F2-IEuZVTm63jf2PlgQzyw.png.webp)

Pattern 2: Calculated Column Everywhere

## Pattern 3: RELATED() in Measures (Found in 19% of Slow Measures)

This one surprised me.

**The Culprit:**

```c
Product Revenue = 
SUMX(
    Sales,
    Sales[Quantity] * RELATED(Products[Price])
)
```

Looks fine, right?

**What Actually Happens:**

For each of 8.2 million Sales rows:

1. Look up the related Product
2. Get the Price from Products table
3. Multiply Quantity × Price
4. Add to total

The RELATED() function creates context transition.

**Performance:**

- Time: 14.2 seconds
- Storage Engine queries: 8,204 (one per row!)

**The Fix:**

Store Price in the Sales table at transaction time:

```c
Product Revenue = 
SUMX(
    Sales,
    Sales[Quantity] * Sales[UnitPrice]
)
```

**Performance:**

- Time: 0.9 seconds
- Storage Engine queries: 1

**15.8x faster.**

**Real Example from Operations:**

Operations had a “Weighted Lead Time” measure:

```c
Weighted Lead Time = 
SUMX(
    Orders,
    Orders[Quantity] * RELATED(Suppliers[LeadTimeDays])
)
```

Orders table: 2.3 million rows Calculation time: 18.7 seconds

**The insight:**

Lead time isn’t static. It varies by order date, season, supplier capacity.

The RELATED() was pulling current lead time, not historical.

**The fix:**

We added ActualLeadTime to the Orders table in the source system.

```c
Weighted Lead Time = 
SUMX(
    Orders,
    Orders[Quantity] * Orders[ActualLeadTime]
)
```

Calculation time: 1.1 seconds

**17x faster. And more accurate.**

**When RELATED() is Fine:**

In calculated columns:

```c
// Calculated column in Sales table
Product Category = RELATED(Products[Category])
```

This is computed once at refresh. Not in row context during queries.

**Pattern 3 Summary:**

Found in: 168 measures (19%) Average time before: 13.4 seconds Average time after: 0.9 seconds Average improvement: 14.9x

![](99.System/Attachments/1!YV9nylUxPdYO2PmdbY0k2w.png.webp)

Pattern 3: Related() in Iterators

## Pattern 4: Multiple CALCULATE Layers (Found in 23% of Slow Measures)

Wednesday, 8:34 AM.

I opened a measure called “Sales Growth vs. Prior Year.”

```c
Sales Growth vs PY = 
VAR CurrentSales = 
    CALCULATE(
        SUM(Sales[Amount]),
        FILTER(
            ALL(Date),
            Date[Year] = YEAR(TODAY())
        )
    )
VAR PriorYearSales = 
    CALCULATE(
        SUM(Sales[Amount]),
        FILTER(
            ALL(Date),
            Date[Year] = YEAR(TODAY()) - 1
        )
    )
VAR Growth = 
    DIVIDE(
        CurrentSales - PriorYearSales,
        PriorYearSales
    )
RETURN Growth
```

Calculation time: 22.6 seconds.

**What’s wrong with it?**

Everything.

**Problem: ALL() Inside FILTER Inside CALCULATE**

```c
CALCULATE(
    SUM(Sales[Amount]),
    FILTER(
        ALL(Date),  // Removes ALL filters from Date
        Date[Year] = YEAR(TODAY())  // Then filters to current year
    )
)
```

This pattern: Remove all filters, materialize entire table, then reapply specific filter.

**The Fix:**

```c
Sales Growth vs PY = 
VAR CurrentYear = YEAR(TODAY())
VAR CurrentSales = 
    CALCULATE(
        SUM(Sales[Amount]),
        Date[Year] = CurrentYear
    )
VAR PriorYearSales = 
    CALCULATE(
        SUM(Sales[Amount]),
        Date[Year] = CurrentYear - 1
    )
VAR Growth = 
    DIVIDE(
        CurrentSales - PriorYearSales,
        PriorYearSales
    )
RETURN Growth
```

Changes:

1. Removed ALL()
2. Removed FILTER()
3. Used direct filter (Date\[Year\] = value)
4. Computed YEAR(TODAY()) once

**Performance:**

- Before: 22.6 seconds
- After: 1.8 seconds

**12.6x faster.**

**But We Can Do Better:**

Use time intelligence functions:

```c
Sales Growth vs PY = 
VAR CurrentSales = SUM(Sales[Amount])
VAR PriorYearSales = 
    CALCULATE(
        SUM(Sales[Amount]),
        SAMEPERIODLASTYEAR(Date[Date])
    )
RETURN 
    DIVIDE(
        CurrentSales - PriorYearSales,
        PriorYearSales
    )
```

**Performance**: 0.4 seconds

**56.5x faster than original.**

**Pattern 4 Summary:**

Found in: 204 measures (23%) Average time before: 15.7 seconds Average time after: 1.3 seconds Average improvement: 12.1x

![](99.System/Attachments/1!Abfy5HlSEqda16jN9IL-sw.png.webp)

Pattern 4: Multiple Calcualte Layers

## Pattern 5: ALL() vs. REMOVEFILTERS() (Found in 31% of Slow Measures)

This is subtle. But it matters.

**The Pattern:**

```c
Total Revenue All Regions = 
CALCULATE(
    SUM(Sales[Revenue]),
    ALL(Geography)
)
```

Looks fine. Removes filters from Geography, calculates revenue across all regions.

**What Actually Happens:**

ALL(Geography) removes filters AND returns the entire Geography table.

Geography table in our model: 850 rows (countries, states, cities).

DAX materializes all 850 rows. Then calculates.

**The Fix:**

```c
Total Revenue All Regions = 
CALCULATE(
    SUM(Sales[Revenue]),
    REMOVEFILTERS(Geography)
)
```

REMOVEFILTERS() doesn’t materialize the table. Just removes filters.

**Performance Comparison:**

ALL(Geography): 3.2 seconds REMOVEFILTERS(Geography): 0.3 seconds

**10.7x faster.**

**When to Use ALL():**

When you need the table returned:

```c
// Need the table
Number of Products = COUNTROWS(ALL(Products))
```

**When to Use REMOVEFILTERS():**

When you just need to remove filters:

```c
// Just removing filters
Total Sales All Regions = 
CALCULATE(
    SUM(Sales[Amount]),
    REMOVEFILTERS(Geography)
)
```

**Real Example from Finance:**

Finance had a “% of Total Revenue” measure:

```c
% of Total Revenue = 
DIVIDE(
    SUM(Sales[Revenue]),
    CALCULATE(
        SUM(Sales[Revenue]),
        ALL(Date),
        ALL(Products),
        ALL(Geography)
    )
)
```

**Performance**: 28.3 seconds

**The fix:**

```c
% of Total Revenue = 
DIVIDE(
    SUM(Sales[Revenue]),
    CALCULATE(
        SUM(Sales[Revenue]),
        REMOVEFILTERS()
    )
)
```

REMOVEFILTERS() with no arguments removes filters from ALL tables.

**Performance**: 1.7 seconds

**16.6x faster.**

**Pattern 5 Summary:**

Found in: 275 measures (31%) Average time before: 12.8 seconds Average time after: 1.1 seconds Average improvement: 11.6x

![](99.System/Attachments/1!Ujxy6C9ouNV4HBJPLJZw2w.png.webp)

Pattern 5: All() vs REmovefilters()

## The Transformation: Before and After

Let me show you what happened when we fixed all 5 patterns.

**The Dashboard That Started This:**

Sales Performance Dashboard

- 15 visuals
- 23 measures
- 8.2M rows in Sales table

**Before Optimization:**

Load time: 38 seconds Interaction time (changing slicer): 18 seconds Users: “Unusable”

**After Optimization:**

Load time: 2.8 seconds (13.6x faster) Interaction time: 1.1 seconds (16.4x faster) Users: “Finally usable”

**Company-Wide Results:**

89 reports optimized 892 slow measures fixed Average improvement: 14.2x faster User satisfaction: 34% → 87%

**Best result:**

We cancelled a $180K Power BI Premium capacity upgrade.

CTO: “You just saved us $180K by writing better DAX?”

“By finding the patterns that kill performance, yes.”

![](99.System/Attachments/1!ZfhRa1TrZBXSPBDWygaTMw.png.webp)

The Transformation Results

## The Framework: How to Audit Your Measures

You don’t need to analyze 5,000 measures.

Here’s how to audit your own:

**Step 1: Identify Slow Measures (10 minutes)**

Open Performance Analyzer in Power BI Desktop.

1. View → Performance Analyzer → Start Recording
2. Interact with your report
3. Stop Recording

Look for DAX queries taking >2 seconds.

**Step 2: Check for the 5 Patterns (5 minutes per measure)**

Pattern 1: Look for SUMX, AVERAGEX, COUNTX on single columns Pattern 2: Check calculated columns (only for filtering?) Pattern 3: Look for RELATED() inside iterators Pattern 4: Look for nested CALCULATE with ALL() Pattern 5: Look for ALL() when REMOVEFILTERS() works

**Step 3: Rewrite and Test (10 minutes per measure)**

1. Rewrite the measure
2. Test in DAX Studio
3. Compare before/after times
4. Deploy if faster
![](99.System/Attachments/1!IiBH0pTD5jssGerk_JYkeQ.png.webp)

The 5 Measure Audit Framework

## What to Do Next

Start with 5 measures.

**The 5-Measure Challenge:**

1. Open your slowest dashboard
2. Run Performance Analyzer
3. Find the 5 slowest measures
4. Check for the 5 patterns
5. Fix one pattern per measure

Time investment: 1 hour

Potential impact: 10x faster dashboard

**That measure that started this investigation:**

Original time: 18.3 seconds

After optimization:

```c
Total Sales YTD = 
CALCULATE(
    SUM(Sales[Amount]),
    DATESYTD(Date[Date])
)
```

New time: 0.3 seconds

**61x faster.**

The VP of Sales still uses that dashboard every day.

He doesn’t know I rewrote his measures.

He just knows it’s fast.

And that’s exactly how it should be.
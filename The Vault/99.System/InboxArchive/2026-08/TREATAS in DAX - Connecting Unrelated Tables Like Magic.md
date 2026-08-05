---
title: "TREATAS in DAX — Connecting Unrelated Tables Like Magic"
source: "https://medium.com/write-your-world/treatas-in-dax-connecting-unrelated-tables-like-magic-653b0ab5f28b"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2026-01-19
created: 2026-07-27
description: "There was no relationship between my Campaign and Sales tables — yet the report filtered perfectly. The secret? One underrated DAX function called TREATAS"
Processed: "Unprocessed"
---
## There was no relationship between my Campaign and Sales tables — yet the report filtered perfectly. The secret? One underrated DAX function called TREATAS

· [Act 1 — The Real-World Pain](#2cbe)  
· [Act 2 — Why Relationships Fail (And Why You Need Another Way)](#65ac)  
· [Act 3 — The Moment I Hit the Wall](#32f5)  
· [Act 4 — Discovering TREATAS](#7231)  
· [Act 5 — A Minimal Working Example](#4248)  
· [Act 6 — A Business Case That Matters](#abfb)  
· [Act 7 — Dynamic Segments and What-If Scenarios](#ac25)  
· [Act 8 — TREATAS vs USERELATIONSHIP vs CROSSFILTER](#6a1f)  
· [Act 9 — Under the Hood: How TREATAS Really Works](#fb18)  
· [Act 10 — Pitfalls and Debugging Checklist](#7ac9)  
· [Act 11 — TREATAS in Action: Real Client Stories](#6c71)  
· [Act 12 — Best Practices and Design Tips](#bf33)  
· [Act 13 — Beyond TREATAS: Virtual Modelling Mindset](#2ec4)  
· [Act 14 — Recap and Key Takeaways](#91f1)  
· [Act 15 — Closing Thoughts](#1632)  
· [💬 Your Turn](#5dd9)

## Act 1 — The Real-World Pain

It started with a marketing dashboard.

A global retail client sent me two flat files:

1. **Campaign.csv** — listing campaign IDs, regions, channels, and promo codes.
2. **Sales.csv** — the company’s transactional data with product, amount, and sometimes (not always) a promo code column.

At first glance it looked simple: connect both on *PromoCode* and calculate “Sales by Campaign Category.”  
Except… both tables had **duplicate codes**, different data types, and came from **two independent systems**.

Creating a relationship in Power BI gave me the dreaded warning:

> “This relationship would create ambiguity between tables.”

I tried the usual tricks — `LOOKUPVALUE`, `MERGE Queries`, even `RELATEDTABLE`.  
Nothing worked without duplicating data or breaking the model.

That’s when I stumbled upon a function hiding in plain sight: **TREATAS**.

## Act 2 — Why Relationships Fail (And Why You Need Another Way)

Power BI’s engine (VertiPaq) expects **one-to-many**, **unique-key** relationships.  
But in the wild, your data rarely behaves.

Common failures:

- Both sides contain duplicate keys.
- Columns are stored in different data types.
- Security or data volume prevents physical joins.
- You need a temporary mapping for scenarios or “What If” analysis.

When any of these hit, you end up with **disconnected islands** inside the model.  
DAX still needs to filter across them — and that’s exactly where TREATAS steps in.

## Act 3 — The Moment I Hit the Wall

The client wanted a matrix:  
**Campaign Category → Total Sales → ROI %**

But “Campaign” and “Sales” weren’t related.  
No relationship, no filter propagation.

My initial formula failed:

```c
Total Campaign Sales =
CALCULATE ( [Total Sales], Campaign[Campaign Category] )
```

DAX returned the same total for every row — it couldn’t “see” the campaign context.

I needed a bridge — not a relationship in the model, but something that *behaved* like one.

## Act 4 — Discovering TREATAS

`TREATAS` allows you to **apply the filter values from one table onto another** *as if a relationship existed.*

In plain English:

> “Take this column of values and treat it as a filter on that column over there.”

The syntax:

```c
TREATAS ( <table>, <column1>, [<column2>] )
```

It doesn’t create a permanent relationship.  
It simply tells DAX — “while evaluating this measure, assume these columns are connected.”

## Act 5 — A Minimal Working Example

```c
Total Campaign Sales =
CALCULATE (
 [Total Sales],
 TREATAS ( VALUES ( Campaign[PromoCode] ), Sales[PromoCode] )
)
```

**Step-by-step:**

1. `VALUES(Campaign[PromoCode])` produces the list of visible promo codes.
2. `TREATAS` applies those codes as a filter on `Sales[PromoCode]`.
3. `CALCULATE` re-evaluates `[Total Sales]` inside that new filter context.

Now, when you drag *Campaign Category* into a visual, each category filters the correct subset of Sales — no relationship required.

\[📊 **Visual 1:** Before TREATAS — two separate tables with no arrows\]  
\[📊 **Visual 2:** After TREATAS — virtual dotted line connecting Campaign→Sales\]

## Act 6 — A Business Case That Matters

The marketing team wanted to measure **sales impact by campaign type** (Digital, In-Store, Affiliate).

Physical relationship failed (duplicate codes), so we wrote:

```c
Sales by Campaign Type =
CALCULATE (
 [Total Sales],
 TREATAS (
 VALUES ( Campaign[CampaignType] ),
 Sales[CampaignType]
 )
)
```

**How it flows:**

- `VALUES(Campaign[CampaignType])` = the list of types visible in current filter.
- `TREATAS` = transfers that filter to `Sales[CampaignType]`.
- `CALCULATE` = re-evaluates \[Total Sales\] under that virtual link.

You’ve just built a **virtual relationship** that exists only while this measure runs.

\[📊 **Visual 3:** Table before vs after TREATAS filter applied\]

## Act 7 — Dynamic Segments and What-If Scenarios

Sometimes there isn’t even a column to join.  
Imagine a **Segment Selector** table:

![](99.System/Attachments/1!tAuvHdQvkU2dD_jfZ85h8Q.png.webp)

Users pick a segment in a slicer, and we want to show only customers in that range.

```c
Selected Segment Sales =
VAR MinVal = SELECTEDVALUE ( Segments[MinSales] )
VAR MaxVal = SELECTEDVALUE ( Segments[MaxSales] )
RETURN
CALCULATE (
 [Total Sales],
 TREATAS (
 FILTER ( Sales, Sales[SalesAmount] >= MinVal &&
 Sales[SalesAmount] <= MaxVal ),
 Sales[SalesAmount]
 )
)
```

Now the measure dynamically applies a range filter without any physical join.

\[📊 **Visual 4:** Segment slicer → Filtered Sales table\]

## Act 8 — TREATAS vs USERELATIONSHIP vs CROSSFILTER

![](99.System/Attachments/1!l635YghwWwpOHj-Bq2-XwA.png.webp)

screenshot by the author

> *🧩* ***Rule of thumb:***

- Existing but inactive → `USERELATIONSHIP`
- Same tables wrong direction → `CROSSFILTER`
- No relationship possible → `TREATAS`

\[📊 **Visual 5:** Decision chart — When to use which function\]

## Act 9 — Under the Hood: How TREATAS Really Works

When CALCULATE encounters TREATAS:

1. It builds a **temporary filter table** in memory (based on the first argument).
2. It **maps** that table’s columns to the specified target columns.
3. It **pushes** those filters down the dependency tree (the “filter context”).

In DAX Studio, you can watch it happen:

```c
EVALUATE
CALCULATETABLE (
 VALUES ( Sales[PromoCode] ),
 TREATAS ( VALUES ( Campaign[PromoCode] ), Sales[PromoCode] )
)
```

The result shows only the matching PromoCodes between the two tables — exactly as if a join existed.

**Performance tip:**  
TREATAS can be heavier than physical relationships because it re-creates filter maps each time the measure runs.  
Cache wisely and test with DAX Studio’s *Server Timings* pane.

## Act 10 — Pitfalls and Debugging Checklist

1. **Data type mismatch** → convert explicitly using `CONVERT()` or calculated columns.
2. **Mismatched cardinality** → avoid mapping high-cardinality text fields.
3. **Existing relationships** on same columns → can produce filter collisions.
4. **Ambiguous filters** → clear context with `REMOVEFILTERS()` before TREATAS.
5. **Test** intermediate tables with `CALCULATETABLE()` to confirm filter flow.

**Debugging tip:**  
To see what TREATAS is doing, wrap your measure with `ISFILTERED()` or `VALUES()` and inspect which rows are actually visible inside the context.

## Act 11 — TREATAS in Action: Real Client Stories

**Scenario 1 — Finance Forecast Alignment**

Budget table from Excel had fiscal period as text (`“2025-Q3”`).  
Sales table used a numeric quarter.  
Instead of creating a transformation layer, we used TREATAS to map:

```c
Sales vs Budget =
CALCULATE (
 [Total Sales],
 TREATAS ( VALUES ( Budget[FiscalPeriod] ), Sales[FiscalPeriod] )
)
```

**Scenario 2 — Ad Spend Attribution**

Digital Marketing team provided a daily spend file with no common key.  
We linked it to Sales dates using a derived “WeekStart” column via TREATAS, achieving a virtual join by date range without physical duplication.

## Act 12 — Best Practices and Design Tips

✅ Use TREATAS only *inside* `CALCULATE` or `CALCULATETABLE`.  
✅ Match column data types exactly.  
✅ Keep cardinality low — use IDs, not long text.  
✅ Avoid nesting multiple TREATAS in one measure.  
✅ Document every virtual relationship in a “Model Notes” page.  
✅ Test each filter flow visually in a simple table before building complex KPIs.

> TREATAS is like an invisible bridge — cross it with purpose, not by habit.

## Act 13 — Beyond TREATAS: Virtual Modeling Mindset

Once you understand TREATAS, you start thinking in **virtual models** rather than physical ones.

- Use `ADDCOLUMNS` and `SUMMARIZE` to create on-the-fly bridge tables.
- Combine with `SELECTCOLUMNS` and `CALCULATETABLE` for temporary joins.
- Build dynamic “scenarios” where the user chooses which dimension controls a KPI.

This approach reduces model bloat and keeps your data model clean, letting DAX handle the relationships logically instead of physically.

## Act 14 — Recap and Key Takeaways

![](99.System/Attachments/1!FdnsQ56cX0yeaGPlywfK9Q.png.webp)

screenshot by the author

> Relationships are the language of data models.  
> TREATAS teaches you how to speak that language without drawing lines.

## Act 15 — Closing Thoughts

TREATAS isn’t just a function — it’s a philosophy of flexibility.  
When you truly understand it, you realize that Power BI models aren’t rigid schemas — they’re frameworks for logic.

Next time you’re stuck with unrelated tables, don’t panic — whisper to DAX:

> ***“Hey, just TREAT them AS connected.”***

## Your Turn

Have you used TREATAS in a real project? What’s the most creative way you’ve connected disconnected data?

Share your story below — let’s build a community of problem-solvers who *think beyond relationships.*
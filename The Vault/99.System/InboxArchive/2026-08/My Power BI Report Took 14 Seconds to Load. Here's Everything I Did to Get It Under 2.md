---
title: "My Power BI Report Took 14 Seconds to Load. Here’s Everything I Did to Get It Under 2"
source: "https://medium.com/towards-artificial-intelligence/my-power-bi-report-took-14-seconds-to-load-heres-everything-i-did-to-get-it-under-2-7ef5de8f5214"
author:
  - "[[Sheth Priyanka]]"
published: 2026-07-24
created: 2026-07-27
description: "No new hardware. No premium capacity. Just seven fixes any analyst can copy — and the one that alone cut the load time in half."
Processed: "Unprocessed"
---
## No new hardware. No premium capacity. Just seven fixes any analyst can copy — and the one that alone cut the load time in half.

![Split-screen Power BI performance cover: on the left a dark dashboard with a red stopwatch reading 14.0s and a spinning loading icon; on the right the same dashboard loading instantly with a green stopwatch reading 1.8s. Bold headline reads “14s to under 2s” with sub-stats: 7 fixes, 0 new hardware, 86% faster. The same report, the same data, the same laptop — before and after seven changes that live entirely inside the model and the DAX.](99.System/Attachments/Split-screen_Power_BI_performance_cover!_on_the_left_a_dark_dashboard_with_a_red_stopwatch_reading_1.webp)

Split-screen Power BI performance cover: on the left a dark dashboard with a red stopwatch reading 14.0s and a spinning loading icon; on the right the same dashboard loading instantly with a green stopwatch reading 1.8s. Bold headline reads “14s to under 2s” with sub-stats: 7 fixes, 0 new hardware, 86% faster. The same report, the same data, the same laptop — before and after seven changes that live entirely inside the model and the DAX.

The demo was at 11 AM. I hit “refresh” on the executive dashboard at 10:58 to make sure everything was warm.

Fourteen seconds.

I watched the visuals spin one by one — the KPI cards, then the trend chart, then the big matrix that everyone actually cared about, crawling in last like it had somewhere better to be. Fourteen seconds of a VP staring at loading spinners is not a demo. It’s an apology.

I’d built that report. The numbers were right. The design was clean. And it was *embarrassingly* slow.

Here’s the thing nobody tells you when you’re learning Power BI: a slow report doesn’t feel like a performance problem. It feels like *you* not being good at your job. Every spinner is the stakeholder quietly deciding the analytics team is a bottleneck.

So the week after that demo, I stopped adding features and spent two days doing nothing but making it fast. I got it from 14 seconds to under 2 — on the same laptop, same dataset, no Premium capacity, no new hardware. Just seven changes, most of which took an afternoon.

Here’s the punchline before the details: most slow Power BI reports aren’t caused by hardware — they’re caused by data model design.

This is the exact Power BI performance optimization playbook, in the order I’d run it again.

## First, Stop Guessing. Measure.

The mistake I made for my first two years was optimizing by vibes. “This visual feels slow, let me delete it.” That’s how you spend a day and save 300 milliseconds.

Power BI ships with one of the best tools to *start* performance tuning: Performance Analyzer. It quickly tells you which visuals deserve investigation before you move on to deeper tools like DAX Studio or VertiPaq Analyzer. It’s under the *View* ribbon. You turn it on, hit “Start recording,” refresh your visuals, and it tells you — per visual — exactly where the time goes.

![Stylised Performance Analyzer panel showing a ranked list of visuals by duration. The top row, a matrix visual, is highlighted in red at 9,240 ms, broken into three coloured segments: DAX query 8,900 ms (large red), Visual display 210 ms (small amber), Other 130 ms (small grey). Below it, smaller bars for KPI cards and a line chart. A callout arrow points to the DAX query segment reading “This is where 90% of your time hides.”](99.System/Attachments/Stylised_Performance_Analyzer_panel_showing_a_ranked_list_of_visuals_by_duration._The_top_row,_a_mat.webp)

Performance Analyzer breaks every visual into DAX query, visual display, and “other.” If the DAX query bar is the long one, your problem is the model — not the chart.

That breakdown changed everything for me. Each visual gets split into three numbers:

- **DAX query** — how long the engine took to fetch the data.
- **Visual display** — how long it took to draw the result on screen.
- **Other** — background overhead.

My slow matrix was 9.2 seconds, and 8.9 of those were **DAX query.** That single fact told me the truth: my problem was never the visuals. It was the model and the measures underneath them. I’d been about to delete charts to fix a data-model problem.

Write down your worst offender’s numbers before you touch anything. You can’t prove you made it faster if you never measured slow.

Once Performance Analyzer identified my slowest visual, I could have gone one step deeper with **DAX Studio** to inspect the query plan and Server Timings. For this report, Performance Analyzer was enough to find the biggest bottlenecks. Worth knowing its limits, though: Performance Analyzer measures client-side execution from the report’s perspective. If you need engine-level diagnostics, tools like DAX Studio and Server Timings give you much deeper insight. Bravo and VertiPaq Analyzer can also help you spot oversized columns and model inefficiencies at a glance.

## Fix 1: The Data Model — Go Star Schema or Go Home

This was the big one. The fix that, on its own, cut my load time roughly in half.

My original model was one giant flat table. Sales, customer details, product attributes, region names, dates — all 40-something columns crammed into a single 12-million-row table because that’s how the CSV arrived and I never restructured it. It felt simpler. It was quietly killing me.

Power BI’s VertiPaq storage engine delivers its best compression and query performance when the model follows a well-designed **star schema:** a skinny fact table in the middle holding the numbers and the keys, surrounded by small dimension tables holding the descriptive attributes. Wide, denormalized tables *can* work — but the engine ends up scanning low-compression columns it was never optimized for, and it shows.

![Side-by-side data model comparison. Left, labelled “Before — flat table (slow)” in red: a single wide box listing 40+ mixed columns (SalesAmount, CustomerName, CustomerCity, ProductCategory, RegionName, Date, and more) with a red “12M rows x 42 cols” tag. Right, labelled “After — star schema (fast)” in green: a small central FactSales table with only keys and measures, connected by relationship lines to four compact dimension tables — DimCustomer, DimProduct, DimDate, DimRegion.](99.System/Attachments/Side-by-side_data_model_comparison._Left,_labelled_“Before_—_flat_table_(slow)”_in_red!_a_single_wid.webp)

Same data, restructured. The flat table on the left forces the engine to scan wide, low-compression rows. The star schema on the right is what VertiPaq was designed to fly through.

I split that monster into a `FactSales` table (keys + measures only) and four dimensions: `DimCustomer`, `DimProduct`, `DimDate`, `DimRegion`. It took an afternoon in Power Query and a bit of relationship cleanup.

The result wasn’t subtle. The matrix’s DAX query dropped from 8.9 seconds to about 4. If you do only one thing on this list, do this one.

While I was in there, I also checked every relationship direction. Unnecessary bi-directional relationships can increase filter propagation and query complexity, especially in larger models. Unless there’s a clear business requirement for one, I keep relationships single-direction.

## Fix 2: Kill the Columns You’re Not Using

Here’s a fact that took me too long to internalize: **VertiPaq stores and compresses data column by column, using dictionary encoding.** Every column you import — even one you never put in a single visual — gets stored, compressed, and loaded into memory. High-cardinality columns (lots of unique values, like transaction IDs, precise timestamps, free-text notes) generate much larger dictionaries, which increases memory usage and slows down scans. In VertiPaq, **column cardinality — the number of unique values — is often more important than row count** when determining model size.

![VertiPaq column compression concept graphic on a dark background. Three vertical bars representing columns. Left bar labelled “Region (5 unique values)” is short and green, tagged “compresses great.” Middle bar “Order Date (365 values)” is medium and amber. Right bar “TransactionID (12M unique)” is very tall and red, tagged “compresses terribly — huge memory.” A caption strip reads: cardinality, not row count, drives model size.](99.System/Attachments/VertiPaq_column_compression_concept_graphic_on_a_dark_background._Three_vertical_bars_representing_c.webp)

VertiPaq stores data column by column. A single high-cardinality column like a raw transaction ID can cost more memory than a dozen low-cardinality ones combined.

I opened my model and asked a blunt question of every column: *does a visual, measure, or relationship actually use this?* If the answer was no, it left.

I dropped a raw `TransactionID` I was never grouping on, a `DateTime` column accurate to the millisecond (I only needed the date — so I split it and kept just the date part), and three "notes" fields nobody had opened since 2023. The model file shrank by about 38%. Smaller model, less to scan, faster queries. Free performance for deleting things you didn't need.

## Fix 3: Split DateTime, and Turn Off Auto Date/Time

Two quick wins that punch above their weight.

First, **never keep a full** `**DateTime**` **down to the second** if you only report by day. That precision is thousands of unique values per day, and it wrecks compression. Split it into a `Date` column and, only if you genuinely need it, a separate `Time` column.

Second — and do this in every model you own — turn off **Auto Date/Time.** Power BI silently builds a hidden date table for *every single date column* in your model. On a model with a dozen date fields, that’s a dozen invisible tables inflating your file and your refresh. Go to *File → Options → Data Load* and uncheck it. Then build one proper date dimension and reuse it. Microsoft itself recommends disabling Auto Date/Time in production models and using a single shared date dimension instead.

```c
// One clean date dimension in DAX, reused everywhere.
// Replaces a pile of hidden auto-generated date tables.
DimDate =
ADDCOLUMNS (
    CALENDAR ( DATE ( 2022, 1, 1 ), DATE ( 2026, 12, 31 ) ),
    "Year",        YEAR ( [Date] ),
    "Month",       FORMAT ( [Date], "MMM" ),
    "MonthNumber", MONTH ( [Date] ),
    "Quarter",     "Q" & QUARTER ( [Date] ),
    "YearMonth",   FORMAT ( [Date], "YYYY-MM" )
)
```

## Fix 4: Fix the Measures — Stop Making DAX Do the Model’s Job

With a clean star schema, most of my measures got faster for free. But a few were still slow because I’d written them badly — asking DAX to do work the model should have done.

The worst pattern was calculated columns doing lookups across tables at refresh time, and measures that iterated row by row when a simple aggregation would do. A classic offender:

```c
-- SLOW: forces a row-by-row context transition across 12M rows
Total Sales Slow =
SUMX (
    FactSales,
    FactSales[Quantity] * RELATED ( DimProduct[UnitPrice] )
)
```

If `UnitPrice` rarely changes, I don't need to recompute that multiplication 12 million times on every visual refresh. I precomputed a `LineTotal` once, upstream in Power Query, and the measure collapsed to:

In my model, `UnitPrice` was fixed at the time of each transaction, so precomputing `LineTotal` in Power Query was completely safe. If prices change historically, or your calculation depends on dynamic business rules, keep the calculation in DAX instead. **Always optimize without changing the business meaning of the calculation.**

```c
-- FAST: a plain aggregation the engine can storage-engine straight through
Total Sales = SUM ( FactSales[LineTotal] )
```

The rule I now follow: **do heavy, repeatable math as far upstream as possible** — in the source, in SQL, or in Power Query — and reserve DAX for the light, dynamic stuff that genuinely has to react to slicers. Every calculation you can move out of the visual’s query path is time you’re not paying for on every single refresh.

Another habit that helped was **measure branching** — building complex measures from smaller, reusable measures instead of repeating the same calculation everywhere. Besides improving readability, it reduces maintenance and often makes the next round of optimization simpler.

One more model-level rule: avoid unnecessary calculated columns when Power Query or SQL can do the transformation once during refresh. A calculated column is computed and stored for every row — doing the work upstream keeps the model leaner and the scans faster.

## Fix 5: Reduce What’s On the Canvas

Only after the model was clean did visual count start to matter — because most visuals issue one or more DAX queries during rendering, so cutting unnecessary ones often reduces the overall query workload. My dashboard had 19 visuals on one page — a lot of queries racing every time it opened.

I cut it to 11. I merged three near-identical KPI cards into a single multi-row card. I moved two “nice to have” charts to a drill-through page that only loads when someone actually clicks in. And I killed a slicer nobody used.

You don’t need to be draconian about it. But if a visual isn’t answering a question the reader actually asks, it’s not decoration — it’s latency.

## Fix 6: Trim the Slicers and Interactions

Slicers are sneaky. Every slicer has to query the model to populate its own list of values, *and* it re-triggers queries on the visuals it filters. A high-cardinality slicer (say, a dropdown of 8,000 customer names) is a real cost.

Two things helped. I replaced open-ended slicers with tighter ones (a “Top 10 customers” filter instead of all 8,000). And I used **Edit Interactions** to stop visuals from cross-filtering each other when they didn’t need to — because every unnecessary interaction is another query waiting to fire.

## Fix 7: If You’re on Fabric — Consider Direct Lake

This one’s situational, so I’ll keep it honest: it only applies if you’re in the Microsoft Fabric world. For the report in this story, the six fixes above got me under 2 seconds and I didn’t need it. But on a larger model I own, moving from Import with scheduled refresh to **Direct Lake** mode — where Power BI reads Delta tables straight from OneLake — removed the refresh bottleneck entirely.

Direct Lake doesn’t automatically make every report faster. Its biggest advantage is avoiding scheduled imports while reading Delta tables directly from OneLake, which lets very large semantic models stay fresh with minimal refresh overhead. It’s not a magic “make it fast” button, and it comes with its own trade-offs — Direct Lake doesn’t replace good modeling practices, it complements them. But if you’re already on Fabric and fighting refresh windows, it belongs on your list. And if your model is very large, **Incremental Refresh** can dramatically cut refresh duration by processing only new or changed partitions instead of reloading everything. (I tested Direct Lake against Import and DirectQuery head-to-head in a [separate post](https://medium.com/towards-artificial-intelligence/i-tested-direct-lake-vs-import-vs-directquery-on-the-same-power-bi-dataset-one-silently-switched-b1f3104392f9) if you want the numbers.)

## What Didn’t Work (Because Something Never Does)

I’d be lying if I said every idea paid off.

**Switching visuals to a “lighter” custom visual did nothing.** I spent an hour swapping my matrix for a fancier third-party visual, convinced the native one was slow. Performance Analyzer proved it was the DAX query the whole time. The visual type was a rounding error.

**Over-aggregating hurt usability.** I got greedy and pre-summarized data so aggressively that a stakeholder couldn’t drill into the detail she needed. Fast and useless is still useless. I had to add a drill-through back. Speed serves the reader — it doesn’t replace them.

**“Just buy Premium capacity” was the wrong first move.** It’s tempting to throw a bigger license at a slow report. But a badly modelled report on Premium capacity is a badly modelled report that costs more. Fix the model first; scale the hardware only if you still need to.

## The Results, By the Numbers

After two days, here’s the before and after on the exact same laptop and dataset:

- **Full report load:** 14.0s → 1.8s (about 86% faster)
- **Worst visual (the matrix) DAX query:** 8.9s → 0.6s
- **Model file size:** 210 MB → 129 MB (~38% smaller)
- **Visuals on the main page:** 19 → 11
- **Number of times a VP has watched a spinner during my demo since:** 0
![Before-and-after horizontal bar chart on a dark background titled “Report load time.” Two bars: the top red bar labelled “Before” stretches to 14.0 seconds; the bottom green bar labelled “After” is a short stub at 1.8 seconds. A green badge on the right reads “86% faster.” Small footnote: same laptop, same data, no new hardware.](99.System/Attachments/Before-and-after_horizontal_bar_chart_on_a_dark_background_titled_“Report_load_time.”_Two_bars!_the_.webp)

Fourteen seconds to 1.8 — the entire improvement came from the model and the measures, not the machine.

## Your Copy-Paste Checklist

If your report is slow and you have one afternoon, do these in this order. The order matters — each one makes the next easier to measure.

![Optimization checklist graphic styled as seven numbered cards on a dark background, each with a short label and an impact tag. 1 Measure with Performance Analyzer (find the real bottleneck). 2 Star schema, not flat tables (biggest win). 3 Remove unused + high-cardinality columns (~38% smaller). 4 Split DateTime and turn off Auto Date/Time. 5 Push heavy math upstream, keep DAX light. 6 Fewer visuals and slicers per page. 7 Consider Direct Lake on Fabric.](99.System/Attachments/Optimization_checklist_graphic_styled_as_seven_numbered_cards_on_a_dark_background,_each_with_a_shor.webp)

The seven-step order I’d repeat on any slow report. If you do only one, do 2.

1. **Measure first with Performance Analyzer.** Find whether it’s the DAX query or the visual. Usually it’s the query.
2. **Restructure to a star schema.** Skinny fact, small dimensions. Biggest single win.
3. **Remove unused and high-cardinality columns.** VertiPaq compresses by column — cut the expensive ones.
4. **Split DateTime and disable Auto Date/Time.** One clean date dimension, reused.
5. **Push heavy math upstream; keep DAX light and dynamic.**
6. **Reduce visuals and slicers per page**. Every visual is a query.
7. **Consider Direct Lake** if you’re on Fabric and fighting refreshes.

These optimizations closely follow Microsoft’s own Power BI modeling best practices around star schema design, efficient DAX, and semantic model optimization — so you’re not just taking my word for it.

## The Bigger Picture

The technical fixes are the easy part. The mindset shift is what stuck with me.

For two years, I treated performance as somebody else’s job — the DBA’s, Microsoft’s, the hardware’s. A slow report was just the weather. It wasn’t until that 11 AM demo that I understood speed *is* part of the design. A report that takes 14 seconds to load is telling the reader their time doesn’t matter. A report that snaps open in under 2 is telling them the opposite before they’ve read a single number.

Fast isn’t a nice-to-have you get to after the real work. For the person waiting on the other side of the spinner, fast *is* the work.

That VP opened the report last week, it loaded before she’d finished sitting down, and she didn’t say a word about it. That silence was the whole point. The best performance work is invisible — nobody notices the spinner that never showed up.

Fourteen seconds to under two. Same laptop. Same data. Just a model that finally respected the reader’s time.

## FAQ

**Why is my Power BI report so slow to load?**  
Nine times out of ten it’s the data model, not the visuals. Turn on Performance Analyzer (View ribbon) and check whether the time is in “DAX query” (a model/measure problem) or “Visual display” (a rendering problem). It’s almost always the query.

**How should I approach Power BI performance optimization?**  
Measure first, then fix the biggest bottleneck before touching anything else. In practice the order is: Performance Analyzer to find the slow visual, star schema and column cleanup on the model, lighter DAX, then fewer visuals per page. Optimize with evidence, not intuition.

**What’s the single biggest Power BI performance fix?  
**Moving from a flat, wide table to a proper star schema — a skinny fact table with small dimension tables. VertiPaq, the engine behind Power BI, delivers its best performance on this shape. It alone cut my load time roughly in half. Every model is different, but in my experience the biggest wins usually come from model design rather than DAX rewrites.

**Does removing unused columns really speed up Power BI?  
**Yes. VertiPaq compresses and stores data column by column, so every column you import costs memory even if no visual uses it. Removing unused and high-cardinality columns (like raw IDs or millisecond timestamps) shrinks the model and speeds up every query.

**Should I upgrade to Premium capacity to fix a slow report?  
**Not first. A poorly modelled report will still be slow on bigger hardware — it’ll just cost more. Fix the model, columns, and DAX first, then scale capacity only if you still need to.
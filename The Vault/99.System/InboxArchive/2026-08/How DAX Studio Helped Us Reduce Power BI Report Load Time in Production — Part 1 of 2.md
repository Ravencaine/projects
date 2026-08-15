---
title: "How DAX Studio Helped Us Reduce Power BI Report Load Time in Production — Part 1 of 2"
source: "https://medium.com/@dashakashkumar636/how-dax-studio-helped-us-reduce-power-bi-report-load-time-in-production-part-1-of-2-c57b8c1138e0"
author:
  - "[[Akash Dash]]"
published: 2026-08-04
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
## Getting Started: How to Debug Power BI Performance with DAX Studio

If you’ve ever opened a Power BI report and watched a visual spin for 10+ seconds before loading, you’ve probably asked yourself: *is it my DAX, my data model, or just… Power BI being slow?*

The honest answer is: you don’t know until you measure it. And that’s exactly the gap DAX Studio fills.

In this two-part series, we’ll walk through how we used DAX Studio to diagnose and fix a genuinely slow measure running against a **1.29 million row** Employee table in a Power BI report.

- **Part 1 (this post):** How to set up DAX Studio, capture a query from your report, and read the two panels that matter most — Server Timings and Query Plan.
- **Part 2:** A real bad-DAX example, screenshots of Server Timings on it, the rewritten “fast” version side by side and comparision between these two.

Let’s start with the tool.

### Why Performance Analyzer alone isn’t enough

Power BI Desktop ships with a built-in **Performance Analyzer** (View tab → Performance Analyzer). It’s a great first step — it tells you, per visual, how long the report spent on:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2BVrswrbRytM8s3D7LI4Vg.png)

- **DAX query** — time spent computing your measures
- **Visual display** — time spent rendering the chart itself
- **Other** — background overhead, like waiting in a queue for other visuals to finish

This is useful for spotting *which* visual is the problem. But it won’t tell you *why* a DAX query is slow. If a card visual takes 4 seconds to compute a single number, Performance Analyzer just shows you “4 seconds” — it can’t show you what’s happening inside the query engine during those 4 seconds.

That’s where DAX Studio comes in.

### What DAX Studio actually does

DAX Studio is a free, open-source tool that connects directly to your Power BI data model (or Analysis Services / Fabric model) and lets you run DAX queries against it while watching exactly how the engine processes them — down to the millisecond and the row count.

Think of Performance Analyzer as a stopwatch, and DAX Studio as the mechanic’s diagnostic scanner you plug in once the stopwatch tells you something’s wrong.

To get started:

- **Download DAX Studio** from [daxstudio.org](http://daxstudio.org/) — it’s free.
- **Open your Power BI Desktop file**, then open DAX Studio. It will auto-detect the running Power BI Desktop session and let you connect to it directly (no need to publish anything to the service first).
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nAi7vKvxcRHVGaMKs90TcQ.png)

- If you’re working against a **live connection / published semantic model** instead of a local.pbix, go to the semantic model’s settings in the Power BI service, copy its **server/XMLA endpoint link**, and paste that into the **Connect** dialog in DAX Studio when it opens, instead of selecting a local Desktop session.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9bRyiyLX6qqV9IhsdDHBQw.png)

- In Power BI, run **Performance Analyzer**, find your slow visual, and click **Copy query**. This copies the exact DAX query Power BI generated for that visual.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*bbqTl9mKKNrhOgTtlbOGPw.png)

- **Paste that query into DAX Studio.**

You’re now looking at the *real* query your report is sending to the engine — not a simplified version, the actual thing.

### The two panels that matter: Server Timings and Query Plan

Before running your query, turn on two things in DAX Studio’s Home ribbon:

- **Server Timings**
- **Query Plan**
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lgjTvxQE4ad2AAsHs5H42w.png)

***Server Timings — the “how long, and where”***

This panel breaks your query’s total execution time into two fundamentally different engines working inside Power BI:

**Storage Engine (SE)** This is the fast, compressed, columnar engine (VertiPaq) that actually holds your data and scans it. It’s multi-threaded, heavily optimized, and generally cheap. When you see a line in Server Timings, it’s usually SE fetching a set of columns.

**Formula Engine (FE)** This is the engine that takes what SE hands back and does the “thinking” — joins, iterations, context transitions, anything SE can’t do natively. Critically, **FE is single-threaded** — no matter how many CPU cores your machine has, the formula engine only ever uses one of them, and it sends its requests to the storage engine one at a time, never in parallel.

> One more detail worth knowing: this SE/FE split behaves differently depending on your storage mode. For **Import mode** (VertiPaq, in-memory), SE is extremely fast and its results are cached as compressed in-memory “datacaches.” For **DirectQuery**, SE is effectively your underlying database (e.g., SQL Server), and every SE request becomes a real query sent over the network — which is part of why DirectQuery reports are often far more sensitive to inefficient DAX than Import-mode reports.

**A quick analogy: counting a word in a book**

**Setup:** You have a 1,000-page book and want to answer: *“Which page has the most occurrences of the word ‘Data’?”*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TMfcT9MeznkUtr1aavlO4w.png)

**Step 1:** Storage Engine does the counting (parallel, mechanical)

Imagine handing the book to a team of workers, each assigned a chunk of pages — say 5 workers, 200 pages each. Each worker just scans their own pages and writes down a simple tally: *page number → count of “Data” on that page.* No worker needs to know what anyone else found. This is fast and parallel, because it’s purely mechanical — exactly what the Storage Engine does when it scans a column.

**Step 2:** Formula Engine does the comparison (serial, needs full picture)

Now you have 1,000 little slips of paper, one per page, each with a count on it. To find the page with the *maximum* count, one person has to go through all 1,000 slips, one at a time, keeping track of the highest number seen so far. This can’t be split across a team the same way — one person (one thread) has to see the whole list to declare a winner. That’s the Formula Engine: single-threaded, working on the already-summarized results.

**The punchline:** SE did the expensive-looking work (reading every page) but did it fast because it was split across many workers. FE did comparatively little raw work (scanning 1,000 numbers, not 1,000 pages) but had to do it alone. And if you gave FE a badly-written instruction — “for every page, re-read the *entire book* to check if it’s the max” — you’d force it to redo SE’s job over and over, page by page. That’s exactly the anti-pattern behind the bad measure we’ll dig into in Part 2.

Server Timings shows you, for the whole query:

- **Total** time
- **SE** time and **% of total**
- **FE** time and **% of total**
- **SE Queries** — how many separate requests were sent to the storage engine
- **SE Cache** — whether any of those requests were served from cache instead of a fresh scan

A healthy query usually looks SE-heavy and FE-light — SE is built for volume, FE is not. **If you see FE time dominating, that’s your first clue something in the DAX itself — not the data volume — is the bottleneck.**

***Query Plan — the “what steps did it take”***

Where Server Timings tells you *timing*, Query Plan tells you *structure*. It shows two versions of the plan the engine built to answer your query:

- **Logical Query Plan** — the abstract sequence of operations (filter, then aggregate, then join, etc.)
- **Physical Query Plan** — the actual operators the engine executed to carry that out

You won’t need to read every line of a Query Plan to get value from it. The key thing to watch for early on is **repetition** — operations that appear far more times than you’d expect for the shape of your data. That repetition is usually the fingerprint of a DAX pattern that’s re-scanning the same data over and over instead of computing it once.

***A simple way to think about it***

> A well-written DAX measure asks the warehouse worker (SE) to do as much of the heavy lifting as possible — grouping, filtering, summing — and only hands the manager (FE) a small, already-organized set of results to finish off.

**What’s next**

In Part 2, we’ll put this into practice. We’ll take a Employee table with 1.29 million rows, write a deliberately bad measure using this exact `FILTER(ALL())` -inside- `CALCULATE` anti-pattern, and walk through:

- What Server Timings shows us when we run it (including a surprising result — the engine doesn’t always scan as many rows as you’d expect, and understanding *why* is a lesson in itself)
- How to spot the Formula Engine callback that’s actually eating the time
- The rewritten, fast version of the same measure — and the before/after Server Timings comparison that proves it

See you in [Part 2](https://medium.com/@dashakashkumar636/how-dax-studio-helped-us-reduce-power-bi-report-load-time-in-production-part-2-of-2-9fc1cdc3573e?sharedUserId=dashakashkumar636).

Follow me for more of such content. Happy Coding:)
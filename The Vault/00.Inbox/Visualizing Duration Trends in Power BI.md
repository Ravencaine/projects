---
title: "Visualizing Duration Trends in Power BI"
source: "https://medium.com/@arhamislam808/visualizing-duration-trends-in-power-bi-613bee718b91"
author:
  - "[[Mohd Arham Islam]]"
published: 2025-11-15
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
Visualizing durations in Power BI — especially in line charts — is one of the most frustrating challenges I’ve faced as a Power BI Developer. Sometimes even the simplest requirement needs a surprising amount of workaround.

In this post, I’ll walk you through the exact issue, why it occurs, and how you can attempt to fix it using dynamic formatting (and also why I don’t recommend it in most cases).

### The Problem: Duration as Text vs Numeric

Suppose you have a dataset with a `Duration` column (in seconds), and you want to show **average duration per month** in a line chart.

It sounds simple… until Power BI reminds you that:

- Duration formats like `hh:mm:ss` are **text**, not numbers
- Charts need **numeric values**, not formatted strings
- Formatting inside visuals behaves inconsistently with durations
![](99.System/Attachments/1!Rikr_hqC5WcJSC6yW6qvhw.png.webp)

### Converting Duration into hh:mm:ss (for KPI Cards)

We can easily display the average duration in a KPI card using a simple DAX measure. One thing I’ve noticed — something many developers don’t know or often overlook — is how the FORMAT function behaves with durations. Power BI expects the value to be in days when applying a time format like “hh:mm:ss”.

So before formatting, we must convert our duration (usually stored in seconds) into days by dividing by (3600 \* 24). If we skip this step, the formatted output will be incorrect. Here’s the DAX:

```c
Avg. Duration = 
VAR Result = AVERAGE('Duration'[Duration]) / (3600 * 24)
RETURN
FORMAT(Result, "hh:mm:ss")
```
![](99.System/Attachments/1!Zwhv4qS2MTWwjSP9zG111w.png.webp)

This works well in a KPI card.  
But the moment you try to put this measure into a line chart… **it fails** — because the result is text.

### Creating a Numeric Version for Line Charts

To plot it, you must keep the value numeric:

```c
Avg. Duration (numeric) = 
AVERAGE('Duration'[Duration]) / (3600 * 24)
```

This works in a line chart, but:

- Data labels become confusing (`0.01`, `0.03` instead of `00:15:23`)
- Users can’t easily read or interpret them

So yes, it plots… but it’s not user-friendly.

![](99.System/Attachments/1!ACl8er7HZ3Q2EaMsjyylVg.png.webp)

### Using Dynamic Formatting (Power BI’s Workaround)

Dynamic formatting can **preserve numeric values** but also **display formatted text** as labels.

![](99.System/Attachments/1!22ciYTVvE1vUMc8sA2_c6Q.png.webp)

You select **Format → Dynamic**, then write DAX like:

```c
VAR Result = [Avg. Duration]
RETURN
SUBSTITUTE(Result, "0", "\0")
```

And yes — this looks bizarre.

Why do we need `SUBSTITUTE(Result, "0", "\0")`?

Because without escaping zeros, Power BI sometimes misreads the formatting string and produces unpredictable results.  
This bug has existed for a long time and still behaves inconsistently.

The outcome

- You get a readable data label (`hh:mm:ss`)
- You can plot the numeric values correctly

**BUT** the y-axis becomes meaningless (shows a single repeated duration like `00:20:54`)  
So you must **disable the y-axis values**.

![](99.System/Attachments/1!9PL0TAmNyJ7pbOV2o_1CBw.png.webp)

### Why I Don’t Recommend Dynamic Formatting (Yet)

Even though dynamic formatting *can* solve the problem, it’s unreliable.

I’ve personally experienced situations where:

- Everything worked perfectly for weeks
- Then suddenly the formatting broke
- Same code, same dataset, different results

Until these issues stabilize, dynamic formatting is fine for demos or POCs — but I don’t recommend it for production dashboards.
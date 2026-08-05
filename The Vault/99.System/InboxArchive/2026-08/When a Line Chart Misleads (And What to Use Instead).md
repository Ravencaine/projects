---
title: "When a Line Chart Misleads (And What to Use Instead)"
source: "https://medium.com/data-and-beyond/what-connecting-the-dots-really-tells-your-audience-and-what-it-hides-e83241d5f1b6"
author:
  - "[[Lumiplot]]"
published: 2026-02-23
created: 2026-08-02
description: "More"
Processed: "Unprocessed"
---
You have just opened a standard analytics dashboard. It is full of the usual suspects: revenue over time, daily active users, maybe website traffic. Almost instinctively, anything with a date column gets connected into a smooth trajectory. We tend to trust it because it feels natural, like a path you could follow.

But a line is not just a way to show time. It is a perceptual instruction. The moment you connect dots, you are telling the viewer that these observations belong together, in this specific order, along a continuous path.

**Line chart = observations + an assumption of continuity.**

If that sounds a bit abstract, don’t worry. It is simply about how our brains work. We are wired to accept that assumption of continuity. The connection principle and the Gestalt bias make scattered points feel like a single object with momentum.

![](99.System/Attachments/0!tu7h-qevzXAOxF9_.png.webp)

You stop seeing individual measurements and start seeing a narrative. Here is the perception shift in a nutshell: show people disconnected dots and they describe points, but connect the same dots and they describe a trend. The data didn’t change, but the story did.

One thing worth knowing is that the segment between points is often just made-up information. It is best treated as a guide rather than literal data. Once the line exists, causal temptation kicks in, and viewers naturally start asking what happened in the empty spaces between your measurements.

## When a line chart works well

- You are plotting truly continuous measurements, like temperature or server load.
- Your data is captured at regular, evenly spaced chronological intervals.
- You are mapping cumulative totals where the path between points is mathematically certain.

## When to skip the line chart

- Your data consists of discrete, bucketed aggregates, like total monthly sales.
- You have significant gaps in your tracking or known missing data.
- Your events happen at highly irregular or unpredictable intervals.

When we assume a line chart is always the right default for time series data, we run into a few structural challenges. That is exactly what we are going to walk through next, looking at how to spot them and what to do instead.

## The discrete aggregate challenge

A very common practice is plotting bucketed aggregates, like monthly churn or quarterly revenue, as a continuous line. These are not continuous signals. They are summaries computed over a period.

![](99.System/Attachments/0!gKUT7m8TQET3h3Iq.png.webp)

If you look at a standard line chart connecting March to April, the slope between the points implies a smooth run rate. It makes it look as if churn gently rose day by day. In reality, churn often arrives in bursts when a contract ends or a system glitches. The line makes a discrete summary feel like a physical law.

The alternative is straightforward. If the data is a discrete aggregate and the path within the period is unknown, it is best to avoid drawing the path. A bar chart is usually a stronger choice here. The distinct visual buckets force an honest comparison between periods without inventing daily momentum.

![](99.System/Attachments/0!cUdaZOUkFLyX4852.png.webp)

## Bridging missing data

Data pipelines fail, but charts rarely show it. Many tools bridge missing periods by default by drawing a straight segment from the last known point to the next known point.

You can usually spot this when you see a perfectly straight diagonal line cutting across a highly variable chart, or a massive immediate drop to the baseline.

![](99.System/Attachments/0!okl-eIxZKBLgyMIr.png.webp)

One important caveat here: a missing period is not “no change” or “zero”. It is a complete lack of information. When a chart bridges the gap with a solid line, it silently interpolates and turns missing data into an unjustified statement of stability, leaving viewers unaware anything was missing.

![](99.System/Attachments/0!3eORuzTNfI9yHS1F.png.webp)

To fix this, break the line and show a visible gap where data is missing. If you absolutely need to connect them for visual context, consider using a clearly different encoding. A dotted segment explicitly labeled “data unavailable” works wonderfully.

![](99.System/Attachments/0!6CKOLu4EJ90ziFdy.png.webp)

## Irregular time spacing

Sometimes we plot time points at equal spacing simply because they are in sequential order. However, in a line chart, slope implies a rate of change.

![](99.System/Attachments/0!rc2j1cB5hw6HMp5z.png.webp)

If a two-hour gap takes up the exact same horizontal space as a three-month gap, the visual rate of change is entirely distorted.

Always use a true datetime axis. When you do this, the physical distance between points accurately reflects the chronological time that passed. If the series is highly irregular, you might want to drop the connecting line entirely and use a scatter plot. This lets the density of the points tell the story.

![](99.System/Attachments/0!cte2EJLdbK836uCI.png.webp)

## The overlapping series problem

It is always tempting to cram fifteen regions or twelve products into one chart to show full coverage. At a certain point, this stops being an aesthetic issue and becomes a limit of working memory.

![](99.System/Attachments/0!dvZkHCq_B_YRU0n3.png.webp)

In a typical “spaghetti chart”, overlapping lines hide each other and trigger false comparisons. Local variance also tends to disappear because the vertical axis gets squashed to accommodate everything.

Focus-plus-context is another great approach. Highlight one primary series in a bold color and gray out the rest. This immediately establishes a central narrative without losing the background context.

![](99.System/Attachments/1!e5drCcy7LQIJk20q6pZcUA.png.webp)

Small multiples are a great solution here. You use the same axes across separate panels. This takes up more space, but looking at each panel side-by-side allows for crystal-clear comparisons.

![](99.System/Attachments/0!BZ0WP-OOPNbHKC-e.png.webp)

## Dual axes and implied correlation

Using two vertical axes is a common way to save space, like plotting revenue on the left and margin on the right.

![](99.System/Attachments/0!aDoPqZSskrrWFQ5n.png.webp)

The catch? Dual axes allow for independent scaling. This means the chart creator entirely controls where the lines appear to align, diverge, or intersect. Geometric alignment on the page triggers causal temptation. Viewers will perceive a correlation simply because the lines move together on the screen, even if the actual relationship is mathematically weak.

Stacked charts with a shared horizontal axis across separate panels work nicely to resolve this.

![](99.System/Attachments/0!mhftoXsxohQA5ULh.png.webp)

Alternatively, index both series to a baseline. Set both series to 100 at the baseline date, then for each later point compute Index = 100 × (value ÷ baseline value). When you look at an indexed chart, a single axis accurately compares their true relative change.

![](99.System/Attachments/0!Zpzu_ajXrrw5eiWN.png.webp)

## The unintended effects of cosmetic smoothing

It is completely understandable to want to smooth a jagged line. We often use splines or a rolling average to calm the noise.

![](99.System/Attachments/0!20_rh63TuUswJUC0.png.webp)

There is a limitation here: spline smoothing can overshoot, dipping below a real bound (like zero) just to maintain its mathematical curvature. Rolling averages also smear sudden, one-day viral spikes across days or weeks, making them look like a gentle, prolonged hill. It introduces lag as well.

Try to avoid cosmetic smoothing for operational metrics. Instead, plot the raw points and overlay a distinct trendline. This preserves the visual truth of daily volatility while still answering the question of long-term direction.

![](99.System/Attachments/0!hPW6OLYSOXOboGvh.png.webp)

## Linear scales for compounding growth

If you plot compounding, exponential growth on a standard linear axis, the early variation gets flattened out completely.

![](99.System/Attachments/0!N7cAtoEawQFV2x3K.png.webp)

The left side of a linear growth chart often becomes a flat line before turning into a “hockey stick”. This essentially teaches the viewer that absolutely nothing interesting happened until the very end.

If you care about percentage change over long horizons, consider using a log scale. A log scale reveals relative growth and early volatility that a linear scale hides.

![](99.System/Attachments/0!H8o84ocrT5xXT1uk.png.webp)

**Below is the line chart that tells the truth: it shows what we observed, what we missed, and what we’re merely estimating.**

![](99.System/Attachments/0!BALx1z4MdJ82NxGc.png.webp)

## Generating your chart

If you would like to test these principles out on your own data, here is a prompt you can use:

Create a \[single / multiple / small multiple\] line chart of \[value variable\] over \[time variable\], grouped by \[category variable\], with \[no markers / raw data points / a trendline overlay\], ensuring the x-axis is a true datetime scale, using \[library: seaborn / matplotlib / plotly / …\].

## Wrapping up

A single line blends several phenomena together: long-term trends, seasonal patterns, random noise, and sudden shocks. Decomposing these elements turns vague debates into precise observations.

The *honest* line chart earns its place by telling the truth. It shows what we observed, what we missed, and what we are merely estimating, which contrasts sharply with default charts that connect everything blindly.

The key things to remember:

- **Respect discrete data:** Use bars or lollipops for period-based aggregates rather than implying smooth daily motion.
- **Show your gaps honestly:** Never let a tool silently bridge a period of missing data.
- **Keep time proportional:** Always use a true datetime axis so that the slope accurately reflects the rate of change.
- **Simplify overlapping series:** Default to small multiples or focus-plus-context views when comparing many categories.

Get those right, and your time series visualizations will become some of the clearest, most reliable guides in your reporting.

Try Lumiplot today at [Lumiplot.ai](https://lumiplot.ai/)

Thanks for reading! Subscribe for free to get new plotting posts as they come out.
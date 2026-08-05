---
title: "What Violin Plots Tell You That Boxplots Hide"
source: "https://medium.com/data-and-beyond/what-violin-plots-tell-you-that-boxplots-hide-b8b9831f855b"
author:
  - "[[Lumiplot]]"
published: 2025-12-08
created: 2026-08-02
description: "More"
Processed: "Unprocessed"
---
Let me paint you a picture. You’re looking at delivery wait times for bike couriers in three cities, and you’ve got a boxplot in front of you. It tells you the median. It shows you the interquartile range. And that’s… kind of it.

What it *doesn’t* tell you is whether your data are lopsided, whether there’s a suspicious long tail of delayed orders, or whether you’ve actually got two completely different patterns hiding in the same box, say, a rush-hour cluster and an off-peak cluster pretending to be one distribution.

**A violin plot can show you all of that.**

Think of a violin as a boxplot that’s been given permission to speak freely. It shows you the shape of your data, not just a handful of summary numbers. You can see where values pile up, where there are gaps, and whether there’s one peak or several competing for attention.

![](99.System/Attachments/1!p_sDBy26qQWqHOBYfjf7LA.png.webp)

If you’re using tools like Lumiplot or working with an LLM to help you plot, being specific about what you want really helps. Something like this works well:

*Create a \[vertical / horizontal\] \[single / grouped / split\] violin plot of \[value variable\] by \[category variable\], with \[no overlay / inner boxplot / quartile lines only / jittered points / beeswarm / rug / full raincloud\], using \[library: seaborn / matplotlib / plotly / …\].*

Not sure what all those options mean yet? That’s exactly what we’re going to walk through.

**So what actually *is* a violin plot?**

Here’s the simple version:

**Violin = boxplot + a smoothed picture of where your data actually lives**

Instead of reducing your data to just a few numbers (median, quartiles, whiskers), a violin shows you an estimate of how your data are distributed across the whole range. It’s wide where lots of values cluster together and narrow where data are sparse.

Inside the violin, you can still draw the familiar boxplot elements, the median line, the quartile marks, if you want them. But the real star of the show is that curvy silhouette.

**A little bit about how it works (just enough to be dangerous)**

Under the hood, the violin is built using something called a kernel density estimate, or KDE. Don’t worry about the maths, here’s the intuition:

1. The plot estimates how spread out your data are along the value axis
2. That density curve gets turned sideways, so density runs horizontally while your values stay vertical
3. The curve gets mirrored around a central spine to create that symmetric violin shape

The width at any point is proportional to how many values are around that spot. Wide = common. Narrow = rare.

![](99.System/Attachments/0!k7Z0Mlk3sHN8HOsi.png.webp)

**One thing worth knowing**: plotting libraries make choices about how smooth or spiky the violin looks. Too smooth and you lose real patterns. Too spiky and you’re just seeing noise. Most tools pick sensible defaults:

![](99.System/Attachments/0!bOg2moBL1z5zP8t1.png.webp)

But remember, the violin is an *estimate* of your distribution, **not the raw data itself**.

**How do you actually read one?**

Think of a violin as a density plot with optional boxplot hints layered on top. It’s not a fancy bar chart, it’s showing you shape.

**If you’re already comfortable with boxplots**

Good news: most violin plots include boxplot-style markers inside. You’ll usually see a horizontal line or dot at the median, and lines or a small box showing the middle 50% of your data.

The new bit to consider is this: **at any given height, the width tells you roughly how common those values are.**

![](99.System/Attachments/0!USBsPuK5AL7QfmGc.png.webp)

**Reading the shape**

Since a violin is just a mirrored density curve:

- **Wide regions** → lots of values cluster here
- **Thin regions** → not many values here
- **Pinched waists** → a gap in your data
- **Multiple bulges** → you might have multiple groups mixed together

Back to our bike courier example: a violin with a fat base and a long thin tail might mean most deliveries are quick, but a few take forever. Two distinct bulges could mean rush-hour deliveries and off-peak deliveries behave very differently.

**One important caveat:** the width shows *density*, not raw counts. Two violins can look similarly wide even if one has far more data points than the other.

**When should you use a violin plot?**

Violin plots shine when you have enough data and you genuinely care about the *shape* of your distribution, not just where the middle is.

**When violins work well**

**You’ve got a decent amount of data with interesting structure.** As a rough guide, aim for at least 30 points per group before trusting a violin, 50 to 100 or more is even better. With hundreds of bike orders per city, violins can reveal skew, long tails, and hidden clusters that a boxplot would completely miss.

**You care about the full picture, not just the median.** Violins are great when your questions sound like:

![](99.System/Attachments/0!uE3NHOsGEdOEsadq.png.webp)

- “Are wait times in City A more lopsided than in City B?”
- “Does one city have a nasty tail of really slow deliveries?”
- “Do we have two distinct patterns here, maybe lunch rush versus late night?”

A boxplot can tell you things are “spread out.” A violin can tell you *how* they’re spread out.

**You’re comparing several groups.** Side-by-side violins work beautifully when you’ve got multiple categories to compare, cities, days of the week, times of day. Horizontal violins are particularly nice when you have many groups or long labels, since you can scan them top to bottom.

**When to skip the violin**

**You don’t have much data.** With fewer than about 30 points per group, the smoothing that creates the violin can invent structure that isn’t really there. A handful of data points can create misleading bumps. If you’ve only got 8 orders from a pilot city, that violin will *look* confident, but it’s making things up.

In these cases, stick to a strip plot, beeswarm, or boxplot with points overlaid.

**Your data are clearly discrete.** If you’re looking at ratings on a 1–5 scale or small integer counts, a violin will imply that values like 2.7 or 3.4 exist, which they don’t. You end up with a misleading sense of continuity. Bar charts or dot plots are better here.

**You’re hunting for specific outliers.** Violins don’t call out outliers explicitly; they just stretch the tails. If your main question is “where are the scary extremes?”, either overlay the actual data points or use a boxplot with explicit outlier markers.

**Making it your own: orientation, overlays, and fancy variations**

This is where you get to make style choices. Violins are flexible, which is great, but it also means it’s easy to overdo things.

**Vertical versus horizontal**

**Vertical violins** put your categories along the x-axis and values up the y-axis. They work well for around 3–10 categories with short labels, and they fit nicely in wide layouts like slides or dashboards. But if your labels are long or you have lots of groups, things get cramped.

**Horizontal violins** flip this around, putting categories on the y-axis. They’re fantastic for many groups or long names because you can sort and scan top to bottom. If you only have a few short labels, though, vertical is probably clearer.

![](99.System/Attachments/0!oPynsjLc0_EAzLlX.png.webp)

**Adding overlays**

Here’s where you can really tailor the plot to your needs.

**Violin + boxplot (or quartile lines):** The violin shows the density; a slim boxplot or horizontal lines show the median and interquartile range. This is great when your audience expects those familiar summary statistics, or when you want that clean, publication-ready look. Works best with moderate to large sample sizes.

![](99.System/Attachments/0!VepM5IU27ku6evpm.png.webp)

**Violin + jittered points:** Each data point gets plotted with a small random horizontal offset so they don’t pile on top of each other. This gives you a quick sanity check that the violin’s shape actually matches your data. Nice for continuous data when you want that extra reassurance.

**Violin + beeswarm:** Points get packed together so they don’t overlap, forming little columns where values repeat. This is lovely when every observation matters and you want each one visible, especially good when you have rounded or discrete-ish values. The downside? With lots of data, the swarm can get wide and chaotic.

**Violin + rug:** Thin tick marks along the axis show where individual values fall. This is a subtle way to remind viewers that the smooth shape comes from real data points, without cluttering the plot. Works well with roughly 100–1,000 points per group. Less useful if you need to highlight specific outliers, since the ticks are easy to miss.

**Grouped versus split violins**

![](99.System/Attachments/0!pAgz8HrHFehkri6l.png.webp)

**Grouped violins** place multiple narrow violins side by side within each main category, say, bike versus car delivery times within each city. Use this when you have 2–4 subgroups and want to compare both within and between categories.

**Split violins** take a different approach: one violin per category, but the left half shows one subgroup and the right half shows another. This is perfect for direct head-to-head comparisons (before versus after, treatment versus control) and saves space when grouped violins would be too crowded. But stick to exactly two subgroups, more than that and it gets confusing.

**Raincloud plots**

If you really want to show everything, rainclouds are your friend. They combine a half-violin (the density), a boxplot or summary marker, and jittered points arranged underneath.

![](99.System/Attachments/0!wfsMbAq2iM2GM_fX.png.webp)

Use rainclouds when you want maximum transparency, density plus summary plus raw data, all in one view. They’re brilliant for exploratory work or scientific reporting where you want readers to see exactly how the smooth shape relates to actual observations.

The catch? They can get chaotic with many categories, and they really need enough space to breathe. For non-technical audiences who are already feeling overwhelmed, sometimes a simple boxplot or basic violin is easier to explain.

**Wrapping up**

Violin plots earn their place when you genuinely care about *how* values are distributed, not just where the median sits.

If you’ve got small samples or discrete scores, stick with points and boxplots. If you’ve got plenty of data and messy, interesting distributions, let the violins play.

The key things to remember:

- **Read width as density**, wide means common, narrow means rare
- **Respect your sample size**, don’t trust a violin built on a handful of points
- **Choose overlays that match your data and audience**, sometimes less is more

Get those right, and violins become one of the cleanest ways to reveal the true shape of your data, without hiding everything behind a single box.

**Using Lumiplot to create violin plots**

In Lumiplot, it’s pretty straightforward:

1. Select “Violin plot” as your plot type
2. Choose your x (category), y (value), and optional grouping variable
3. Pick your display style, plain violin, violin + box, jittered points, beeswarm, whatever suits your needs
4. Run it

You focus on the question: *what shape should these wait times have?*

Lumiplot focuses on drawing the violin that actually answers it.

**Try Lumiplot today at** [**Lumiplot.ai**](https://lumiplot.ai/)

*Thanks for reading! Subscribe for free to get new plotting posts as they come out.*
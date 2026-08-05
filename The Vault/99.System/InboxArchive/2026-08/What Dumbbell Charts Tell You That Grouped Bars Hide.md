---
title: "What Dumbbell Charts Tell You That Grouped Bars Hide"
source: "https://medium.com/data-and-beyond/what-dumbbell-charts-tell-you-that-grouped-bars-hide-4d2df3425ccf"
author:
  - "[[Lumiplot]]"
published: 2026-02-09
created: 2026-08-02
description: "More"
Processed: "Unprocessed"
---
Let me paint you a picture. You’re in a quarterly review, looking at a slide comparing last year’s employee satisfaction scores to this year’s across a dozen categories. You’ve got a grouped bar chart in front of you. That’s 24 bars jammed into one frame.

![](99.System/Attachments/0!6DE2ZNnAv3xJtxaN.png.webp)

It tells you the values are there. It shows you the bars side-by-side. And that’s… kind of it.

What it *doesn’t* tell you is the *story*. Your eyes bounce between colours, you’re doing subtraction in your head, and by the time you’ve decoded that “Team Collaboration” is up by 2 points, the meeting has already moved on. The real insight-what changed and by how much-gets buried in the ink.

**A dumbbell chart can show you all of that.**

![](99.System/Attachments/1!-mQjW4lRo73Nd81LWVUlgg.png.webp)

Think of a dumbbell chart as a grouped bar chart that’s been given permission to speak freely. Instead of two bricks sitting next to each other, it connects the “before” and “after” points with a line. That line physically represents the magnitude of change. You don’t have to do the maths in your head; you can *see* the maths.

If you’re using tools like Lumiplot or working with an LLM to help you plot, being specific about what you want really helps. Something like this works well:

*Create a \[horizontal / vertical\] \[dumbbell / slopegraph / diverging delta\] chart of \[value variable\] comparing \[before label\] vs \[after label\] by \[category variable\], sorted by \[after value / delta / alphabetical\], with \[delta labels / reference line at X / aggregate overlay\].*

Not sure what all those options mean yet? That’s exactly what we’re going to walk through.

## So what actually is a dumbbell chart?

Here’s the simple version:

**Dumbbell = dot plot + a physical connector line**

Instead of forcing you to compare the height of two neighbouring bars, a dumbbell plot places a dot at each value and draws a line between them. The length of that line is the story-it’s the change, right there on the page.

![](99.System/Attachments/0!oPQWdq6e0NgJAjP2.png.webp)

If your boss asks, “Where did we move the needle?”, this is the chart you reach for.

## A little bit about how to read one

Don’t worry, this bit is intuitive. Here’s what to look for:

**Long lines** → big changes (good or bad, depending on direction)

**Short lines** → not much movement

**Dot on the right further along** → improvement (assuming right = better)

**Dot on the left further along** → decline

![](99.System/Attachments/0!qhMzjkdrvwcsQ0a-.png.webp)

One thing worth knowing: plotting libraries love alphabetical order by default. But if you sort alphabetically, you just get a random scatter.

![](99.System/Attachments/0!Y3YbnB9riM7EIZoh.png.webp)

**Sort by the “After” value instead.** This creates a ranked list that tells a story. When you plot the data this way, the headlines jump out at you: “Tools & systems” skyrocketed (+17), while “Career growth” tanked (-10).

**Label the connector.** Don’t make your audience squint at the axis. Put the +17 or -10 right on the line.

![](99.System/Attachments/0!W5JARbFPolP4f1-r.png.webp)

**Add a reference line if it helps.** If the target is 60%, draw a line there so people can see who’s above and below the threshold at a glance.

![](99.System/Attachments/0!H9KZ6oUoBWR2UwPn.png.webp)

## When should you use a dumbbell chart?

Dumbbell charts shine when you’re comparing exactly two time points (or two conditions) and you genuinely care about the *magnitude of change*, not just the raw values.

**When dumbbells work well**

**You’ve got a “before” and “after” to compare.** This year vs last year, pre-intervention vs post-intervention, budget vs actual. The two-dot structure is made for this.

**You care about *which categories moved the most*.** Dumbbells are brilliant when your questions sound like:

> *“Where did we improve the most?”*
> 
> *“Which areas got worse?”*
> 
> *“Did the training programme actually move the needle?”*

A grouped bar chart can technically show you this information. A dumbbell makes it *obvious*.

**When to skip the dumbbell**

**You have more than two time points.** If you’re tracking something over five quarters, a dumbbell gets awkward. You’d need multiple lines per category, which defeats the purpose. Use a line chart instead.

**The absolute values matter more than the change.** If your audience needs to know that Team A scored 78 and Team B scored 42, a bar chart might actually be clearer. Dumbbells emphasise the *difference*; they de-emphasise the levels.

**You only have a handful of categories.** With just two or three categories, a simple grouped bar chart is perfectly readable. Dumbbells really prove their worth when you’ve got 8, 10, 15+ categories and the grouped bars become overwhelming.

## When rank matters more than magnitude: the slopegraph

Sometimes the absolute number matters less than the pecking order. Did we drop from 1st place to 5th? Who overtook whom?

A grouped bar chart is terrible at showing this. A **slopegraph** is made for it.

![](99.System/Attachments/0!FHvv_Oc8-tFjqjey.png.webp)

It looks a bit like spaghetti at first-each category is a line connecting two pillars. But the *crossings* reveal the rank swaps instantly. You can see at a glance which categories leapfrogged others.

One thing worth knowing: if everything is bold, nothing is. A common technique is to grey out the flat lines and highlight only the big movers. This creates what’s sometimes called “focus and context” styling-the story pops out while the background stays available for reference.

![](99.System/Attachments/0!w84m7I0jUWIGr6O0.png.webp)

**When slopegraphs work well**

Your question is about relative position: “Who moved up? Who fell behind?”

You want to show convergence or divergence between categories

You have 5–15 categories (fewer gets sparse; more gets tangled)

**When to skip the slopegraph**

If you have lots of categories with similar values, the lines bunch together and become impossible to read. And if absolute magnitude matters (”we need to know the actual scores”), the slopegraph de-emphasises that in favour of rank.

## When you just want the difference: diverging delta charts

Sometimes the baseline is irrelevant. You don’t care if satisfaction went from 20 to 25 or from 80 to 85; you just want to know who’s winning and who’s losing.

For this, compute the difference (After minus Before) and plot it as a **diverging bar chart** centred on zero.

![](99.System/Attachments/0!Z7oYZLLD_a8DvfqJ.png.webp)

Use this when the question is simply “What should we prioritise next quarter?” and you need a clean “winners vs losers” view. Bars pointing right are improvements; bars pointing left are declines. Sort by the delta, and you’ve got an instant priority list.

This can also be shown as a dumbbell or lollipop chart if you prefer, but the rule stays the same: center on zero, encode only the delta, and sort by size so the biggest movers jump out first.

![](99.System/Attachments/0!4ibG9zFA-5q6SVwU.png.webp)

**When diverging deltas work well**

The starting values don’t matter-only the change

You want a quick “good news / bad news” split

You’re presenting to a non-technical audience who just needs the headline

**When to skip diverging deltas**

If your audience needs context about where things started (”Wait, was that category already good or already terrible?”), a diverging delta hides that information. You’d need to pair it with another view or use a dumbbell instead.

## Making it your own: aggregate overlays

If you’re plotting a dozen lines and people are getting lost in the weeds, here’s a trick that often helps: add an **aggregate overlay**.

![](99.System/Attachments/0!1YNm8dIPW2I_9pnu.png.webp)

Think of it as two reading modes:

**Micro:** The faint lines show individual categories

**Macro:** A bold summary line (mean or median) shows the overall trend

And if your audience asks, “Is this improvement broad-based or just one outlier?”, you can overlay a boxplot on top of the dots. It shows the spread instantly.

![](99.System/Attachments/0!UPnU4mysDSK7BzCe.png.webp)

## Using Lumiplot to create these charts

If you’re using Lumiplot or working with an LLM, here are the prompt templates I keep in my notes:

**For a dumbbell chart:**

*“Create a horizontal dumbbell chart of \[value\_variable\] for \[before\_label\] vs \[after\_label\] by \[category\_variable\]. Sort by the ‘after’ value. Use line connectors between the dots. Label the delta directly on the line.”*

**For a slopegraph:**

*“Create a ranked slopegraph comparing \[before\_label\] vs \[after\_label\]. Use focus-and-context styling: grey out lines with small changes, and highlight the top 3 biggest movers in bold colours.”*

**For diverging deltas:**

*“Calculate the delta (\[after\] minus \[before\]). Plot a vertical diverging bar chart of the delta centred at 0. Sort by the delta descending. Colour positive values green and negative values red.”*

## Wrapping up

Dumbbell charts, slopegraphs, and diverging deltas earn their place when you genuinely care about *change* -not just the values at each time point, but what happened in between.

If you’ve got more than two time points, or the absolute values matter most, stick with line charts or standard bars. If you’ve got a clear before-and-after comparison and you want the story to pop, let the dumbbells do the talking.

The key things to remember:

**Dumbbells** show *magnitude of change* -use them when you care how much things moved

**Slopegraphs** show *rank changes* -use them when position matters more than points

**Diverging deltas** show *winners vs losers* -use them when you just need the headline

**Sort thoughtfully and label clearly** -the small details make the difference between a confusing chart and an obvious one

Get those right, and these charts become some of the cleanest ways to show what actually changed-without forcing your audience to do mental arithmetic.

**Try Lumiplot today at** [**Lumiplot.ai**](https://lumiplot.ai/)

*Thanks for reading! Subscribe for free to get new plotting posts as they come out.*
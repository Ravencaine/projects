---
title: "What Scatter Plots Tell You That Summary Statistics Hide"
source: "https://medium.com/data-and-beyond/what-scatter-plots-tell-you-that-summary-statistics-hide-ef2ac2241f40"
author:
  - "[[Lumiplot]]"
published: 2026-02-02
created: 2026-08-02
description: "More"
Processed: "Unprocessed"
---
There’s a moment at the start of every analysis that feels a bit like staring at a locked door. You’ve got a dataset in front of you, maybe a CSV you just pulled, maybe a SQL dump you waited twenty minutes for, and it’s just two columns. X and Y. The question hanging in the air: *are these two things actually related?*

The numbers in the table won’t answer that. You could compute a correlation coefficient, but that’s just one number, it won’t show you *how* the variables relate, whether the relationship is linear or curved, or whether there’s something strange happening at the edges.

![](99.System/Attachments/0!s94eXEeE6qpktzeJ.png.webp)

A scatter plot is the quickest way to actually *see* the relationship. It’s the workhorse of exploratory analysis. And yet, I often see analyses stop at the default scatter(x, y), a cloud of dots appears, everyone nods, and the meeting moves on.

**There’s usually a lot more hiding in that cloud.**

If you’re using tools like Lumiplot or working with an LLM to help you plot, being specific about what you want really helps. Something like this works well:

*Create a scatter plot of \[Y variable\] vs \[X variable\]. Use a \[linear / log\] scale for axes. Handle overplotting with \[alpha transparency / hexbins\]. Colour points by \[Group variable\] and add \[marginal histograms / boxplots\] to the sides. Overlay a \[LOESS / linear\] fit line and \[directly label / use a legend for\] the categories.*

If terms like “LOESS” or “marginals” aren’t familiar yet, don’t worry, we’ll cover all of them below.

## So what actually is a scatter plot?

At its core:

**Scatter plot = position encoding for two continuous variables**

Each dot is one observation. Horizontal position encodes one measurement; vertical position encodes the other. The overall pattern, the shape of the cloud, reveals how the two variables relate.

No aggregation, no binning, no summary statistics standing between you and the data. You’re looking directly at the raw relationship.

## When should you reach for a scatter plot?

Scatter plots shine when you have two continuous variables and you want to understand the *nature* of their relationship, not just whether one exists, but what shape it takes.

**When scatter plots work well**

**You’re exploring how two things relate.** Is there a trend? Is it linear, curved, or something stranger? Scatter plots are ideal when your questions sound like:

> *“Does spending more on X actually improve Y?”*
> 
> *“Is there a threshold, or is it a gradual climb?”*
> 
> *“Are there distinct groups hiding in what looks like one population?”*

**You want to spot outliers and anomalies.** Summary statistics flatten everything into a few numbers. A scatter plot makes the weird cases visible, and those are often the most interesting part of your data.

**You have a moderate number of observations.** Scatter plots work beautifully with anywhere from a few dozen to a few thousand points. Below about 20, the pattern may be too sparse to interpret. Above about 10,000, you’ll need techniques to handle overplotting (more on that shortly).

**When to skip the scatter plot**

**One or both variables are categorical.** If your X-axis is “Department” or “Region,” you’ll end up with vertical stacks of dots. A strip plot, boxplot, or violin might serve you better.

**You have millions of points.** At extreme scales, even transparency struggles. You may need density contours, sampling, or aggregation before plotting.

**The audience only needs the headline.** If the sole question is “is there a correlation?” and a single number will do, a scatter plot might be more detail than required. But if you’re trying to understand *how* things relate, the scatter plot earns its place.

## Getting the foundation right

Before chasing insights, it’s worth making sure the basics are solid. Most misleading scatter plots aren’t wrong because of fancy statistics, they’re wrong because the frame itself distorts reality.

**Check your coordinates**

Every point needs a valid X and Y value. This sounds obvious, but it’s where data integrity problems hide: nulls treated as zeros, mixed units, duplicated rows, truncated values. If the coordinates aren’t trustworthy, neither is any story you build on top of them.

![](99.System/Attachments/0!qzWwbG_U2Gs6T-AL.png.webp)

**Choose your scale deliberately**

The choice between linear and logarithmic axes isn’t cosmetic, it’s an analytical decision. It changes which differences your eye treats as meaningful.

Look at this comparison. Same dataset, three different views:

![](99.System/Attachments/0!Fc6PgkQuMaBDrdGf.png.webp)

On the linear scale, everything bunches against the origin. Switch to log-log, and what looked like a messy curve becomes a clean straight line. If a log-log transformation straightens your data, you may have found a power-law relationship.

The question to ask yourself: are you interested in absolute differences (adding 10) or relative differences (multiplying by 10)? The scale you choose answers that question implicitly.

**Consider your aspect ratio**

A square chart isn’t always the honest choice. If the trend is shallow, a wider plot can separate signal from noise. If the trend is steep, a taller plot prevents the slope from being visually exaggerated. Don’t let library defaults dictate how steep the world appears.

![](99.System/Attachments/0!1TyujDOMU0gfPzg6.png.webp)

## Reading the pattern

With the foundation in place, it’s time to look for what the data is telling you. I typically scan for three things:

![](99.System/Attachments/0!6aSvlMK07fNDJWcX.png.webp)

**Trend:** Do the variables move together? Is the relationship linear, curved, saturating, or essentially flat?

**Groups:** Is this one population, or are there several mixed together? (Often there’s a hidden categorical variable at play.)

**Outliers:** Which points don’t fit? Is that isolated dot a data error, or the most interesting observation in the whole dataset?

**Adding a guide for the eye**

A raw cloud of points can feel overwhelming. Adding a light summary layer helps readers perceive the shape you’re describing.

![](99.System/Attachments/0!heChIF5qzvyUagYZ.png.webp)

**LOESS (locally estimated scatterplot smoothing):** This is my go-to for exploratory work. Think of it as a flexible wire that threads through the data, finding the local trend without imposing a mathematical formula. It’s honest about where the relationship bends.

**Linear regression:** Forces a straight line through the data. Only appropriate when you have reason to believe the underlying relationship is actually linear.

**Logistic regression:** Essential when your outcome is binary (Success/Fail, Yes/No). This produces an S-shaped curve that models probability rather than raw values.

A note on confidence bands: that grey ribbon around the fitted line isn’t just decoration. It shows uncertainty in the estimate. A narrow band means you have enough data to be confident about where the line sits. A wide, flaring band is a warning: “We don’t have enough observations here to know where the trend really goes.”

## Handling the mess: real-world data problems

Tutorial datasets are tidy. Real data overlaps, clumps, and generally refuses to cooperate. Here’s how to handle the common issues.

**Dealing with overplotting**

Overplotting happens when points pile on top of each other until the chart becomes a solid blob. A black patch might represent ten observations or ten thousand, you can’t tell.

![](99.System/Attachments/0!P_xG2YkZD6x8yFs0.png.webp)

Here’s the order I try things:

**Transparency first.** Set alpha to 0.1, 0.05, even 0.02. When points stack up, darker regions emerge, revealing density.

**Binning if needed.** If transparency alone isn’t enough, switch to hexbins or a 2D histogram.

One practical note: don’t jump straight to fancy density contours. A small alpha value usually does the job while keeping individual points visible.

**Showing the marginal distributions**

A scatter plot shows how X and Y relate to each other, but it can hide what each variable looks like on its own. When that matters, add marginal histograms or density curves along the axes.

![](99.System/Attachments/0!Ij2gRzE9bK8nHIi9.png.webp)

Think of marginals as shadows cast onto the walls. They can reveal skew, truncation, ceiling effects, or bimodality that the central cloud conceals. Sometimes the middle looks like one population, while the margins quietly show it was two all along.

**When points represent estimates**

Sometimes a dot isn’t a single observation, it’s a mean, a prediction, or some other summary. In those cases, a bare dot tells an incomplete story. Add error bars (whether SD, SE, or CI), and always indicate which one you’re showing.

![](99.System/Attachments/0!5N7ooHz0Are34u9W.png.webp)

## Encoding additional variables

When your data contains distinct populations, treating everything as one grey cloud obscures the story. You can separate groups by encoding a third variable.

**Categorical variables**

![](99.System/Attachments/0!qpTi3go1IUlZ-6kX.png.webp)

Colour is the primary tool here because it’s pre-attentive, the eye groups colours automatically, before conscious thought kicks in. Shape is weaker; relying on shape alone forces readers to scan point by point. I typically reserve shape as a backup for accessibility reasons (particularly for colourblind readers).

Beyond just colouring the dots, consider whether groups behave differently. Fitting separate trend lines for each group can reveal when the relationship itself, especially the slope, changes by category.

**Continuous variables**

![](99.System/Attachments/0!m2w0EiWlPiwyog0I.png.webp)

To encode a third numeric variable, you can vary point size (creating a bubble chart). This adds another dimension to the story, but use it sparingly. If bubbles grow too large, they overlap and obscure position, the very thing that makes scatter plots useful in the first place.

**Showing clusters**

![](99.System/Attachments/0!LsiGnOhzBrrlgaFF.png.webp)

When distinct clusters exist (different cohorts, markets, experimental conditions), decide what claim you’re trying to make:

**Centroids:** If the message is “these groups are distinct,” add a clear centroid marker for each group. This reduces cognitive load immediately.

**Separate fit lines:** If the message is “these groups behave differently,” fit and draw separate lines. A single pooled line can actively mislead.

## Specialised comparisons

Sometimes the standard X-Y layout isn’t the clearest way to present your data.

**Paired data (before and after)**

When plotting pre-test against post-test scores, add a diagonal reference line where x = y. Points above the line improved; points below declined. This gives the chart an instant visual logic that readers grasp immediately.

![](99.System/Attachments/0!ZJqZHitpSuIE346O.png.webp)

## Why annotation matters

Something I’ve come to believe firmly: **direct labelling beats legends almost every time.**

The purpose of a chart isn’t just to display data, it’s to guide the reader’s eye toward what matters. We’re not merely showing coordinates; we’re constructing a narrative. Consider the difference annotation can make:

![](99.System/Attachments/0!XWUqZzd1lvzPV_J5.png.webp)

In the first version, we see a vague scatter. In the second, adding colour to the high-cost cases and a reference line for the average transforms the plot from a distribution into a performance review. The expensive cases are instantly visible.

In this example, the raw plot shows a correlation, true enough, but not particularly illuminating.

![](99.System/Attachments/0!vfmimGgwZuIOxx0a.png.webp)

The annotated version uses three tools to transform it into an argument:

**A diagonal reference line** that instantly answers “which group has higher values?”

**Context regions** (shaded areas for Normal, Overweight, Obese) that translate abstract numbers into meaningful categories

**Direct callouts** that name the interesting outliers explicitly, rather than leaving readers to hunt for them

Annotation isn’t decoration. It’s what turns a picture into an argument, bridging the gap between “here is the data” and “here is what it means.”

## Wrapping up

Scatter plots earn their place when you care about the *shape* of a relationship, not just whether a correlation exists, but how the variables move together, where the pattern bends, and which observations don’t fit.

If all you need is a correlation coefficient, compute it directly. But if you want to *understand* the relationship, let the scatter plot show you the full picture.

The key things to remember:

**Get the foundation right**, validate coordinates, choose scales deliberately, and respect aspect ratio

**Look for trend, groups, and outliers**, these are the three stories hiding in most scatter plots

**Handle messy data honestly**, use transparency for overplotting, marginals to reveal hidden distributions, error bars when points are estimates

**Annotate with purpose**, direct labels, reference lines, and context regions turn raw data into insight

Get those right, and scatter plots become one of the most honest ways to explore a bivariate relationship, without hiding anything behind summary statistics.

## Using Lumiplot to create scatter plots

In Lumiplot, the process is straightforward:

> *1\. Select “Scatter plot” as your plot type*
> 
> *2\. Choose your X and Y variables*
> 
> *3\. Add overlays as needed: trend lines, marginals, or categorical colouring*
> 
> *4\. Run it*

You focus on the question: *what’s the relationship here?*

Lumiplot handles the rest.

**Try** [**Lumiplot**](https://lumiplot.ai/) **today at Lumiplot.ai**

*Thanks for reading! Subscribe for free to get new plotting posts as they come out.*
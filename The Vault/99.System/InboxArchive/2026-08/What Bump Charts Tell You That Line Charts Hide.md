---
title: "What Bump Charts Tell You That Line Charts Hide"
source: "https://medium.com/microsoft-power-bi/what-bump-charts-tell-you-that-line-charts-hide-b630758d6458"
author:
  - "[[Lumiplot]]"
published: 2026-03-28
created: 2026-08-02
description: "More"
Processed: "Unprocessed"
---
You are looking at a dashboard tracking five competing products over the last year. The standard line chart shows sales fluctuating for everyone. The lines rise and fall together in a tight cluster, and you are squinting at the screen, trying to figure out who is actually winning at any given moment. You are wondering exactly who overtook whom, and when the leadership changed.

![](99.System/Attachments/0!6v8-X-_MntnosQYw.png.webp)

In 1815, on a stretch of the River Isis too narrow for boats to row side by side, Oxford University developed a new kind of rowing race. You did not just try to finish first. You tried to row fast enough to physically bump the boat in front of you and take its place in the ranking.

![](99.System/Attachments/0!m3zjH9ua5Mhde7Nc.png.webp)

Two centuries later, that same idea lives on in one of the most distinctive visualization types in analytics. That is why the name fits so well. It is not really about trend lines. It is about position changes.

And that is why these charts can be brilliant.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## The Definition

Bump chart = a line chart that tracks categorical rank over time instead of raw value.

Each line represents one competitor. Its horizontal position shows time, and its vertical position shows its rank. That is it.

Bump charts are best when the story is ordinal, not quantitative. If that sounds a bit abstract, do not worry. It is highly intuitive once you see it in practice.

## Reading the chart

Reading these is straightforward once you know the three basic rules:

- A line moving up the page means a better rank.
- A flat line means a stable rank, not a stable value. It simply means nobody passed you.
- The vertical distance between lines is ordinal, not magnitude.

The real storytelling power of a bump chart lives in the crossings. Each crossing marks an overtake. This is exactly why this chart is better at showing competitive friction than a standard line chart. You can see the exact moment a challenger breaks through or a leader falls behind.

Keep in mind what a crossing does *not* mean. It signals a change in **order**, but it does not mean the underlying values were far apart. Nor does it guarantee a dramatic real-world difference unless you show that context elsewhere. That is one of the most important reader protections to remember.

There is another important caveat here: the strength of this chart is also its biggest limitation. It shows order, not distance. A move from rank 1 to rank 2 could reflect a tiny difference in sales. Or it could reflect a catastrophic collapse. The chart treats both exactly the same because it only cares that the order changed.

Suppose a company drops from 50 percent market share to 30 percent, but its nearest competitor is still only at 20 percent. It stays in the number one spot. On the ranking chart, the top line looks calm and stable. In reality, the business has taken a major hit. When your readers need both rank and value, stacking the charts is a highly practical fix. You can put the bump chart on top, place a value chart directly below it, use a shared time axis, and highlight the exact same entities in both.

![](99.System/Attachments/0!3NmdTg5n3DrrPxVH.png.webp)

A side-by-side rank view and value view makes this tradeoff concrete. In the figure below, the bump chart shows who moved in the pecking order, while the companion value chart shows how large the underlying changes actually were.

This is why the pairing works so well. On the left, NovaAI looks completely stable because no one overtakes it. On the right, you can see that its underlying value falls sharply over time. MemoSpark’s climb and EchoWrite’s late surge are visible in both panels, but each panel answers a different question. The bump chart tells you who rose, fell, and overtook. The value chart tells you how big those changes really were.

There is one more practical consideration to keep in mind. Rank is most comparable when the field is reasonably stable over time, or when changes in the field are clearly explained. Keep the field of competitors stable, since dropping from rank three to five means something very different in a field of five versus twenty.

## When to use a bump chart

Use this when the reader mainly needs to understand a rank narrative. Good use cases include:

- Sports standings: Who led the league across the season? When did a team lose first place? Who climbed late?
- App store rankings: Which app surged from the middle of the pack into the top five? Which incumbent slid down?
- Market-share leaders: Which brand overtook another across several quarters or years?
- Election race positions: Who entered the top three, who lost momentum, and who had a brief surge?
- Business unit rankings: Which region, product, or segment moved into the lead?

## When to skip the bump chart

There are also clear situations where you should avoid this approach, or at least avoid using it alone:

- Magnitude is the real story: If the actual size of the gap matters more than the order, use a line chart, bar chart, or area chart.
- There are too many categories: If you have twenty or thirty series and all of them matter equally, the result is usually unreadable.
- The rankings are unstable: In polling, survey data, noisy operational metrics, or small samples, rank changes may reflect noise rather than meaningful change. If tiny value differences, rounding, or sampling noise can flip ranks, the chart may overstate the drama.
- Ties are common and important: Standard designs assume a clean ranking ladder. Ties create overlap problems that need deliberate handling.
- The audience expects raw values: If viewers are likely to read line spacing as value spacing, you need to educate them or choose another form.

A lot of visualization confusion disappears if you separate these three clearly:

- **Line chart:** shows how values change over time. Use it when the actual numbers matter.
- **Slope chart:** compares two points in time. Use it when you want a clean before-versus-after view.
- **Bump chart:** tracks changes in rank across multiple time points. Use it when the competitive ordering is the story.

To make that actionable: use a slope chart for two points, a line chart for values, and a bump chart for multi-period rank changes.

## Data Prep Logic

You do not need to be a data engineering expert here, but the preparation is where many errors happen. A clean chart needs clean rules.

1. **Define the ranking variable.** Rank means nothing without a specific metric.
2. **Rank within each time period.** Every week, month, or quarter needs its own distinct ordering.
3. **Set tie-breaking rules.** Ties are interpretive, not just technical. Standard designs assume a clean ranking ladder. Ties create overlap problems that need deliberate handling. If left unmanaged, ties can hide lines entirely. Document whether you are resolving them by alphabetical order, previous rank, or by sharing the rank.

**4\. Handle missing periods honestly.** If a category drops out and returns, breaking the line is usually the most truthful approach. Missing periods should usually break the line rather than fake continuity.

![](99.System/Attachments/0!IEKf5sglb6cW_V-l.png.webp)

**5\. Respect time intervals.** Do not make unevenly spaced time points look perfectly even without an explanation.

![](99.System/Attachments/0!vncwZs-h_dVnTsAK.png.webp)

## The Design System

Most messy charts fail in predictable ways. They have too many lines, too many colors, and no clear explanation. Here is a practical system to keep your graphics readable:

- **Labeling:** Label lines directly, especially at the endpoints.
- **Color:** Highlight one to three key series and mute the rest in gray.
- **Axis direction:** Put rank 1 at the top. Higher on the page is read as better by default.
- **Markers:** Show markers at actual time points to distinguish true observations from the connecting path.

Here is something I have come to believe strongly: direct labeling beats legends almost every time. A legend forces the reader to look away, decode a color, and then return to the chart to reconnect that color to a path. Direct labels let the eye stay comfortably with the data.

When too many lines occupy the same space, your eye cannot follow individual paths. One common strategy is to show the top N and gray out or remove the rest.

Alternatively, when many categories matter, small multiples are often better than forcing everything into one tangled chart.

There is one caveat worth noting with the top-N approach. Showing only the leaders clarifies the chart, but it can also hide active competitors just below the cutoff and make a rising challenger appear to suddenly materialize out of nowhere.

And what about line shapes? If the chart is analytical, prefer straight lines. They are honest and simply connect one observed rank to the next. Smooth curves can look better, but they may imply motion between observations that was never measured. If you use them for editorial graphics, make sure you use visible markers to anchor the real observations.

## Common Stumbling Blocks

Before you share your chart, watch out for these predictable pitfalls:

- Leaving rank 1 at the bottom of the y-axis.
- Using too many equally emphasized lines.
- Relying on disconnected legends.
- Ignoring ties and letting lines overlap invisibly.
- Using a bump chart when the raw magnitude is the actual story.

## A Quick Publishing Checklist

A short checklist goes a long way to making your post much more practical:

- Is rank really the story?
- Is rank 1 at the top?
- Are key lines directly labeled?
- Are ties handled explicitly?
- Is missing data shown honestly?
- Would a companion value chart help?

## Prompting for Bump Charts

Ready to build your own? Here is a prompt you can use:

Create a \[straight-line / smooth-curve\] bump chart tracking \[categorical variable\] ranked by \[value variable\] over \[time variable\], with \[all lines colored / top 3 highlighted and rest gray\], including markers at each point and direct labels at the \[start / end / both\].

## Wrapping up

Tables are for lookup. Line charts are for value trends. Slope charts are for before-and-after comparisons. Bump charts are for races. They make competition visible, surface leadership churn, and turn rankings into narrative.

**The key things to remember:**

- **Prioritize rank over magnitude:** Use this when you want to highlight overtakes and hierarchy changes.
- **Keep it clean:** Highlight what matters, gray out the noise, and always put rank 1 at the top.
- **Label directly:** Skip the legend and place labels right next to the lines so readers can follow the story without cognitive overload.
- **Respect the data:** Have a clear plan for ties and missing periods to avoid misleading your audience.

Because in analytics, just like in those Oxford rowing races, the real drama is not in the lines alone. It is in the bump.

Try [Lumiplot](https://lumiplot.ai/) today at Lumiplot.ai

Thanks for reading! Subscribe for free to get new plotting posts as they come out.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----b630758d6458---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Any

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization
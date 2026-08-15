---
title: "Deep dive into tooltip options in Power BI visuals (Generally Available)"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-tooltip-options-in-Power-BI-visuals-Generally/ba-p/5255518?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-07-06
created: 2026-08-08
description: "Tooltips give consumers context about the data point they're hovering over — the full value, a year-over-year change, a related KPI, a quick"
Processed: "Unprocessed"
---
Tooltips give consumers context about the data point they're hovering over — the full value, a year-over-year change, a related KPI, a quick explanation — without ever leaving that data point. Power BI offers a flexible set of tooltip options so you can start with the defaults and add as much customization as the report needs.

The options progress from least to most custom:

1. **Default visual tooltip** — Power BI builds the tooltip from the fields in your visual.
2. **Tooltip field well** — Add extra fields to enrich the default tooltip.
3. **Tooltip fields only** and **Sentence format only** (newly generally available) — Curate the exact field list or write the hover content as a sentence.
4. **Report page tooltip** — Replace the tooltip entirely with a report page you design.

A separate **Help tooltip** icon in the visual header gives consumers guidance about the visual itself rather than the data point, and it coexists with whichever data tooltip you pick.

## Default visual tooltips and the Tooltip field well

By default, a visual tooltip shows the field name and value for every field used in the visual, any extra fields you add to the **Tooltip** field well, and an actions footer for **Drill down**, **Drill up**, and **Drill through** on supported visuals.

![DataZoe_0-1782798746793.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354260i1EB462454952A95F/image-size/large?v=v2&px=999 "DataZoe_0-1782798746793.png")

*Figure: Default tooltip showing the data fields, added tooltip fields, and supported drill actions for the hovered data point.*

To shape the default tooltip, select the visual, open **Format visual** > **General** > **Tooltips**, and adjust **Text**, **Background**, and **Actions**. Tooltips also inherit colors from the report theme, so styling stays consistent across visuals unless you override it here. The **Options** section is where the newly generally available settings live.

![DataZoe_1-1782798746800.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354261i0F8E80501BF63306/image-size/large?v=v2&px=999 "DataZoe_1-1782798746800.png")

*Figure: Tooltip formatting options in the visual settings, including text, background, actions, and the generally available tooltip options.*

## Tooltip fields only: Curate the list

With **Tooltip fields only** turned on, the tooltip shows just the fields in the **Tooltip** field well — the visual's encoded fields are hidden. That gives report authors complete control over the hover content.

![curate the tooltip.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354273i1BE67450A3A43E2C/image-size/large?v=v2&px=999)

curate the tooltip.png

*Figure: Tooltip fields only limits the hover content to the fields explicitly added to the Tooltip field well.*

Use it when:

1. You want to be specific about which fields appear in the tooltip. For example, when a field is in the visual for formatting or sorting purposes and doesn't need to be surfaced on hover.
2. You want to surface supplementary fields, such as year-over-year change, without listing every series in the chart.
3. To turn it on, select the visual, open **Format visual** > **General** > **Tooltips** > **Options**, and turn on **Tooltip fields only**.

## Sentence format: Write the insight as a phrase

Sentence format lets you add a written sentence about the data point to the tooltip. You write a template that mixes plain text with field references — wrap any available field in curly braces, such as {Sales}, and Power BI substitutes the value for the hovered data point. Turn on **Bold values** to emphasize the substituted values.

By default, the sentence appears at the bottom of the tooltip, below whatever fields the tooltip already shows — whether that's the full set of visual and tooltip fields or just the curated list from **Tooltip fields only**. Turn on **Sentence format only** when you want the tooltip to display only the sentence.

For example, this template:

{Segment} sales changed by {Sales YoY} ({Sales YoY %}) from same period last year with a total of {Sales} across all years.

renders as:

Small Business sales changed by $3,701,592 (44%) from same period last year with a total of $42,427,919 across all years.

![sentence mode tooltip.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354263i81FE7314548EE283/image-size/large?v=v2&px=999)

sentence mode tooltip.png

*Figure: Sentence format turns a template with field references into readable tooltip text for the hovered data point.*

## Sentence format with field parameters

Field parameters let consumers swap the field a visual uses. In a sentence template, you can reference both the parameter's selected field name and its value:

- {Field parameter} returns the name of the selected field.
- {Field parameter Fields} returns the value of the selected field. The word *Fields* matches the value column name in the field parameter.

![tooltips with field parameters.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354266iE41F18369541E8CD/image-size/large?v=v2&px=999)

tooltips with field parameters.png

*Figure: Field parameters can be referenced in the sentence template so the tooltip reflects the consumer's selected field.*

Template example:

We had {Field parameter Fields} in {Field parameter} for {Segment}.

Result:

We had $940,097 in Profit for Enterprise.

Learn more about how to [Use Field Parameters in Power BI Reports](https://learn.microsoft.com/power-bi/create-reports/power-bi-field-parameters)

## Sentence format with a drillable hierarchy

When the visual drills up and down a hierarchy, the sentence should read correctly at every level. Add a measure that resolves the in-scope level, add it to the **Tooltip** field well, and reference it in the template.

```js
Segment or Product Drill =
SWITCH ( TRUE(),
    ISINSCOPE(Financials[Segment]) && ISINSCOPE(Financials[Product]),
        SELECTEDVALUE(Financials[Segment]) & " (Segment) " & SELECTEDVALUE(Financials[Product]) & " (Product)",
    ISINSCOPE(Financials[Segment]), SELECTEDVALUE(Financials[Segment]),
    ISINSCOPE(Financials[Product]), SELECTEDVALUE(Financials[Product]),
    BLANK()
)
```

Use the measure in a template such as:

{Segment or Product Drill} has {Sales} in sales, a change of {Sales YoY} ({Sales YoY %}) since last year.

The tooltip now reads correctly whether the chart shows Segment, Product, or both.

![drill with sentence tooltip.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354267iCE9F6ABB0274BBBA/image-size/large?v=v2&px=999)

drill with sentence tooltip.png

*Figure: A hierarchy-aware sentence uses a measure to display the right segment, product, or combined level as consumers drill through the visual.*

## Chart-specific tooltips

In the same **Options** card, **Chart-specific tooltips** add context tailored to the chart type, such as the percentage of the first and previous values on a funnel chart. It's on by default. Turn it off when you'd rather rely solely on your selected fields or sentence.

## Report page tooltips for full customization

When telling isn't enough, do what Power BI does best and show it. Design a report page as the tooltip — add the visuals, KPIs, or images you want, and turn on **Page information** > **Allow use as tooltip**. On the consuming visual, open **Format visual** > **General** > **Tooltips** > **Options**, set **Type** to **Report page**, and pick your page. Filters from the hovered data point flow through automatically.

![Report page tooltip.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354268i277E1FBF2BE48AD0/image-size/large?v=v2&px=999)

Report page tooltip.png

*Figure: Report page tooltips replace the standard hover card with a custom report page filtered by the selected data point.*

Report page tooltips aren't interactive — consumers can hover and read, but they can't select slicers or click visuals inside the tooltip. When consumers need to interact with the filtered view, build a drillthrough page in the same report or in another report in the same workspace, and let consumers right-click a data point to open it. Read more about [Drillthrough in Power BI Reports: Navigate to Detailed Insights](https://learn.microsoft.com/power-bi/create-reports/desktop-drillthrough)

If you turn on the **modern visual defaults** preview, you get tooltip canvas sizes you can choose from when sizing the report page for tooltip use. These sizes are smaller than the main report page sizes, so the page renders at appropriate dimensions for a tooltip without manual resizing. Read more about [Visual defaults in Power BI reports](https://learn.microsoft.com/power-bi/create-reports/power-bi-reports-visual-defaults).

![tooltip page sizes.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354269iB2BD86B435CD4075/image-size/large?v=v2&px=999)

tooltip page sizes.png

*Figure: Modern visual defaults include larger tooltip canvas sizes that help report page tooltips render at an appropriate hover-card size.*

## The Help tooltip

The **Help tooltip** icon in the visual header explains the visual itself, not the data. Turn it on under **Format visual** > **General** > **Header icons** > **Icons**, and choose typed text for short guidance or a report page for richer content. It pairs well with the visual tooltip when consumers are new to a report.

![help tooltip.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1354272iC81B99FF46BDCA47/image-size/large?v=v2&px=999)

help tooltip.png

*Figure: The Help tooltip icon provides visual-level guidance, either as short typed text or as a richer report page experience.*

For a short, video-style walkthrough, point the Help tooltip at a report page that uses an animated GIF as its background. The GIF plays each time a consumer hovers the help icon, giving them a quick demo of how to interact with the visual — for example, how to drill, cross-filter, or use a custom selector.

## Next steps

- Try out the different tooltip options in your reports!
- Learn more with the [Tooltips overview.](https://learn.microsoft.com/power-bi/visuals/power-bi-visualization-tooltips-overview)
- Style your tooltips across your report with [Visual defaults in Power BI reports](https://learn.microsoft.com/power-bi/create-reports/power-bi-reports-visual-defaults).
- Submit ideas and feedback at [Microsoft Fabric Ideas.](https://community.fabric.microsoft.com/t5/Fabric-Ideas/idb-p/fbc_ideas)
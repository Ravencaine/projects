---
created: 2026-08-04
updated: 2026-08-05
source: "How to Build a Gantt Chart in Power BI Using Only Core Visuals.md"
note_type: gotcha
tags: [powerbi, visualization, alignment, gotcha, overlay, gantt]
---

# Chart Alignment Between Two Stacked Visuals

When two native visuals are stacked to fake a single composite chart (e.g. a transparent column chart timeline + a transparent-fill bar chart body for a Gantt chart), the chart only "looks right" if the two X-axes are explicitly aligned — otherwise bars drift off the timeline and the illusion breaks.

## Expected Behaviour

Stack two native visuals on top of each other, set each one's irrelevant pieces to transparent, and the result should look like one custom chart: timeline grid behind, task bars in front, all aligned.

## Actual Behaviour

The bar chart's X-axis and the column chart's X-axis are independent by default. Even when both bounds are set to the same `Min Calendar Date` / `Max Project Date`, the bar chart's bars can sit visibly off the column chart's date gridlines — bars appear to start a few pixels before the first gridline, or end a few pixels after the last gridline, or float somewhere in between.

## Why It Happens

The bar chart and the column chart have **independent axis scales:** they don't auto-sync just because they're stacked. They differ in how they pad their axes, how they treat the first/last bar edge, and how they bin dates. Even identical min/max bounds don't produce identical pixel layouts because the two visuals apply different default padding for "first bucket" and "last bucket". The article's author calls this out explicitly: "I needed to make sure that the **right end of the bar chart** was flush with the **right end of the column chart**, and that the **left start of the bar chart** was flush with the **first date (and vertical gridline) of the X-axis of the column chart**."

## How to Handle It

1. **Wire both visuals to the same bound measures.** Both X-axis minimums should reference `Min Calendar Date`; both X-axis maximums should reference `Max Project Date`. Don't set one of them manually.
2. **Use a transparent Date Start Buffer on the bar chart.** The buffer is `DATEDIFF(min calendar date, min project date) + DATEDIFF(min project date, task start date)`. It pushes each bar to its true horizontal position, so the left edge of the first bar aligns with the first gridline of the column chart.
3. **Verify alignment via tooltip.** Add `Task Start Date` and `Task End Date` to the bar chart's tooltip. Hovering over a bar shows the actual numeric range; compare against the column chart's gridlines by eye (or by screenshot pixel-peeping) until the two match.
4. **Accept some pixel nudging.** The article notes that "this slightly shifts the bars to the right — this is to accommodate tasks that end later." Expect to spend a few iterations aligning the X-axis ranges and visually re-checking.
5. **Hide every chart element that gives the layering away.** Disable axis titles, hide Y-axis values, remove the legend, set backgrounds transparent on both visuals — otherwise the viewer sees two stacked charts, not one Gantt chart.

## Related Gotchas

- [[Bar-to-Area-Conversion]] — same family of "hide the chart's own markers to fake a different shape" tricks; alignment is simpler there because it's a single visual.
- [[Error-Band-as-White-Out-Mask]] — another native-visual override where decorative elements are repurposed; alignment to a background PNG is the equivalent concern.
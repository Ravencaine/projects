---
title: "How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI"
source: "https://medium.com/@iwasanjaya/how-to-highlight-a-segment-in-a-100-stacked-chart-and-move-it-to-the-baseline-in-power-bi-fbb68f3dade6"
author:
  - "[[Iwa Sanjaya]]"
published: 2026-07-27
created: 2026-07-27
description: "Let the reader pick which segment is easy to read — it drops to the baseline in color, everything else fades to grey. Works on any category with 2 or more segments (status, size, material, whatever you stack)."
Processed: "Unprocessed"
---
## Let the reader pick which segment is easy to read — it drops to the baseline in color, everything else fades to grey. Works on any category with 2 or more segments (status, size, material, whatever you stack).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TlFRkQScEvSJirYbjIr3cQ.jpeg)

Cover Image — Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline

Link to the interactive dashboard:

## [Power BI Report](https://app.powerbi.com/view?r=eyJrIjoiYmRiN2QzNjYtMDNlNi00NTdmLTg0MmItNjIyNTViODg2NWQ2IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9&source=post_page-----fbb68f3dade6---------------------------------------)

### Report powered by Power BI

app.powerbi.com

> ***Method: one measure per stacking position, not one measure split by a category field.*** *A 100% stacked chart bound the normal way (one measure + a category in the Series/Legend field) can* never *reorder its own segments — the stack order follows the field’s sort order, not the data. So instead, each* position in the stack *becomes its own measure, and the selected category’s measure always occupies position 1. See* Why this method? *for the full reasoning.*

## Contents

1. What you’re building
2. Naming used in this guide
3. The building blocks
4. Block 1 — `Selector` (the slicer’s choices)
5. Optional — sorting your *real* category column, not just the Selector
6. Block 2 — Position measures
7. Block 3 — Color by position
8. Wiring it up in the report
9. Optional — re-sort categories by the highlighted position
10. Optional — a custom tooltip
11. Quick test checklist
12. Why this method?

## What you’re building

In a 100% stacked bar or column chart, only the segment sitting right on the baseline is genuinely easy to compare across bars — everything stacked above it “floats,” so its length is hard to judge at a glance once you’re comparing a dozen bars.

This technique lets the reader choose which segment gets that treatment:

- Pick a category (e.g. a pizza size like “Large”) → That category’s segment drops to the **baseline**, in a highlight color
- Everything else → Stacks above it, in **grey**
- Optional → Bars **re-sort** by the highlighted segment’s value, best-to-worst

One slicer click, and every bar in the chart re-highlights and re-bases at once.

*(Example: a pizza sales chart split into S / M / L / XL / XXL — pick “Large,” and every pizza type’s bar shows its % of Large-size sales sitting on the baseline in color, with the other four sizes greyed out above it. Works for any small set of mutually-exclusive categories that currently sum to 100% in your stacked chart.)*

**The trick:** a 100% stacked chart normally takes one measure and a category field (in Series/Legend), and Power BI decides the stacking order from that field’s own sort order — DAX can’t touch it. So instead of one measure + a field, you feed the chart **N separate measures**, one per stacking slot. Whichever category is selected always computes into “Position 1” — and because Position 1 is plotted first, it’s always the one touching the baseline, no matter which category that is.

## Naming used in this guide

Replace these placeholders with your own names:

- `Dim`: The dimension table holding your category column (e.g. `Product[Size]`, `Quality[Status]`)
- `Category`: The column whose values you want to be selectable/highlightable
- `[N]`: How many distinct values `[Category]` has (3, 5, however many — this method scales to any N)
- `[Your Measure]`: The value being split by category (e.g. a sales, count, or % measure)

Objects you’ll create: `Selector` (disconnected table), `Position 1` through `Position N` (one measure per stacking slot). Optional: `Tooltip Position` (disconnected table) + `Ord Category` / `Ord Value` / `Ord Absolute Value` / `Ord Font Color`, for a custom tooltip.

## The building blocks

- `**Selector**` **(Disconnected helper table):** The N categories, feeding one slicer
- `**Position 1**` **…** `**Position N**` (Measures): One per stacking slot; `Position 1` always equals the selected category
- **Color rule (Visual formatting):** Highlight color on `Position 1`, grey (gradient) on the rest
- *(Optional)* **Sort** (Visual formatting): Re-sort the chart’s categories by `Position 1`, descending
- *(Optional)* `**Tooltip Position**` **+** `**Ord …**` **measures** (Disconnected table + measures): Custom tooltip with real category names, sorted highlighted-first

## Block 1 — Selector (the slicer’s choices)

A tiny disconnected table (no relationship to your data) — create via *Modeling → New table*:

```c
Selector =
DATATABLE (
    "Category", STRING,
    {
        { "Value A" },
        { "Value B" },
        { "Value C" }
        -- one row per distinct value of Dim[Category]
    }
)
```

> **If your categories don’t sort correctly alphabetically** (e.g. S/M/L/XL/XXL, or Low/Medium/High), add a second literal column in the same `DATATABLE` — e.g. `"Sort Order", INTEGER` with `{ "Value A", 1 }, { "Value B", 2 }, …` — then set **Category → Column tools → Sort by column → Sort Order.**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*HPHM2F9T7VEptYo8)

Figure 4.1: Creating the highlight selector table

> ⚠️ Gotcha: don’t build `Sort Order` as a *separate calculated column* that reads `Category` (e.g. a `SWITCH` on the category text). Power BI will refuse it with “a circular dependency was detected” — because the sort-by column would depend on `Category`, while `Category` ’s display order depends on the sort-by column. The fix is exactly what’s shown above: put both columns in the *same* `DATATABLE` call as literal data pairs, so neither one is a formula that reads the other.

## Optional — sorting your real category column, not just the Selector

The gotcha above covers `Selector` (a small disconnected helper table). If `Dim[Category]` itself doesn’t sort correctly either (the same S/M/L/XL/XXL problem, but on your **actual imported dimension table** this time, not the helper), the fix is different — because `Dim` isn’t a `DATATABLE` you can just rewrite; it’s loaded from a real source (CSV, SQL, etc.), so there’s no single DAX statement to put both columns into.

**Add the sort column in Power Query (M), not as a DAX calculated column.** A calculated column added in DAX would read `Dim[Category]` in its formula — and the moment you set that as `Category` ’s Sort By Column, you hit the exact same circular-dependency error, for the exact same reason. A column added in **M**, on the other hand, loads in as a plain Data column with no DAX expression at all — so nothing in the model’s dependency graph ever links it back to `Category`, even though it was obviously derived from it upstream in the query.

The conditional column, added via Power Query’s Add Column step:

```c
if [Category] = "S" then 1
else if [Category] = "M" then 2
else if [Category] = "L" then 3
else if [Category] = "XL" then 4
else if [Category] = "XXL" then 5
else null
```

### Steps:

1. **Power Query Editor** → select your table → **Add Column** → **Custom Column** → paste the expression above, naming the result something like `Category Sort Order`.
2. **Close & Apply.**
3. Back in the model: hide the new column, then set `Category` → **Column tools** → **Sort by column** → `Category Sort Order`. This now works cleanly — no circular dependency, because the sort column has no formula tie to `Category` from the engine’s point of view.

## Block 2 — Position measures

This is what makes the reorder possible. Each measure asks: *“which category sits in this stacking slot, given what’s selected?”*

`**Position 1**` is always the selected category:

```c
Position 1 =
VAR Sel = SELECTEDVALUE ( Selector[Category] )
RETURN
    IF ( NOT ISBLANK ( Sel ), CALCULATE ( [Your Measure], Dim[Category] = Sel ) )
```

`**Position 2**` **through** `**Position N**` are the *remaining* categories, in their original order, skipping whichever one is selected. Rather than writing a different `SWITCH` by hand for each one (fine for N=3, tedious past that), use this general formula — it works for any N:

```c
Position 2 =
-- for "Position k", replace every 1 below with (k - 1)
VAR Sel = SELECTEDVALUE ( Selector[Category] )
VAR SelRank =
    SWITCH ( Sel, "Value A", 1, "Value B", 2, "Value C", 3 /* …, "Value N", N */ )
VAR TargetRank = IF ( 1 < SelRank, 1, 1 + 1 )
VAR TargetCategory =
    SWITCH ( TargetRank, 1, "Value A", 2, "Value B", 3, "Value C" /* …, N, "Value N" */ )
RETURN
    IF ( NOT ISBLANK ( Sel ), CALCULATE ( [Your Measure], Dim[Category] = TargetCategory ) )
```

Why this works: give every category a fixed rank (1, 2, 3…, N, in whatever order you want them to stack). Removing the *selected* rank from that list and asking for “the k-th value still remaining” always resolves to: *k, if k comes before the selected rank; k + 1, otherwise.* That’s the one line (`TargetRank = IF ( k < SelRank, k, k + 1 )`) doing all the reordering work — no matter which category is selected, the non-selected ones always come out in their original relative order.

Copy `Position 2` for each further slot, changing only the `k` value (`1` → `2` → `3` …) in `TargetRank = IF ( k < SelRank, k, k + 1 )` and the top-level measure name.

> ***Only 3 categories?*** *You can skip the rank formula and just write two direct* `*SWITCH*` *branches per non-base position (one for each way the selected value could shift things) — simpler to read for a small, fixed N. The formula above is there for when hand-writing every branch gets unwieldy (5+ categories).*
> 
> ***Design choice — default when nothing’s selected:*** *the formulas above return* ***blank*** *for every position until the reader picks something (so the chart shows nothing until they do). If you’d rather have a sensible default segment on the baseline before any selection, change* `*SELECTEDVALUE ( Selector[Category] )*` *to* `*SELECTEDVALUE ( Selector[Category], "Value A" )*` *(or whichever default you want).*

## Block 3 — Color by position

Colors are set per measure, not per category — because from the chart’s point of view, the categories *are* the measures now (`Position 1`, `Position 2`, …).

### 1\. Select the chart → Format visual → Data colors.

### 2\. You’ll see one color swatch per Position measure. Set:

- `**Position 1**` → your highlight color (e.g. your brand color)
- `**Position 2**` **…** `**Position N**` → a grey, ideally a light-to-dark gradient the further a slot sits from the baseline (e.g. `#CED4DA` → `#ADB5BD` → `#6C757D` → `#495057`)

### 3\. Turn the legend off (Format visual → Legend → Show = Off).

The legend would show “Position 1 / 2 / 3…”, not your real category names — since the series are position-based, not category-based, the legend can’t label them meaningfully.

## Wiring it up in the report

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*nYmrvyKi0aFy2saX)

Figure 8.1: Building the chart

### Build (or rebind) the chart:

1. **Visual type: 100% Stacked Bar chart or 100% Stacked Column chart.**
2. **Category / Axis:** whatever you’re comparing across (e.g. pizza types, products, dates…).
3. **Y-axis / Values:** add **all N** `**Position**` **measures** — *not* one measure plus your `[Category]` field in Series. If you’re converting an existing chart that currently has `[Category]` in the Series/Legend well, remove it; the position measures replace that binding entirely.

### Add the selector slicer:

1. Insert a **Slicer** → field `**Selector[Category]**`.
2. Format → **Selection** → **Single select = On** — cleanest UX, though the measures above already resolve to blank on no/multi-selection, so nothing breaks if you leave it off.

### Colors & legend — see Block 3 above.

Now picking a category in the slicer should drop that segment to the baseline in your highlight color, with the rest stacked above in grey.

## Optional — a custom tooltip

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*qNdWHaaq42f8VIbr)

Figure 10.1: Creating a custom tooltip

The chart’s **native** tooltip is barely useful here — it shows the raw position-measure names (“Position 1”, “Position 2”…), not real category names, since the series are position-based rather than category-based (Block 3). A custom tooltip page fixes this: hover any bar, and it shows the real category name, its %, and its absolute value — with the highlighted one listed first.

**Why this needs its own tiny position table:** a table/matrix visual can’t dynamically re-sort its rows by a measure unless that measure is a visible column — and here, the row order needs to change every time the slicer selection changes. So instead of grouping the tooltip by `Dim[Category]` and trying to sort it, group it by a small `Tooltip Position` table (1 … N) — the rows then come out **pre-sorted**, highlighted-first, with no helper sort column needed.

```c
Tooltip Position =
DATATABLE ( "Pos", INTEGER, { {1}, {2}, {3} /* …, {N} */ } )
```

`**Ord Category**` — which category occupies *this row’s* position (reads the row context from `Tooltip Position`, not from the chart):

```c
Ord Category =
VAR Pos = SELECTEDVALUE ( 'Tooltip Position'[Pos] )
VAR Sel = SELECTEDVALUE ( Selector[Category] )
VAR SelRank = SWITCH ( Sel, "Value A", 1, "Value B", 2, "Value C", 3 /* …, "Value N", N */ )
VAR Offset = Pos - 1
VAR TargetRank = IF ( Pos = 1, SelRank, IF ( Offset < SelRank, Offset, Offset + 1 ) )
RETURN
    IF ( NOT ISBLANK ( Sel ), SWITCH ( TargetRank, 1, "Value A", 2, "Value B", 3, "Value C" /* …, N, "Value N" */ ) )
```

This is the *same* rank-arithmetic idea as Block 2’s `Position k` measures, just inverted: instead of computing a value for a fixed, hardcoded position, it computes the **category name** for whatever position the current row happens to be — one measure covers all N rows, since the row context now comes from the table itself.

`**Ord Value**` and `**Ord Absolute Value**` — the % and raw value for that row’s category:

```c
Ord Value =
VAR TargetCategory = [Ord Category]
RETURN
    IF ( NOT ISBLANK ( TargetCategory ), CALCULATE ( [Your % Measure], Dim[Category] = TargetCategory ) )

Ord Absolute Value =
VAR TargetCategory = [Ord Category]
RETURN
    IF ( NOT ISBLANK ( TargetCategory ), CALCULATE ( [Your Measure], Dim[Category] = TargetCategory ) )
```

**Optional —** `**Ord Font Color**`, to bold/color the highlighted (position 1) row only:

```c
Ord Font Color =
IF ( SELECTEDVALUE ( 'Tooltip Position'[Pos] ) = 1, "#004E89" )
```

Returns blank for the other rows so they keep their normal readable color.

**Wiring it up:**

1. Add a new page → Format pane → **Page type: Tooltip.**
2. Drop a **Matrix** visual on it (not a plain Table — see the gotcha below) → **Rows:** `**Tooltip Position[Pos]**` → **Values:** `**Ord Category**`**,** `**Ord Value**`**,** `**Ord Absolute Value**`**.**
3. Apply `Ord Font Color` as the field’s conditional font color.
4. On the main chart → **Format visual** → **Tooltips** → **Type: Report page** → point it at this new page.

> *Expected, not a bug: while you’re just looking at the tooltip page in the* ***editor*** *with nothing picked in the slicer, it’ll show empty — every* `*Ord …*` *measure depends on* `*SELECTEDVALUE ( Selector[Category] )*`*, which is blank until a category is actually selected. Pick one on the main page (slicer selections apply report-wide) and the tooltip populates.*

## Quick test checklist

Pick each category in the slicer in turn and confirm:

- **Position 1:** Always equals the *selected* category’s value
- **Position 2 … N:** The *other* categories, in their original relative order
- **Sum of all positions:** Equals the un-split total — should be unchanged from before you added this feature
- **Nothing selected:** All positions blank (or your chosen default, if you set one)
- **Legend:** Off — the position-based series would otherwise show meaningless labels
- ***(If built)* Custom tooltip:** `Ord Category` at position 1 matches the slicer selection

## Why this method?

A 100% stacked chart bound the ordinary way — one measure + your category field in Series/Legend — draws its segments in whatever order Power BI sorts that field. DAX measures can influence *values*, but they cannot reach into the chart engine and tell it “draw this segment first.” The only lever you have over stacking order is *which measure is plotted first* — so if you want the order to depend on a live selection, the selection has to determine *which measure* holds which position, not just what value that measure returns. That’s the whole reason this method trades “one measure split by a field” for “N measures, one per position.”

I appreciate you taking the time to read this! Hopefully, this article offered valuable insights and ignited your curiosity. If you have questions or want to dive deeper, don’t hesitate to reach out on [LinkedIn](https://www.linkedin.com/in/iwasanjaya/) or via [email](mailto:hello.powerlib@gmail.com). For more on data visualization techniques and creative ideas, **visit my** [**website**](https://powerlib.super.site/), or support my work on [**Ko-Fi**](https://ko-fi.com/powerlib) or [**Buy Me a Coffee**](https://buymeacoffee.com/powerlib) by **following** or **joining as a member for exclusive documentation.**
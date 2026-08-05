---
created: 2026-08-04
updated: 2026-08-05
source: "Analyzing Survey Comments in Power BI Using AI.md"
note_type: workflow
tags: [powerbi, dashboard, survey-comments, theme-overview, sentiment-distribution, trend-analysis, text-search, conditional-formatting, svg]
related: [LLM-Survey-Enrichment-GPT4, GPT-4-Thematic-Coding, svg-visualizations-in-power-bi, rept-unichar-8203-zwsp]
---

# Survey Comments Dashboard (5-Section Layout)

A Power BI dashboard layout that turns a tagged survey-results table (`Comment`, `Theme`, `SentimentScore`, `Date`) into a navigable, multi-resolution story. Five sections: **Theme Overview → Sentiment Distribution → Trend Analysis → Search + Cross-Filtering → Details Table**.

## Prerequisites

- A loaded table `Comments` with at minimum: `Comment` (text), `Theme` (text), `SentimentScore` (1–5 numeric), `SubmissionDate` (date).
- Two core measures: `[Sentiment score]` (the simple average) and `[Sentiment value]` (the 5-tier SWITCH categorisation — see [[rept-unichar-8203-zwsp]] for the `REPT(UNICHAR(8203), N)` trick).
- Card visuals, donut, clustered bar chart, line chart, table, plus the text-search filter (a Slicer visual set to text-search mode).

## Steps

### 1 — Theme Overview (top-left)

**Type:** Table visual.
**Columns:** `Theme` (Rows), `Count of Comments` (via `COUNTROWS`), `[Sentiment score]` (Average).
**Sort:** by `Count of Comments` descending.
**Purpose:** the *index* — readers scan the themes to find what they want to drill into.

Add summary KPI cards to the right:

- **Total Comments** = `COUNTROWS(Comments)`
- **% Positive** = `DIVIDE(CALCULATE(COUNTROWS(Comments), Comments[SentimentScore] > 3.2), [Total Comments])`
- **# Themes** = `DISTINCTCOUNT(Comments[Theme])`

### 2 — Sentiment Distribution + Theme Breakdown

**Top:** Donut chart — `Sentiment value` (the 5-tier category) on the slice field, count of comments as the value. Gives a top-down "is the overall balance positive or negative?" read.

**Bottom:** Clustered bar chart — theme on the axis, sentiment bucket on the legend, count of comments as the value. Lets the reader see *which themes skew negative* (e.g., "Speed and Timeliness of Service" might dominate the red bucket).

### 3 — Trend Analysis Over Time

**Type:** Line chart (or area chart with toggle — see [[Field-Parameters]]).
**X-axis:** `SubmissionDate` (month-level usually).
**Y-axis:** a parameter that swaps between *average sentiment* and *count of comments* via a field parameter or a slicer.
**Cross-filter dimension:** theme — click a theme in section 1 and this chart shows that theme's sentiment evolution.

### 4 — Search + Cross-Filtering (cross-cutting)

A **text-search Slicer** at the top of the page filters all visuals:

- Set to a column that lists theme names.
- Tick "Search" in the Slicer header.
- Users type "product" → "Product Quality and Reliability" surfaces → all visuals respond.

Plus the natural cross-filtering: clicking any theme or sentiment slice in sections 1–2 refines sections 2–5.

### 5 — Detailed Answers Table (bottom)

**Type:** Table visual.
**Columns:** `SubmissionDate`, `Theme`, `[Sentiment value]` (the 5-tier categorical), `Comment` (full text, wrap text enabled).
**Conditional formatting:** `Sentiment value` cell → SVG icon column (red/yellow/green faces, or arrow indicators, or thumbs-up/down rendered as SVG strings) — see [[svg-visualizations-in-power-bi]].

This is the row-level escape hatch: filter to a theme, then scroll the actual comments that gave that theme its score. Useful for QA on the LLM tagging ("did GPT-4 call this 'Pricing' or 'Value'?") and for copy-pasting quotes into executive reports.

## Variations

- **Replace donut with stacked bar.** Same information, but easier to compare when buckets have very different magnitudes.
- **Add a sentiment-drift alert.** Highlight themes whose 30-day rolling sentiment has fallen by > 0.5 points — a primitive form of early-warning.
- **Use Field Parameters for the trend view.** Bittar's later "Power BI Time Hacks" article generalises this; see [[Time-Period-Slicers]] for the underlying pattern.
- **Export-to-Excel button.** A bookmark that triggers `Export data` on the details table — for the few users who still want raw rows.
- **Embed PBIX / Tableau side-by-side.** Unusual but useful when stakeholders already have a Tableau ingestion habit.

## Common Errors

- **Theme column shows "Error" rows.** GPT-4 tagging failed for some comments. Either re-run the pipeline, drop the "Error" rows with `FILTER(Comments, Comments[Theme] <> "Error")`, or replace with a hand-coded fallback.
- **Cross-filter feels "stuck".** When field parameters switch between avg-sentiment and count, Power BI's cross-filter direction can flip — reset the cross-filter direction for the trend visual explicitly.
- **Text search returns nothing.** Most common cause: slicer connected to a *measure* not a *column*. Search works on column-bound slicers.
- **Sentiment scores are all 3.** GPT-4's bias toward the middle — re-prompt with `temperature=0` and a clear "1 = strongly negative, 5 = strongly positive" rubric; consider lowering the bar for "neutral".

## Related

- [[LLM-Survey-Enrichment-GPT4]] — produces the input table this dashboard consumes
- [[GPT-4-Thematic-Coding]] — the upstream tagging pattern
- [[svg-visualizations-in-power-bi]] — for the details-table sentiment icons
- [[rept-unichar-8203-zwsp]] — for the `REPT(UNICHAR(8203), N)` 5-tier sort trick
- [[Time-Period-Slicers]] — for a year/month/week X-axis minimum switcher

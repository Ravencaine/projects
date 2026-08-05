---
created: 2026-08-05
updated: 2026-08-05
source: Analyzing Survey Comments in Power BI Using AI (Isabelle Bittar)
note_type: atomic
tags: [power-bi, dashboard, survey, sentiment, theme, svg, cross-filter, search]
---

# Survey AI Dashboard Components

Six Power BI visual sections that Isabelle Bittar builds from the GPT-4-enriched survey CSV: Theme Overview, Sentiment Distribution, Theme Breakdown, Trend Analysis, Search/Cross-Filtering, and Detailed Answers Table.

## 1. Theme Overview

A **Table** visual grouping all comments by their GPT-4-assigned theme, showing:
- Number of responses per theme
- Average sentiment score per theme (using `AVERAGE(Comments[SentimentScore])`)
- Sentiment classification label (`Sentiment value` measure)

Supported by summary stats cards:
- Total number of comments
- % classified as positive
- Total number of unique themes

## 2. Sentiment Distribution

A **Donut chart** showing the breakdown of all comments into three sentiment buckets (Positive / Neutral / Negative). Created by counting rows grouped by the `Sentiment value` measure.

Use case: gives executives a one-glance read on overall feedback balance.

## 3. Theme Analysis Bar Chart

A **clustered bar chart** comparing sentiment distribution per theme. Each bar represents a theme; within the bar, segments show the count of comments at each sentiment level (Positive → Negative).

Purpose: immediately surface themes that are skewing negative (e.g., "Speed and Timeliness of Service") so operational teams can prioritise.

## 4. Trend Analysis

A **line chart** tracking either:
- Average sentiment score over time (by month), or
- Number of comments over time (volume trend)

Built using a Date column (from the original survey submission) and either `AVERAGE(SentimentScore)` or `COUNTROWS(Comments)`.

Key insight: if a theme's sentiment line dips in a particular month, it prompts a deeper operational review.

## 5. Search and Cross-Filtering

A **Text filter** (slicer with search enabled) at the top of the page. Typing a keyword (e.g., "product") dynamically filters all themes containing that word, updates all visuals, and allows users to drill into specific areas.

All visuals on the page are cross-filtered:
- Clicking a theme in the Theme Overview table filters the donut chart, bar chart, and trend line to that theme
- Clicking a month in the trend chart filters the detailed table

## 6. Detailed Answers Table

A **Table** visual showing every individual comment with:
- Original comment text
- Assigned theme
- Sentiment classification (using SVG-based conditional formatting for colour-coded icons)
- Timestamp

Use cases:
- Quality assurance — spot-check GPT-4 tagging accuracy
- Copy/paste actual quotes into executive reports
- Identify frequent wording patterns under specific themes
- Export to Excel for further analysis

## SVG Sentiment Icons

Sentiment icons are applied using Power BI's conditional formatting on the `Sentiment value` column with custom SVG data URIs. Isabelle's SVG article covers this technique in detail.

## PBIX Reference

[Survey_Comments_AI_Power_BI.pbix](file:///C:/Users/krlsa/Documents/00%20Projects/The%20Vault/99.System/Attachments/Survey_Comments_AI_Power_BI.pbix) — 440 KB — contains all six sections as working Power BI examples.

## Related

- [[Analyzing-Survey-Comments-AI-Power-BI-Isabelle-Bittar-source]]
- [[Python-GPT4-Survey-Enrichment-Workflow]]
- [[Survey-Sentiment-Scorecard]]
- [[SWITCH-REPT-UNICHAR-Custom-Sorting]]

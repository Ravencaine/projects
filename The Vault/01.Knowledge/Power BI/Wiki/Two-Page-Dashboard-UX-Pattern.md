---
created: 2026-08-10
updated: 2026-08-10
source: Building a Product Hierarchy Analytics Dashboard in Power BI: A Beginner's Journey
source_url: https://medium.com/@mitalimunot64/building-a-product-hierarchy-analytics-dashboard-in-power-bi-a-beginners-journey-6b3c72375d41
note_type: pattern
tags: [power-bi, dashboard-design, user-experience, page-structure, drill-down, navigation]
---

# Two-Page Dashboard UX Pattern: Overview First, Details Second

Split a dashboard into two pages that serve two distinct mental modes: a **summary page** that orients a first-time viewer, and a **drill-down page** for someone who already knows what they want to investigate. This is a UX decision, not a technical one — it reflects how real curiosity flows.

## Two Pages, Two Mindsets

| Page | Mental mode | Goal |
|------|-------------|------|
| Page 1 — Executive Summary | "Orient me" | Give a first-time viewer the shape of the data in 10 seconds |
| Page 2 — Analysis / Drill-Down | "Let me investigate" | Go from a rough question to an exact answer in 3 clicks |

## Page 1: Executive Summary

**Who it's for:** Anyone who needs the big picture fast — executives, recruiters, classmates.

**Structure:**
- KPI cards at the top (4–6 key numbers)
- Summary visuals that answer one question each
- Filter panels so the page is interactive, not static
- No detail tables — the numbers lead, not the raw data

**Example KPIs (Product Hierarchy):** Total Products, Primary Categories, Secondary Categories, Tertiary Categories. These 4 numbers alone communicate the catalog's structure.

## Page 2: Drill-Down / Analysis

**Who it's for:** Someone who has seen Page 1 and now has a specific question.

**Structure:**
- Multiple slicers stacked for top-down hierarchy navigation
- More granular visuals (treemaps, detailed bar charts)
- A detail table at the bottom showing exact records behind the numbers
- "After exploring the visuals, the table is where you go to actually see the raw products behind the numbers"

## The Principle

> "I could have crammed everything onto one page. I didn't, because a summary view and a drill-down view serve two different mental modes."

Cramming everything onto one page forces the user to hold both mental modes simultaneously — overwhelming and slow.

## KPI Cards Are Underrated

Four KPI cards at the top of Page 1 take five seconds to build and do ~30% of the communication work in the entire dashboard. They give the user a mental model before they read a single chart.

## Question-First, Chart-Second

Before building any visual: sketch the questions it needs to answer. Once the question is clear, picking the right chart type follows naturally.

## Related

- [[Treemap-Beats-Bar-Chart-15-Plus-Categories]] — when to choose treemap over bar chart
- [[Cascading-Slicers-Mirror-Hierarchical-Data]] — filter UI matching data structure
- [[Dashboard-Design-Neutral-Tones-Low-Saturation]] — color design principles

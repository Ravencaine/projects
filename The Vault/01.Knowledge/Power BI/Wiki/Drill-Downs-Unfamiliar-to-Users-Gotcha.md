---
created: 2026-08-09
updated: 2026-08-09
source: "Designing for Impact 6 Ideas to Enhance the User Experience and Accessibility of Your Power BI Dashboards.md"
note_type: gotcha
tags: [power-bi, ux, drill-down, non-power-bi-users, gotcha]
---

# Drill-Downs Unfamiliar to Non-Power-BI Users — Gotcha

> **Type:** gotcha
> **Routed to:** Power BI
> **Primary source:** Isabelle Bittar — 2024-03-02

## Problem

Drill-down arrows on Power BI visuals are not obvious to users unfamiliar with Power BI. They don't know to click them, don't know what they do, or don't feel comfortable using them.

## Why It Happens

Drill-down requires two non-obvious behaviors:
1. Discovering that drill-down exists (the arrow buttons are small and unlabeled)
2. Understanding that clicking them changes the visual's granularity

Most Power BI training focuses on slicers, not drill-down. Many end users have never been shown drill-down functionality.

## The Trap

Report authors add drill-down capability to enable detailed exploration — but users never discover or use it.

## Impact

- The drill-down feature is wasted development effort
- Users who could benefit from deeper exploration don't know they can
- Authors may misinterpret lack of drill-down usage as "users don't want detail"

## Solutions

1. **Replace with drop-down slicers:** one click, fully visible, no discovery required
2. **Add on-visual instructions:** text label directly on the chart: "Use the arrows to explore by Category → Subcategory"
3. **If drill-down is essential:** test with real users and actively teach them during UAT

## See Also

- [[Source-Designing-for-Impact-6-Ideas]] — source article
- [[Non-Data-Savvy-User-Design-Pattern]] — design for the actual audience

---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring Data Analysis with Power BI's Decomposition Tree.md"
source_url: "https://databear.com/power-bi-decomposition-tree/"
author: "[[Boniface Muchendu]]"
site: https://databear.com
published: 2024-05-19
source_type: article
kb_routing: Power BI
tags: [power-bi, decomposition-tree, ai-visual, drill-down, hierarchy]
---

# Exploring Data Analysis with Power BI's Decomposition Tree

Boniface Muchendu · Data Bear · databear.com · 2024-05-19

## What this article covers

Decomposition Tree visual: AI visual that breaks down a measure across multiple dimensions in hierarchical view. Setup (Analyze Field + Explain By), manual drill-down (+), AI splits (High/Low Value), limits (50 levels, 5,000 data points), AI splits not supported on-prem/Azure AS/PBIRS/publish to web.

## Fields

- **Analyze Field**: the metric to break down (measure or aggregate)
- **Explain By**: dimensions to use for breakdown

## AI Splits

- **High Value**: AI identifies dimension contributing most to high values
- **Low Value**: AI identifies dimension contributing least

## Limits

- Max 50 levels
- 5,000 data points
- AI splits: on-prem AS, Azure AS, PBIRS, publish to web = NOT supported

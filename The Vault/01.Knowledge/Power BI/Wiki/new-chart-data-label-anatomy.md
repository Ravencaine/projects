---
created: 2026-08-02
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: atomic
tags: [powerbi, chart, data-label, feature]
---

# New Chart Data Label Anatomy (Power BI December 2023+)

Three components make up the new customizable chart data label in Power BI.

## Components

| Component | Description |
|----------|-------------|
| **Value** | The primary metric — does not have to match the chart's underlying measure. Can be any DAX measure. |
| **Title** | Optional header above the value. Defaults to the measure name. Supports dynamic font color via `fx`. |
| **Detail** | Sub-values beneath the main value. Multiple detail sub-values can be added, each independently formatted (font, color, size). |

## Key Advantage

Detail sub-values allow rich context (e.g., total + variance from prior period) in a single label — reduces the need for additional chart elements or tooltips.

## Limitation

The detail background cannot be customized with an `fx` dynamic color — only a fixed background option exists (per series, not per detail sub-value).

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21

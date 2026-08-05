---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Dashboard Design Principles Used by Top Companies.md
note_type: pattern
tags: [power-bi, pattern, slicer, design, filter, ux, discipline]
---

# Slicer Discipline — Filter Intent, Not Fields

A dashboard slicer is a decision the user must make before seeing anything useful. Every slicer added is cognitive load imposed on the viewer — limit slicers to the 3–4 dimensions that actually change the story.

## The Principle

It is tempting to add a slicer for every column in the dataset. Resist this. A credit risk dashboard does not need a slicer for every one of the 22 borrower attributes — just the handful (date, branch, loan type, customer segment) that a risk analyst actually filters by day to day.

## Core Slicer Set

For most dashboards, this set of 3–4 slicers covers 80% of use cases:

| Slicer | When to Include | Notes |
|---|---|---|
| **Date range** | Almost always | Month-to-date vs prior period is the most common comparison |
| **Region / branch** | Any geographically segmented data | Enables comparison across locations |
| **Customer segment** | B2B or multi-segment B2C | Performance comparison across segments |
| **Product category** | When comparing product lines | Product-level performance breakdown |

## When to Add a Slicer

Add a slicer only when:
1. A meaningful subset of users filters by this dimension daily
2. The dimension meaningfully changes the headline numbers
3. Users need to compare across values of this dimension

Do not add a slicer when:
- The dimension is only relevant to 5% of users
- The dimension is better handled by a drill-through page
- Users always want to see the total, not filtered by this dimension

## Slicer Type Choices

| Type | Best For |
|---|---|
| **Dropdown** | 10+ values — saves canvas space |
| **List / checkbox** | 5–10 values — fast scanning |
| **Between (date)** | Date ranges — start/end selection |
| **Slicer** (native list) | Single-select scenarios |

Single-select slicers reduce cognitive load compared to multi-select — users make one decision instead of managing multiple active filters.

## Related

- [[dashboard-design-principles-framework]] — `pattern`
- [[progressive-disclosure-pattern]] — `pattern`
- [[kpi-validation-programmatic-check]] — `pattern`

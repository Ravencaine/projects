---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, gotcha, Power BI]
---

# Stacked native Power BI visuals have independent X-axis scales and can drift apart

<!-- When two native visuals are stacked to create composite charts, their X-axes are independent by default. Even identical min/max bounds produce different pixel layouts because each visual applies different default padding for first/last bucket. This causes bars to float off the timeline gridlines. -->

## Claim

When two native visuals are stacked to create composite charts, their X-axes are independent by default. Even identical min/max bounds produce different pixel layouts because each visual applies different default padding for first/last bucket. This causes bars to float off the timeline gridlines.

## Evidence

- Stated in [[Chart-Alignment-Between-Stacked-Visuals-Gotcha]] — Actual Behaviour

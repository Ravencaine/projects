---
created: 2026-08-01
updated: 2026-08-02
source: "From Messy to Masterpiece The Ultimate Power BI Dashboard Checklist .md"
note_type: atomic
tags: [dashboard-design, rounding, data-presentation, power-bi]
---

# Consistent Rounding — Strike a Balance

Apply uniform rounding rules across all visuals to maintain readability without losing meaningful precision.

## Principle

Mixing decimal places across visuals on the same dashboard creates cognitive friction — the reader cannot compare values quickly when one shows `12.50%` and another shows `13%`. Decide on a rounding convention and apply it everywhere. Over-precision (too many decimals) is as harmful as under-precision (too coarse).

## Guidelines

- Match rounding to the audience's decision threshold: executives may need whole numbers; analysts may need one decimal
- Standard rule: 1–2 decimal places for percentages, whole numbers or 1 decimal for currency
- Never mix `12.5%` and `12.500%` on the same page
- Use `K`, `M`, `B` suffixes for large numbers to reduce visual noise

## Related

- [[label-formatting-units-truncation-tooltips]] — units and formatting go hand-in-hand with rounding
- [[Visual-Design-Principles]] — consistency as a design principle
- [[power-bi-dashboard-checklist]] — consistent formatting across the report

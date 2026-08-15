---
created: 2026-08-10
updated: 2026-08-10
source: BI Case Study: Automating Quarterly Financial Reporting for Contoso Ltd using Power BI and Power Automate
source_url: https://medium.com/@benjohnokezie/automating-quarterly-financial-reporting-for-using-power-bi-and-power-automate-22b07300a706
note_type: atomic
tags: [power-bi, dashboard-design, user-experience, color, cognitive-load]
---

# Dashboard Color — Neutral Tones and Low Saturation

Use neutral tones and low-saturation colors in report design. High-saturation colors pull attention regardless of context, increasing cognitive load. Chart colors should stand out from the background (navigation bar, page background), but the overall palette should remain restrained.

## The Principle

> Bright, high-saturation colors pull the brain's attention regardless of context — even when the data is not the point.

This means users may remember the colorful shapes instead of the data insights. The goal: dashboards attractive enough to be useful, not so flashy they become distracting.

## Practical Rules

| Rule | Reason |
|------|--------|
| Neutral background tones | Reduces visual competition with data |
| Low-saturation accent colors | Conveys data urgency without overwhelming |
| Chart colors > background + nav bar colors | Foreground data must visually dominate |
| Iterate design based on user feedback | First design is a hypothesis; test and refine |

## Design Before/After

- **Before (bad):** High-saturation blues, reds, greens on bright white background; navigation bar same brightness as chart data
- **After (good):** Muted greys, slate blues, desaturated accents; chart colors clearly separated from chrome (nav, background)

## When Bright Colors Are Appropriate

Reserved for:
- True KPI alerts (actual threshold breach, not decoration)
- Status indicators: green/amber/red for genuine state
- Highlighted cells in table matrices

## Related

- [[10-CSS-KPI-Card-Techniques-Reference]] — CSS color techniques for KPI cards
- [[Sticky-Slicer-This-Month-Auto-Select]] — UX improvements that reduce user cognitive effort

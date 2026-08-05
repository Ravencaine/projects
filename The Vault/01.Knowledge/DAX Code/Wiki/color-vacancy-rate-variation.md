---
created: 2026-08-02
updated: 2026-08-05
source: Next-Level Dashboard Design With Power BI's New Card Visual With Reference Labels
note_type: function
tags: [dax, measure, color, conditional, kpi]
---

# Color Vacancy Rate Variation (IF on KPI Variance Sign)

Returns a hex color string based on whether a KPI variance is positive or negative — applied to detail sub-values or font `fx` fields.

```dax
Color Dark Green = "#428C8D"
Color Dark Red   = "#ED3030"

Color Vacancy Rate Variation =
    IF(
        [Vacancy Rate Variation] > 0,
        [Color Dark Red],
        [Color Dark Green]
    )
```

**Logic:** positive variance → red (bad), negative → green (good). Sign convention depends on the metric — for vacancy rate, an increase is unfavorable.

**Usage:** assign `Color Vacancy Rate Variation` to the target measure's data color `fx` or font color `fx` field in the card visual. The measure carries the color decision into the formatting engine.

> Hex constants can be extracted into a shared `Color Constants` note — see `color-process-duration-variation.md` for a parallel example.

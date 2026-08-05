---
created: 2026-08-04
note_type: pattern
tags: [power-bi, dax, forecast, conditional-flag, comparison]
---

# Forecast vs Actual Flag Pattern

A DAX pattern that creates a categorical flag comparing forecast and actual values — useful for visual color-coding, slicers, and narrative measures.

## The Flag Pattern

```dax
Forecast vs Actual Flag =
VAR Actual = [Total Sales]
VAR Forecast = [Forecasted Sales]
VAR Diff = Actual - Forecast
VAR DiffPct = DIVIDE(Diff, Forecast)
RETURN
    SWITCH(
        TRUE(),
        ISBLANK(Forecast), BLANK(),
        DiffPct >= 0.1, "📈 Beat",
        DiffPct >= 0,   "✓ On Target",
        DiffPct >= -0.1, "⚠️ Miss",
        TRUE,           "❌ Badly Miss"
    )
```

## Color Mapping for Visual Conditional Formatting

| Flag | Hex Color | Use Case |
|------|-----------|----------|
| Beat | `#00B050` (Green) | Exceeded forecast by ≥10% |
| On Target | `#92D050` (Light Green) | Within ±10% of forecast |
| Miss | `#FFC000` (Amber) | Missed by 10–25% |
| Badly Miss | `#FF0000` (Red) | Missed by >25% |

Apply via **Field → Cell Elements → Background Color** using the measure:

```dax
Flag Background Color =
SWITCH(
    [Forecast vs Actual Flag],
    "📈 Beat", "#00B050",
    "✓ On Target", "#92D050",
    "⚠️ Miss", "#FFC000",
    "❌ Badly Miss", "#FF0000",
    "#CCCCCC"
)
```

## Variance Measure (for tooltip)

```dax
Forecast Variance =
VAR Actual = [Total Sales]
VAR Forecast = [Forecasted Sales]
RETURN
    DIVIDE(Actual - Forecast, Forecast)
```

## Related

- [[holt-winters-forecasting-in-power-query]] — forecast generation in Power Query
- [[conditional-variance-display-percent-hide]] — hiding small variances in visuals

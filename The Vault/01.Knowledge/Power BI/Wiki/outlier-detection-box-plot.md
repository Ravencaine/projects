---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [outliers, box-plot, detection, extreme-values, anomaly]
---

# Outlier Detection via Box Plot

A box plot flags extreme values as outliers — points beyond 1.5 × IQR from the nearest quartile.

## Purpose

Identify data points that are unexpectedly far from the typical range. Outliers may indicate data entry errors, measurement failures, or genuine extreme observations.

## Components

| Component | Definition |
|-----------|-----------|
| **IQR** | Interquartile Range = Q3 − Q1 |
| **Lower bound** | Q1 − 1.5 × IQR |
| **Upper bound** | Q3 + 1.5 × IQR |
| **Outliers** | Any data point beyond the bounds |

## Interpretation

| Scenario | Likely cause |
|---------|-------------|
| Outlier at 6.7 instead of 67 | Data entry error — check original source |
| Outlier at 0.1°C sensor reading | Sensor failure |
| Outlier at 99.9% satisfaction score | Genuine extreme but valid data |

## How to Detect in Power BI

1. Create a Python Visual with matplotlib box plot: `showfliers=True`
2. Hover over outlier dots to identify which entities they represent
3. Return to Power Query to investigate or fix

## What to Do with Outliers

| Option | When |
|--------|------|
| **Delete** | Clearly a data entry or measurement error |
| **Cap** | Replace with boundary value (winsorisation) |
| **Investigate** | Not sure if error or real — check source |
| **Keep** | Genuine extreme value that belongs in the dataset |

## Related

- [[outlier-handling-strategies]]
- [[box-plot-anatomy]]
- [[anomaly-detection-visual]]

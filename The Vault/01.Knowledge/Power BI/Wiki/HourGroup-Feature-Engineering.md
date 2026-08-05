---
created: 2026-08-05
updated: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
note_type: atomic
tags: [feature-engineering, hour-group, time-bucketing, anomaly-detection, python]
---

# HourGroup Feature Engineering

Converting raw time strings into categorical time-period buckets (Morning, Midday, Afternoon, Evening, Night) adds context that helps anomaly detection models flag suspicious off-hours transactions.

## Definition

A feature engineering step that takes a raw `Time` string column (e.g., `"14:36"`) and maps it to one of five named time periods. The bucketed column (`HourGroup`) is then one-hot encoded as a model feature.

## Key Points

- **Replaces granular time with semantic context:** Raw `"14:36"` is harder for a model to use than `"Afternoon"` — bucketing turns a high-cardinality string into a low-cardinality category.
- **Captures off-hours risk:** Expenses at Night or outside business hours are more suspicious for many expense types.
- **Customisable buckets:** The boundaries depend on the business context — hospitality, shift-based teams, or global companies may need different ranges.
- **Implementation:** A Python function parses the hour integer and maps it to a bucket string; applied via `df['Time'].apply(group_hour)`.

## HourGroup Mapping (Isabelle Bittar's example)

| Hour range | HourGroup |
|-----------|-----------|
| 06:00–09:59 | Morning |
| 10:00–13:59 | Midday |
| 14:00–17:59 | Afternoon |
| 18:00–21:59 | Evening |
| 22:00–05:59 | Night |

## Related

- [[Feature-Engineering-for-Anomaly-Detection]]
- [[Isolation-Forest-Power-Query-Pattern]]
- [[Isolation-Forest-Python-Pandas-One-Hot-Snippet]]
- [[python-script-in-power-query]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[anomaly-detection-data-requirements]]

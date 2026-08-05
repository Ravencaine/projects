---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [box-plot, anatomy, min, q1, mean, median, q3, max, whiskers, iqr]
---

# Box Plot Anatomy

A box plot decomposes a distribution into six statistics visualised as a box, whiskers, and optional outlier points.

## Definition

```
        ──── Max (excluding outliers)
        │
   ─────┤ Q3 (75th percentile)
   │    │
   │█████│ ← IQR = Q3 - Q1
   │    │
   ─────┤ Q1 (25th percentile)
        │
        ──── Min (excluding outliers)
        ▲ Mean (optional)
        │ ← Median (50th percentile)
```

## Key Points

| Component | Statistic | What it shows |
|-----------|-----------|---------------|
| **Box** | Q1 to Q3 | Middle 50% of data (IQR) |
| **Line in box** | Median | 50th percentile |
| **Triangle** | Mean | Average value |
| **Whiskers** | Min / Max (within 1.5×IQR) | Typical range |
| **Dots** | Outliers | Points beyond 1.5 × IQR |

## Interpreting Shape

| Observation | Conclusion |
|-------------|-----------|
| Mean ≈ Median, box symmetrical | Normal distribution |
| Mean > Median, box left of centre | Right-skewed |
| Mean < Median, box right of centre | Left-skewed |
| Long whisker + many dots | Heavy-tailed / many outliers |

## Related

- [[box-plot-visual]]
- [[distribution-shapes-normal-right-skewed-left-skewed]]
- [[outlier-detection-box-plot]]

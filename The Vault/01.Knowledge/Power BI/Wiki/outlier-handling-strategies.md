---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [outliers, handling, delete, cap, train-model]
---

# Outlier Handling — Decision Tree

Four options for handling outliers once detected.

## Purpose

Outliers require different responses depending on whether they are errors or genuine extreme values.

## Decision Tree

```
Outlier detected via box plot
        │
        ▼
Is it a data error? ──Yes──► Delete the row
        │ No
        ▼
Is it a genuine extreme value? ──Yes──► Keep (document it)
        │ No / Unknown
        ▼
Is the model sensitive to extremes? ──Yes──► Cap at boundary
        │ No
        ▼
Train model to recognise outlier class
```

## Strategies

| Strategy | Method | Use when |
|---------|--------|---------|
| **Delete** | Remove row in Power Query | Clearly erroneous value (e.g., negative age) |
| **Cap / Winsorise** | Replace with Q3+1.5×IQR | Genuine extreme but distorting the model |
| **Investigate** | Check source system | Not sure if error or real |
| **Keep** | No action | Genuine valid extreme value |
| **Train to recognise** | Use anomaly detection | outliers ARE the signal (e.g., fraud, machine failure) |

## Related

- [[outlier-detection-box-plot]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[bias-not-always-a-problem]]

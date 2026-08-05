---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: gotcha
tags: [data-volume, model-accuracy, plateau, diminishing-returns]
---

# Model Accuracy Plateaus Before You Think

Adding more data improves accuracy only up to a point — beyond that point, more data provides diminishing returns, not infinite improvement.

## Expected Behaviour

More training data = more model accuracy. The curve is always upward-sloping.

## Actual Behaviour

Model accuracy follows a curve: it improves quickly with initial data, then the improvement slows and eventually plateaus. Beyond the plateau, adding more data provides negligible accuracy improvement.

```
Accuracy
  0.9 |          _______________
  0.8 |        /
  0.7 |      /
  0.6 |    /          ← accuracy plateau
  0.5 |  /
  0.4 |/
      0   1K   10K   100K   1M rows
              Training data size
```

## Why It Happens

- The model has learned the learnable patterns — remaining errors are irreducible noise
- The model's representational capacity is exhausted (e.g., a linear model can't capture nonlinear relationships regardless of data size)
- The data lacks sufficient signal for the target variable

## What to Do Instead of Adding More Data

1. **Improve feature engineering**: add new informative features
2. **Improve data quality**: fix errors, handle missing data better
3. **Use a more powerful model**: switch from linear to gradient boosting or neural networks
4. **Address bias**: ensure the data represents the target population

## Related

- [[garbage-in-garbage-out]]
- [[feature-engineering-versus-selection-versus-importance]]

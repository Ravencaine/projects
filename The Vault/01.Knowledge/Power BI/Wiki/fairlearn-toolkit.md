---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: reference
tags: [fairlearn, reference, fairness-metrics, toolkit, microsoft]
---

# Fairlearn — Reference Note

Microsoft's open-source fairness assessment and mitigation library for ML models.

## Quick Reference

```bash
pip install fairlearn
```

## Core Modules

| Module | Contents |
|--------|---------|
| `fairlearn.metrics` | MetricFrame, selection_rate, demographic_parity_difference |
| `fairlearn.reductions` | ExponentiatedGradient, ThresholdOptimizer |
| `fairlearn.datasets` | load_adult (UCI Census income dataset) |
| `fairlearn.visualizations` | RadarChart, group_summary_stacked |

## Key Classes

| Class | Purpose |
|-------|---------|
| `MetricFrame` | Compute metrics broken down by sensitive feature groups |
| `ExponentiatedGradient` | Fairness-aware training with demographic parity constraints |
| `ThresholdOptimizer` | Post-hoc threshold adjustment for fairness |

## Common Fairness Metrics

```python
from fairlearn.metrics import (
    demographic_parity_difference,
    equalized_odds_difference,
    selection_rate
)

dpd = demographic_parity_difference(y_true, y_pred, sensitive_features=s_test)
eod = equalized_odds_difference(y_true, y_pred, sensitive_features=s_test)
```

## Related

- [[fair-models-identify-mitigate-unfairness]]
- [[responsible-ai-six-principles]]

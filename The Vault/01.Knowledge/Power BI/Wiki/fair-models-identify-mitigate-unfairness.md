---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [fairlearn, fairness, fairness-assessment, identify-unfairness, mitigate]
---

# Fair Models — Identify and Mitigate Unfairness

Use Fairlearn to assess fairness metrics across demographic groups and apply mitigation algorithms.

## Purpose

A model that performs well overall may perform poorly for specific demographic groups. Fairlearn identifies these disparities and provides algorithms to mitigate them.

## Fairlearn Workflow

### 1. Identify Unfairness

```python
from fairlearn.metrics import MetricFrame
mf = MetricFrame(
    metrics=accuracy_score,
    y_true=y_test,
    y_pred=y_pred,
    sensitive_features=sensitive_test  # e.g., gender, race
)
mf.by_group.plot.bar(subplots=True)
```

This shows accuracy broken down by group — disparity becomes immediately visible.

### 2. Assess Fairness Metrics

| Metric | What it measures |
|--------|-----------------|
| **Selection rate** | % predicted positive per group |
| **Accuracy parity** | Accuracy equal across groups? |
| **False positive rate parity** | FPR equal across groups? |
| **Equalised odds** | TPR and FPR equal across groups |

### 3. Mitigate

Fairlearn provides three mitigation approaches:

| Approach | When to use |
|---------|------------|
| **Exponentiated Gradient** | Grid search over fairness constraints; best for most cases |
| **Threshold Optimiser** | Adjust decision thresholds per group; post-hoc |
| **Correlation Remover** | Remove correlation with sensitive attributes; pre-processing |

## Azure ML Integration

Azure ML Designer → Fairlearn can be used as a Python component within the Designer pipeline.

## Related

- [[fairlearn-toolkit]]
- [[responsible-ai-six-principles]]
- [[mitigating-bias-in-ml-datasets]]

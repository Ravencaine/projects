---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [bias, ml, dataset, resampling, algorithm, minority-class]
---

# Mitigating Bias in ML Datasets

Bias in training data causes models to reinforce unfair patterns. Mitigation requires awareness of what bias means and which techniques to apply.

## Purpose

A biased dataset leads to a biased model that performs unequally across different groups.

## Components

### What Bias Looks Like

- A hiring model trained on historical data where 80% of hires were male → learns to favour male candidates
- A healthcare model trained on a hospital with predominantly elderly patients → performs poorly on younger patients

### Mitigation Strategies

| Strategy | Approach |
|---------|---------|
| **Resampling** | Oversample minority class or undersample majority class |
| **Algorithm selection** | Some algorithms handle imbalanced data better (e.g., anomaly detection for rare-event classification) |
| **Synthetic data** | SMOTE: generate synthetic minority class examples |
| **Stratified splits** | Ensure train/test splits maintain class proportions |
| **Bias-aware algorithms** | Use fairness-aware ML libraries (e.g., Fairlearn) |

## Key Points

- Bias is not always a problem — sometimes minority class IS the signal (e.g., fraud detection)
- The right mitigation depends on whether bias is noise or signal
- Azure ML Designer supports stratified splitting to preserve class distributions

## Related

- [[bias-not-always-a-problem]]
- [[fair-models-identify-mitigate-unfairness]]
- [[responsible-ai-six-principles]]

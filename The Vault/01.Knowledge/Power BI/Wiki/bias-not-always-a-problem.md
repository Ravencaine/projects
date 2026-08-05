---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: gotcha
tags: [bias, minority-class, signal, anomaly-detection, fraud]
---

# Bias Is Not Always a Problem — Sometimes It's the Signal

Imbalanced classes are not always noise. Sometimes the minority class is exactly what the model should detect.

## Expected Behaviour

Bias (imbalanced classes) in training data is a problem that must be fixed through resampling or algorithm changes.

## Actual Behaviour

For some use cases, the minority class is the target. Fixing the imbalance by oversampling or undersampling the majority class would destroy the signal.

## Why It Happens

- In **fraud detection**, fraudulent transactions are <1% of all transactions. The imbalance IS the business problem.
- In **anomaly detection**, the goal is to find the rare event. The rarity is the signal.
- In **predictive maintenance**, failures are rare by definition. A model that predicts "no failure" 99% of the time is not useful; the model must be sensitive to the rare failure pattern.

## How to Handle It

Choose the right **algorithm** for the imbalance, not the other way around:

- Use **anomaly detection** (unsupervised) for rare-event problems
- Use algorithms designed for imbalanced data: SMOTE, class-weighted loss functions
- Do NOT blindly oversample/undersample when the minority class IS the business problem

## Related

- [[mitigating-bias-in-ml-datasets]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[fair-models-identify-mitigate-unfairness]]

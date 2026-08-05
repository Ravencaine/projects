---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: gotcha
tags: [data-quality, garbage-in-garbage-out, gigo, ml-prerequisite]
---

# Garbage In, Garbage Out — Data Quality Over Data Quantity

The most accurate model is worthless if trained on poor-quality data. Data quality is the single most important prerequisite for reliable AI.

## Expected Behaviour

Adding more data improves model accuracy. A larger training set means the model sees more examples and generalises better.

## Actual Behaviour

Adding noisy, biased, or incomplete data to a model can make it *worse*. A model trained on poor-quality data will confidently produce poor-quality predictions — and often appear to be performing well in evaluation because the evaluation data has the same quality problems.

## Why It Happens

- **Noisy labels**: training examples with incorrect labels teach the model the wrong thing
- **Missing data**: null values handled poorly introduce systematic bias
- **Biased samples**: training data that doesn't represent the production population
- **Measurement error**: sensor noise, data entry errors, parsing mistakes
- **Leakage**: features that contain information from the target variable outside the intended time window

## What to Do

1. **Profile before training**: use Column Quality, Distribution, and Profile
2. **Clean before transforming**: fix data entry errors before creating features
3. **Validate representativeness**: does training data look like production data?
4. **Audit for leakage**: check that features don't encode the target before the event
5. **Document known issues**: if data quality is imperfect, document it and account for it in interpretation

## Related

- [[column-profiling-default-1000-row-cap]]
- [[handling-missing-data-strategies]]
- [[mitigating-bias-in-ml-datasets]]

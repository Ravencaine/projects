---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [differential-privacy, smartnoise, privacy, noise-injection, statistical-privacy]
---

# Differential Privacy — SmartNoise

A mathematical guarantee that adding noise to individual data points prevents re-identification while preserving aggregate statistical properties.

## Definition

Differential privacy adds carefully calibrated random noise to query results so that the presence or absence of any single individual cannot be determined — but aggregate statistics (mean, histogram, model parameters) remain accurate.

## Key Properties

| Property | Effect |
|---------|--------|
| **ε (epsilon)** | Privacy budget — smaller = more private, less accurate |
| **δ (delta)** | Probability of privacy violation (set very small) |
| **Noise distribution** | Calibrated to ε and sensitivity (max change from one record) |

## SmartNoise

SmartNoise is Microsoft's open-source differential privacy library:

```
pip install smartnoise-sdk
```

It provides:
- **SQL-based aggregations** with differential privacy guarantees
- **Core libraries** for Python: mockdp, pydp
- **Azure SQL integration** for differentially private queries

## Why It Matters

Even after removing direct identifiers, aggregate statistics can still leak individual information. Differential privacy provides a mathematical proof that this is not possible.

## Related

- [[remove-pii-from-datasets]]
- [[responsible-ai-six-principles]]

---
created: 2026-08-05
updated: 2026-08-05
source: 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)
note_type: atomic
tags: [data-cleaning, outlier, data-quality, min-max, power-bi]
---

# Ignoring Outliers: Detection and Action

An outlier (e.g., ₹20,00,000 for a keychain) silently warps averages, disrupts forecasting models, and renders trend lines useless — until a stakeholder asks why a keychain sale looks like a real estate transaction.

## The Problem

Outliers distort statistical aggregates and visualisations:

- **Mean (average):** Highly sensitive to outliers — one extreme value pulls the average dramatically
- **Trend lines:** A single spike creates a false trend that doesn't represent the actual pattern
- **Forecasting models:** Training data with unhandled outliers produces biased predictions

## Most Common Cause

> "Did a tired data entry operator fall asleep on the zero key?" — DigitalBYKewat

A keychain priced at ₹2,000 entered as ₹20,00,000. Most outliers are human data entry errors, not genuine anomalies.

## Detection: The Min/Max QA Check

Before publishing any report, check the minimum and maximum values of every numeric column:

| Column | Min | Max | Expected Max | Status |
|--------|-----|-----|--------------|--------|
| Unit Price | 0.50 | 2,000 | 5,000 | ✓ |
| Transaction Amount | 10 | 20,00,000 | 50,000 | ⚠ Investigate |

If a value "looks like a phone number instead of a price," it needs investigation.

## Investigation Steps

1. Filter the visual to the outlier rows
2. Check if the original source data matches (data entry error vs genuine)
3. Decide: correct the value, replace with `NULL`, or document as a known anomaly

## When Outliers Are Genuine

If the outlier is real (e.g., a luxury item with a genuinely high price), use the **median** instead of the mean for central tendency measures. The median is robust to outliers.

```dax
Median Price = MEDIAN('Products'[Price])
```

## Prevention

- Data validation rules at source entry (e.g., max value constraint)
- Automated min/max alerts in the data pipeline
- Pre-publish review of statistical summaries

## Related

- [[Dashboard-Health-Checklist]]
- [[Data-Cleaning-Pipeline-Flow]]

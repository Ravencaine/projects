---
created: 2026-08-05
updated: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
source_url: https://medium.com/the-bi-corner/how-to-do-anomaly-detection-in-power-bi-no-external-tools-needed-b12973e58b2b
note_type: source
tags: [power-bi, python, power-query, anomaly-detection, isolation-forest, employee-expenses, unsupervised]
---

# How to Do Anomaly Detection in Power BI (Isabelle Bittar)

A hands-on case study using Python and Isolation Forest — run entirely inside Power Query to flag suspicious employee expenses.

> **Type:** article
> **Author:** Isabelle Bittar (KI Data Science)
> **Published:** 2025-08-09
> **URL:** https://medium.com/the-bi-corner/how-to-do-anomaly-detection-in-power-bi-no-external-tools-needed-b12973e58b2b
> **Routed to:** Power BI (primary), Power Query

## Summary

Isabelle Bittar demonstrates how to run an Isolation Forest unsupervised anomaly detection model entirely inside Power Query using Python — flagging suspicious employee expenses (unusually high amounts, odd hours, duplicate entries) without external tools, Premium features, or labeled training data.

## Key Claims

- Isolation Forest isolates anomalies faster than normal points by random data splitting — fewer splits = more anomalous
- Unsupervised ML requires no labeled fraud examples — the model learns "normal" from the data itself
- Python inside Power Query accepts `dataset` as a pandas DataFrame and returns one DataFrame
- Feature engineering drives model quality: bucketing time into HourGroup, one-hot encoding categoricals
- `contamination=0.02` means ~2% of rows are flagged as anomalies
- Dashboard UX matters: conditional formatting with clear Anomaly/Normal pills drives user adoption

## Notable Details

- The PBIX is available for download (Google Drive link in source)
- The Python script drops nulls in Amount, Category, Department, PaymentType, Time before modelling
- One-hot encoding via `pd.get_dummies()` converts all categorical features to numeric
- Results are merged back into the full dataset (including rows with nulls that were excluded from the model)
- Customisation options: adjust contamination, add/modify features, change hour buckets, add review labels, wire Power Automate alerts
- Power BI's built-in Anomaly Detection (SR-CNN) requires time-series data; this approach works on any tabular structured data

## Extracted Notes

Links to notes derived from this source:

- [[Isolation-Forest-How-It-Works]] — `atomic` — how Isolation Forest isolates anomalies via random splitting
- [[Isolation-Forest-Power-Query-Pattern]] — `pattern` — the full Python pattern: null-drop → HourGroup → one-hot → fit → merge back
- [[HourGroup-Feature-Engineering]] — `atomic` — bucketing raw time strings into time-period categories
- [[Feature-Engineering-for-Anomaly-Detection]] — `atomic` — which features to include and why
- [[Isolation-Forest-Parameters-Quick-Reference]] — `reference` — `contamination`, `n_estimators`, `random_state` at a glance
- [[Python-Data-Preparation-for-ML-Power-Query]] — `reference` — null-drop, one-hot, merge-back checklist
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[anomaly-detection-data-requirements]]
- [[python-script-in-power-query]]

## Metadata

| Field | Value |
|-------|-------|
| Source file | How to Do Anomaly Detection in Power BI (Isabelle Bittar).md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-05 |
| Word count | ~750 |
| PBIX attachment | [Anomaly_Detection_Power_BI.pbix](file:///C:/Users/krlsa/Documents/00%20Projects/The%20Vault/99.System/Attachments/Anomaly_Detection_Power_BI.pbix) |

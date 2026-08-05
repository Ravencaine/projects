---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [pii, personally-identifiable-information, remove, redact, gdpr, privacy]
---

# Remove PII from Datasets

Identify and remove or mask personally identifiable information before using data in AI/ML pipelines.

## Purpose

Training ML models on PII creates privacy, compliance (GDPR, CCPA), and ethical risks. PII must be identified and removed or pseudonymised before training.

## Categories of PII

| Category | Examples |
|----------|---------|
| Direct identifiers | Name, email, phone number, SSN, passport number |
| Indirect identifiers | ZIP code + birth date, race + gender + birth date |
| Sensitive data | Health records, financial data, biometric data |

## Techniques

| Technique | Method | When to use |
|-----------|--------|------------|
| **Remove columns** | Delete columns containing PII | Column is entirely PII |
| **Pseudonymisation** | Replace PII with random IDs | Need to preserve relationships |
| **Generalisation** | Round dates to year, ZIP to region | Reduce precision while preserving signal |
| **Aggregation** | Group by region instead of individual | Analysis at population level |

## Tools

- **Azure Cognitive Services PII Detection**: flags PII in text
- **Power Query**: filter or replace identified PII columns
- **Azure ML Designer**: filter columns before training

## Related

- [[pii-detection]]
- [[differential-privacy-smartnoise]]
- [[responsible-ai-six-principles]]

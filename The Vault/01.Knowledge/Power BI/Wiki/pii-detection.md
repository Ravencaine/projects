---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [cognitive-services, pii-detection, personally-identifiable-information, api, privacy]
---

# PII Detection — Flag Personally Identifiable Information

Detects and redacts personally identifiable information (PII) in text: names, email addresses, phone numbers, SSNs, and more.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Text Analytics |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/entities/recognition/pii` |
| Method | POST |
| Input | `{ "documents": [{ "id": "...", "language": "en", "text": "..." }] }` |
| Output | `{ "documents": [{ "entities": [{ "text", "category", "subcategory", "confidenceScore" }] }] }` |

## PII Categories

| Category | Examples |
|----------|---------|
| Person | Full name |
| Email | user@example.com |
| Phone | +1-555-123-4567 |
| SSN | 123-45-6789 |
| Credit Card | 4111-1111-1111-1111 |
| Address | 123 Main Street, Redmond, WA |
| DateOfBirth | 01/15/1980 |

## Use Cases

- Flag PII in survey responses before sharing with third parties
- Audit datasets for compliance with GDPR, CCPA
- Pre-process data before publishing — remove PII from customer feedback datasets

## Related

- [[remove-pii-from-datasets]]
- [[responsible-ai-six-principles]]

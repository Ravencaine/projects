---
created: 2026-08-05
updated: 2026-08-05
source: 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)
note_type: atomic
tags: [data-cleaning, date-format, iso, power-query, locale, data-quality]
---

# Inconsistent Date Formats: ISO Standardisation

The same date written as `01/04/2026`, `04-01-2026`, and `2026/04/01` is unambiguous to a human but catastrophic for a BI tool — grouping sales into the wrong month or year without warning.

## The Problem

Different source systems export dates using regional conventions:

| Format | Ambiguity |
|--------|-----------|
| `DD/MM/YYYY` | `01/04/2026` = 1 April or 1 January? |
| `MM/DD/YYYY` | `04/01/2026` = 4 January or April 1? |
| `DD-MM-YYYY` | Same ambiguity as slash variants |
| `YYYY-MM-DD` | Unambiguous — ISO 8601 |

Power BI parses dates during import. If the import locale does not match the source format, the dates are silently misinterpreted.

## Real-World Example

A retailer experienced a sudden, unexplained drop in March sales. Investigation revealed that thousands of April transactions had been imported as January due to conflicting regional date formats in the source exports.

## The Fix: ISO Format

**Standardise at the source:** Convert all source systems to emit `YYYY-MM-DD` (ISO 8601) before any export.

**Standardise in Power Query:**

1. Change column type using **Transform → Data Type → Date**
2. If regional formats are mixed: **Detect Data Type** or manually set the locale (**Use Locale → Set the locale that matches the source**)
3. For ambiguous sources: split the string, reorder components, recombine as `Date.FromText()`

## Power Query Locale Setting

When changing column type, click the **ABC icon** → **Using Locale** → select the source system's locale (e.g., UK for `DD/MM/YYYY`, US for `MM/DD/YYYY`).

## Prevention

- Enforce `YYYY-MM-DD` in source system exports
- Document the date format convention for each data source
- QA step: compare date range in the source vs what Power BI imported — if max date is unexpectedly old, format mis-parsing is likely

## Related

- [[Dashboard-Health-Checklist]]
- [[Data-Cleaning-Pipeline-Flow]]

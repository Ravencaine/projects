---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Data Cleaning Checklist Before Creating Dashboards 12 Essential Steps That Save Hours of Rework.md
source_url: https://medium.com/@digitalbykewat/power-bi-data-cleaning-checklist-before-creating-dashboards-12-essential-steps-that-save-hours-of-28ee73ac8c09
note_type: source
tags: [power-bi, power-query, medium, data-cleaning, data-quality, checklist, best-practices]
---

# Power BI Data Cleaning Checklist Before Creating Dashboards

A practitioner's 12-step pre-dashboard data cleaning checklist — covering Power Query transformations, relationship validation, numeric auditing, and post-load quality monitoring. Core argument: a dashboard is only as good as the data behind it; 20–30 minutes of cleaning prevents hours of live-meeting embarrassment.

> **Type:** checklist / best practices / data quality
> **Author:** DigitalBYKewat
> **Published:** 2026-07-30
> **URL:** https://medium.com/@digitalbykewat/power-bi-data-cleaning-checklist-before-creating-dashboards-12-essential-steps-that-save-hours-of-28ee73ac8c09
> **Routed to:** Power BI / Power Query

## Summary

12-step data cleaning workflow: (1) Remove duplicates — inspect before removing, create duplicate count column first; (2) Standardize column names — human-readable labels; (3) Fix data types explicitly — never trust auto-detection (dates, decimals, text for IDs, percentages); (4) Handle missing blanks — deliberate resolution: Unknown/Unassigned, remove row, or default value; (5) Trim spaces and hidden characters — Trim + Clean on all text columns; (6) Standardize date formats — single consistent format, check for year 1900/2099 anomalies; (7) Validate numeric values — Column Distribution min/max catches impossible outliers; (8) Validate relationships — unique primary keys, matching foreign keys, no uncontrolled many-to-many; (9) Delete unused columns — lean model; (10) Standardize categories — group typos and regional variants; (11) Test aggregations in Matrix before visuals; (12) Create hidden data quality page. Bonus: `DateTime.LocalNow()` refresh indicator.

## Key Claims

- Auto-detected data types are unreliable — explicitly set every column type
- A blank `Product Category` silently creates a "Blank" chart segment visible to stakeholders
- A relationship that "almost works" produces numbers that "almost look right" — the most dangerous class of error
- 20–30 minutes of upfront cleaning saves hours of live-meeting troubleshooting

## Notable Details

- Duplicate inspection before removal: duplicate count column helps identify why data multiplied
- Trailing spaces: invisible to humans, breaks relationships and grouping in Power BI
- Multi-source date format chaos: `05/06/2026` vs `June 5, 2026` vs `2026-06-05` — standardize before loading
- Numeric outlier examples: Age = 250, Order Quantity = -5, Discount = 300%
- Data quality page: hidden tab with row counts, NULL counts, duplicate counts, min/max dates
- Refresh indicator: `DateTime.LocalNow()` in Power Query → measure for display

## Extracted Notes

- [[power-query-data-cleaning-checklist]] — `pattern` — Full 12-step Power Query workflow with details
- [[data-quality-page-pattern]] — `pattern` — Hidden data quality monitoring tab + refresh indicator
- [[pre-dashboard-cleaning-checklist-reference]] — `reference` — Condensed checklist for pre-build use

## Metadata

| Field | Value |
|-------|-------|
| Source file | `Power BI Data Cleaning Checklist Before Creating Dashboards 12 Essential Steps That Save Hours of Rework.md` |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-02 |
| Word count | ~1,200 |
| Language | English |

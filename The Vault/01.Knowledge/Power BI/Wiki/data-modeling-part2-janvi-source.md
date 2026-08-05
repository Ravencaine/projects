---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling (Part 2).md"
source_url: "https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-data-modeling-part-2-c48c9043280f"
note_type: source
tags: [power-bi, data-modeling, beginner, tutorial, testing, troubleshooting, role-playing-dates]
---

# Data Modeling Part 2 — Janvi Gupta

> **Type:** tutorial / beginner guide
> **Author:** Janvi Gupta
> **Published:** 2025-12-26
> **URL:** https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-data-modeling-part-2-c48c9043280f
> **Routed to:** Power BI
> **KB:** Power BI

## Summary

Part 2 of the data modeling series: building a complete e-commerce model from a flat Excel file. Step-by-step: split flat file into Orders (fact), Customers, Products, and Date dimensions; create the Date table with DAX CALENDAR + ADDCOLUMNS; mark as Date table; build relationships; create measures in a _Measures table; then test with five systematic checks. Also covers common problems and fixes (10x inflated numbers, slicers not working, blank rows) and DAX calculated columns for relationship bridging.

## Key Insight

68% file size reduction from a flat 2.8MB table to a 0.9MB star schema — before any DAX or visualisation.

## Extracted Notes

- [[ecommerce-model-step-by-step]] — `atomic` — flat file → Orders/Customers/Products/Date tables; Duplicate + Remove Columns pattern; DAX Date table with CALENDAR
- [[data-model-5-testing-checks]] — `atomic` — 5 checks: Basic Table, Slicer, Cross-Filter, Blank, Measure; compare totals to source
- [[data-model-5-common-problems-fixes]] — `atomic` — 10x inflated numbers (many-to-many), slicers not filtering (wrong direction), blank rows (orphan keys), role-playing dates
- [[role-playing-date-calculated-columns]] — `atomic` — multiple date columns (OrderDate, ShipDate) need separate calculated columns + USERELATIONSHIP

## Metadata

| Field | Value |
|-------|-------|
| Source file | Master Power BI Introduction to Data Modeling (Part 2).md |
| Ingestion date | 2026-08-01 |
| Word count | ~2,500 |
| Level | Beginner |
| Category | Data Model |

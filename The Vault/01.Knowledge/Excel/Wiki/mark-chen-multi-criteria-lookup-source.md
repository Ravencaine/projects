---
created: 2026-08-01
updated: 2026-08-02
source: "Mastering Multi-Criteria Lookups in Excel with XLOOKUP and SUMPRODUCT.md"
source_url: "https://medium.com/@markchen69/mastering-multi-criteria-lookups-in-excel-with-xlookup-and-sumproduct-58bcc2dd2606"
note_type: source
tags: [excel, lookup, xlookup, sumproduct, filter, multi-criteria]
---

# Multi-Criteria Lookups — Mark Chen

> **Type:** tutorial
> **Author:** Mark Chen
> **Published:** 2024-11-14
> **URL:** https://medium.com/@markchen69/mastering-multi-criteria-lookups-in-excel-with-xlookup-and-sumproduct-58bcc2dd2606
> **Routed to:** Excel
> **KB:** Excel

## Summary

Three techniques for multi-criteria lookups in Excel: XLOOKUP with concatenation (single match), FILTER (multiple matches), SUMPRODUCT (conditional summing). VLOOKUP and HLOOKUP handle only one criterion — these three methods solve that limitation.

## Extracted Notes

- [[xlookup-multi-criteria-concatenation]] — `atomic` — concatenate criteria into one string; concatenate search columns the same way; replace hard-coded values with cell references
- [[filter-function-multi-match]] — `atomic` — FILTER returns all matching rows; multiply conditions with `*`; dynamic array
- [[sumproduct-multi-criteria-summing]] — `atomic` — SUMPRODUCT multiplies boolean arrays by values; SUMIF alternative; returns total instead of individual matches

## Metadata

| Field | Value |
|-------|-------|
| Source file | Mastering Multi-Criteria Lookups in Excel with XLOOKUP and SUMPRODUCT.md |
| Ingestion date | 2026-08-01 |
| Word count | ~600 |
| Level | Intermediate |
| Category | Lookup |

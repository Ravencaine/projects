---
created: 2026-08-01
updated: 2026-08-02
source: "TREATAS in DAX - Connecting Unrelated Tables Like Magic.md"
source_url: "https://medium.com/write-your-world/treatas-in-dax-connecting-unrelated-tables-like-magic-653b0ab5f28b"
note_type: source
tags: [dax, treatas, virtual-relationships, virtual-modeling, intermediate]
---

# TREATAS in DAX — Tejwani

> **Type:** virtual relationship technique / intermediate
> **Author:** Gulab Chand Tejwani
> **Published:** 2026-01-19
> **Routed to:** DAX Code
> **KB:** DAX Code

## Summary

TREATAS applies filter values from one table onto another as if a relationship existed — virtual relationship inside CALCULATE. Handles duplicate keys, data type mismatches, security constraints, and what-if scenarios where physical relationships fail. Key functions: TREATAS, VALUES, FILTER, SELECTEDVALUE. Performance cost: re-creates filter maps on each measure evaluation.

## Extracted Notes

- [[treatas-virtual-relationships]] — `atomic` — TREATAS syntax, VALUES pattern, marketing/Forecast examples, virtual vs physical relationship
- [[treatas-dynamic-segments-whatif]] — `atomic` — TREATAS + FILTER for dynamic segment selector, range filters, what-if scenarios without physical join
- [[treatas-uselationship-crossfilter]] — `atomic` — TREATAS vs USERELATIONSHIP vs CROSSFILTER: when each fits; rule of thumb
- [[treatas-performance-pitfalls]] — `atomic` — data type mismatch (CONVERT), high cardinality, filter collisions, nested TREATAS, debugging with CALCULATETABLE

## Metadata

| Field | Value |
|-------|-------|
| Source file | TREATAS in DAX — Connecting Unrelated Tables Like Magic.md |
| Ingestion date | 2026-08-01 |
| Word count | ~1,800 |
| Level | Intermediate |
| Category | Advanced DAX Patterns |

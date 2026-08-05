---
created: 2026-07-27
updated: 2026-08-02
source: "TREATAS in DAX: Connecting Unrelated Tables Like Magic"
source_url: "https://medium.com/write-your-world/treatas-in-dax-connecting-unrelated-tables-like-magic-653b0ab5f28b"
note_type: source
tags: [dax, treatas, virtual-relationships, cross-table-filtering]
---

# TREATAS in DAX: Connecting Unrelated Tables Like Magic

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-09-10
> **URL:** https://medium.com/write-your-world/treatas-in-dax-connecting-unrelated-tables-like-magic-653b0ab5f28b
> **Routed to:** DAX Code

## Summary

TREATAS() applies a table expression's values as filters to a target column without requiring an active relationship, enabling virtual cross-table filtering. Unlike USERELATIONSHIP which activates an existing inactive relationship, TREATAS creates a new filter context from scratch.

## Key Claims

- TREATAS does not require any relationship (active or inactive) between tables
- Common use case: filtering a fact table by a calculated set of values (e.g., top N products from a different table)
- TREATAS returns a table — must be used as a filter argument inside CALCULATE or as a table expression
- TREATAS vs USERELATIONSHIP: TREATAS creates new filter; USERELATIONSHIP activates existing inactive relationship

## Notable Details

- TREATAS requires both sides to have compatible data types (same column type)
- Dynamic segmentation using TREATAS + a parameter table enables "what-if" scenarios
- For performance: TREATAS on small sets (Top N values) is fast; TREATAS on large sets can be expensive

## Extracted Notes

- [[treatas-function]] — function
- [[treatas-vs-userelationship-comparison]] — comparison
- [[treatas-dynamic-segmentation-pattern]] — pattern

## Metadata

| Field | Value |
|-------|-------|
| Source file | TREATAS in DAX — Connecting Unrelated Tables Like Magic.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~1,545 |

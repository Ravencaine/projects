---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
source_url: https://medium.com/@kbaylas/building-a-data-warehouse-from-scratch-a-case-study-in-kimball-modeling-bcbcaacd5b95
note_type: source
tags: [data-warehouse, kimball, dimensional-modeling, etl, elt, medallion, data-modeling]
---

# Kimball Dimensional Modeling Case Study — Baylas 2026

Real-world data warehouse built from scratch using Kimball methodology, blended with medallion architecture and ELT practices. Covers methodology choice, three-layer architecture, common cleansing problems, dimensional modeling decisions, and a data quality philosophy.

> **Type:** article
> **Author:** Kaan Baylas
> **Published:** 2026-07-02
> **URL:** https://medium.com/@kbaylas/building-a-data-warehouse-from-scratch-a-case-study-in-kimball-modeling-bcbcaacd5b95
> **Routed to:** Data Modeling

## Summary

A practical account of building a data warehouse from transactional source systems using Kimball dimensional modeling, adapted with a medallion architecture (raw → cleansed → dimensional) and ELT patterns. The project prioritized speed of delivery, business-user clarity, and transparent data quality handling over strict adherence to any single methodology.

## Key Claims

- Operational systems fail in three ways: performance collision, data model mismatch, and the multiple-source problem — all solved by a dedicated analytical layer
- Kimball's bottom-up approach suits small teams needing fast delivery of a single subject area; Inmon suits large organizations with long-term enterprise data strategy; Data Vault suits highly regulated, source-volatile environments
- The medallion architecture (raw / cleansed / dimensional) separates concerns: raw answers "what came in," cleansed answers "what is correct," dimensional answers "how should this be analyzed"
- Common cleansing problems include false-unique keys, inconsistent code meanings, duplicate rows, and type mismatches — all detectable with SQL
- Dimensional decisions include junk dimension criteria, bridge table handling of many-to-many lists, and multi-source merge priority
- Data quality philosophy: flag-and-preserve over delete-or-assume; never silently discard non-matching values
- Indexing should be deferred until the schema is fully stabilized, then applied based on concrete join and filter scenarios

## Notable Details

- Surrogate key pragmatism: only use surrogate keys for low-cardinality dimensions (status, priority, category); high-volume tables keep natural keys (UUIDs) to avoid lookup overhead
- Two independent list columns in a source (locations and access points) were found to have non-parallel indices — required separate bridge tables, not index-matched pairing
- The archive source always takes priority over the active source when merging duplicate entities; load sequencing must respect this (archive first, then delete old active, then upsert remaining active)

## Extracted Notes

Links to notes derived from this source:

- [[inmon-vs-kimball-vs-data-vault-decision-framework]] — `reference` — comparison of three modeling methodologies with decision criteria
- [[medallion-architecture-raw-cleansed-dimensional]] — `reference` — three-layer architecture with ELT and CDC discipline
- [[cdc-column-selection-created-vs-updated-vs-etl-date]] — `reference` — choosing the right CDC column based on table behavior
- [[unique-key-that-isnt-primary-key-verification]] — `atomic` — always verify column uniqueness assumptions with COUNT vs COUNT(DISTINCT)
- [[same-code-different-meanings-code-column-reliability]] — `atomic` — code columns may carry inconsistent meanings over time
- [[flag-and-preserve-data-quality-philosophy]] — `atomic` — never silently discard non-matching values; add is_matched flags instead
- [[junk-dimension-combine-vs-separate]] — `pattern` — decision criteria for combining or separating low-cardinality attributes
- [[bridge-tables-many-to-many-list-unpivoting]] — `pattern` — handling many-to-many relationships and comma-separated list unpivoting
- [[multi-source-merge-archive-priority-load-sequencing]] — `pattern` — archive-first merge strategy and three-step load sequencing
- [[indexing-strategy-defer-until-schema-complete]] — `reference` — when and how to add indexes based on concrete join paths
- [[surrogate-key-pragmatism-when-to-use-natural-keys]] — `pattern` — measured surrogate key usage for high-volume vs low-cardinality tables

## Metadata

| Field | Value |
|-------|-------|
| Source file | <!-- archived after ingestion --> |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-06 |
| Word count | ~5,800 |

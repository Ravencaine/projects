---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: pattern
tags: [data-warehouse, etl, elt, multi-source, merge, upsert, archive]
---

# Multi-Source Merge — Archive Priority and Load Sequencing

When the same entity exists in multiple source tables (e.g., active and archived), the archive version always takes priority. Resolving the merge requires a disciplined three-step load sequencing to prevent double-counting.

## The Problem

A record may appear in both an active table and an archive table simultaneously. If not handled correctly, the same entity is counted twice — once as "active" and once as "archived."

## Rule

> **Archive version always takes priority.** Being archived represents the final, confirmed state of a record.

## Three-Step Load Sequencing

```
1. UPSERT from archive source    ← always first; priority source
2. DELETE old active rows      ← remove records now in archive
3. UPSERT from active source   ← only for records NOT already in archive
```

**Without step 2:** the old "active" row lingers; reports double-count the entity.

**Without step 3:** records that are active but not yet archived are never loaded.

## Related

- [[cdc-column-selection-created-vs-updated-vs-etl-date]] — CDC column choice that drives the upsert condition
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`

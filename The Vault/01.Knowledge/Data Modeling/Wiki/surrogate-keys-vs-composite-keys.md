---
created: 2026-07-27
updated: 2026-08-02
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: pattern
tags: [surrogate-key, composite-key, star-schema, data-modeling, performance]
---

# Surrogate Keys vs Composite Keys

Using integer surrogate keys instead of multi-column composite keys dramatically reduces memory consumption and improves join performance in Power BI — a core performance principle for any star schema.

## Purpose

Composite keys (multi-column string joins like `CONCAT(ProductID, ColorID, SizeID)`) are common in raw source systems but are slow in Power BI because:
- Strings take 1 byte per character (VARCHAR) or 2 bytes per character (NVARCHAR) per row
- Multi-column join predicates require more comparison work than single integer comparisons

A **surrogate key** is an arbitrary integer assigned at ETL time to guarantee uniqueness — typically 4 bytes (int) or even 2 bytes (smallint) regardless of how many source columns it replaces.

## Components

- ETL step: assign a new integer ID at dimension load time
- Join: single integer column instead of multi-column predicate
- Data types: tinyint (1 byte), smallint (2 bytes), int (4 bytes), bigint (8 bytes)

## Memory Comparison

| Key Type | Example | Bytes/Row |
|----------|---------|-----------|
| NVARCHAR composite (6 cols × 20 chars) | "PROD001_RED_CLASSIC_M_" | ~240 bytes |
| Integer surrogate | 1,847,293 | 4 bytes |

At 1 million rows: composite key ≈ 240 MB vs surrogate key ≈ 4 MB — a 60× difference.

## When to Use

- **Always** for fact table foreign keys: always use integer surrogate keys, never multi-column strings
- **Dimension tables**: surrogate key as primary join key, original business keys as attribute columns
- **Bridge tables**: integer keys on both sides of the bridge

## Related

- [[composite-key-strategy-itemkey]] — the CONCAT-based key pattern (different context: D365 F&O)
- [[star-schema-vs-snowflake-schema]] — the schema pattern this key type supports

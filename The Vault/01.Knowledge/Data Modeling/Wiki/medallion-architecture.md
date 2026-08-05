---
created: 2026-07-27
updated: 2026-08-02
source: "3 Easy Data Architecture Interview Questions (Conceptual)"
source_url: "https://medium.com/@jjr8888/3-easy-data-architecture-interview-questions-conceptual-bc156c36e851"
note_type: atomic
tags: [medallion, bronze, silver, gold, delta-lake, databricks]
---

# Medallion Architecture (Bronze / Silver / Gold)

A layered data lake organisation pattern that progressively cleanses and aggregates data from raw source to business-ready assets.

## Definition

The medallion architecture divides a data lake into three progressive layers — Bronze (raw), Silver (validated), Gold (aggregated) — each with a distinct purpose, quality bar, and consumer audience. It answers the question: *where does data live as it moves from raw to report-ready?*

## Key Points

**Bronze (Raw):**
- Landing zone for exact source copies
- Append-only; no transformations
- Enables reprocessing from source if logic changes
- Supports full audit trail

**Silver (Validated):**
- Cleansed and deduplicated data
- Business rules applied; data types enforced
- Ready for analytics teams to query directly

**Gold (Aggregated):**
- Pre-computed metrics and KPIs
- Denormalised for fast dashboard queries
- Business-ready; may be consumed directly by BI tools

**Why it works:**
- Separation of concerns: each layer has a clear owner and purpose
- Reprocessing: Silver and Gold can be rebuilt from Bronze if rules change
- Quality gates: validation happens in controlled stages, not at the end
- Cost optimisation: aggregations in Gold reduce repeated computation

## Examples

A retail organisation ingesting POS data:
1. **Bronze:** raw JSON events from POS terminals landed in ADLS, unchanged
2. **Silver:** events deduplicated, schema-enforced, joined to product dimension — a Synapse serverless table
3. **Gold:** daily sales aggregates by store/date/product written as a Delta Lake table for Power BI DirectQuery

## Related

- [[data-lake-vs-data-warehouse]] — where medallion fits in the lake/warehouse landscape
- [[batch-processing-vs-stream-processing]] — ingestion patterns that feed the Bronze layer

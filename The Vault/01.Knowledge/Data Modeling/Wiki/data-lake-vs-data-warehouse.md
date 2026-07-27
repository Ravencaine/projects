---
created: 2026-07-27
source: "3 Easy Data Architecture Interview Questions (Conceptual)"
source_url: "https://medium.com/@jjr8888/3-easy-data-architecture-interview-questions-conceptual-bc156c36e851"
note_type: atomic
tags: [data-lake, data-warehouse, architecture]
---

# Data Lake vs Data Warehouse

Two foundational storage patterns for analytical workloads — each optimised for different stages of the data lifecycle.

## Definition

A **Data Lake** stores raw data in native format (JSON, CSV, Parquet, images, logs) with schema applied at read time (schema-on-read). A **Data Warehouse** stores processed, structured, pre-modelled data optimised for fast analytical queries with schema enforced at write time (schema-on-write).

## Key Points

- **Schema-on-read** (lake): flexibility to store anything; structure imposed when queried
- **Schema-on-write** (warehouse): enforced structure; data validated before storage
- Data lakes support all data types including unstructured; warehouses are primarily tabular
- Lakes risk becoming "data swamps" without governance — no enforced schema means bad data proliferates
- Modern architectures use **both**: lake for cheap raw storage, warehouse for fast curated queries
- Delta Lake and Lakehouse architectures blur the line by adding warehouse features to a data lake

## Examples

| Pattern | Storage cost | Query speed | Governance |
|---------|-------------|-------------|-----------|
| Data Lake | Low (S3, ADLS) | Slower | Minimal |
| Data Warehouse | Higher (Synapse, Snowflake, BigQuery) | Fast | Strong |

Real-world use: an organisation ingests raw event logs and CSV exports into ADLS (lake), then transforms and curates business-level datasets into Snowflake (warehouse) for dashboarding.

## Related

- [[medallion-architecture]] — layered lake structure that bridges raw lake and curated warehouse
- [[batch-processing-vs-stream-processing]] — how data moves into each

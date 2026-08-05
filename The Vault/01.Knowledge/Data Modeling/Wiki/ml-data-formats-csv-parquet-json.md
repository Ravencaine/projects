---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [data-formats, csv, parquet, json, ml, data-storage]
---

# Data Formats for ML — CSV, Parquet, JSON, Plain Text

Four common formats for storing data used in ML pipelines.

## Quick Reference

| Format | Structure | Compression | Best for | Azure ML support |
|--------|---------|------------|---------|----------------|
| **CSV** | Plain text, comma-delimited | None (large files) | Tabular data, interoperability | Native read/write |
| **Parquet** | Columnar binary | Built-in (small) | Large analytical datasets, columnar queries | Native read/write |
| **JSON** | Key-value, nested | None | Semi-structured data, APIs | Native read/write |
| **Plain text** | Unstructured | None | Text data, NLP pipelines | Read as string |

## When to Use Each

| Scenario | Format |
|---------|--------|
| Small tabular dataset (<100K rows) | CSV |
| Large analytical dataset (>100K rows) | **Parquet** |
| Semi-structured data (nested records) | JSON |
| NLP training (reviews, articles) | Plain text |
| Azure ML AutoML input | CSV or Parquet |
| Azure ML Designer input | CSV |
| Azure Blob Storage | Any |

## Parquet Advantages

- **Columnar storage**: reads only needed columns, fast for analytics
- **Built-in compression**: 2–10× smaller than CSV
- **Schema preservation**: stores column types, not inferred on read
- **Azure ML optimised**: Spark-based engines read Parquet much faster than CSV

## Related

- [[structured-versus-semi-structured-data]]
- [[fixing-data-structure-pq]]

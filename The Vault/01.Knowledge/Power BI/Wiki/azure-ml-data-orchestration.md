---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: reference
tags: [azure-ml, data-factory, synapse, data-orchestration, etl]
---

# Azure ML Data Orchestration — Data Factory and Synapse

Enterprise tools for building data pipelines that feed ML models.

## Azure Data Factory (ADF)

| Capability | What it does |
|-----------|-------------|
| Data integration | Copy data between 90+ connectors (SQL DB, Blob, REST, SAP, etc.) |
| Data flows | Visual ETL/ELT with Spark-based transformation |
| Pipelines | Orchestrate data movement and transformation activities |
| Triggers | Schedule-based, event-based, and tumbling window triggers |

## Azure Synapse Analytics

| Capability | What it does |
|-----------|-------------|
| Serverless SQL | Query data in Blob Storage without provisioning servers |
| Spark pools | Run PySpark/Spark for large-scale data processing |
| Synapse Pipelines | ADF-equivalent orchestration built into Synapse |
| ML integration | Azure ML linked service for scoring in Synapse notebooks |

## When to Use Each

| Scenario | Tool |
|---------|------|
| Simple scheduled ETL | Data Factory |
| Complex transformation with Spark | Data Factory Data Flows |
| Enterprise data warehouse + ML | Synapse Analytics |
| Ad-hoc data exploration | Synapse serverless SQL |
| Notebooks for ML prototyping | Synapse Spark pools |

## Related

- [[data-science-process-five-phases]]
- [[azure-ml-workspace-compute-cluster-dataset]]

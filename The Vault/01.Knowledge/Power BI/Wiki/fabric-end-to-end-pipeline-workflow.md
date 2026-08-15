---
created: 2026-08-13
source: "5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)"
source_url: "https://medium.com/powerbi-microsoft-fabric/5-mistakes-beginners-make-in-microsoft-fabric-and-how-to-avoid-them-269ac1739472"
note_type: workflow
tags: [microsoft-fabric, pipeline, lakehouse, one-lake, direct-lake]
---

# Fabric End-to-End Pipeline: Lakehouse → Transform → Report

The correct way to build in Fabric: route data through the Lakehouse using medallion layers, then connect Power BI via Direct Lake.

## Prerequisites

- A Fabric workspace with a Lakehouse item
- Source data accessible via Fabric Data Factory or uploaded to the workspace
- Power BI report authoring permissions in the same workspace

## Steps

1. **Create a Fabric Lakehouse** in the workspace — this provisions a OneLake container with Bronze/Silver/Gold shortcuts
2. **Load raw data to Bronze** — use Data Factory pipelines or the Lakehouse UI to ingest source files (Excel, CSV, Parquet) into the Bronze layer
3. **Transform to Silver/Gold** — use Fabric Spark notebooks or Dataflow Gen2 to cleanse, deduplicate, and aggregate the data into the Gold layer
4. **Expose Gold via OneLake shortcut** — create a shortcut in the Lakehouse pointing to the Gold folder
5. **Create a Power BI semantic model** — connect to the Lakehouse using Direct Lake storage mode
6. **Build reports** — author Power BI reports on the semantic model and publish to the workspace

## Variations

**Using Dataflow Gen2 instead of Spark:**
- Step 3 can use Dataflow Gen2 for no-code transformations
- Outputs written directly to OneLake Gold layer
- Lower barrier to entry for business analysts

**Using Data Factory for ingestion:**
- Step 2 can be a Data Factory pipeline with copy activities
- Supports broad connector ecosystem (SQL DB, Salesforce, REST APIs, etc.)
- Scheduled or event-triggered execution

## Common Errors

- **No Gold layer shortcut available** — ensure the Lakehouse is fully initialized and Spark write completed before creating the Power BI connection
- **Direct Lake not available in the semantic model** — confirm the data is in OneLake (not an external Lakehouse or shortcut to ADLS)



See [[skipping-lakehouse-causes-problems]] for the specific risks of skipping the Lakehouse.

## Related

- [[medallion-architecture]] — the architecture pattern this workflow implements
- [[direct-lake-vs-import-vs-directquery]] — why Direct Lake is the target connection mode
- [[fabric-is-a-complete-data-platform]] — understanding the full Fabric platform context

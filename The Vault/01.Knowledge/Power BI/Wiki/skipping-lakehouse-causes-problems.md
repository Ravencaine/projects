---
created: 2026-08-13
source: "5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)"
source_url: "https://medium.com/powerbi-microsoft-fabric/5-mistakes-beginners-make-in-microsoft-fabric-and-how-to-avoid-them-269ac1739472"
note_type: gotcha
tags: [microsoft-fabric, lakehouse, one-lake, data-modeling]
---

# Skipping the Lakehouse Causes Data Duplication and Messy Models

Beginners skip the Lakehouse and load data directly into Power BI reports, replicating every mistake from standalone Power BI.

## Expected Behaviour

Beginners expect to upload an Excel file into Power BI inside Fabric, just like they always have — one step, done.

## Actual Behaviour

Fabric is designed around a layered lakehouse. Skipping it produces:

- **Data duplication** — same source loaded multiple times across reports
- **Poor performance** — no Direct Lake mode possible without OneLake data
- **Messy models** — no bronze/silver/gold discipline, transforms not reusable

The result is a broken data estate that grows harder to maintain with every new report.

## Why It Happens

Fabric's Lakehouse is opt-in, not mandatory. The UI does not force you to use it, so beginners take the path of least resistance.

Additionally, the "Get Data" experience in Fabric still offers direct Power BI Desktop-style imports, making it easy to fall back to old habits.

## How to Handle It

Always route data through the Lakehouse first:

1. Create a Fabric Lakehouse in the workspace
2. Ingest source files (Excel, CSV, Parquet) into the Bronze layer
3. Use Spark notebooks or Dataflow Gen2 to transform to Silver/Gold
4. Connect Power BI reports via Direct Lake mode to the Gold layer shortcut

This discipline scales: adding a new report means pointing it at the existing Gold layer, not re-importing data.



See [[direct-lake-vs-import-vs-directquery]] for the full three-mode comparison.

## Related

- [[medallion-architecture]] — the architecture pattern this gotcha violates
- [[fabric-is-a-complete-data-platform]] — why the platform exists
- [[star-schema-fact-table-principles]] — dimensional modeling principles that still apply in Fabric

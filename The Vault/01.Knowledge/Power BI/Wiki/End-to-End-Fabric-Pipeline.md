---
created: 2026-08-13
source: 5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)
note_type: pattern
tags: [microsoft-fabric, lakehouse, pipeline, etl, elt, power-bi]
---

# End-to-End Fabric Pipeline

<!-- Source: Anurodh Kumar, "5 Mistakes Beginners Make in Microsoft Fabric", 2026-05-03 -->

## Purpose

Fabric is a complete data platform — not just Power BI with extra features. Data must flow through a structured pipeline before reports are built.

## Components

1. **Lakehouse** — stores raw and transformed data in OneLake
2. **Transform step** — cleanse, deduplicate, enforce schema
3. **Semantic model / Direct Lake** — expose curated data to Power BI
4. **Report** — build visuals on top of the Gold layer

## Structure

```
Source → Lakehouse (Bronze) → Transform → Lakehouse (Silver) → Curate → Lakehouse (Gold) → Power BI Direct Lake → Report
```

Not:

```
Source → Power BI (direct import) → Report
```

## Example

A retail organisation starting with Fabric:

1. Ingest raw POS CSV files into OneLake Bronze via Data Factory
2. Use a Spark notebook to deduplicate, standardise schema, join to product dimension — write to Silver
3. Aggregate daily sales by store/date/product — write to Gold
4. Connect Power BI via Direct Lake mode to Gold shortcuts — no import needed

## Key Anti-Pattern

Uploading Excel files directly into Power BI reports instead of routing through OneLake. Causes data duplication, no sharing across workloads, no medallion layer benefits.

## Related

- [[Medallion-Architecture-Fabric]] — Data Modeling: medallion layers in Fabric
- [[Direct-Lake-vs-Import-vs-DirectQuery]] — when to use Direct Lake over Import
- [[Fabric-Governance-Setup]] — RBAC + workspace structure that supports this pipeline

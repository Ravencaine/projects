---
created: 2026-08-13
updated: 2026-08-13
source: 5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)
note_type: atomic
tags: [medallion-architecture, bronze, silver, gold, microsoft-fabric, onelake, direct-lake]
---

# Medallion Architecture (Bronze / Silver / Gold)

<!-- extended from [[medallion-architecture]] — Fabric-specific guidance added -->

## Fabric / OneLake Implementation (Anurodh Kumar, 2026-05-03)

In Microsoft Fabric, OneLake serves as the single logical data lake for all Fabric workloads. The medallion layers map directly to OneLake:

| Layer | OneLake Location | Fabric Tooling | Content |
|-------|-----------------|----------------|---------|
| Bronze | Default OneLake container | Data Factory, Eventstream | Raw files: Parquet, CSV, JSON — source-as-is |
| Silver | OneLake Silver container | Spark notebooks, Dataflow Gen2 | Cleansed, deduplicated, schema-enforced |
| Gold | OneLake Gold container | Shortcuts | Pre-aggregated, business-ready; exposed to Power BI |

**Direct Lake mode:** Power BI connects to Gold layer via Direct Lake mode, querying OneLake files directly without importing into memory. This eliminates the import/refresh cycle for large datasets and is the primary advantage of using medallion architecture in Fabric over traditional Power BI import.

## Fabric Beginner Mistake: Skipping the Lakehouse

Many Fabric beginners upload Excel files directly into Power BI reports instead of routing them through OneLake. This bypasses the medallion layer and causes:

- Poor report performance
- Data duplication across reports
- No single source of truth
- Inability to share data across Fabric workloads

**Fix:** Always route data through the Lakehouse: Raw → Clean → Curated pipeline before building reports.

## Related

- [[medallion-architecture]] — core atomic note (layer definitions, why it works)
- [[medallion-architecture-raw-cleansed-dimensional]] — three-layer variant naming
- [[End-to-End-Fabric-Pipeline]] — Power BI pattern: full pipeline workflow
- [[Direct-Lake-vs-Import-vs-DirectQuery]] — Power BI comparison: when Direct Lake applies

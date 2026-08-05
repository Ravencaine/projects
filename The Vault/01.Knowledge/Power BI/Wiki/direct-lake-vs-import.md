---
created: 2026-08-01
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md"
note_type: atomic
tags: [power-bi, performance, direct-lake, import-mode, fabric, incremental-refresh, intermediate]
---

# Direct Lake vs Import Mode

Direct Lake is a Fabric-specific storage mode that reads Delta tables directly from OneLake — avoiding the import refresh bottleneck. It's a complement to good modeling, not a replacement for it.

## Import Mode Recap

Import mode loads all data into Power BI's in-memory cache. Fast queries, but requires a full or incremental refresh on a schedule. On large models, refresh can be slow and resource-intensive.

## Direct Lake

Direct Lake reads Delta Parquet files directly from OneLake without importing them into the cache:

```
Delta tables in OneLake → Direct Lake → Power BI semantic model
```

**Biggest advantage:** Eliminates the refresh bottleneck entirely for very large models. No import step = no refresh window to manage.

**Trade-offs:**
- Requires Microsoft Fabric (not available in standard Power BI)
- Requires Delta table format (Lakehouse or Warehouse in Fabric)
- Best suited for very large models; overkill for small to mid-sized reports
- Still benefits from good model design — bad star schemas are slow in Direct Lake too

## When Direct Lake Helps Most

- Very large semantic models (>10GB) where import refresh takes too long
- Scenarios requiring near-real-time data without the lag of scheduled refreshes
- When the team is already in Fabric and using Delta tables

## Incremental Refresh (All Storage Modes)

For very large Import or DirectQuery models, **Incremental Refresh** partitions the data and processes only new or changed partitions instead of reloading everything:

```
Partition 1 (2022-2023): processed once, never touched again
Partition 2 (2024):      processed weekly
Partition 3 (2025):      processed weekly
Partition 4 (2026 YTD):  processed daily
```

Setup: right-click the table in Power BI → Incremental Refresh → define the window and policy.

## What Doesn't Help

- "Just buy Premium" before fixing the model — a badly modelled report is still bad on bigger hardware
- Swapping to a "lighter" custom visual — if DAX query is the bottleneck, the visual type is irrelevant

## Related

- [[star-schema-performance-impact]] — good modeling applies to all storage modes
- [[vertipaq-column-cardinality]] — model size affects import and Direct Lake differently but both benefit from compression

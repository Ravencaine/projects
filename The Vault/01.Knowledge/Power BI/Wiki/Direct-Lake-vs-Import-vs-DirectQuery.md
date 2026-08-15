---
created: 2026-08-13
source: 5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)
note_type: comparison
tags: [microsoft-fabric, direct-lake, import-mode, directquery, power-bi, performance, one-lake]
---

# Direct Lake vs Import vs DirectQuery

## Summary

Direct Lake is the recommended mode for large datasets in Fabric — it queries OneLake files directly without importing, combining the performance of Import with the freshness of DirectQuery.

## Direct Lake

### Pros
- Queries OneLake files directly — no import step
- Fast performance on large datasets (millions of rows)
- No scheduled refresh needed — data is always current
- Native to Fabric / OneLake

### Cons
- Requires OneLake as the data source (Fabric-only)
- Some DAX limitations vs Import mode
- Requires Premium capacity (PPU / Premium per capacity)

### When to Use
- Large datasets where performance matters
- Real-time or near-real-time requirements
- When data lives in OneLake (Fabric Lakehouse Gold layer)

---

## Import Mode

### Pros
- Fastest query performance (data in memory)
- Full DAX feature support
- Works on all SKUs

### Cons
- Data copied into Power BI — memory limits apply
- Requires scheduled refresh for up-to-date data
- Large models = long refresh times

### When to Use
- Small to medium datasets (< 1 GB)
- When data doesn't change frequently
- When maximum query speed is critical

---

## DirectQuery

### Pros
- Always live — no stale data
- No model size limit

### Cons
- Slowest query performance (query pushed to source on every interaction)
- Limited DAX support (no time intelligence, limited row-level security)
- Source database must handle query load

### When to Use
- Very large datasets that can't be imported
- When real-time data is essential and Direct Lake unavailable
- Against SQL Server, Azure SQL, etc.

---

## Comparison Table

| Criteria | Direct Lake | Import | DirectQuery |
|----------|------------|-------|------------|
| Query speed | Fast | Fastest | Slow |
| Data freshness | Real-time | Refresh-dependent | Real-time |
| Model size limit | OneLake capacity | ~2 GB (Pro) / larger (Premium) | None |
| DAX support | Near-full | Full | Limited |
| SKUs | Premium/PPU | All | All |
| Requires OneLake | Yes | No | No |

## Beginner Mistake (Anurodh Kumar)

Fabric beginners fall back to old habits: Import mode (familiar from Power BI) or DirectQuery (from traditional BI). They miss Direct Lake entirely — the mode purpose-built for Fabric's OneLake architecture.

**Fix:** Use Direct Lake when data is large, performance matters, and you want a real-time-like experience without the refresh cycle.

## Related

- [[Medallion-Architecture-Fabric]] — Direct Lake connects Power BI to Gold layer
- [[End-to-End-Fabric-Pipeline]] — how Direct Lake fits the full Fabric pipeline
- [[incremental-refresh-pattern]] — Power BI: Import mode strategy for large models
- [[import-vs-directquery-performance]] — Data Modeling: detailed performance comparison

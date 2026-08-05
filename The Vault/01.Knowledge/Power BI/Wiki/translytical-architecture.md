---
created: 2026-08-01
updated: 2026-08-02
source: "Translytical Task Flows Just Hit GA. They Quietly Change What a Power BI Report Actually Is.md"
note_type: atomic
tags: [power-bi, fabric, translytical, architecture, SQL-DB, async, bulk, CI/CD, advanced]
---

# Translytical Task Flows: Architecture Decisions

Five architectural decisions to make deliberately before deploying.

## 1. SQL Database vs Warehouse vs Lakehouse

**Microsoft's explicit recommendation:** Fabric SQL databases for most write-back scenarios.

Why: OLTP-optimized for heavy concurrent read/write patterns. Warehouses and Lakehouses are OLAP-optimized — great for bulk analytical queries, struggle under high-frequency single-record updates.

Implication: Fabric SQL databases are relatively new. If analytical data already lives in Lakehouse/Warehouse, you'll likely add a SQL database specifically for the translytical workload, then sync analytically across.

```
Fabric SQL DB (write — translytical)
     ↕ (sync)
Lakehouse / Warehouse (read — analytical)
```

**Decision:** Make this consciously, not by accident.

## 2. Synchronous vs Asynchronous Processing

UDFs run **synchronously by default**: user clicks → function runs → user waits.

| Response time | UX |
|--------------|-----|
| Sub-second | Fine |
| Multi-second (external APIs, bulk updates, AI generation) | Poor UX — user stares at button |

**No native "fire and forget"** in current GA. For async behavior:
- UDF writes request to a queue
- Process downstream asynchronously
- Notify user when done

This is solvable, but not free.

## 3. Single-Row vs Bulk Write-Back

| Complexity | Single-row CRUD | Bulk operations |
|-----------|----------------|-----------------|
| List iteration | Simple | Complex |
| Transactional behavior | Straightforward | Must handle partial failure |
| Concurrency | Well-supported | Requires explicit design |

Single-row: well-supported, reasonably easy.
Bulk: possible, requires deliberate design.

## 4. Identity Inheritance and Security Model

**Correct design:** UDF runs with calling user's Microsoft Entra ID identity. Workspace permissions, RLS, and CLS apply automatically.

Implication: Users can write back **only with permissions they have in the workspace**.

If security model didn't anticipate users writing to the analytical data store → **revise before deployment**.

## 5. CI/CD Limitations

**Known gap (as of GA docs):** Translytical Task Flows **lack full Fabric deployment pipeline support**.

Promoting report with translytical buttons from dev → test → production may require **manual rebinding of data function buttons**.

For teams with formal CI/CD on their BI estate: plan for manual steps until this is resolved. Microsoft signals intent to close this gap.

## Decision Checklist

- [ ] Data store: dedicated Fabric SQL DB for translytical workload?
- [ ] Sync vs async: what's the UX threshold for async?
- [ ] Bulk ops: bounded (single-row) or ambitious (bulk)?
- [ ] Security model: workspace permissions anticipate write-back?
- [ ] CI/CD: can you accept manual rebinding steps in the pipeline?

## Related

- [[translytical-tradeoffs]] — honest tradeoffs beyond architecture
- [[translytical-vs-alternatives]] — architectural fit assessment
- [[fabric-ai-integration]] — how these decisions compound into the broader Fabric estate

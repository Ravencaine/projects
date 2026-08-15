---
created: 2026-08-11
source: How DAX Studio Helped Us Reduce Power BI Report Load Time in Production — Part 1 of 2.md
note_type: atomic
tags: [dax, performance, storage-engine, formula-engine, vertipaq, engine]
---

# Storage Engine (SE) vs Formula Engine (FE)

Power BI's query engine is split into two distinct engines — the fast, parallel Storage Engine (SE) and the slower, single-threaded Formula Engine (FE). Writing fast DAX means pushing work to SE and keeping FE minimal.

## Definition

| Engine | Role | Character |
|--------|------|-----------|
| **Storage Engine (SE)** | Scans compressed columnar data (VertiPaq), handles filtering, grouping, aggregation | Multi-threaded, fast, cheap |
| **Formula Engine (FE)** | Handles DAX logic that SE cannot do natively: context transition, joins, complex iterations | Single-threaded, comparatively expensive |

SE fetches and summarises data from the in-memory VertiPaq cache. FE receives SE's output and executes the remaining DAX logic — filter context, iterators, CALCULATE context transitions, etc.

## Key Points

- **SE is parallel; FE is serial** — no matter how many CPU cores, FE runs on one thread
- **SE work is fast because it is distributed** — each core scans its own column segment independently
- **FE work is slow because it is serial** — one thread processes all SE results sequentially
- **Healthy DAX is SE-heavy, FE-light** — let SE do the heavy lifting (filter, group, sum); keep FE's work small
- **FE time dominating is the primary signal** that the DAX itself — not data volume — is the bottleneck
- **Anti-pattern:** any DAX that forces FE to re-scan SE data repeatedly (e.g., FILTER(ALL()) inside CALCULATE) turns a fast engine into a slow one

## SE/FE by Storage Mode

- **Import mode:** SE = VertiPaq in-memory engine; results cached in datacaches
- **DirectQuery:** SE = underlying database (e.g., SQL Server); every SE request is a live query over the network — making inefficient DAX far more costly

## Examples

A measure that scans 10 million rows in SE in 200ms then does a single MAX() in FE is fast. A measure that scans 100 rows repeatedly in FE for each row of a large table is slow — even if the total row-count is smaller.

## Related

- [[SE-FE-Performance-Model]] — single-threaded FE analogy and the counting-the-book mental model
- [[DAX-Studio-Debug-Workflow]] — how to capture and analyse SE/FE timing in practice
- [[FILTER-ALL-Inside-CALCULATE-AntiPattern]] — the classic FE-heavy anti-pattern

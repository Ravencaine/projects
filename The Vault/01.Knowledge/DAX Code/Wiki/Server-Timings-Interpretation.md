---
created: 2026-08-11
source: How DAX Studio Helped Us Reduce Power BI Report Load Time in Production — Part 1 of 2.md
note_type: pattern
tags: [dax, performance, dax-studio, server-timings, diagnostics]
---

# Server Timings Interpretation

Reading the Server Timings panel in DAX Studio to identify whether a slow query is SE-bound or FE-bound.

## What Server Timings Shows

| Metric | What it means |
|--------|--------------|
| **Total** | Total query execution time |
| **SE** time + % | Time spent in the Storage Engine; how much of total is SE work |
| **FE** time + % | Time spent in the Formula Engine; how much of total is FE work |
| **SE Queries** | Number of separate requests sent to the storage engine |
| **SE Cache** | Whether results were served from cache instead of a fresh scan |

## How to Read It

**Healthy query (SE-heavy, FE-light):**
- SE time dominates (80–100% of total)
- SE Queries is low (ideally 1–5 for a simple measure; a few dozen for a complex one)
- FE time is a small fraction

**Problematic query (FE-heavy):**
- FE time dominates (>20–30% of total)
- SE Queries is high (each FE iteration can trigger a new SE request)
- This is the primary signal that the **DAX itself — not data volume — is the bottleneck**

## Key Rule of Thumb

> If FE time dominates, the DAX measure is doing work that SE should be doing. The measure is likely re-scanning data that SE already summarised.

## Common FE-Dominant Patterns

- `FILTER(ALL())` inside `CALCULATE` — forces FE to iterate every row before context transition
- Nested iterators (`SUMX` inside `MAXX` etc.) — each inner iteration triggers a new SE request
- Missing context removal — measures that re-evaluate in the wrong filter context

## Related

- [[Storage-Engine-vs-Formula-Engine]] — SE vs FE explained
- [[SE-FE-Performance-Model]] — the warehouse analogy
- [[DAX-Studio-Debug-Workflow]] — full debugging workflow
- [[FILTER-ALL-Inside-CALCULATE-AntiPattern]] — the most common FE-heavy anti-pattern

---
created: 2026-08-01
updated: 2026-08-02
source: "I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md"
note_type: author
tags: [dax, performance-tuning, benchmarking, power-bi, auditing]
---

# Gulab Chand Tejwani

Power BI practitioner and author of the empirical DAX performance study: *I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance* (Medium/Towards AI, 2026-02-16).

## Study Overview

Analyzed 5,247 DAX measures across 89 production Power BI reports over 4 weeks using DAX Studio (XMLA endpoint), Performance Analyzer, and Server Timings. Found that 78% of slow measures (>2s) shared just 5 patterns. Average speedup after fixing: 14.2x.

Study model: 8.2M rows in Sales table.

## Key Findings

- 364 measures (41%): unnecessary iterators — SUMX/SUM(A[Col]) instead of SUM(A[Col]) — avg 19.5x speedup
- 249 measures (28%): calculated columns for aggregation — 890 MB memory, 22 extra minutes refresh — 67% memory reduction after fix
- 168 measures (19%): RELATED() inside iterators — 14.2s → 0.9s — avg 14.9x speedup
- 204 measures (23%): nested CALCULATE + FILTER(ALL()) — 15.7s → 1.3s — avg 12.1x speedup
- 275 measures (31%): ALL() when REMOVEFILTERS() works — 12.8s → 1.1s — avg 11.6x speedup
- Cancelled $180K Premium capacity upgrade after optimisation

## Sources Ingested

- [[tejwani-5000-dax-measures-performance-source]] — full study with methodology and before/after metrics
- [[tejwani-claude-mcp-power-bi-source]] — Claude + MCP semantic model auditing; 3 client case studies; honest scorecard

## Connect

- Medium: https://medium.com/@AIAnalyticsWithNadiya (no dedicated profile confirmed — Tejwani published via Towards AI)

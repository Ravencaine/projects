---
created: 2026-08-09
updated: 2026-08-09
source: "Do You Really Need Medallion Architecture.md"
note_type: pattern
tags: [data-modeling, medallion-architecture, layer-selection, bronze, silver, gold, landing, curated, analytics, pattern]
---

# Medallion Architecture Layer Selection Pattern

> **Type:** pattern
> **Routed to:** Data Modeling
> **Primary source:** Boniface Muchendu, Data Bear — 2026-03-24

## Decision: Full Medallion vs Simplified Architecture

### Full Medallion: Bronze → Silver → Gold

**When to use:**
| Condition | Implication |
|-----------|-------------|
| Source schemas change frequently | Separation between raw and processed data needed |
| Multiple teams modifying data | Ownership boundaries required |
| Shared platform across domains | Governance at each layer |
| Large data volumes | Transformation management at each stage |

**Layer responsibilities:**
| Layer | Purpose |
|-------|---------|
| Landing/Raw | Initial data ingestion |
| Bronze | Raw copy of source data |
| Silver | Cleaning, casting, trimming, validation, calculated columns |
| Gold | Aggregated, analytics-ready datasets |

### Simplified: Landing → Curated → Analytics

**When to use:**
| Condition | Implication |
|-----------|-------------|
| Data is structured | No complex schema evolution handling needed |
| Source schemas are stable | No frequent raw-vs-processed separation needed |
| Single team | No multi-team ownership boundaries needed |
| Simple domain | No shared platform governance needed |

**Layer responsibilities:**
| Layer | Purpose |
|-------|---------|
| Landing | Data ingestion from source |
| Curated | Clean star schema (facts + dims), data validation, quality constraints |
| Analytics | Pre-aggregated datasets (optional) |

## Decision Questions

Before choosing architecture, answer:

1. **How often do source schemas change?** → Frequent change = medallion; stable = simplified
2. **How many teams will modify the data?** → Multiple teams = medallion; single team = simplified
3. **Is the platform shared across domains?** → Yes = medallion; no = simplified
4. **Do we need intermediate physical datasets?** → Yes = medallion layers; no = virtualized (medallion may still be overkill)

## Key Principle

> The goal of architecture is clarity and responsibility, not adding more layers.

## See Also

- [[Source-Do-You-Really-Need-Medallion-Architecture]] — source article
- [[Layers-Equal-Responsibility-Boundaries]] — each layer must have a clear responsibility
- [[Semantic-Model-Replaces-Gold-Layer]] — when Power BI replaces the Gold layer
- [[Materialized-Views-Data-Quality-Pattern]] — materialized views in the curated layer

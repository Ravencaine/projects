---
created: 2026-08-09
updated: 2026-08-09
source: "Do You Really Need Medallion Architecture.md"
note_type: atomic
tags: [data-modeling, medallion-architecture, layer-responsibility, responsibility-boundary, architecture-design]
---

# Layers = Responsibility Boundaries — Architecture Principle

> **Type:** atomic
> **Routed to:** Data Modeling
> **Primary source:** Boniface Muchendu, Data Bear — 2026-03-24

## The Principle

> Data architecture should not be based on habits or trends. Each layer should exist because it represents a **clear responsibility boundary**.

## Layer Responsibility Reference

| Layer | Responsibility |
|-------|---------------|
| Landing | Data ingestion from source systems |
| Curated | Data quality and modeling (star schema, validation) |
| Analytics | Aggregation and reporting optimization |

## When a Layer Is Justified

A layer is justified if it has a **distinct, unambiguous responsibility** that no other layer handles:
- Landing = ingestion only
- Curated = quality + modeling only
- Analytics = aggregation only

## When a Layer Is Over-Engineering

A layer is over-engineering if:
- Its responsibility is unclear or overlapping with adjacent layers
- No team actually needs to consume it independently
- It exists "because that's the pattern"

## The Question to Ask

> If this layer didn't exist, who would be hurt and why?

If no one is hurt by removing the layer, it may not need to exist.

## Key Insight

> The goal of architecture is clarity and responsibility, not simply adding more layers.

## See Also

- [[Source-Do-You-Really-Need-Medallion-Architecture]] — source article
- [[Medallion-Architecture-Layer-Selection-Pattern]] — applying this principle
- [[Medallion-Materialization-Overhead-Gotcha]] — the cost of unjustified layers
- [[Avoid-Architecture-by-Habit-Gotcha]] — avoiding habit-driven architecture

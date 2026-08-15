---
created: 2026-08-09
updated: 2026-08-09
source: "Do You Really Need Medallion Architecture.md"
note_type: gotcha
tags: [data-modeling, medallion-architecture, habit, default-pattern, anti-pattern, gotcha]
---

# Avoid Architecture by Habit — Gotcha

> **Type:** gotcha
> **Routed to:** Data Modeling
> **Primary source:** Boniface Muchendu, Data Bear — 2026-03-24

## Problem

Teams automatically implement Bronze → Silver → Gold without evaluating whether those layers actually solve a problem for their specific situation.

## The Wrong Question

> "Where should the Bronze layer go?"

## The Right Questions

Before designing architecture, ask:

1. **How often does the source schema change?** → drives how much separation you need between raw and processed
2. **How many teams will modify the data?** → drives ownership boundaries
3. **Is the platform shared across domains?** → drives governance needs
4. **Do we need intermediate physical datasets?** → drives whether materialization is justified

Only after answering these questions should you choose an architecture.

## Why "Bronze/Silver/Gold" Becomes a Habit

- It's the default pattern in Fabric, Databricks, Snowflake documentation
- It sounds mature and well-organized
- It gives teams a framework they can explain to stakeholders
- It looks good in architecture diagrams

But looking organized ≠ solving the right problems.

## The Blind Spots

| Habit | Blind spot |
|-------|-----------|
| Always add Bronze | What if source data is already clean? |
| Always add Silver | What if no cleaning is needed? |
| Always add Gold | What if Power BI handles aggregation? |
| Always add 4 layers | What if 2 layers do the job? |

## See Also

- [[Source-Do-You-Really-Need-Medallion-Architecture]] — source article
- [[Medallion-Architecture-Layer-Selection-Pattern]] — evidence-based selection
- [[Layers-Equal-Responsibility-Boundaries]] — the correct basis for layer decisions

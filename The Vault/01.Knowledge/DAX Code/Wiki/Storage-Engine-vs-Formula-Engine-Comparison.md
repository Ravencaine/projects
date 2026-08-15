---
created: 2026-08-09
updated: 2026-08-09
source: "DAX Fundamentals Part 3 The Patterns That Make Reports Work.md"
note_type: comparison
tags: [dax, storage-engine, formula-engine, performance, vertipaq, iterator, optimization]
---

# Storage Engine vs Formula Engine — DAX Query Processing

> **Type:** comparison
> **Routed to:** DAX Code
> **Primary source:** Havens Consulting — DAX Fundamentals Part 3

## Overview

Every DAX query runs through two engines in sequence:

```
User Query → Storage Engine → Formula Engine → Result
```

## Storage Engine (VertiPaq)

| Property | Detail |
|----------|--------|
| What it does | Retrieves and constructs data from the compressed in-memory model |
| Compression | Columnar (VertiPaq), highly compressed |
| Parallelisation | Yes — multiple queries run in parallel |
| Speed | Very fast |
| Memory | Bounded by model size |

**Storage Engine-friendly patterns:**
- Direct column references
- Simple aggregations: `SUM`, `COUNT`, `MIN`, `MAX`
- Basic `CALCULATE` with table filters
- Star schema with clean foreign key relationships

## Formula Engine

| Property | Detail |
|----------|--------|
| What it does | Evaluates DAX expressions: CALCULATE, iterators, variables, complex logic |
| Compression | None — computes at runtime |
| Parallelisation | No — single-threaded |
| Speed | Slower than Storage Engine |

**Formula Engine-heavy patterns:**
- Complex iterators: `SUMX` with nested logic
- Nested `CALCULATE` inside `CALCULATE`
- Row-by-row processing
- Any `X` / iterator function with complex inner expressions
- Many-to-many relationships without bridge tables

## Many-to-Many Relationships

- One-to-many and one-to-one: have **dictionaries** (pre-computed row-by-row mappings)
- Many-to-many: **no dictionary:** relationships resolved at query time (real-time lookup, no cache)
- Avoid many-to-many unless bridge tables are genuinely impractical

## Performance Rule of Thumb

> Push as much work as possible to the Storage Engine.

**Model design** (star schema + simple aggregations) → Storage Engine → **fast**

**DAX complexity** (nested iterators, many-to-many, complex CALCULATE) → Formula Engine → **slow**

**Trade-off:**宁可模型稍大（多一些表），DAX 简单 = Fabric/Power BI 计算成本低，整体更优。

## See Also

- [[Source-DAX-Fundamentals-Part-3-Havens]] — source video by Havens Consulting
- [[Calculation-Groups]] — related: calc groups push logic out of measures into model layer

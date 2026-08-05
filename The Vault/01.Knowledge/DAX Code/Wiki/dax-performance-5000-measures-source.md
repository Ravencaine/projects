---
created: 2026-07-27
updated: 2026-08-02
source: "I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance"
source_url: "https://medium.com/write-your-world/i-analyzed-5000-dax-measures-here-are-the-5-patterns-that-kill-performance-01bb5fafb4a7"
note_type: source
tags: [dax, performance, anti-patterns, iterator-misuse, nested-calculate]
---

# I Analyzed 5,000 DAX Measures: The 5 Patterns That Kill Performance

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-07-28
> **URL:** https://medium.com/write-your-world/i-analyzed-5000-dax-measures-here-are-the-5-patterns-that-kill-performance-01bb5fafb4a7
> **Routed to:** DAX Code

## Summary

Analysis of 5,000 real-world DAX measures revealed 5 recurring anti-patterns that systematically degrade performance. Each anti-pattern is described with its root cause, impact quantification, and the correct alternative.

## The 5 Patterns That Kill Performance

### Pattern 1: Iterator on a Single Column (SUMX over SUM)
Using SUMX to sum a single column instead of SUM. Performance gap: **27x slower**.

### Pattern 2: Nested CALCULATEs
Multiple CALCULATEs nested inside each other. Each CALCULATE re-evaluates the entire inner expression. Performance gap: **up to 8x slower** per nesting level.

### Pattern 3: No Measure Branching (Duplicated Logic)
The same calculation logic (often a complex SUMX) is copy-pasted into 10-15 different measures. When data changes, every copy recalculates independently.

### Pattern 4: Missing Variables (Redundant Expression Evaluation)
The same expression appears multiple times within a measure (e.g., [Revenue] used 4 times in a complex formula) without VAR — the engine re-evaluates it each time.

### Pattern 5: Iterator Over Large Fact Tables
SUMX iterating over a multi-million-row fact table without pre-filtering. The iteration cost grows linearly with row count.

## Extracted Notes

- [[sumx-vs-sum-gotcha]] — atomic — Pattern 1
- [[nested-calculate-gotcha]] — gotcha — Pattern 2
- [[measure-branching-pattern]] — pattern — Pattern 3 (cross-reference)
- [[var-in-dax]] — atomic — Pattern 4 (cross-reference)
- [[iterator-performance-pattern]] — pattern — Pattern 5

## Metadata

| Field | Value |
|-------|-------|
| Source file | I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~2,594 |

---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: atomic
tags: [dax, isinscope, isatlevel, architectural-location, measure, visual-calculation, report-layer, semantic-model, atomic]
---

# ISINSCOPE vs ISATLEVEL — Architectural Location

**Type:** Atomic · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

ISINSCOPE and ISATLEVEL detect hierarchy level identically. The choice is **not** about correctness — it is about **where** the logic lives: semantic model layer vs report layer.

## ISINSCOPE — Semantic model layer

- Lives in a **measure** in the semantic model
- Inspects the **group-by columns of the query**
- Reusable across all reports consuming this dataset
- Requires semantic model authoring rights to create
- Can access any data in the model, including data not shown in the visual

## ISATLEVEL — Report layer

- Lives in a **visual calculation** on a specific visual
- Inspects the **visual layout** (VISUAL SHAPE of the query)
- Confined to one visual — not shared across reports
- Requires no semantic model changes
- Report developers without model rights can implement it
- Cannot access data outside the visual

## When it actually matters

| Scenario | Choice |
|----------|--------|
| You own the model, want reusability | ISINSCOPE in a measure |
| Shared dataset, no model rights | ISATLEVEL in a visual calculation |
| Logic needs data not in the visual | ISINSCOPE (mandatory) |
| Purely presentation logic, performance-sensitive | ISATLEVEL (operates on visual rowset) |
| Same content across multiple reports | ISINSCOPE |
| Formatting is report-specific | ISATLEVEL |

## The result is often the same

In a standard hierarchical matrix, the visual shape mirrors the group-by columns, so both produce identical visible results. The difference is in **who can maintain it**, **where it lives**, and **what it can access**.

## Related

- [[ISINSCOPE-Per-Level-Conditional-Formatting]] — ISINSCOPE implementation
- [[ISATLEVEL-Visual-Calculation]] — ISATLEVEL implementation
- [[Choose-ISINSCOPE-vs-ISATLEVEL-Workflow]] — decision workflow

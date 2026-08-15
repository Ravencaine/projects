---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: workflow
tags: [dax, isinscope, isatlevel, decision-tree, semantic-model, shared-dataset, workflow]
---

# Choose ISINSCOPE vs ISATLEVEL Workflow

**Type:** Workflow · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

Decision workflow: which level-detection function should you use for per-level formatting logic?

## Step 1 — Do you own the semantic model?

```
YES → Go to Step 2
NO  → Use ISATLEVEL in a visual calculation
```

## Step 2 — Is the logic reusable across multiple reports?

```
YES → Use ISINSCOPE in a measure
NO  → Go to Step 3
```

## Step 3 — Does the logic need data not shown in the visual?

```
YES → Use ISINSCOPE in a measure (mandatory — visual calcs can't access outside data)
NO  → Go to Step 4
```

## Step 4 — Is the logic purely presentation-related?

```
YES → ISATLEVEL preferred (keeps model clean; better performance)
NO  → ISINSCOPE (keeps formatting with the data model)
```

## Step 5 — Is performance critical for this visual?

```
YES → ISATLEVEL (operates on visual rowset, not full model)
NO  → Either works
```

## Summary decision table

| Condition | ISINSCOPE | ISATLEVEL |
|-----------|-----------|-----------|
| Can modify model | ✓ | ✓ (but unnecessary) |
| Shared dataset | ✗ (no rights) | ✓ |
| Cross-report reuse needed | ✓ | ✗ |
| Needs data outside visual | ✓ (mandatory) | ✗ |
| Presentation-only logic | Either | ISATLEVEL preferred |
| High rowcount visual | Either | ISATLEVEL preferred |
| Want to avoid model clutter | ✗ | ✓ |

## Remember: result is usually the same

Both produce identical visible output in a standard hierarchical matrix. The choice is about **maintainability**, **access rights**, and **where the logic belongs architecturally**.

## Related

- [[ISINSCOPE-Per-Level-Conditional-Formatting]] — ISINSCOPE implementation
- [[ISATLEVEL-Visual-Calculation]] — ISATLEVEL implementation
- [[ISINSCOPE-vs-ISATLEVEL-Architectural-Location]] — deep dive on the distinction

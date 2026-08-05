---
created: 2026-08-01
updated: 2026-08-02
source: "Visual Calculations Just Went GA. They'll Save You Hours — and Quietly Fragment Your Model If You Let Them.md"
note_type: atomic
tags: [power-bi, visual-calculations, architecture, GA-May-2026]
---

# Visual Calculations Architecture

## Definition

A visual calculation is "a DAX calculation defined and executed directly on a visual" (Microsoft).

Three core properties:

| Property | Implication |
|----------|-------------|
| Lives on the visual, not in the model | Delete the visual → calculation deleted |
| Operates on the visual matrix | Cannot see hidden columns, other tables, or unrelated model data |
| Works on pre-aggregated data | Often faster than equivalent measures (small grid arithmetic vs. fact table scan) |

## What the Visual Matrix Is

The visual calculation works on the *visual matrix* — the data grid behind the visual with whatever aggregation has already happened. It cannot access:
- Hidden columns
- Other tables in the model
- Related tables via relationships
- `RELATED()`, `USERELATIONSHIP()`, or other relationship functions

## Template Functions

Purpose-built functions not found in classic DAX:

| Function | Purpose |
|----------|---------|
| `RUNNINGSUM` | Running total down rows |
| `MOVINGAVERAGE` | Moving average over N periods |
| `PREVIOUS` / `NEXT` | Reference prior/subsequent row |
| `FIRST` / `LAST` | First/last row in partition |
| `COLLAPSE` / `EXPAND` | Navigate hierarchy levels |
| `LOOKUP` | Cross-row lookup on visual |
| `ISATLEVEL` | Conditional logic by hierarchy level |

Plus **Axis** and **Reset** parameters to control hierarchy traversal.

## Custom Totals

Built on the same engine. Control what a total row shows:
- Sum, Average, Min, Max, Count of displayed rows
- Independent of what the underlying measure does
- Ends the "total row is lying" problem

## The One-Liner

```c
Running sum = RUNNINGSUM([Sales Amount])
```

Replaces the windowing measure that intermediate developers get wrong on the first try.

---
created: 2026-07-26
source: dax.pdf
note_type: concept
tags: [dax, visual-calculations, preview]
---

# Visual Calculations (Preview)

Visual calculations allow DAX formulas to be written directly in a report visual, without needing a model-level measure. This enables rapid prototyping and visual-specific calculations.

## Status: Preview

Visual calculations are currently in preview in Power BI. Features and behavior may change before general availability.

## How It Works

Instead of creating a measure in the model, you write a DAX expression directly in the visual's field well. The expression can reference:
- Other fields in the same visual (as if using TREATAS)
- Model columns and measures
- Other visual calculations

## Key Differences from Measures

| | Measure | Visual Calculation |
|---|---|---|
| **Location** | Model | Visual field well |
| **Scope** | Model-wide | Visual-specific |
| **Speed** | Standard | Fast iteration |
| **Deployment** | Saved to model | Ad-hoc |

## When to Use

- Rapid prototyping of calculations
- Visual-specific calculations that don't need to be reused
- Testing DAX patterns before committing to a model measure
- User-defined calculations in self-service scenarios

## Syntax

Visual calculations use standard DAX syntax but can reference:
- Fields available in the visual context
- Model-level measures
- Other visual calculations

## Limitations

- Not persisted to the model (lost when visual is deleted)
- Cannot be used by other visuals
- Preview features may change

## Related

- [[treatas]]
- [[calculate]]
- [[dax-overview]]

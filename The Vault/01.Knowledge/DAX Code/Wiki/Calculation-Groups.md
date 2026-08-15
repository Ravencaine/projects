---
created: 2026-08-06
updated: 2026-08-06
source: Calculation Groups in Power BI
note_type: atomic
tags: [calculation-groups, dax, tabular, time-intelligence]
---

# Calculation Groups

A Tabular/DAX feature that lets a single Calculation Item apply a time-intelligence expression (e.g., MTD, QTD, YTD) to any measure simultaneously — replacing multiple measure definitions with one shared expression.

<!-- one-line description: A reusable time-intelligence wrapper that applies a calculation expression to any measure without duplicating measure definitions -->

## Definition

Calculation Groups are created in **Tabular Editor** and appear as a table in the Power BI model. Each **Calculation Item** within the group is a DAX expression wrapped around `SELECTEDMEASURE()`. When a Calculation Item is selected via slicer, it rewrites the filter context for every measure in the visual — allowing MTD, QTD, YTD, etc. to be applied to Sales, Quantity, Revenue, and Cost from a single set of items.

## Key Points

- Created in **Tabular Editor** (external tool), not directly in Power BI Desktop
- Appear as a regular table in the model after refresh
- Each Calculation Item wraps `SELECTEDMEASURE()` — a placeholder for whichever measure the visual is currently computing
- Consumed via a slicer on the report canvas — users pick the time period (MTD, QTD, YTD, etc.)
- The **Precedence** property on Calculation Groups controls application order when multiple groups exist
- Calculation Groups are evaluated in the **DAX query engine**, not the visual layer
- Compatible with both Import and DirectQuery modes (with restrictions in DirectQuery)
- The **ALM Toolkit** can deploy Calculation Groups between models
- **Power BI Desktop Model View** (June 2025+) can create CGs directly without external tools — see [[CG-Creation-Power-BI-Model-View]]

## Gotchas

- **Variant data type:** Adding a CG promotes all measures to variant type. This breaks dynamic format string reuse patterns where one measure references another. Workaround: use a DAX UDF for the format string expression. See [[CG-Variant-Data-Type-Gotcha]].
- **ISNUMERIC guard:** Math operations in CG expressions error on non-numeric measures (e.g., dynamic title measures). Guard with `ISNUMERIC(SELECTEDMEASURE())`. See [[ISNUMERIC-Guard-Pattern-for-CG]].
- **Implicit measures excluded:** The *Discourage implicit measures* property must be enabled for CGs to work — calculation items only apply to explicit (user-created) measures.

## Examples

- A Time Intelligence Calculation Group with items: MTD, QTD, YTD, PY, PY MTD
- A Currency Conversion Calculation Group with items: USD, EUR, GBP
- A Scenario Analysis Calculation Group with items: Budget, Forecast, Actual

## Related

- [[SELECTEDMEASURE]] — the DAX function used inside every Calculation Item
- [[Create-a-Calculation-Group]] — step-by-step workflow for creating one
- [[Calculation-Group-External-Tools]] — Tabular Editor, DAX Studio, and ALM Toolkit
- [[avoiding-pitfalls-calculation-groups-precedence-source]] — precedence order when multiple groups exist

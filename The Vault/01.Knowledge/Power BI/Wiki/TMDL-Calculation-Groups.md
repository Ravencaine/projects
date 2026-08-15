---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: pattern
tags: [power-bi, tmdl, calculation-group, semantic-model, governance]
---

# TMDL Calculation Groups: Reuse Semantic Model Logic

Use TMDL (Tabular Model Definition Language) calculation groups to embed reusable time intelligence and business logic once, then apply it to any measure in the model.

## Purpose

Without calculation groups, time intelligence logic (YTD, MTD, YoY, etc.) must be rewritten for every measure. TMDL calculation groups let you define that logic once and apply it to any measure via a slicer or filter — dramatically reducing DAX boilerplate and ensuring consistency across the model.

## Components

- **Prerequisite**: "Discourage implicit measures" must be enabled in Model View before TMDL calculation groups can be applied
- **TMDL View**: paste-ready XML-based definition of the calculation group
- **Calculation items**: named members (e.g., YTD, MTD, YoY, Previous Period) each with their own DAX expression
- **Application**: drop the calculation group onto a visual axis or use as a slicer
- **Compatibility**: check table/column names, dependencies, and formats before applying

## Structure

TMDL calculation group (abbreviated):
```tmdl
CalculationGroup
{
    Name: "Time Intelligence";
    CalculationItem "YTD"
    {
        Expression = """
            CALCULATE(
                SELECTEDMEASURE(),
                DATESYTD('Date'[Date])
            )
        """
    }
    CalculationItem "MTD"
    {
        Expression = """
            CALCULATE(
                SELECTEDMEASURE(),
                DATESMTD('Date'[Date])
            )
        """
    }
}
```

## Example

1. Enable "Discourage implicit measures" in Model View
2. Go to TMDL View
3. Paste calculation group code
4. Apply and refresh
5. Drop calculation group on a visual — all measures now support YTD/MTD/etc. without additional DAX

## Related

- [[field-parameters-vs-calculation-groups]] — comparison of field parameters vs calculation groups
- [[tmdl-power-bi-semantic-model-governance]] — existing note on TMDL governance

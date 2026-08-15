---
created: 2026-07-26
updated: 2026-08-08
source: dax.pdf
note_type: function
tags: [dax, function, information, calculation-groups]
---

# SELECTEDMEASURE

Applies to: Calculated column Calculated table Measure Visual calculation Used by expressions for calculation items or dynamic format strings to reference the measure currently being evaluated.

## Syntax

```dax
SELECTEDMEASURE()
```

No parameters.

## Returns

The scalar value of the measure currently being evaluated in the visual's filter context. Returns a scalar — the exact value of the active measure under the current filter context.

## Usage in Calculation Groups

Inside a Calculation Item's DAX expression, `SELECTEDMEASURE()` is the **placeholder** that represents whichever measure the visual is currently computing:

```dax
-- MTD Calculation Item in Tabular Editor
CALCULATE(
    SELECTEDMEASURE(),
    DATESMTD('Date'[Date])
)
```

When the user selects "MTD" from the Calculation Group slicer, every measure in the visual (Sales, Quantity, Revenue, Cost) is automatically wrapped with the MTD time intelligence expression — without needing a separate MTD version of each measure.

`SELECTEDMEASURE()` is evaluated independently for each measure in the visual. In a Matrix with two measures, the CG expression is evaluated twice — once per measure — with `SELECTEDMEASURE()` resolving to each in turn.

## Examples

### YOY Percentage Change (with ISNUMERIC Guard)

```dax
VAR CurrentValue = SELECTEDMEASURE()
VAR PriorValue = CALCULATE(
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR('Date'[Date])
)
RETURN
    IF(
        ISNUMERIC(CurrentValue) && PriorValue <> 0,
        (CurrentValue - PriorValue) / PriorValue,
        SELECTEDMEASURE()
    )
```

### Branch by Measure Name (SELECTEDMEASURENAME)

```dax
SWITCH(
    TRUE(),
    SELECTEDMEASURENAME() = "Sales",
        CALCULATE(SELECTEDMEASURE(), DATESMTD('Sales'[OrderDate])),
    SELECTEDMEASURENAME() = "Orders",
        CALCULATE(SELECTEDMEASURE(), DATESMTD('Orders'[OrderDate])),
    SELECTEDMEASURE()
)
```

## Notes

- `SELECTEDMEASURE()` only works inside a calculation item expression — errors if used in a regular measure
- Use `SELECTEDMEASURENAME()` alongside it to get the text name of the active measure
- Use `SELECTEDMEASUREFORMATSTRING()` to retrieve the current format string of the active measure
- Not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules

## Related

- [[Calculation-Groups]] — where SELECTEDMEASURE() is used
- [[CG-Creation-Power-BI-Model-View]] — workflow using SELECTEDMEASURE()
- [[ISNUMERIC-Guard-Pattern-for-CG]] — ISNUMERIC guard pattern using SELECTEDMEASURE()
- [[CG-Dynamic-Format-String]] — SELECTEDMEASUREFORMATSTRING() for dynamic format strings
- [[Controlling-Calculation-Group-Selection]] — SELECTEDMEASURE in selection expression context
- [[ISNUMERIC]] — the guard function
- [[ISSELECTEDMEASURE]] — companion function
- [[SELECTEDMEASURENAME]] — text name of the active measure
- [[SELECTEDMEASUREFORMATSTRING]] — format string of the active measure

---
created: 2026-08-02
updated: 2026-08-02
source: Here's a Quick Way to Switch Measures in Power BI.md
note_type: pattern
tags: [power-bi, pattern, field-parameters, calculation-groups, comparison]
---

# Field Parameters vs Calculation Groups

Both field parameters and calculation groups enable dynamic switching between measures or dimensions in Power BI — but they differ significantly in scope, capability, and performance. Choosing the right one depends on the use case.

## Comparison

| Aspect | Field Parameters | Calculation Groups |
|---|---|---|
| **Scope** | Visual level | Visual, page, or report level |
| **Relationships** | Supported — can relate to other tables | Not supported — errors if you try |
| **Performance** | Minimal overhead | Can slow queries when adding/removing/modifying filters |
| **Creation** | UI (Modeling tab) or DAX | Tabular Editor or DAX |
| **Use with composite models** | Not supported | Supported |
| **Supports time intelligence** | Limited — separate parameters needed per measure | Native — one calculation group applies YTD/QTD/YoY to any base measure |
| **Dynamic formatting** | Per-measure formatting | Per-calculation formatting |
| **Best for** | Toggling between specific measures or dimensions | Applying time period calculations (YTD, QTD, YoY%) across all measures |

## Decision Framework

### Use Field Parameters when:
- Users want a toggle between **existing measures**: Revenue, Margin, Units
- You need to switch **dimensions**: Country, Region, City
- You need the parameter table to **participate in relationships** with other tables
- You are using a **composite model**

### Use Calculation Groups when:
- Users toggle between **time calculations** (YTD, QTD, YoY%) applied to **any base measure**
- You want the toggle to apply across **multiple visuals on a page or report** simultaneously
- You need **conditional formatting per calculation**

### Use Both when:
- Users toggle between measures AND need conditional formatting per measure
- Combine field parameters (measure selection) with calculation groups (time period selection)

## Syntax Note

Field parameters use `NAMEOF()` to reference fields:

```dax
"KPI Selector" =
{
    ("Revenue", NAMEOF('Sales'[Revenue]), 1),
    ("Margin %", NAMEOF('Sales'[Margin %]), 2)
}
```

Calculation groups use `SELECTEDMEASURE()` and `ISSELECTEDMEASURE()` to detect the active measure.

## Related

- [[field-parameters-calculated-tables]] — `atomic`
- [[field-parameter-build-workflow]] — `pattern`
- [[field-parameter-limitations]] — `gotcha`
- [[field-parameter-best-practices]] — `reference`

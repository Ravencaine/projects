---
created: 2026-08-02
updated: 2026-08-02
source: Here's a Quick Way to Switch Measures in Power BI.md
note_type: pattern
tags: [power-bi, pattern, field-parameters, slicer, dynamic-visuals]
---

# Field Parameter Build Workflow

Step-by-step process for creating a field parameter in Power BI Desktop, binding it to a visual, and configuring it for clean dynamic switching between measures or dimensions.

## Steps

### 1. Create the Parameter

1. Go to the **Modeling** tab
2. Click **New Parameter** → select **Fields**
3. Add the metrics or dimensions to switch between (e.g., Revenue, Margin, Units)
4. Select **Add slicer to this page** (optional — creates the slicer automatically)
5. Click **Create**

Power BI generates three things:
- A **slicer** pre-bound to the parameter on the current page
- **Metadata properties** (`ParameterMetadata`, `GroupByColumns`) marking it as a field parameter
- A **calculated table** with `NAMEOF` and three columns: display name, field reference, sort order

### 2. Connect to a Visual

1. Drag the **parameter field** onto the visual's X or Y axis
2. Power BI substitutes the selected field into the visual dynamically

### 3. Configure the Slicer

1. Change slicer type to **button slicer**
2. Turn on **single select**
3. Turn on **force selection** (ensures a value is always selected)

### 4. Group Parameters into Categories (Optional)

Add a second column for group sorting order to organize large parameter lists:

```
| KPI Selector    | KPI Selector Fields    | Group Order |
|-----------------|------------------------|-------------|
| Revenue         | [Revenue]              | 1           |
| Margin          | [Margin %]             | 1           |
| Units Sold      | [Units]                | 2           |
```

### 5. Add a Hierarchy (Optional)

For date or geographic hierarchies, add the hierarchy levels to the parameter:

- **Dates**: Year, Quarter, Month, Day
- **Geography**: Country, Region, City

### 6. Enable Hierarchy Persistence

If using matrix visuals with drill-down:
1. Options and Settings → Options
2. Current File → Report Settings → Field Parameters
3. Enable **Persist hierarchy level**

This keeps row expansions intact when switching parameters — users don't need to re-expand after changing the field.

## Manual DAX Creation

Field parameters can also be created via DAX calculated table:

```dax
"KPI Selector" =
{
    ("Revenue", NAMEOF('Sales'[Revenue]), 1),
    ("Margin %", NAMEOF('Sales'[Margin %]), 2),
    ("Units", NAMEOF('Sales'[Units]), 3)
}
```

Use `NAMEOF` instead of hard-coded strings — it auto-propagates renames.

## Related

- [[field-parameters-calculated-tables]] — `atomic`
- [[field-parameters-vs-calculation-groups]] — `pattern`
- [[field-parameter-limitations]] — `gotcha`
- [[field-parameter-best-practices]] — `reference`

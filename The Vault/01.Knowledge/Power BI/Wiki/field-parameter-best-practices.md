---
created: 2026-08-02
updated: 2026-08-02
source: Here's a Quick Way to Switch Measures in Power BI.md
note_type: reference
tags: [power-bi, reference, field-parameters, best-practices, performance]
---

# Field Parameter Best Practices

Proven guidelines for designing, deploying, and maintaining field parameters in Power BI reports.

## Design Guidelines

### NAMEOF Over Hard-Coded Strings
Always use `NAMEOF` to reference columns and measures in field parameters:

```dax
("Revenue", NAMEOF('Sales'[Revenue]), 1)
```

`NAMEOF` automatically propagates renames — if you rename `Revenue` to `Total Revenue`, the parameter updates without breaking.

### Keep Parameter Lists Under 10–15 Options
Large lists make slicers hard to navigate. Group related fields into separate parameters:

```
| Parameter | Fields |
|---|---|
| Measure Selector | Revenue, Margin %, Units |
| Geography Level | Country, Region, City |
| Time Period | Monthly, Quarterly, Yearly |
```

### Use Dropdown Slicers for Large Lists
Button slicers work well for under 10 options. For longer lists, use **dropdown slicer style:** it scales without cluttering the report canvas.

### Separate Parameters for Measures and Dimensions
Keep measure and dimension parameters separate. A single parameter trying to handle both creates confusing slicer UIs and harder DAX logic.

### Explicit Measures Only
Never drag a column with implicit `SUM` into a field parameter. Always create an explicit DAX measure first:

```dax
Total Revenue = SUM(Sales[Revenue])
```

## Performance

### Test with Calculation Groups
When combining field parameters with calculation groups, test performance in **DAX Studio:** the interaction between the two features can introduce query overhead.

### Persist Hierarchy Level — Test Per Report
The **Persist hierarchy level** setting (Options → Report Settings) is useful for matrix drill-down reports but can cause unexpected behavior in card/KPI layouts. Evaluate it per report.

## Security

### Combine with Object-Level Security (OLS)
Field parameters work correctly with OLS. If certain roles should not see certain measures, apply OLS to the underlying columns and measures — the parameter will respect the security model.

## Consolidation

### Consolidate Report Pages
Instead of creating separate pages for each measure, build one page with dynamic visuals and a parameter slicer. A single page with field parameters replaces 3–5 static pages.

## Limitations to Plan Around

- Not compatible with composite models
- Not supported in Q&A or AI visuals
- Pure live connections cannot use field parameters
- Date columns with auto date/time lose hierarchy when in parameters — use explicit Year/Quarter/Month levels instead

## Related

- [[field-parameters-calculated-tables]] — `atomic`
- [[field-parameter-build-workflow]] — `pattern`
- [[field-parameters-vs-calculation-groups]] — `pattern`
- [[field-parameter-limitations]] — `gotcha`

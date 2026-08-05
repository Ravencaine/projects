---
title: "Here’s a Quick Way to Switch Measures in Power BI"
source: "https://medium.com/@BIWave/heres-a-quick-way-to-switch-measures-in-power-bi-6b8212307adc"
author:
  - "[[Mikhail Mikushin]]"
published: 2026-07-30
created: 2026-08-02
description: "More"
Processed: "Unprocessed"
---
Everything Changed When I Created a Field Parameter

![Field Parameters in Power BI — How to create dynamic visuals and switch measures and dimensions using Power BI Field Parameters](99.System/Attachments/Field_Parameters_in_Power_BI_—_How_to_create_dynamic_visuals_and_switch_measures_and_dimensions_usin.webp)

Field Parameters in Power BI — How to create dynamic visuals and switch measures and dimensions using Power BI Field Parameters

## What are the field parameters?

Field parameters are calculated tables that reference columns or measures.

Each row in the table has a field reference, a display label, and a sort order. When a user picks a value from a slicer bound to the parameter, Power BI will [substitute the selected field into the visual](https://biwave.substack.com/p/dashboard-clutter-is-killing-your) instead of a static column or measure.

A slicer connected to the parameter table changes the appearance of the visual.

## Use cases:

Use them when you want to:

- Change geographic levels (country, region, city).
- Show data in multiple formats.
- View values in different units.
- Switch between [time periods (monthly, quarterly, yearly](https://biwave.substack.com/p/power-bi-time-intelligence)).

## How to create a field parameter:

1. Go to the \[Modeling\] tab.
2. Click \[New Parameter\] and select \[Fields\].
3. Add the metrics you want to switch on the visualization.
4. Select the \[Add slicer to this page**\]** option.
5. Click \[Create\].
6. As a result, Power BI will generate three things:
- A slicer will be created on the current page, pre-bound to the parameter.
- Metadata properties (ParameterMetadata and GroupByColumns) that mark this table as a field parameter
- A calculated table with the NAMEOF function with three columns: display name, field reference, and sort order value.

7\. The next step is to connect the parameter to a visual. Drag the parameter field on the visual on the X or Y axis.

8\. Change slicer types to \[button slicer\] and turn on \[single select\] and \[force selection\]***.***

8\. Group Parameters into Categories. Add a second column for group sorting order.

9\. You can also add a hierarchy. Select the columns that will use the hierarchy (year, quarter, or month for dates or region or location for geography) and add them to the parameter.

## Persisting Matrix State:

Usually, when you expand rows in a Power BI matrix (drilling down into categories, etc.), those expansions collapse if you switch the field parameter to show a different dimension or measure.

If you turn on the persist hierarchy level option, Power BI will remember how far you expanded and keep that same view when you change parameters. Now you don’t have to re‑expand everything again.

Go to \[Options and settings\] > \[Options\] > \[Current File\] > \[Report Settings\] > \[Field Parameters\] > \[Persist hierarchy level\] and turn it on.

## Limitations:

- Composite Model Limitation: Field parameters stop working in composite models.
- Q&A visual not supported. AI visuals and Q&A cannot interpret field parameters.
- No live connection without local model. Pure live connections to Power BI semantic models or Analysis Services do not support field parameters. [DirectQuery](https://biwave.substack.com/p/data-modeling-in-power-bi) for Power BI semantic models with a local model (composite model) does work.
- Implicit measures: Fields relying on implicit aggregation dragged into a visual that use automatic SUM, do not work when referenced through a field parameter. Create explicit [DAX measures](https://biwave.substack.com/p/complex-dax) and reference those measures in the parameter.
- No drill-through or tooltip page linking: Field parameters cannot be used as linked fields on drill-through or tooltip pages. Link individual columns referenced within the parameter.
- SELECTEDVALUE incompatibility: The Group By Columns property prevents standard single-value detection. Use MAX or the SUMMARIZE + SELECTCOLUMNS workaround.
- Date column with [auto date/time:](https://biwave.substack.com/p/why-is-my-power-bi-so-slow-after) Date Hierarchy is lost when you use a date column in a field parameter with auto date/time enabled. Create the parameter with explicit hierarchy levels (Year, Quarter, Month, Day).

## The SELECTEDVALUE problem:

You cannot use SELECTEDVALUE directly on a field parameter’s display column.

**Workaround 1: Use** [**MAX:**](https://biwave.substack.com/p/iterator-functions-in-power-bi)

If the slicer uses single-select, `MAX` returns the selected value:

```c
Selected Measure Name = MAX('KPI Selector'[KPI Selector])
```

**Workaround 2: SUMMARIZE + SELECTCOLUMNS**  
For multi-select you can use this:

```c
VAR SelectedValue =
 SELECTCOLUMNS(
 SUMMARIZE(
 'KPI Selector',
 'KPI Selector'[KPI Selector],
 'KPI Selector'[KPI Selector Fields]
 ),
 'KPI Selector'[KPI Selector]
 )
 RETURN
 IF(COUNTROWS(SelectedValue) = 1, __SelectedValue)
```

**Workaround 3: Add a Calculated Column:**

Add a calculated column that copies the display column. The new column will not inherit the [composite key](https://biwave.substack.com/p/from-chaos-to-clarity-my-data-cleaning) property:

```c
KPI Name = 'KPI Selector'[KPI Selector]
```

## Field Parameters vs Calculation Groups:

- Field parameters scope their impact at the visual level.
- [Calculation groups](https://biwave.substack.com/p/power-bi-c%EE%80%80alculation-groups) can apply at the visual, page, or report level.
- Field parameter tables support relationships with other tables.
- When you add a relationship to a calculation group, the model returns an error.
- [Performance overhead](https://biwave.substack.com/p/why-is-my-power-bi-so-slow-after) for field parameters is minimal.
- If calculation groups add, remove, or modify filters, they can slow down queries.

### When to use what?

- If users want to have a toggle between existing measures (Revenue, Margin, Units), use the Field parameter.
- If users toggle between time calculations (YTD, QTD, YoY %) applied to any base measure, use a calculation group.
- If users toggle between measures AND need conditional formatting per measure, use the combination of both.

## Best practices:

- Combine field parameters with [Object-Level Security](https://biwave.substack.com/p/power-bi-security).
- Use the NAMEOF function instead of hard-coded strings. NAMEOF automatically propagates renames automatically and prevents invalid references when you [rename columns or measures](https://biwave.substack.com/p/power-bi-model-documentation).
- Use field parameters to consolidate report pages. Build one page with dynamic visuals.
- Keep parameter lists under 10–15 options. Larger lists make slicers hard to navigate. Group related fields into separate parameters or use a dropdown slicer style.
- Use dropdown slicer style for large field lists. Button slicers work good for under ten options, but dropdown mode is even better.
- Use separate parameters for measures and dimensions.
- Test hierarchy persistence settings per report. Some designs will benefit from the collapsed-on-change behavior.
- Test [performance](https://biwave.substack.com/p/why-is-my-power-bi-so-slow-after) with [DAX Studio](https://biwave.substack.com/p/dax-formulas-debugging) when you combine field parameters with [calculation groups](https://biwave.substack.com/p/power-bi-calculation-groups). The two features work well together.
- Use explicit measures for numeric columns you want in parameters. Field parameters do not support implicit measures.

> **Follow me if you want more articles about Power BI.**
> 
> **What is your best optimization trick?**
> 
> **Let me know in the comments👇**
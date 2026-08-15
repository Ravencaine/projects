---
created: 2026-08-06
updated: 2026-08-06
source: Calculation Groups in Power BI
note_type: workflow
tags: [calculation-groups, dax, tabular-editor, power-bi, time-intelligence]
---

# Create a Calculation Group

Build a reusable time-intelligence Calculation Group in Power BI using Tabular Editor — enabling a single MTD/QTD/YTD slicer to apply to any measure in a visual.

## Prerequisites

- Power BI Desktop **or** Tabular Editor
- A Date table in the model (for time intelligence CGs)

> **Two creation paths exist:**
> 1. **Power BI Desktop Model View:** ribbon button, no external tools needed. See [[CG-Creation-Power-BI-Model-View]] for the full step-by-step.
> 2. **Tabular Editor:** external tool, advanced configuration options. See below.

## Steps

1. **Check for External Tools tab**  
   Open Power BI Desktop. On the ribbon, look for the **External Tools** tab. If it is not there, close Power BI, install Tabular Editor, DAX Studio, and ALM Toolkit, then reopen Power BI. The tools appear automatically if versions are compatible.

2. **Open Tabular Editor**  
   Click **Tabular Editor** in the External Tools tab. Tabular Editor connects to the active Power BI model automatically.

3. **Create the Calculation Group table**  
   In the object tree, right-click the model → **Add Calculation Group**. Name it (e.g., "Time Intelligence").

4. **Add a Calculation Item**  
   Right-click **Calculation Items** within the new group → **Add Calculation Item**. Rename it to a meaningful name (e.g., `MTD`).

5. **Write the DAX expression**  
   Double-click the Calculation Item to open the DAX editor. Write the time-intelligence expression using `SELECTEDMEASURE()` as the measure placeholder:

   ```dax
   CALCULATE(
       SELECTEDMEASURE(),
       DATESMTD('Date'[Date])
   )
   ```

   Add additional Calculation Items for QTD, YTD, PY (Prior Year), etc.

6. **Save and refresh**  
   In Tabular Editor, click **Save**. Back in Power BI Desktop, click **Refresh** on the ribbon to reload the model. The Calculation Group table appears as a regular table.

7. **Add a slicer to the canvas**  
   Drag the Calculation Group's name column onto the report canvas as a slicer visual. Users select a time period (MTD, QTD, YTD) and the expression applies to all measures in every visual.

8. **Add the base measure to the visual (optional)**  
   To display the base measure alongside the time-intelligence result, add `SELECTEDMEASURE()` as a separate measure in the visual — it returns the unfiltered value.

## Variations

- **Multiple Calculation Groups:** Assign a **Precedence** value (in Tabular Editor) to control which group applies first when multiple groups exist in the same model.
- **Currency Conversion:** Use a Calculation Group with a measure-switching expression instead of time intelligence.
- **Scenario Analysis:** Items for Budget, Forecast, Actual applied to the same base measures.

## Common Errors

- Tabular Editor not appearing: check versions — Power BI Desktop, Tabular Editor, and Analysis Services must be compatible.
- Calculation Group table not showing in model: ensure you clicked **Save** in Tabular Editor and **Refresh** in Power BI.

## Related

- [[Calculation-Groups]] — concept overview
- [[SELECTEDMEASURE]] — the DAX placeholder used inside every Calculation Item
- [[Calculation-Group-External-Tools]] — Tabular Editor, DAX Studio, and ALM Toolkit setup
- [[avoiding-pitfalls-calculation-groups-precedence-source]] — precedence order gotchas
- [[CG-Creation-Power-BI-Model-View]] — Power BI Desktop Model View path (no external tools)
- [[CG-Variant-Data-Type-Gotcha]] — variant data type side effect when CGs are added

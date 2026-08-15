---
created: 2026-08-10
updated: 2026-08-10
source: "Give Users Full Control Over KPI Scale with Dynamic Formatting"
source_url: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Give-Users-Full-Control-Over-KPI-Scale-with-Dynamic-Formatting/ba-p/5297206"
note_type: workflow
tags: [power-bi, workflow, dynamic-format, measure-tools, dax]
---

# Dynamic Format String Implementation

Step-by-step workflow to implement user-controlled KPI scale using Dynamic Format Strings in Power BI.

## Prerequisites

- Power BI Desktop (Dynamic Format Strings require the modern modelling experience)
- A base KPI measure that returns a whole numeric value
- A disconnected dimension table with scale options

## Steps

### Step 1 — Create the Scale Dimension Table

Create a disconnected table in DAX with scale options and an integer sort order:

```dax
Scale =
DATATABLE(
    "Scale Name", STRING,
    "Scale ID", INTEGER,
    {
        { "Actuals", 1 },
        { "Thousands", 2 },
        { "Millions", 3 },
        { "Billions", 4 }
    }
)
```

Sort the `Scale Name` column by `Scale ID` so the slicer shows options in logical order (smallest to largest scale).

### Step 2 — Create the Scale Selection Measure

```dax
Selected Scale = SELECTEDVALUE ( 'Scale'[Scale Name] )
```

This measure reads the current slicer selection and drives the format string.

### Step 3 — Write the Base KPI Measure

```dax
Total Profit = SUM ( Financials[Profit] )
```

**Critical:** Do not divide by 1000 or 1,000,000 in DAX. Keep the number whole. Scaling is handled entirely by the format string.

See [[Keep-Base-Measure-Whole]] for why this matters.

### Step 4 — Apply the Dynamic Format String

1. Select the base KPI measure in the **Data** pane
2. Go to **Measure Tools** ribbon → **Format** dropdown
3. Change from *General* (or Currency) to **Dynamic**
4. A new formula bar appears labelled "Format"
5. Paste the SWITCH logic:

```dax
SWITCH (
    [Selected Scale],
    "Thousands", "$#,##0,.00",
    "Millions",  "$#,##0,,.00",
    "Billions",  "$#,##0,,,.00",
    "Actuals",   "$#,##0.00",
    "$#,##0,,.00"
)
```

The last value in SWITCH is the default fallback — used when no slicer selection is active.

## Variations

- **Single scale only:** Omit the Actuals/Thousands options if users only need Millions vs Billions
- **Percentage scaling:** Use `"0.0%"` format for percentage views
- **Custom currency symbols:** Replace `$` with any currency symbol in the format string

## Common Errors

- Forgetting to sort the Scale table → slicer shows alphabetical order instead of logical order
- Scaling inside the DAX measure instead of the format string → causes calculation inconsistencies across visuals
- SWITCH without a default fallback → blanks appear when no slicer selection is active

## Related

- [[Dynamic-KPI-Scale-Disconnected-Table-SWITCH]] — pattern
- [[Multi-Currency-Dynamic-Format-SWITCH]] — bonus use case

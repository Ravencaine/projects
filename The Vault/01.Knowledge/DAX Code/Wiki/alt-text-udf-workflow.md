---
created: 2026-08-11
source: Power BI Alt Text UDF Library
note_type: pattern
tags: [dax, udf, accessibility, power-bi, alt-text]
---

# Alt Text UDF Library — Usage Workflow

How to load and use the Juls Power BI Alt Text UDF library in a Power BI model.

## Prerequisites

- Power BI Desktop (DAX Query View enabled)
- GitHub repository: https://github.com/Juls-BI/powerbi-alttext-udfs
- PBIX for demo: [[Attachments/UDF for SVG Pills.pbix]]

## Files in the Library

| File | Contents |
|------|---------|
| AltText\_Context.dax | Core context UDF |
| AltText\_ChangeNarrative.dax | Change narration UDF |
| AltText\_LineChart.dax | Line chart alt text UDF |
| AltText\_VisualPatterns.dax | 6 KPI pattern UDFs (ProgressBar, BulletChart, SparkBars, RatingDots, StatusPill, VarianceChip) |
| AltText\_VisualPatterns\_Demo.dax | Placeholder measures + example calls |

## Steps

1. Download the repository or clone it
2. Open your PBIX in Power BI Desktop
3. Open **DAX Query View** (Modeling ribbon > DAX Query View)
4. Open the desired .dax file in a text editor
5. Copy the UDF definitions
6. Paste into DAX Query View and run to add to the model
7. Call the UDF in a measure: `Alt Text = AltText_ProgressBar( [Context], [Current], [Target] )`

## Creating UDFs in DAX (FUNCTION syntax)

DAX UDFs use the `DEFINE FUNCTION ... RETURN` syntax in DAX Query View or via TMDL. The library functions follow this pattern:

```
DEFINE FUNCTION AltText_ProgressBar(context STRING, current NUMBER, target NUMBER)
RETURN "Current progress is " & current & " out of " & target & "..."
```

## Calling a UDF in a Measure

```dax
Alt Text =
AltText_ProgressBar(
    [Region] & " sales progress",
    [Sales],
    [Target]
)
```

## Related

Six functions available: [[progressbaralttext]], [[bulletchartalttext]], [[sparkbarsalttext]], [[ratingdotsalttext]], [[statuspillalttext]], [[variancechipalttext]]

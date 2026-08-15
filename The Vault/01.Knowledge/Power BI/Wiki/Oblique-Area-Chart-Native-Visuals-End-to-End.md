---
created: 2026-08-09
updated: 2026-08-09
source: "⚡How I Built a Modern Oblique Area Chart in Power BI (Using Only Native Visuals)"
note_type: pattern
tags: [power-bi, native-visuals, line-chart, area-chart, oblique, error-bars, white-fill, background, png, figma, dynamic-axis, custom-tooltip, healthcare]
---

# Oblique Area Chart via Native Visuals (End-to-End)

Build a modern oblique area chart in Power BI using only native visuals. The technique layers a PNG background behind a line chart, computes dynamic Y-axis bounds with DAX, and uses Analytics pane error bars as white fill zones above/below the data lines — creating the illusion of a filled area chart without a custom visual.

## Prerequisites

- Power BI Desktop
- A table with Date, Value, and a metric type column (e.g. "Average", "Max", "Min")
- Figma or another design tool (optional, for custom PNG background)

## Step-by-Step

### Step 1: Create DAX Measures for Average, Max, Min

```dax
Average Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER('Vital Stats', 'Vital Stats'[Measure Type] = "Average")
    )

Max Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER('Vital Stats', 'Vital Stats'[Measure Type] = "Max")
    )

Min Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER('Vital Stats', 'Vital Stats'[Measure Type] = "Min")
    )
```

### Step 2: Create Dynamic Range Measures

```dax
Max Graph Area =
VAR _MaxVital = CALCULATE(MAXX(ALL('Vital Stats'[Date]), [Max Vital]))
RETURN _MaxVital + 0.05 * _MaxVital

Min Graph Area =
VAR _MinVital = CALCULATE(MINX(ALL('Vital Stats'[Date]), [Min Vital]))
RETURN _MinVital - 0.05 * _MinVital
```

### Step 3: Build the Line Chart

- Add Date to X-axis
- Add Average Vital, Max Vital, Min Vital to Values
- Add Max Graph Area and Min Graph Area to Values
- Set Y-axis min = `[Min Graph Area]` measure
- Set Y-axis max = `[Max Graph Area]` measure

### Step 4: Add PNG Background

- Insert → Image → select PNG
- Resize to cover the plot area → Send to back
- Chart Format → Background → Off

### Step 5: Error Bars as White Fill

- Analytics pane → Error bars → Add
- **Max Vital series:**
  - Upper: `[Max Graph Area]`, Lower: `[Max Vital]`
  - Style: Fill → Color: White → Transparency: 0%
- **Min Vital series:**
  - Upper: `[Min Vital]`, Lower: `[Min Graph Area]`
  - Style: Fill → Color: White → Transparency: 0%
- Set Max Graph Area and Min Graph Area line color → White

### Step 6: Final Formatting

- Average Vital line: dark blue, width 4px
- Max/Min Vital lines: 6px markers
- Remove axis titles
- Add custom tooltip page (hides helper measures)

## Result

A modern oblique area chart with clean visual design — no custom visuals required.

## Related

- [[Source-Oblique-Area-Chart-Native-Visuals-Isabelle-Bittar]] — source
- [[Measure-Type-Filter-Pattern]] — Step 1 DAX measures
- [[MAXX-MINX-ALL-Date-Dynamic-Range]] — Step 2 DAX measures
- [[VAR-for-Intermediate-Measure-Calculation]] — VAR pattern used throughout
- [[Error-Bars-White-Fill-Zones]] — Step 5 core technique
- [[PNG-Background-Behind-Chart]] — Step 4 background
- [[Dynamic-Y-Axis-Min-Max-via-Measures]] — Step 3 dynamic axis
- [[Custom-Tooltip-Page-Hidden-Measures]] — Step 6 tooltip

---
created: 2026-08-04
note_type: pattern
tags: [power-bi, visual-design, area-chart, conditional-formatting, markers]
---

# Color Area Charts with Markers

Combining area chart conditional coloring with data markers and target lines to create multi-layered visual storytelling on a single chart.

## When to Combine

Use markers + color + target lines together when:
- You want to show **actual vs target** across a time series
- The target line is static (benchmark, budget) while actual varies
- Color communicates status (above/below target) and markers draw attention to key points

## Structure

```
Chart: Stacked Area (or 100% Stacked Area)
└── Layer 1: Area fill (color-coded by threshold)
└── Layer 2: Target line (constant value via a separate series)
└── Layer 3: Data markers on significant points only
```

## Step 1 — Build the Area Series

```dax
Sales Area := [Total Sales]
```

## Step 2 — Build the Target Line Series

```dax
Sales Target := [Annual Target] / COUNTROWS(VALUES('Date'[Month]))
```

Add as a **Line** chart type overlaid on the area chart.

## Step 3 — Color the Area by Threshold

Use **Field → Cell Elements → Background Color**:

```dax
Area Fill Color :=
VAR Actual = [Total Sales]
VAR Target = [Sales Target]
RETURN
    IF(
        ISBLANK(Target), "#CCCCCC",
        Actual >= Target, "#00B050",   -- green: on/above target
        Actual >= Target * 0.9, "#FFC000",  -- amber: within 10%
        "#FF0000"   -- red: missed by >10%
    )
```

## Step 4 — Add Markers Selectively

Don't marker every data point — only annotate key moments:

```dax
Significant Point Marker :=
VAR Sales = [Total Sales]
VAR Target = [Sales Target]
VAR PctToTarget = DIVIDE(Sales, Target)
RETURN
    SWITCH(
        TRUE(),
        PctToTarget >= 1.2, "●",   -- beat by >20%
        PctToTarget <= 0.8, "●",   -- missed by >20%
        PctToTarget >= 1.1, "◐",   -- strong beat
        PctToTarget <= 0.9, "◑",   -- significant miss
        BLANK()
    )
```

## Related

- [[color-coding-4-techniques]] — Technique 4: overlay approach
- [[dynamic-line-area-chart-color]] — dynamic color for line/area charts
- [[forecast-actual-flag-pattern]] — flag pattern for threshold coloring

---
created: 2026-08-05
updated: 2026-08-05
source: Arrow Charts in Power BI Enhancing Data Visualization (Boniface Muchendu)
note_type: atomic
tags: [power-bi, conditional-formatting, dual-series, if-blank, positive-negative, markers]
---

# Dual-Measure Conditional Formatting: Positive/Negative Split

The Power BI workaround for conditional formatting on line chart markers: create two separate series using IF/BLANK — one for positive values, one for negative — so each can be coloured independently.

## The Problem

Power BI's built-in conditional formatting options for line chart markers are limited. There is no native "if value > threshold then colour green else red" option for line chart data points.

## The Solution

Split the single measure into two series — one that returns the value only when positive, one that returns the value only when negative. Assign each series a different colour in the formatting pane.

## Formula Pattern

```dax
<SeriesName> Positive =
IF(
    <primary measure> > <comparison measure>,
    <primary measure>,
    BLANK()
)

<SeriesName> Negative =
IF(
    <primary measure> < <comparison measure>,
    <primary measure>,
    BLANK()
)
```

`BLANK()` is invisible in Power BI visuals — so each series only shows on data points where its condition is true.

## Usage in Arrow Chart

| Series | Condition | Marker colour | Arrow direction |
|--------|-----------|-------------|----------------|
| `Sales Positive` | Current > Previous | Green | Up |
| `Sales Negative` | Current < Previous | Red | Down |

## Generalised Form

The pattern applies to any scenario requiring binary conditional formatting in a line chart:

```dax
-- Target vs Actual
Actual Over Target =
IF([Actual] > [Target], [Actual], BLANK())

Actual Under Target =
IF([Actual] < [Target], [Actual], BLANK())

-- Forecast vs Budget
Budget Favourable =
IF([Forecast] >= [Budget], [Forecast], BLANK())

Budget Unfavourable =
IF([Forecast] < [Budget], [Forecast], BLANK())
```

## Limitations

- At any data point, only one of the two series has a value (the other is BLANK) — so the line appears as a single line, not two overlapping lines
- The BLANK means no marker appears for the "non-active" condition at that point — this is the desired behaviour
- Works only for binary conditions (positive/negative, above/below). Three-way splits require three series.

## Related

- [[Arrow-Chart-Build-Line-Marker-ErrorBar]]
- [[Period-over-Period-DAX-Measures-Arrow-Chart]]

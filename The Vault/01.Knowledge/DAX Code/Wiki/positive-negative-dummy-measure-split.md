---
created: 2026-08-02
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: pattern
tags: [dax, conditional-formatting, chart, workaround, if, split]
---

# Positive/Negative Dummy Measure Split

Pattern for conditional visual formatting without an fx button: split a single measure into `_Positive` and `_Negative` variants so each half can be independently styled in a chart.

## Core Pattern

```c
My Measure := [Actual] - [Prior]

My Measure_Positive :=
    IF([My Measure] < 0,   // negative variance shown as positive (up = improvement)
        [My Measure]
    )

My Measure_Negative :=
    IF([My Measure] >= 0,  // positive variance shown as negative (down = worsening)
        [My Measure]
    )
```

> Note: `< 0` → `_Positive` because in the turnover example, lower turnover = improvement, so a negative variance is the "good" result that should receive the green label.

## Adding to the Chart

1. Add both `_Positive` and `_Negative` to the chart's **Values** field
2. Each series appears in the **Format pane → Data labels → Series**
3. Set background color, font color, and transparency per series
4. Set all series **Bar color** to the same value for a seamless bar/column

## Extending to Three Bands

```c
My Measure_Positive :=
    IF([My Measure] < 0, [My Measure])

My Measure_Neutral :=
    IF([My Measure] = 0, [My Measure])

My Measure_Negative :=
    IF([My Measure] > 0, [My Measure])
```

## Related

- [[dual-measure-label-background-trick]]
- [[label-font-color-variance-based]]

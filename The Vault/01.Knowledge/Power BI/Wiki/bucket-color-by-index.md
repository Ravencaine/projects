---
created: 2026-08-02
updated: 2026-08-05
source: Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!) 🎢.md
note_type: pattern
tags: [powerbi, dax, switch, color, conditional-formatting]
---

# Bucket Color by Index

A DAX measure that returns a hex color string for each bucket index, applied via conditional formatting to color stacked bar segments from darkest (top bucket) to lightest (bottom bucket).

## Purpose

Assigns a gradient of accent colors to bar chart segments based on their bucket position — darker shades for higher-value buckets (top spenders), lighter shades for lower-value buckets — giving the chart visual hierarchy and aiding interpretation.

## Structure

```dax
_Color Primary  = "#3631F9"
_Color Accent 1 = "#7285FE"
_Color Accent 2 = "#E3E9F0"
_Color Accent 3 = "#E9EDF2"
_Color Accent 4 = "#BCC7D9"

Bucket Color =
    SWITCH ( [Bucket Index],
        5, [_Color Primary],
        4, [_Color Accent 1],
        3, [_Color Accent 3],
        2, [_Color Accent 2],
        1, [_Color Accent 4]
    )
```

## How It Works

- `SELECTEDVALUE(Buckets[BucketIndex])` (implicit via `[Bucket Index]`) reads the current bucket row.
- `SWITCH` maps each index to a named color constant.
- Applied to the bar chart via **Conditional formatting → Field value** on data colors.

## Variations

- **Diverging palette:** Use green for low buckets and red for high buckets when highlighting outliers.
- **Single accent:** Apply one brand color to all buckets, or vary only between "normal" and "highlighted" states.

## Related

- [[quintile-bucket-min-max-amount]]
- [[dynamic-bin-bar-chart-from-percentile-buckets]]

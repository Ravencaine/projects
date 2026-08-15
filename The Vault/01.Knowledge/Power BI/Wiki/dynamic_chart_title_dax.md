---
created: 2026-08-09
updated: 2026-08-09
source: 10 Ways to Instantly Improve Your Power BI Charts
note_type: pattern
tags: [dynamic-title, dax, format, switch, power-bi]
---

# Dynamic Chart Title via DAX (SWITCH + FORMAT)

<!-- build an insight-bearing chart title that shows current value and period-over-period change using DAX variables and SWITCH logic -->

## Purpose

Replace a static chart title with a dynamic one that communicates the key takeaway: the current KPI value and its direction of change versus the prior period. People scan visuals — the title should carry the insight, not just label the subject.

## Components

- `FORMAT` — format a measure value as a percentage or number string
- `SWITCH(TRUE(), ...)` — evaluate a series of conditions (greater than, less than, equal to) and return the matching text
- DAX variables (`VAR`/`RETURN`) — build the title in discrete steps for readability

## Structure

```dax
Turnover Title =
VAR _InitialText = "Turnover "
VAR _FormattedTurnover = FORMAT( [Turnover Last 12 months], "0.0%")
VAR _FormattedVariation = FORMAT([Turnover Variation], "+0.0%;-0.0%;0.0%")
VAR _VariationText =
    SWITCH(
        TRUE(),
        [Turnover Variation] < 0, "decreased by " & _FormattedVariation & " to ",
        [Turnover Variation] > 0, "increased by " &  _FormattedVariation & " to ",
        "remained the same at "
    ) &  _FormattedTurnover & " since last month"
RETURN _InitialText & _VariationText
```

## Example

Assign `Turnover Title` as the Title field in the visual formatting pane → the chart title reads:
"Turnover increased by 2.3% to 14.7% since last month"

For color-coded SVG titles, render the measure via the Image visual.

## Variations

- Add an emoji prefix: VAR _InitialText = "📈 Turnover " for visual urgency
- Swap the time period reference: "since last quarter", "vs prior year"
- Conditionally prepend a warning emoji when variation exceeds a threshold using nested IF

## Related

- [[chart_title_as_insight]]
- [[dynamic-text-titles-in-power-bi]]

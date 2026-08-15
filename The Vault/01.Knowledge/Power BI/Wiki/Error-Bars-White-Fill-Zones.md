---
created: 2026-08-09
updated: 2026-08-09
source: "⚡How I Built a Modern Oblique Area Chart in Power BI (Using Only Native Visuals)"
note_type: pattern
tags: [power-bi, native-visuals, error-bars, analytics-pane, white-fill, area-chart, oblique, fill, chart-formatting]
---

# Error Bars as White Fill Zones

In the Power BI Analytics pane, error bars can be used creatively to paint white fill zones above and below data lines. By flipping the Upper and Lower bounds, a solid band is created — which visually extends the chart background beyond the data line.

## How It Works

| Series | Upper Bound | Lower Bound | Style | Result |
|--------|-------------|-------------|-------|--------|
| Max Vital | Max Graph Area (+5%) | Max Vital (data line) | Fill, Color: White, Transparency: 0 | White fill above the max line |
| Min Vital | Min Vital (data line) | Min Graph Area (−5%) | Fill, Color: White, Transparency: 0 | White fill below the min line |

## Setup Steps

1. Select the line chart → **Analytics** pane
2. **Error bars** → Add → select "Max Vital" series
3. Set **Upper bound** = `[Max Graph Area]` measure
4. Set **Lower bound** = `[Max Vital]` measure
5. Enable **Error band** → Style: **Fill**
6. Set color: **White**, Transparency: **0%**
7. Repeat for "Min Vital" series with flipped bounds
8. Set line color of `Max Graph Area` and `Min Graph Area` series → **White**

## Why This Creates the Oblique Effect

The Max Graph Area / Min Graph Area lines (set to white) define the top and bottom of the chart. The error band fills from the actual data line to these white boundaries — appearing as pure white. This makes the PNG background visible through what looks like the chart body, creating the oblique area chart illusion.

## Related

- [[Source-Oblique-Area-Chart-Native-Visuals-Isabelle-Bittar]] — source
- [[Dynamic-Graph-Area-Buffer]] — DAX: the buffer measures that define upper/lower bounds
- [[PNG-Background-Behind-Chart]] — the background image that shows through the white fill
- [[Oblique-Area-Chart-Native-Visuals-End-to-End]] — end-to-end combining all elements

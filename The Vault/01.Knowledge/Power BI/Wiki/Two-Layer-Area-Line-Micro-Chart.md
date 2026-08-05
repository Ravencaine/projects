---
created: 2026-08-04
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: pattern
tags: [plotly, pattern, micro-chart, area-chart, layered-traces, dashboard]
---

# Two-Layer Area-Line Micro-Chart

Build a modern dashboard mini-chart by layering two Plotly `go.Scatter` traces: a transparent `fill="tozeroy"` trace underneath and a `lines+markers` trace on top. The fill creates a soft area; the top trace provides crisp line and data-point markers. Hover is handled exclusively by the top trace via `hoverinfo="skip"` on the fill layer.

## Purpose

Single-trace Plotly area charts show a flat fill. Two layers give visual depth — the semi-transparent fill grounds the line, and the top trace's markers make exact values readable. The pattern is optimised for dashboard KPI cards where the chart is small (~110px) and must communicate trend without visual noise.

Use when:
- The micro-chart is inside a KPI card or dashboard tile.
- The chart height is ≤ 150px and a standard axis-annotated chart would overwhelm the card.
- The visual goal is "trend at a glance" rather than precise value reading.

## Components

- `go.Scatter` with `mode="lines"`, `fill="tozeroy"`, `line=dict(width=0)` — the fill layer; invisible line, semi-transparent fill from data to Y=0.
- `hex_to_rgba(hex_color, alpha)` — converts hex colour to `rgba(r,g,b,alpha)` for the fill colour.
- `go.Scatter` with `mode="lines+markers"`, explicit `line=dict(width=2)`, `marker=dict(size=5)` — the data layer; handles all hover via `hovertemplate`.
- `hoverinfo="skip"` on the fill layer — prevents duplicate hover labels from the transparent base.
- `customdata` + `hovertemplate` on the data layer — clean, controlled hover text.

## Structure

```python
import plotly.graph_objects as go

def hex_to_rgba(hex_color, alpha=0.18):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

def mini_area_line(data, color, xlabels=None):
    xs = list(range(len(data)))
    layout = chart_base()               # shared layout helper
    if xlabels:
        layout["xaxis"] = dict(
            visible=True,
            tickvals=xs,
            ticktext=xlabels,
            tickfont=dict(size=9, color="#888"),
            showgrid=False,
            zeroline=False,
            range=[-0.5, len(xs) - 0.5],
        )
        layout["margin"]["b"] = 20
    layout["showlegend"] = False

    fig = go.Figure()

    # Layer 1 — fill only; line hidden (width=0); hover skipped
    fig.add_trace(go.Scatter(
        x=xs, y=data,
        mode="lines",
        fill="tozeroy",
        line=dict(color=color, width=0),
        fillcolor=hex_to_rgba(color, 0.25),
        hoverinfo="skip",
    ))

    # Layer 2 — line+markers on top; hover handled here
    fig.add_trace(go.Scatter(
        x=xs, y=data,
        mode="lines+markers",
        line=dict(color=color, width=2),
        marker=dict(size=5, color=color, line=dict(width=0)),
        customdata=xlabels or xs,
        hovertemplate="<b>%{customdata}</b><br>%{y}<extra></extra>",
    ))

    fig.update_layout(**layout)
    return fig
```

## Variations

- **Single colour, multiple cards** — reuse `hex_to_rgba()` with the same alpha across all cards for a consistent palette, varying only the hue per card.
- **Horizontal bar chart instead of area** — for a different micro-chart shape, `go.Bar(orientation="h")` with `autorange="reversed"` to put highest value at top.
- **No markers** — drop `+markers` from the top trace's `mode` for a cleaner, line-only look on wider cards.

## Related

- [[chart-base-plotly]] — the shared layout helper used by this pattern; the pattern composes on top of `chart_base()`.
- [[Component-First-Dashboard-Design]] — the micro-chart is a reusable component built once, used many times.
- [[Data-UI-Separation-Principle]] — data (values, labels) flows in; the chart builder produces a figure; no state held internally.
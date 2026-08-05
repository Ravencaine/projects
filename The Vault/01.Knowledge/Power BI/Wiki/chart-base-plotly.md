---
created: 2026-08-04
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: function
tags: [python, dash, plotly, function, layout, chart]
---

# chart_base() — Consistent Plotly Layout Helper

Returns a fresh dict defining a shared baseline Plotly layout: dark template, transparent backgrounds, no margins, hidden axes, fixed height. Called by every chart builder instead of repeating layout properties inline. Returns a new dict every call to avoid Plotly's in-place layout mutation.

## Signature

```python
def chart_base() -> dict:
    ...
```

## Returns

A Python `dict` with keys: `template`, `margin`, `paper_bgcolor`, `plot_bgcolor`, `xaxis`, `yaxis`, `height`.

```python
{
    "template": "plotly_dark",
    "margin": {"l": 0, "r": 0, "t": 0, "b": 0},
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "xaxis": {"visible": False},
    "yaxis": {"visible": False},
    "height": 110,
}
```

## Parameters

None.

## Examples

```python
# Every chart builder calls chart_base() — no inline layout duplication
def mini_area_line(data, color, xlabels=None):
    xs = list(range(len(data)))
    layout = chart_base()           # shared baseline
    if xlabels:
        layout["xaxis"] = {         # override only what this chart needs
            "visible": True,
            "tickvals": xs,
            "ticktext": xlabels,
            ...
        }
        layout["margin"]["b"] = 20  # extra bottom margin for labels
    layout["showlegend"] = False
    fig = go.Figure()
    fig.add_trace(...)
    fig.update_layout(**layout)
    return fig
```

```python
# Table uses same helper — different traces, same layout baseline
def mini_table(headers, rows):
    fig = go.Figure(go.Table(...))
    fig.update_layout(**chart_base(), height=160)  # override height only
    return fig
```

## Notes

- **Returns a new dict every call.** Plotly mutates layout dicts in place. Storing `chart_base()` in a module-level variable and reusing it causes layout bleed across chart renders. Always call it fresh per chart.
- **`paper_bgcolor` vs `plot_bgcolor`**: `paper_bgcolor` is the area outside the plot; `plot_bgcolor` is the plotting area itself. Both set to `"rgba(0,0,0,0)"` (fully transparent) so the card's CSS background shows through.
- **`template="plotly_dark"`** applies a dark colour scheme globally — chart lines, text, grid colours all follow the dark palette without hardcoding each one.

## Related

- [[Two-Layer-Area-Line-Micro-Chart]] — uses `chart_base()` as its layout foundation.
- [[Data-UI-Separation-Principle]] — the same motivation: centralize shared configuration so it can be changed in one place.
- [[Component-First-Dashboard-Design]] — `chart_base()` is a component-level helper that enforces layout consistency across all chart components.
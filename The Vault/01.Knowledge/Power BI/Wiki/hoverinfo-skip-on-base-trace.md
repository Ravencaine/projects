---
created: 2026-08-06
updated: 2026-08-06
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: gotcha
tags: [plotly, gotcha, hover, layered-traces, micro-chart, dashboard]
---

# hoverinfo="skip" on Hidden Fill Trace to Avoid Duplicate Hover Labels

When a Plotly chart layers a semi-transparent `fill="tozeroy"` trace beneath a `lines+markers` trace (the two-layer micro-chart pattern), the hidden base trace still produces a hover label by default — appearing at every data point and overlapping with the top trace's custom hovertemplate. Setting `hoverinfo="skip"` on the base trace tells Plotly to ignore it for hover events, leaving hover handling entirely to the top trace.

## Expected Behaviour

You layer two traces for visual depth — a transparent fill on the bottom and a crisp line+markers on top. You expect hovering over a data point to show one clean label driven by the top trace's `hovertemplate`:

```python
fig.add_trace(go.Scatter(x=xs, y=data, mode="lines", fill="tozeroy", line=dict(width=0)))
fig.add_trace(go.Scatter(x=xs, y=data, mode="lines+markers", hovertemplate="%{y}<extra></extra>"))
```

One hover label, controlled by the top trace.

## Actual Behaviour

Both traces respond to hover events by default. Because the bottom trace is full-height (from data to Y=0), moving the cursor anywhere between the line and the X-axis triggers a hover label on the bottom trace — often with a generic `<trace 0>` annotation rather than the top trace's formatted template. Result: duplicate or clashing tooltips at every data point.

## Why It Happens

Plotly registers hover events per trace, not per render layer. A `fill="tozeroy"` trace is a complete trace with its own hover behaviour, even when its visual line has `width=0`. Without an explicit override, both traces trigger hover independently.

## How to Handle It

Add `hoverinfo="skip"` to the hidden base trace:

```python
fig.add_trace(go.Scatter(
    x=xs, y=data,
    mode="lines",
    fill="tozeroy",
    line=dict(color=color, width=0),
    fillcolor=hex_to_rgba(color, 0.25),
    hoverinfo="skip",                              # single source of truth for hover
))

fig.add_trace(go.Scatter(
    x=xs, y=data,
    mode="lines+markers",
    line=dict(color=color, width=2),
    marker=dict(size=5, color=color),
    customdata=xlabels or xs,
    hovertemplate="<b>%{customdata}</b><br>%{y}<extra></extra>",
))
```

**Variations:**

- **Use `hoverinfo="x+y"` on the base trace** if you want the bottom trace to show raw coordinates instead of skipping — useful for developers debugging fill behaviour.
- **Set `showlegend=False` on both** when the layered chart is a single visual concept; the legend otherwise shows two identical-looking entries.
- **`hovertemplate="<extra></extra>"`** on the top trace hides the trace-name box that Plotly adds by default next to the label.

## Related Gotchas

- [[plotly-layout-mutation-gotcha]] — sibling Plotly gotcha; in a multi-chart dashboard, shared layout dicts that get `hoverinfo` set on the fill layer will leak that property into other charts.
- [[autorange-reversed-horizontal-bar-top]] — another Plotly default that trips dashboard code: first-item-at-bottom for horizontal bars.

## Related

- [[Two-Layer-Area-Line-Micro-Chart]] — uses this gotcha in its structure; the `hoverinfo="skip"` line on layer 1 is what makes the layered pattern work cleanly.
- [[hex-to-rgba-python]] — the colour helper feeding `fillcolor` on the base trace.

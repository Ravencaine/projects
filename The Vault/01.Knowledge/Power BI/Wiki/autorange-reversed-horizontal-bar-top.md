---
created: 2026-08-06
updated: 2026-08-06
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: gotcha
tags: [plotly, gotcha, bar-chart, axis, order, horizontal-bar]
---

# Plotly Horizontal Bar Chart: First Item Appears at Bottom by Default

A Plotly `go.Bar(orientation="h")` chart shows the first item in the data array at the **bottom** of the Y-axis, not the top. To put the first item at the top — the way readers expect for ranking charts — the Y-axis must be set to `autorange="reversed"`.

## Expected Behaviour

You provide data in ranked order — best country first — and expect the highest-ranked country to appear at the top of the chart:

```python
countries = ["Germany", "France", "Spain", "Italy"]
values    = [120, 95, 80, 65]

fig = go.Figure(go.Bar(x=values, y=countries, orientation="h"))
fig.show()
```

You expect Germany at the top.

## Actual Behaviour

Plotly's categorical Y-axis is bottom-up. Germany appears at the **bottom**, Italy at the top — the visual opposite of the data order. For ranking lists, "top performer" sits at the bottom of the chart, which most readers misread as a low value.

## Why It Happens

Plotly's default categorical axis treats the first category as `y=0` and draws upward from there. There's no auto-flip for `orientation="h"` — the orientation only changes which trace property maps to which axis, not the axis direction.

## How to Handle It

Set `autorange="reversed"` on the Y-axis:

```python
fig = go.Figure(go.Bar(
    x=values,
    y=countries,
    orientation="h",
))

fig.update_layout(
    yaxis=dict(
        autorange="reversed",  # Germany at top, Italy at bottom
        showgrid=False,
        zeroline=False,
    ),
)
```

**Variations:**

- **Vertical column chart:** the opposite axis (X) needs the same fix when categorical and ordered: `xaxis=dict(autorange="reversed")`.
- **Sort the data instead:** `[{"country": c, "value": v} for c, v in sorted(zip(countries, values), key=lambda r: -r[1])]` then plot. No axis override needed, but loses the ability to view the data in input order.
- **List reversed at construction:** `countries[::-1]`. Same trade-off as sorting.

The `autorange="reversed"` approach is the lightest: data order is preserved semantically, only the display order is flipped. Sorting or reversing the data discards the original order, which can confuse downstream code that assumes the input order.

## Related Gotchas

- [[plotly-layout-mutation-gotcha]] — another Plotly default that bites in dashboard code: layout dicts are mutated by `update_layout()`, so passing `yaxis=dict(autorange="reversed")` into a shared layout dict also mutates the Y-axis settings of any later chart that reuses it.
- [[hoverinfo-skip-on-base-trace]] — sibling Plotly gotcha where duplicate hover labels appear from hidden fill traces unless the base layer sets `hoverinfo="skip"`.

## Related

- [[Two-Layer-Area-Line-Micro-Chart]] — uses Plotly scatter, not bar, so the reversal gotcha doesn't apply; the chart_base() helper hides both X and Y axes for KPI-card micro-charts.

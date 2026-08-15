---
created: 2026-08-06
updated: 2026-08-06
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: gotcha
tags: [plotly, gotcha, layout, mutation, dict, debugging]
---

# Plotly Mutates Layout Dicts in Place

Plotly's `fig.update_layout(**layout)` mutates the dict you pass in. Reusing the same dict across multiple figures (or across multiple `update_layout()` calls on the same figure) compounds the changes — invisible until the second or third render, where colours, margins, or hidden axes from a previous chart appear on the current one.

## Expected Behaviour

You write a helper that returns a layout dict, store the dict in a module-level variable, and reuse it across figures:

```python
LAYOUT = chart_base()  # called once at module load

def make_chart_a():
    fig = go.Figure(...)
    fig.update_layout(**LAYOUT)  # expected: each chart gets the baseline
    return fig

def make_chart_b():
    fig = go.Figure(...)
    fig.update_layout(**LAYOUT)  # expected: same baseline applied
    return fig
```

## Actual Behaviour

`update_layout()` mutates `LAYOUT` in place. The second call receives a layout that already carries the first chart's overrides. Subsequent renders show drifted `xaxis`, `yaxis`, `margin`, or `showlegend` settings — usually diagnosed as "why is my second chart's axis showing?"

```python
# Actual behaviour: LAYOUT is permanently mutated by every update_layout call
LAYOUT = {"xaxis": {"visible": False}, "yaxis": {"visible": False}, ...}

fig_a.update_layout(**LAYOUT)        # LAYOUT unchanged in shape, may copy fields
fig_b.update_layout(**LAYOUT)        # LAYOUT now reflects fig_a's adjustments
```

## Why It Happens

Plotly's `update_layout` accepts `**dict` and walks the dict, applying each setting to the figure's internal layout state. The implementation does not defensively copy the input — it treats the passed dict as a structure to merge from. Calling helpers like `layout["xaxis"] = {...}` then propagate back because they're the same Python objects.

## How to Handle It

**Always return a fresh dict from your layout helper.**

```python
# Correct — returns a fresh dict on every call
def chart_base():
    return dict(
        template="plotly_dark",
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=110,
    )

def make_chart():
    layout = chart_base()       # new dict every call
    layout["xaxis"] = dict(visible=True, ...)
    fig = go.Figure()
    fig.update_layout(**layout)
    return fig
```

The fix is structural — a function that returns a new `dict()` literal each call — not a runtime `dict(layout)` copy. The latter hides the problem until someone mutates one of the nested dicts (`layout["xaxis"]["tickvals"] = ...` still propagates).

**Variations of the gotcha:**

- **Nested dict mutation:** `layout["xaxis"]["tickvals"] = [...]` mutates the shared `xaxis` sub-dict across all future layouts. Copy nested dicts too.
- **Module-level constants:** `LAYOUT = dict(...)` then `update_layout(**LAYOUT)` — never. Use a function.
- **List arguments:** `layout["annotations"] = [...]` is appended to, not replaced.
- **`fig.layout`:** accessing `fig.layout` returns the figure's internal layout object — modifying it directly mutates the figure. Use `update_layout()` instead of direct attribute assignment when you want the documented API.

## Related Gotchas

- [[chart-base-plotly]] — the helper that demonstrates the correct pattern: a function returning a fresh dict. This gotcha is the reason it must be a function, not a constant.
- [[hoverinfo-skip-on-base-trace]] — sibling Plotly gotcha where dropping `hoverinfo="skip"` on the hidden fill layer produces duplicate hover labels; the mutation gotcha compounds by making the same fill trace appear in multiple cards.
- [[autorange-reversed-horizontal-bar-top]] — another Plotly-axis gotcha where the default orientation is opposite of what dashboard designers expect.

## Related

- [[Two-Layer-Area-Line-Micro-Chart]] — uses `chart_base()` correctly; mutation awareness is why the layout is rebuilt per chart.

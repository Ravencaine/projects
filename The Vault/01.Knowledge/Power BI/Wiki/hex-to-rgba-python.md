---
created: 2026-08-06
updated: 2026-08-06
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: function
tags: [python, plotly, function, color, hex-to-rgba, dashboard]
---

# hex_to_rgba() — Hex Color → RGBA String Converter

Converts a CSS-style hex colour string (e.g. `"#818cf8"`) to an `rgba(r, g, b, alpha)` string with a configurable alpha. Used to derive semi-transparent fills from a base hex colour without maintaining parallel colour tables.

## Signature

```python
def hex_to_rgba(hex_color: str, alpha: float = 0.18) -> str:
    ...
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `hex_color` | `str` | A hex colour string, with or without the leading `#` (e.g. `"#818cf8"` or `"818cf8"`). |
| `alpha` | `float` | Opacity in `[0.0, 1.0]`. Defaults to `0.18`. |

## Returns

A `str` of the form `"rgba(r,g,b,alpha)"` — values are space-free for direct embedding in CSS or Plotly `fillcolor` properties.

```python
hex_to_rgba("#818cf8", 0.25)  # -> "rgba(129,140,248,0.25)"
```

## Examples

```python
# Reuse across multiple chart builders for consistent transparency
PRIMARY     = "#818cf8"
ACCENT      = "#fb923c"

soft_primary = hex_to_rgba(PRIMARY, 0.25)
soft_accent  = hex_to_rgba(ACCENT, 0.25)

# Pass the transparent fill into a Plotly scatter trace
fig.add_trace(go.Scatter(
    x=xs, y=data,
    mode="lines",
    fill="tozeroy",
    line=dict(width=0),
    fillcolor=soft_primary,             # semi-transparent fill
))
fig.add_trace(go.Scatter(
    x=xs, y=data,
    mode="lines+markers",
    line=dict(color=PRIMARY, width=2),
    marker=dict(color=PRIMARY, size=5),
))
```

```python
# Works on a per-card basis to vary the alpha while keeping the palette stable
def card_fill(card_hex, alpha=0.18):
    return hex_to_rgba(card_hex, alpha)
```

## Notes

- **Strips the leading `#`** with `.lstrip("#")` so both forms work.
- **Slices byte-pairs `[0:2]`, `[2:4]`, `[4:6]`:** assumes a 6-digit hex (`#RRGGBB`). 3-digit shorthand (`#abc`) is not supported.
- **Returns comma-separated, no spaces** to match CSS / Plotly string format. Add spaces only if a downstream renderer demands it.
- **No validation:** malformed input raises `ValueError` from `int(..., 16)` rather than a friendly error. Wrap or sanitise upstream if user input is the source.
- **Alpha is independent of the source colour.** The helper does not blend against a background — it sets a flat opacity. Effective rendering depends on what sits behind (the card's `linear-gradient` or `paper_bgcolor`).

## Related

- [[Two-Layer-Area-Line-Micro-Chart]] — the primary consumer; uses `hex_to_rgba()` for the bottom fill layer.
- [[chart-base-plotly]] — sibling utility in the same dashboard architecture; both helpers are tiny, dependency-free, and reused across all chart builders.
- [[CSS-Flip-Card-Dash]] — the card backgrounds use raw hex colours directly (no alpha), so the helper is not used there.

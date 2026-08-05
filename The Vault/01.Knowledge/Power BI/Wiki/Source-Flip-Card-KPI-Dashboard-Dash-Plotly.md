---
created: 2026-08-04
updated: 2026-08-05
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
source_url: "https://medium.com/@esthersm/building-an-interactive-flip-card-kpi-dashboard-with-dash-plotly-css-6ad367b165f5"
note_type: source
tags: [python, dash, plotly, dashboard, css, flip-card, KPI, component-design, data-driven-ui]
---

# Building an Interactive Flip Card KPI Dashboard with Dash, Plotly & CSS

A Python/Dash walkthrough of a KPI dashboard built around four principles: data separated from UI, a shared chart layout helper, CSS-driven interaction (no JavaScript), and data-defined card geometry. The dashboard uses flip cards — click to reveal a detail view behind the KPI — implemented entirely with CSS 3D transforms, with Dash callbacks handling only the class-toggle state.

> **Type:** article
> **Author:** [[Author-Esther|Esther]] (Medium / @esthersm)
> **Published:** 2026-04-11
> **URL:** https://medium.com/@esthersm/building-an-interactive-flip-card-kpi-dashboard-with-dash-plotly-css-6ad367b165f5
> **Routed to:** Power BI

## Summary

The article builds a KPI dashboard in Dash/Plotly/CSS where each card flips on click to reveal a detail view. The core argument is that good dashboards are built from reusable components, not from pages — data is loaded once at startup, chart layout is shared via a single helper function, interaction is CSS-only, and card geometry is defined as a list of tuples rendered via list comprehension. The stack is deliberately minimal: Dash for app/callbacks, Plotly for charts, CSS for flip animation.

## Key Claims

1. **Data separation from UI** — reading from CSV files at startup via `read_csv()` rather than hardcoding values keeps the UI clean and makes switching to an API or database a one-line change.
2. **Consistent chart system via `chart_base()`** — a single Python function returning a shared Plotly layout dict (`plotly_dark` template, transparent backgrounds, zero margins, hidden axes, fixed height) eliminates layout duplication across all chart builders.
3. **Two-layer micro-charts** — layering a transparent `fill="tozeroy"` scatter trace under a `lines+markers` scatter trace creates a modern area-chart feel with depth and clearer trend reading.
4. **CSS handles interaction** — the flip animation uses CSS `transform: rotateY(180deg)` with `backface-visibility: hidden`; the only Dash callback is a state toggle (`n_clicks % 2`) that adds/removes the `flipped` class name.
5. **Data-driven UI** — cards are defined as a list of tuples `(card_id, title, value, subtitle, back_fig, front_fig)` and rendered with a single list comprehension over `dbc.Row/dbc.Col`. Adding a new card requires only a new tuple, not a new component.
6. **Responsive layout** — `dbc.Row([dbc.Col(flip_card(*c), xs=12, sm=8, md=4) for c in CARDS])` adapts to 1-column (mobile), 2-column (tablet), 3-column (desktop).
7. **"Build components, not pages"** — the author's closing principle: a usable dashboard shows less, makes it interactive, makes it intuitive.

## Notable Details

- The `hex_to_rgba()` helper converts hex colour strings to `rgba(r,g,b,alpha)` for semi-transparent area fills — avoids hardcoded RGBA values.
- The `mini_table()` builder transposes row data via `list(zip(*rows))` before passing to Plotly Table — Plotly expects columns, not rows.
- The `mini_map()` uses a Europe-scoped Choropleth with `TRANSPARENT` ocean/background and `scope="europe"` + `projection_type="natural earth"` for a compact regional view.
- `autorange="reversed"` on the horizontal bar's Y-axis puts the first country at the top (Plotly bar charts default to first-item-at-bottom).
- The `flip()` callback is written generically using `*[Output(...)]` and `*[Input(...)]` splat operators so it adapts to `len(CARDS)` without manual per-card wiring.
- `dbc.themes.DARKLY` provides the Bootstrap dark theme; `box-shadow: none !important` on card faces prevents Bootstrap from applying default card styling.

## Extracted Notes

- [[Data-UI-Separation-Principle]] — `atomic` — separating data loading from UI definition enables swap-in of APIs/databases without touching component code.
- [[Component-First-Dashboard-Design]] — `atomic` — building reusable components instead of pages makes dashboards scalable and easier to extend.
- [[chart-base-plotly]] — `function` — shared `chart_base()` helper returning a consistent Plotly layout dict, eliminating layout duplication across all chart builders.
- [[Two-Layer-Area-Line-Micro-Chart]] — `pattern` — layering a transparent `fill="tozeroy"` scatter trace under a `lines+markers` trace for modern dashboard micro-charts.
- [[CSS-Flip-Card-Dash]] — `pattern` — CSS `rotateY(180deg)` + `backface-visibility: hidden` for 3D flip; Dash callback handles only the class-toggle state, not the animation.
- [[Data-Driven-UI-Card-Tuples]] — `pattern` — defining card geometry as data tuples and rendering with list comprehension; adding a card is a new tuple, not a new component.

## Metadata

| Field | Value |
|-------|-------|
| Source file | Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md |
| Archived at | — (still in Inbox) |
| Ingestion date | 2026-08-04 |
| Word count | ~420 |
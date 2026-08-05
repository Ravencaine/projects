---
created: 2026-08-04
updated: 2026-08-05
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: atomic
tags: [dash, architecture, component-design, dashboard-design, reusability, scalability]
---

# Component-First Dashboard Design

Build dashboards from small, reusable, single-responsibility components rather than as monolithic page-level layouts. A dashboard made of components can be understood piece by piece, extended by adding new components, and refactored without rewriting the whole page.

## Definition

A dashboard is a composition of independent, self-contained components, each rendering a defined piece of the UI. Components receive data as parameters and have no knowledge of the page layout or sibling components. The page assembles them.

## Key Points

- **Components are the unit of reuse.** A flip card works whether it is the first card or the tenth — it takes data in and renders a UI out. The same component type used with different data produces different outputs.
- **Components have a single responsibility.** The flip card does one thing: it shows a KPI value on front, a detail chart on back, and responds to clicks. A `chart_base()` helper does one thing: it returns a shared layout dict. A `mini_area_line()` chart builder does one thing: it returns a two-layer area-line figure.
- **Adding a new card requires no component code.** Because card geometry is defined as data tuples, adding a new KPI is a new tuple entry — the component definition stays unchanged.
- **Testing is per-component.** You can test a flip card's rendering, a chart builder's output, or a layout assembler's composition independently.
- **Separation of concerns.** The component doesn't know how it's laid out on the page; the page doesn't know how the component renders internally. This is the same principle as Power BI's shape compositing: a KPI card shape doesn't know it's on a report page.

## Examples

```python
# Each card is a self-contained component
def flip_card(card_id, title, value, subtitle, back_fig, front_fig):
    # builds the full card — front, back, callback wiring
    ...

# Cards assembled into a row
dbc.Row(
    [dbc.Col(flip_card(*c), md=4) for c in CARDS]
)

# New KPI card added without touching component code:
CARDS = [
    ("c1", "Revenue",  "€950K", "↑ +12%", mini_area_line(...), mini_map(...)),
    ("c2", "Profit",   "€260K", "↑ Stable", mini_table(...), country_hbar(...)),
    ("c3", "New KPI",  "€100K", "↑ +5%",  mini_area_line(...), ...),  # new tuple only
]
```

In Power BI terms: building a report from reusable shape-measure groups (KPI card shape + badge + trend mini-chart) is the same pattern. The report page is the container; the card is the component.

## Related

- [[Data-UI-Separation-Principle]] — component-first depends on data separation: components receive data, they don't own it.
- [[Data-Driven-UI-Card-Tuples]] — the implementation mechanism: card definitions as data, not component code.
- [[CSS-Flip-Card-Dash]] — a specific component: the 3D flip card built from CSS transforms and a Dash state toggle.
- [[chart-base-plotly]] — a component-level helper: one shared layout builder used by all chart components.
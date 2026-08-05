---
created: 2026-08-04
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: atomic
tags: [python, dash, architecture, data-layer, separation-of-concerns, scalability]
---

# Data Separation Principle (UI Reads from Data, Not Hardcoded)

Load data at application startup — from CSV files, an API, or a database — and pass it into UI components as arguments. Never hardcode values in component definitions. This separates the data layer from the presentation layer, making the UI reusable and the data source swappable.

## Definition

A component receives its data through parameters or a shared data module rather than embedding raw values in its own definition. Changing the data source requires changing one loader function, not every component that uses the data.

## Key Points

- **One place to change data.** When the data source changes (CSV → API, API → database), only the data reader function changes — all components that call it work unchanged.
- **UI components become pure functions.** A flip card that takes `(card_id, title, value, subtitle, back_fig, front_fig)` is a pure layout function — it has no opinion about where the data comes from.
- **Enables testing and simulation.** With data separated, you can inject mock data without touching the UI. `read_csv()` can be swapped for `fetch_api()` transparently.
- **Improves scalability.** Adding a new KPI card requires a new data tuple, not a new hardcoded entry in the component tree. The pattern scales to dozens of cards without component code growth.
- **Supports live updates.** Dash `dcc.Interval` or polling callbacks can refresh the data module while the component definitions remain static.

## Examples

```python
# Bad — data embedded in component definition
def flip_card():
    return html.Div([
        html.Div("€950K"),  # hardcoded
        ...
    ])

# Good — data passed in
def flip_card(card_id, title, value, subtitle, back_fig, front_fig):
    return html.Div([
        html.Div(value),
        ...
    ])

# Data loaded once at startup, passed to all components
_trend = read_csv("revenue_trend.csv")
REVENUE_VALUES = [int(r["value"]) for r in _trend]

CARDS = [
    ("c1", "Revenue", "€950K", "↑ +12%", mini_area_line(REVENUE_VALUES, ...), ...),
]
```

In Power BI terms: this is equivalent to binding a visual's fields to a model rather than hardcoding static text into a shape. The model is the data layer; shapes and visuals are the presentation layer.

## Related

- [[Component-First-Dashboard-Design]] — complements this principle: when data is separated, components become reusable containers.
- [[Data-Driven-UI-Card-Tuples]] — the specific implementation: card geometry as a list of data tuples, rendered via list comprehension.
- [[chart-base-plotly]] — another example of separation: layout configuration in a shared helper, not repeated in each chart builder.
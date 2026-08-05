---
created: 2026-08-04
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: pattern
tags: [dash, pattern, data-driven, component, tuple, list-comprehension, scalability]
---

# Data-Driven UI — Card Geometry as Tuples

Define the geometry and content of dashboard cards as data (a list of tuples) rather than as component code. Render the full UI from the data using list comprehension. Adding, removing, or reordering cards requires only a change to the data — no component code is touched.

## Purpose

In a dashboard with many KPI cards, every card follows the same structure (card_id, title, value, subtitle, back_fig, front_fig). If the card component is hardcoded per card, adding a new card means writing new component code. Defining card content as data and rendering with a comprehension makes the dashboard scalable — a new card is a new tuple.

## Components

- A **data tuple** per card: `(card_id, title, value, subtitle, back_fig, front_fig)` — the canonical argument order for the card builder function.
- A **`CARDS` list** collecting all tuples — the single source of truth for dashboard card content.
- A **card builder function** (`flip_card()`) that unpacks a tuple and returns an HTML component.
- A **list comprehension** over `CARDS` in the layout: `[flip_card(*c) for c in CARDS]`.
- The generic **Dash flip callback** using splat operators: `*[Output(f"c{i}-inner", ...)]` and `*[Input(f"c{i}-inner", ...)]` — adapts automatically to `len(CARDS)`.

## Structure

```python
# Data — one tuple per KPI card
CARDS = [
    (
        "c1",
        "Revenue",
        "€950K",
        "↑ +12% vs last month",
        mini_area_line(REVENUE_VALUES, "#818cf8", REVENUE_LABELS),   # back
        mini_map(MAP_ISO3, MAP_VALUES, "€Revenue", ...),           # front
    ),
    (
        "c2",
        "Gross Profit",
        "€260K",
        "↑ Stable margin",
        mini_table(PROFIT_TABLE_HEADERS, PROFIT_TABLE_ROWS),         # back
        country_hbar(HBAR_COUNTRIES, HBAR_VALUES, "#fb923c"),       # front
    ),
]

# Layout — renders all cards from data
app.layout = dbc.Container([
    dbc.Row(
        [dbc.Col(flip_card(*c), md=4) for c in CARDS],  # one comprehension, no per-card code
        justify="center",
    ),
])

# Flip callback — one output/input per card, auto-adapts to len(CARDS)
@app.callback(
    *[Output(f"c{i}-inner", "className") for i in range(1, len(CARDS) + 1)],
    *[Input(f"c{i}-inner", "n_clicks")  for i in range(1, len(CARDS) + 1)],
)
def flip(*clicks):
    return [
        "flip-card-inner flipped" if n and n % 2 == 1 else "flip-card-inner"
        for n in clicks
    ]
```

## Variations

- **Dict-based cards** — use a list of dicts `{"card_id": "c1", "title": "Revenue", ...}` instead of tuples for self-documenting field names and easier slicing.
- **Grouped sections** — nest lists: `[dbc.Col([flip_card(*c) for c in group], md=4) for group in CARD_GROUPS]`.
- **Filtered cards** — apply a filter before rendering: `[flip_card(*c) for c in CARDS if c[3].startswith("↑")]`.
- **Power BI analogue** — the same pattern in Power BI: define card data as a measure/column set, bind a KPI card visual to it via field well, and use a slicer to filter which cards are visible.

## Related

- [[Component-First-Dashboard-Design]] — the card builder function is a reusable component; data-driven UI defines what goes in it.
- [[CSS-Flip-Card-Dash]] — the card builder is `flip_card()`; it receives the data tuple and renders the component.
- [[Data-UI-Separation-Principle]] — the tuple data is loaded once; components receive it as parameters; changing data doesn't touch component code.
- [[chart-base-plotly]] — chart builders (`mini_area_line`, `mini_map`, `mini_table`) are called from within the tuple data, not from the layout — data references functions as values.
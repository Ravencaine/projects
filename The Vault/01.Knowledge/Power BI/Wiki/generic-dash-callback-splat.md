---
created: 2026-08-06
updated: 2026-08-06
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: pattern
tags: [dash, pattern, callback, splat, scalability, variable-cardinality]
---

# Generic Dash Callback via Splat (Variable-Cardinality Outputs/Inputs)

Build a Dash callback whose output and input lists scale automatically with the size of a data structure, using Python's unpacking operators `*[...]`. The callback's body iterates over all `n_clicks` values — no per-card wiring, no manual count.

## Purpose

In a dashboard with N KPI cards (where N is data-driven and may grow), you need a callback that responds to N independent click events. Hand-writing `Output(...)` and `Input(...)` for each card id grows the callback signature linearly and breaks when the data changes. The splat pattern derives the callback signature from `len(CARDS)` at decorator-definition time.

Use when:
- A callback needs one Output and one Input per item in a list (cards, rows, tabs, dropdown options).
- Items are added or removed by changing the data, not the code.
- The body of the callback is symmetrical across all items (toggle, format, validate).

## Components

- A **list of items** the callback operates over — `CARDS`, `ROWS`, `TABS`, etc.
- A **named builder** for each id — `f"c{i}-inner"` where `i in range(1, len(items) + 1)`.
- **Splat unpacking** `*[Output(...)]` and `*[Input(...)]` to expand the iterable into decorator arguments.
- A **callback body** that accepts `*clicks` (or `*values`) and returns a list — one element per Output, in the same order.

## Structure

```python
@app.callback(
    *[Output(f"c{i}-inner", "className") for i in range(1, len(CARDS) + 1)],
    *[Input (f"c{i}-inner", "n_clicks") for i in range(1, len(CARDS) + 1)],
)
def flip(*clicks):
    return [
        "flip-card-inner flipped" if n and n % 2 == 1 else "flip-card-inner"
        for n in clicks
    ]
```

**Render side:** pair with a list comprehension that creates the matching components:

```python
dbc.Row(
    [dbc.Col(flip_card(*c), md=4) for c in CARDS]
)
```

## Example

A generic toggle that formats N status pills uniformly:

```python
@app.callback(
    *[Output(f"row-{r['id']}-status", "children") for r in ROWS],
    *[Input (f"row-{r['id']}-filter", "value")   for r in ROWS],
)
def format_status(*values):
    return [
        "✅ Active" if v and v != "all" else "—"
        for v in values
    ]
```

The order of `Output`s in the decorator must match the order of `Input`s in the body — both iterate `range(1, len(items) + 1)` in the same sequence.

## Variations

- **Mixed properties:** splat multiple property names: `*[Output(f"c{i}-inner", prop) for prop in ["className", "style"] for i in ...]`. Produces 2N outputs.
- **Mixed element types:** splat heterogeneous ids: `*[Output(id, prop) for id, prop in pairs]`. Useful when output ids come from data.
- **State instead of Input:** swap `Input` for `State` to read without triggering: `*[State(f"c{i}-inner", "n_clicks_timestamp") for i in ...]`.
- **Single Output with Multi-Input:** instead of `*[]` splat, use a list-returning helper and `Input("n_clicks", "value")` with `prevent_initial_call=True`. Splat pattern still applies when Output side needs to scale.

## Why It Works

`@app.callback(...)` accepts variable positional arguments for `Output` and `Input`. The `*[expr for x in items]` form evaluates to a sequence that the decorator unpacks into separate `Output(...)` / `Input(...)` calls. The body receives them as `*args` in order. Adding a tuple to `CARDS` automatically grows both decorator args and body args — no manual wiring.

The catch: callbacks are registered at import time. If `len(CARDS)` is not yet known when the decorator runs, generation must be deferred to a function registered via `app.callback` (not the `@` form).

## Related

- [[Data-Driven-UI-Card-Tuples]] — companion pattern that provides the data structure the splat callback iterates over.
- [[CSS-Flip-Card-Dash]] — concrete example: the flip callback is the splat pattern in action.

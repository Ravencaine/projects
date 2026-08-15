---
created: 2026-08-04
updated: 2026-08-05
source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly and CSS.md"
note_type: pattern
tags: [dash, css, pattern, interaction, flip-card, component, 3d-transforms]
---

# CSS-Driven Flip Card (Dash)

A KPI card that reveals a detail view when clicked, implemented with CSS 3D transforms (`rotateY(180deg)` + `backface-visibility: hidden`) and a Dash callback that toggles a `flipped` class name on the card's inner container. The animation is entirely CSS — no JavaScript required. Dash handles only the class-toggle state.

## Purpose

Show two views of the same KPI in the same physical space — a summary (KPI value + mini-chart) on the front, a detail view (trend chart, map, table) on the back — without consuming twice the screen real estate. The user chooses when to flip, keeping the dashboard clean while enabling drill-down on demand.

Use when:
- KPI cards have both a high-level summary and a detail view worth showing.
- Screen space is constrained (dashboard, mobile layout).
- You want to minimise visual noise — only reveal detail on user intent (click).

## Components

**CSS (3D stage):**
- `.flip-card { perspective: 1000px; }` — creates the 3D depth environment; `1000px` is the standard distance that makes the rotation feel natural.
- `.flip-card-inner { transform-style: preserve-3d; transition: transform 0.65s cubic-bezier(0.4, 0.2, 0.2, 1); }` — the rotating element; `preserve-3d` keeps front and back in the same 3D space; `cubic-bezier` is an ease-out-in that accelerates into the flip and decelerates out.
- `.flip-card-inner.flipped { transform: rotateY(180deg); }` — the class toggle target; CSS applies the rotation.
- `.flip-card-front, .flip-card-back { backface-visibility: hidden; }` — hides the face when it is rotated 180° away from the viewer, preventing the mirror-image artefact.
- `.flip-card-back { transform: rotateY(180deg); }` — pre-rotates the back face 180° so it appears correctly when the inner container rotates.

**Dash (state only):**
- `n_clicks` property on the inner container — increments on every click; the only state Dash tracks.
- `Output(f"{card_id}-inner", "className")` → toggles `"flip-card-inner flipped"` vs `"flip-card-inner"`.
- `Input(f"{card_id}-inner", "n_clicks")` → odd clicks = flipped, even = unflipped.

## Structure

```python
# Python — card builder (front + back faces as HTML children)
def flip_card(card_id, title, value, subtitle, back_fig, front_fig):
    front = html.Div(
        className="flip-card-front",
        children=[
            html.Div(title),
            html.Div(value, className="card-value"),
            dcc.Graph(figure=front_fig, config={"displayModeBar": False}),
        ],
    )
    back = html.Div(
        className="flip-card-back",
        children=[
            html.Div(title),
            dcc.Graph(figure=back_fig, config={"displayModeBar": False}),
        ],
    )
    return html.Div(
        className="flip-card",
        children=[
            html.Div(
                id=f"{card_id}-inner",
                className="flip-card-inner",
                n_clicks=0,
                children=[front, back],
            )
        ],
    )
```

```css
/* CSS — 3D flip animation, no JavaScript */
.flip-card { perspective: 1000px; }
.flip-card-inner {
  position: relative; width: 100%; height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.65s cubic-bezier(0.4, 0.2, 0.2, 1);
  cursor: pointer;
}
.flip-card-inner.flipped { transform: rotateY(180deg); }
.flip-card-front,
.flip-card-back {
  position: absolute; width: 100%; height: 100%;
  border-radius: 16px;
  backface-visibility: hidden;
  padding: 18px 20px;
}
.flip-card-back { transform: rotateY(180deg); background: #1c1c1c; }
```

```python
# Dash callback — generic over len(CARDS), one output per card
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

- **Y-axis flip:** use `rotateX(180deg)` instead of `rotateY(180deg)` for a top-down flip.
- **Partial flip:** apply `rotateY(-15deg)` on hover for a subtle "peek" preview without requiring a full click.
- **Delay flip:** add `transition-delay: 0.2s` to `.flip-card-inner` to delay animation start.
- **Accessibility:** add `aria-label` to the card container and `aria-expanded` state driven by the Dash callback; consider `prefers-reduced-motion` media query to disable the animation.

## Related

- [[Data-Driven-UI-Card-Tuples]] — cards are data tuples, not component code; `flip_card()` is called once per tuple in a list comprehension.
- [[Component-First-Dashboard-Design]] — the flip card is a reusable component; the page assembles, it renders.
- [[Data-UI-Separation-Principle]] — front and back figures are generated from data and passed in; the card component owns only layout and interaction.
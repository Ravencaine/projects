---
title: "🚀📊 Building an Interactive Flip Card KPI Dashboard with Dash, Plotly & CSS"
source: "https://medium.com/@esthersm/building-an-interactive-flip-card-kpi-dashboard-with-dash-plotly-css-6ad367b165f5"
author:
  - "[[Esther]]"
published: 2026-04-11
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!IUMQ-lVKXugD8GFql3lxIA.gif)

I built a small KPI dashboard where the focus wasn’t on adding more charts, but on:

👉 **clean structure, reusable components, and simple interaction**

The stack is minimal:

- Dash → app & callbacks
- Plotly → charts
- CSS → interaction (flip animation)

## 🧠 1. Data Layer (Separated from UI)

Instead of hardcoding values, the app reads from 4 example CSV files, this is the first:

![](99.System/Attachments/1!CaZmU5ds3SuhEBK0uS-x9A.png.webp)

```c
from utils.data_reader import read_csv
```
```c
_trend = read_csv("revenue_trend.csv")
REVENUE_LABELS = [r["month"] for r in _trend]
REVENUE_VALUES = [int(r["value"]) for r in _trend]
```

👉 Why this matters:

- keeps UI clean
- makes switching to API/database easy later
- improves scalability

## 🎨 2. Consistent Chart System

All charts share a base layout:

```c
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
```

👉 Result:

- consistent look
- zero duplication
- avoids Plotly layout mutation issues

## 📊 3. Layered Micro-Charts (Better UX)

Instead of simple lines, the main chart uses **two layers**:

```c
fig.add_trace(go.Scatter(
    x=xs, y=data,
    fill="tozeroy",
    line=dict(width=0),
    fillcolor=hex_to_rgba(color, 0.25),
))
```
```c
fig.add_trace(go.Scatter(
    x=xs, y=data,
    mode="lines+markers",
    line=dict(color=color, width=2),
))
```

👉 This creates:

- depth
- clearer trends
- modern dashboard feel

## 🎴 4. Reusable Flip Card Component

Each KPI is a reusable component:

```c
def flip_card(card_id, title, value, subtitle, back_fig, front_fig):
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

👉 Structure:

- front → KPI + quick visual
- back → detailed view
- click → flip

## 🎨 5. CSS Handles the Interaction (No JS)

The flip effect is entirely CSS-driven.

## Flip trigger

```c
.flip-card-inner.flipped {
  transform: rotateY(180deg);
}
```

## 3D environment

```c
.flip-card {
  perspective: 1000px;
}
```
```c
.flip-card-inner {
  transform-style: preserve-3d;
  transition: transform 0.65s cubic-bezier(0.4, 0.2, 0.2, 1);
}
```

## Hide reversed side

```c
.flip-card-front,
.flip-card-back {
  backface-visibility: hidden;
}
```

## Back side setup

```c
.flip-card-back {
  transform: rotateY(180deg);
}
```

👉 Result:

- smooth 3D animation
- no JavaScript needed
- clean separation of concerns

## 🔁 6. Minimal Backend Logic

The interaction logic is intentionally simple:

```c
@app.callback(
    Output("c1-inner", "className"),
    Input("c1-inner", "n_clicks"),
)
def flip(n):
    return "flip-card-inner flipped" if n and n % 2 else "flip-card-inner"
```

👉 Behavior:

- odd click → flipped
- even click → reset

## 📦 7. Data-Driven UI

Cards are defined as data:

```c
CARDS = [
    (
        "c1", "Revenue", "€950K", "↑ +12% vs last month",
        mini_area_line(REVENUE_VALUES, "#818cf8", REVENUE_LABELS),
        mini_map(MAP_ISO3, MAP_VALUES, "€Revenue", ...),
    ),
]
```

👉 Benefits:

- scalable
- reusable
- easy to extend

## 🧱 8. Responsive Layout

```c
dbc.Row(
    [dbc.Col(flip_card(*c), xs=12, sm=8, md=4) for c in CARDS],
)
```

👉 Automatically adapts:

- mobile → 1 column
- tablet → 2
- desktop → 3

## 💡 Key Takeaways

- Build **components, not pages**
- Use **CSS for interaction whenever possible**
- Keep charts **minimal and contextual**
- Separate **data from presentation**

## ⚠️ Final Thought

Most dashboards fail because they try to show everything.

👉 A better approach:

- show less
- make it interactive
- make it intuitive

That’s what actually makes a dashboard usable.

Full structure and code:

![](99.System/Attachments/1!wKzcixGTzOn_gLpXob9hUw.png.webp)

app.py

```c
from dash import Dash, html, dcc, Input, Output  # Dash core components and callback tools
import dash_bootstrap_components as dbc            # Bootstrap UI components and themes
import plotly.graph_objects as go                  # low-level Plotly chart objects
from utils.data_reader import read_csv             # CSV helper from utils/

# ── Load data from data/ ─────────────────────────────────────────

_trend = read_csv("revenue_trend.csv")             # monthly revenue trend
REVENUE_LABELS = [r["month"]      for r in _trend] # month abbreviations (x-axis)
REVENUE_VALUES = [int(r["value"]) for r in _trend] # revenue values (y-axis)

_map = read_csv("revenue_map.csv")                 # revenue by country
MAP_ISO3   = [r["iso3"]        for r in _map]      # ISO-3 country codes
MAP_VALUES = [int(r["value"])  for r in _map]      # corresponding values

_hbar = read_csv("profit_hbar.csv")                # profit by country
HBAR_COUNTRIES = [r["country"]    for r in _hbar]  # country names
HBAR_VALUES    = [int(r["value"]) for r in _hbar]  # profit values

_tbl = read_csv("profit_table.csv")                # profit breakdown by category
PROFIT_TABLE_HEADERS = list(_tbl[0].keys())        # header row from first dict's keys
PROFIT_TABLE_ROWS    = [tuple(r.values()) for r in _tbl]  # each row as a tuple

# ── App init ─────────────────────────────────────────────────────

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])  # dark Bootstrap theme

TRANSPARENT = "rgba(0,0,0,0)"  # reusable transparent colour for chart backgrounds

# ── Helpers ──────────────────────────────────────────────────────

# Returns a fresh dict every call — Plotly mutates layout dicts in place
def chart_base():
    return dict(
        template="plotly_dark",
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor=TRANSPARENT,
        plot_bgcolor=TRANSPARENT,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=110,
    )

# Converts a hex colour string to rgba() for semi-transparent fills
def hex_to_rgba(hex_color, alpha=0.18):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

# ── Chart builders ───────────────────────────────────────────────

# Two-layer chart: semi-transparent area fill + crisp line+marker trace on top
def mini_area_line(data, color, xlabels=None):
    xs = list(range(len(data)))
    layout = chart_base()
    if xlabels:
        layout["xaxis"] = dict(
            visible=True,
            tickvals=xs,
            ticktext=xlabels,
            tickfont=dict(size=9, color="#888"),
            showgrid=False,
            zeroline=False,
            range=[-0.5, len(xs) - 0.5],
        )
        layout["margin"]["b"] = 20              # extra bottom margin for tick labels
    layout["showlegend"] = False
    fig = go.Figure()
    fig.add_trace(go.Scatter(                   # layer 1 — fill only, line hidden
        x=xs, y=data,
        mode="lines",
        fill="tozeroy",
        line=dict(color=color, width=0),
        fillcolor=hex_to_rgba(color, 0.25),
        hoverinfo="skip",                       # layer 2 handles hover
    ))
    fig.add_trace(go.Scatter(                   # layer 2 — line+markers on top
        x=xs, y=data,
        mode="lines+markers",
        line=dict(color=color, width=2),
        marker=dict(size=5, color=color, line=dict(width=0)),
        customdata=xlabels or xs,
        hovertemplate="<b>%{customdata}</b><br>%{y}<extra></extra>",
    ))
    fig.update_layout(**layout)
    return fig

# Plotly table with alternating row backgrounds
def mini_table(headers, rows):
    fig = go.Figure(go.Table(
        header=dict(
            values=headers,
            fill_color="#1a1a1a",
            font=dict(color="#888", size=9),
            align="left",
            line=dict(color="#2a2a2a", width=1),
            height=22,
        ),
        cells=dict(
            values=list(zip(*rows)),            # transpose rows → columns for Plotly Table
            fill_color=["#111", "#0d0d0d"] * (len(rows) // 2 + 1),
            font=dict(color="#ccc", size=10),
            align="left",
            line=dict(color="#1e1e1e", width=1),
            height=20,
        ),
    ))
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=TRANSPARENT,
        plot_bgcolor=TRANSPARENT,
        height=160,
        margin=dict(l=0, r=0, t=0, b=0),
    )
    return fig

# Choropleth map scoped to Europe, coloured by metric value
def mini_map(iso3, values, label, colorscale):
    fig = go.Figure(go.Choropleth(
        locations=iso3,
        z=values,
        colorscale=colorscale,
        showscale=False,
        marker=dict(line=dict(color="#222", width=0.5)),
        hovertemplate="<b>%{location}</b><br>" + label + ": %{z}K<extra></extra>",
    ))
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=TRANSPARENT,
        plot_bgcolor=TRANSPARENT,
        height=140,
        margin=dict(l=0, r=0, t=0, b=0),
        geo=dict(
            scope="europe",
            bgcolor=TRANSPARENT,
            showframe=False,
            showcoastlines=False,
            showland=True,  landcolor="#1a1a1a",
            showocean=True, oceancolor=TRANSPARENT,
            showcountries=True, countrycolor="#2a2a2a",
            projection_type="natural earth",
        ),
    )
    return fig

# Horizontal bar chart — first country in list appears at the top
def country_hbar(countries, values, color):
    fig = go.Figure(go.Bar(
        x=values,
        y=countries,
        orientation="h",
        marker=dict(color=color, opacity=0.8, line=dict(width=0)),
        hovertemplate="<b>%{y}</b><br>€%{x}K<extra></extra>",
    ))
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=TRANSPARENT,
        plot_bgcolor=TRANSPARENT,
        height=160,
        margin=dict(l=0, r=4, t=4, b=0),
        xaxis=dict(visible=False),              # bar length is self-evident
        yaxis=dict(
            visible=True,
            tickfont=dict(size=9, color="#888"),
            showgrid=False,
            zeroline=False,
            autorange="reversed",               # top country = first in list
        ),
    )
    return fig

# ── Flip card builder ────────────────────────────────────────────

# Builds a 3-D flip card — front shows KPI+chart, back shows trend on click
def flip_card(card_id, title, value, subtitle, back_fig, front_fig):
    arrow = "↑" if "↑" in subtitle else ("↓" if "↓" in subtitle else "→")
    badge_color = "success" if arrow == "↑" else ("danger" if arrow == "↓" else "secondary")

    badge = dbc.Badge(
        [arrow, " ", subtitle.lstrip("↑↓→ ")],  # arrow + text e.g. "+12% vs last month"
        color=badge_color,
        pill=True,
        style={"fontSize": "9px", "fontWeight": "600"},
    )

    title_row = dbc.Stack(                       # title and badge on opposite ends
        [
            html.Span(title, style={
                "fontSize": "11px", "color": "#666",
                "textTransform": "uppercase", "letterSpacing": "0.08em",
            }),
            badge,
        ],
        direction="horizontal",
        className="justify-content-between align-items-center",
    )

    front = html.Div(                            # front face — KPI value + chart
        className="flip-card-front",
        children=[
            title_row,
            html.Div(value, className="card-value"),
            dcc.Graph(
                figure=front_fig,
                config={"displayModeBar": False},
                style={"flex": "1", "marginTop": "4px"},
            ),
        ],
    )

    back = html.Div(                             # back face — revealed after click
        className="flip-card-back",
        children=[
            title_row,
            dcc.Graph(
                figure=back_fig,
                config={"displayModeBar": False},
                style={"flex": "1", "marginTop": "8px"},
            ),
        ],
    )

    return html.Div(                             # outer div = 3-D stage
        className="flip-card",
        children=[
            html.Div(                            # inner div = rotating element
                id=f"{card_id}-inner",
                className="flip-card-inner",
                n_clicks=0,
                children=[front, back],
            )
        ],
    )

# ── KPI card data ────────────────────────────────────────────────
# Tuple order: (card_id, title, value, subtitle, back_fig, front_fig)

CARDS = [
    (
        "c1", "Revenue", "€950K", "↑ +12% vs last month",
        mini_area_line(REVENUE_VALUES, "#818cf8", REVENUE_LABELS),  # back: monthly trend
        mini_map(MAP_ISO3, MAP_VALUES, "€Revenue", [[0, "#1a1030"], [1, "#818cf8"]]),  # front: map
    ),
    (
        "c2", "Gross Profit", "€260K", "↑ Stable margin",
        mini_table(PROFIT_TABLE_HEADERS, PROFIT_TABLE_ROWS),        # back: breakdown table
        country_hbar(HBAR_COUNTRIES, HBAR_VALUES, "#fb923c"),       # front: horizontal bar
    ),
]

# ── Layout ───────────────────────────────────────────────────────

app.layout = dbc.Container(
    [
        html.Div("KPI Dashboard", style={        # page title
            "textAlign": "center", "color": "#f0f0f0",
            "fontSize": "18px", "fontWeight": "600",
            "letterSpacing": "0.05em", "textTransform": "uppercase",
            "marginTop": "32px", "marginBottom": "4px",
        }),
        html.Div("Click a card to see the trend", style={  # subtitle hint
            "textAlign": "center", "color": "#444",
            "fontSize": "11px", "marginBottom": "40px",
        }),
        dbc.Row(
            [dbc.Col(flip_card(*c), xs=12, sm=8, md=4) for c in CARDS],  # one card per column
            justify="center",
            className="g-3 pb-5",
        ),
    ],
    fluid=True,                                  # full-width, no max-width cap
)

# ── Flip callback ────────────────────────────────────────────────

# Odd click count → flipped (back visible); even → front visible
@app.callback(
    *[Output(f"c{i}-inner", "className") for i in range(1, len(CARDS) + 1)],  # one output per card
    *[Input(f"c{i}-inner", "n_clicks")  for i in range(1, len(CARDS) + 1)],  # one input per card
)
def flip(*clicks):
    return [
        "flip-card-inner flipped" if n and n % 2 == 1 else "flip-card-inner"
        for n in clicks
    ]

if __name__ == "__main__":
    app.run(debug=True)  # debug=True enables hot reload and error overlay
```

style.css:

```c
/* ── Global ─────────────────────────────────────────────────────── */
body, .container-fluid {
  background-color: #474343 !important;
}

/* ── Flip card stage ─────────────────────────────────────────────
   perspective creates the 3-D depth for the rotation effect       */
.flip-card {
  width: 100%;
  height: 260px;
  perspective: 1000px;
}

/* ── Rotating element ────────────────────────────────────────────
   preserve-3d keeps front/back in the same 3-D space;
   transition drives the smooth flip animation                     */
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.65s cubic-bezier(0.4, 0.2, 0.2, 1);
  transform-style: preserve-3d;
  cursor: pointer;
}

/* flipped class toggled by the Dash callback on click             */
.flip-card-inner.flipped {
  transform: rotateY(180deg);
}

/* ── Front & back shared styles ─────────────────────────────────
   backface-visibility: hidden hides the face when it is rotated
   180 ° away from the viewer                                      */
.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 16px;
  border: 1px solid #2a2a2a;
  box-shadow: none !important;
  backface-visibility: hidden;
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.flip-card-front {
  background: linear-gradient(160deg, #222 0%, #1a1a1a 100%);
}

/* back face is pre-rotated 180 ° so it appears correct after flip */
.flip-card-back {
  background: #1c1c1c;
  transform: rotateY(180deg);
}

/* subtle border highlight on hover                                */
.flip-card-inner:hover .flip-card-front,
.flip-card-inner:hover .flip-card-back {
  border-color: #3a3a3a;
}

/* ── Typography ─────────────────────────────────────────────────── */
.card-title {
  color: #666;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 500;
}

.card-value {
  font-size: 32px;
  color: #f0f0f0;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1;
}
```
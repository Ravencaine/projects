---
created: 2026-08-09
updated: 2026-08-09
source: "Creating a Custom KPI Scorecard in Power BI.md"
note_type: workflow
tags: [power-bi, kpi, scorecard, dax, unichar, conditional-formatting, matrix]
---

# KPI Scorecard — UNICHAR + SWITCH Matrix Pattern

Build a custom KPI scorecard in Power BI using a Matrix visual, DAX measures, and conditional formatting — replacing the built-in KPI visual with full control over thresholds and symbols.

## Prerequisites

- Power BI Desktop
- A fact table with a numeric measure to serve as the KPI value (e.g., sales, revenue)
- Optional: a date dimension for period-over-period comparison

## Steps

### 1. Create the KPI Value measure

Define a base measure to serve as the KPI's numeric value. This is what gets compared against your thresholds.

```dax
KPI Value = YEAROVERYEAR(SUM(Sales[Amount]))
```

> Any measure works — revenue, margin %, count of orders, etc. The key is it must be a single scalar value per context.

### 2. Create the KPI Status measure (threshold logic)

Use `SWITCH(TRUE(), ...)` to assign a status code based on defined thresholds. Centralising thresholds here means they update everywhere automatically.

```dax
KPI Status = SWITCH(TRUE(),
    [KPI Value] < -5, -1,   // negative threshold
    [KPI Value] > 5,   1,   // positive threshold
    0                    // neutral (within ±5%)
)
```

| Status | Meaning |
|--------|---------|
| `-1` | Below negative threshold — negative trend |
| `0` | Within the neutral band |
| `1` | Above positive threshold — positive trend |

### 3. Create the KPI Indicator measure (UNICHAR symbols)

Render a Unicode arrow symbol based on the status. This replaces numeric status codes with visual indicators.

```dax
KPI Indicator =
VAR UpArrow      = UNICHAR(8593)    // ↑
VAR DownArrow    = UNICHAR(8595)    // ↓
VAR SidewaysArrow = UNICHAR(8596)  // →
RETURN
    SWITCH([KPI Status],
        -1, DownArrow,
         1, UpArrow,
        SidewaysArrow)
```

### 4. Create the KPI Color measure (conditional formatting driver)

Define the color names as a text measure. These feed Power BI's conditional formatting.

```dax
KPI Color =
SWITCH([KPI Status],
    -1, "Red",
     1, "Green",
    "Yellow")
```

### 5. Apply conditional formatting to the Matrix

1. Add a Matrix visual to the canvas
2. Drag your row/category fields to **Rows**
3. Replace the numeric KPI field with **KPI Indicator** and **KPI Color**
4. Select the Matrix → **Format** pane → **Cell elements**
5. For the **KPI Indicator** field: **Font color** → **Conditional formatting** → **Field value** → select `KPI Color`
6. For the **KPI Value** field: repeat the conditional font color step

### 6. Add a Report Tooltip (optional)

Create a tooltip measure that surfaces on hover:

```dax
Report Tooltip = SELECTEDVALUE(Sales[Amount])
```

Enable tooltips on the Matrix fields and link to a detail page or leave as-is for inline value display.

### 7. Verify

Hover over KPI indicators to confirm:
- Arrows render correctly (▲ ↓ →)
- Font colors match the status (red/green/yellow)
- Thresholds apply consistently across all rows

## Variations

**Percent-of-target pattern:** Replace `[KPI Value] < -5` with `DIVIDE([Actual], [Target]) - 1 < -0.05`

**Multi-tier thresholds (5 levels):** Extend the SWITCH with two intermediate values — e.g., `[-10, -5)` = deep red, `[-5, 0)` = amber, `0` = neutral, `(0, 5]` = lime, `> 5` = bright green

**Emoji variant:** Replace UNICHAR codes with emojis (`"📈"`, `"📉"`, `"➖"`) for richer visual impact in text boxes and KPI cards

## Common Errors

- **Blanks in KPI Value** → Status returns blank, not 0. Wrap in `IF(ISBLANK(...), 0, ...)` if blanks are possible
- **Wrong threshold direction** → Verify the sign convention: `< -5` means more than 5 percentage points negative
- **UNICHAR not rendering** → Test in Power BI Service — some fonts do not support all Unicode glyphs

## Related

- [[UNICHAR-KPI-Indicator-SWITCH-Pattern]] — the three-measure composition (status + indicator + color)
- [[emoji-kpi-card-dax-patterns]] — emoji-based KPI status (no conditional formatting dependency)
- [[emoji-kpi-card-trend-icon]] — simple delta-based trend emoji in KPI cards
- [[UNICHAR]] — DAX function reference
- [[SWITCH]] — SWITCH(TRUE(), ...) threshold pattern
- [[conditional-formatting-in-power-bi]] — conditional formatting reference
- [[power-graphing]] — Matrix visual as chart replacement
- [[enhancing-data-narratives-power-bi-tooltips]] — tooltip patterns for KPI detail

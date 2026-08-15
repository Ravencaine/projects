---
created: 2026-08-09
updated: 2026-08-09
source: "Creating a Custom KPI Scorecard in Power BI.md"
note_type: pattern
tags: [power-bi, dax, kpi, unichar, switch, conditional-formatting, matrix, scorecard]
---

# UNICHAR KPI Indicator — Three-Measure Chain

A reusable composition for rendering KPI status indicators inside Matrix, table, and card visuals using Unicode characters driven by a status-measure intermediary.

## Purpose

Separates KPI rendering into three single-purpose measures that chain together: a status code, an icon renderer, and a color driver. This keeps each measure composable and independently testable.

## Components

| Measure | Role | Key function |
|---------|------|-------------|
| `KPI Status` | Threshold logic → returns −1 / 0 / 1 | `SWITCH(TRUE(), ...)` |
| `KPI Indicator` | Renders Unicode symbol from status code | `SWITCH(...)` + `UNICHAR()` |
| `KPI Color` | Returns named color string for conditional formatting | `SWITCH(...)` |

## Structure

```dax
-- Measure 1: Status code (threshold-driven)
KPI Status =
SWITCH(TRUE(),
    [<value_expression>] < [<neg_threshold], -1,
    [<value_expression>] > [<pos_threshold],  1,
    0)

-- Measure 2: Icon from status
KPI Indicator =
VAR UpArrow       = UNICHAR(8593)    -- ▲
VAR DownArrow     = UNICHAR(8595)   -- ▼
VAR SidewaysArrow = UNICHAR(8596)   -- ▶
RETURN
    SWITCH([KPI Status],
        -1, DownArrow,
         1, UpArrow,
        SidewaysArrow)

-- Measure 3: Color for conditional formatting
KPI Color =
SWITCH([KPI Status],
    -1, "Red",
     1, "Green",
    "Yellow")
```

## Example

Applied to Year-over-Year sales:

```dax
KPI Status = SWITCH(TRUE(),
    [YoY %] < -5, -1,
    [YoY %] >  5,  1,
    0)

KPI Indicator = SWITCH([KPI Status],
    -1, UNICHAR(8595),   -- ▼
     1, UNICHAR(8593),   -- ▲
            UNICHAR(8596)) -- ▶

KPI Color = SWITCH([KPI Status],
    -1, "Red",
     1, "Green",
    "Yellow")
```

Apply `KPI Color` as a field value in the Matrix formatting pane under **Font color → Conditional formatting → Field value**.

## Variations

**Three-tier with color labels (not arrows):**

```dax
KPI Label = SWITCH([KPI Status],
    -1, "🔴 Below Target",
     1, "🟢 Above Target",
            "🟡 On Target")
```

**Percent-based thresholds (relative to target):**

```dax
KPI Status = SWITCH(TRUE(),
    DIVIDE([Actual], [Target]) - 1 < -0.05, -1,
    DIVIDE([Actual], [Target]) - 1 >  0.05,  1,
    0)
```

**Five-tier (extends with intermediate bands):**

```dax
KPI Status = SWITCH(TRUE(),
    [Value] <= -10, -2,
    [Value] <   -5, -1,
    [Value] <    5,  0,
    [Value] <   10,  1,
              2)
```

## Related

- [[UNICHAR]] — Unicode character rendering in DAX
- [[SWITCH]] — SWITCH(TRUE(), ...) for threshold logic
- [[emoji-kpi-card-dax-patterns]] — emoji-based alternatives to UNICHAR arrows
- [[emoji-direction-dynamic-format]] — Unicode arrows via dynamic format strings
- [[kpi-card-arrow-color-from-growth]] — KPI card visual with arrow + color (different implementation)
- [[sameperiodlastyear-yoy]] — YoY measure used in the source example
- [[selectedvalue]] — SELECTEDVALUE used in the Report Tooltip measure

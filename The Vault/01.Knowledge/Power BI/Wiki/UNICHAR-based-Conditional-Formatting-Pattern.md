---
created: 2026-08-06
updated: 2026-08-06
source: Conditional Formatting in Power BI Multi-Row Card Visuals
note_type: pattern
tags: [conditional-formatting, multi-row-card, dax, unichar, icon, pattern]
---

# UNICHAR-based Conditional Formatting Pattern

DAX pattern for conditional formatting in Power BI visuals that lack built-in conditional formatting (Multi-Row Card, Card, KPI card) — using UNICHAR() to return icon characters based on measure thresholds.

## Pattern 1 — Circle Indicators (Green/Red)

Use for profit growth, variance, or any binary positive/negative metric.

```dax
ProfitGrowthIndicator :=
VAR GreenCircle = UNICHAR(11044)  -- green circle
VAR RedCircle   = UNICHAR(128308) -- red circle
RETURN
    IF(
        [Profit Growth] > 0,
        GreenCircle & " " & FORMAT([Profit Growth], "0.0%"),
        RedCircle   & " " & FORMAT([Profit Growth], "0.0%")
    )
```

To show blank instead of a misleading icon when data is missing:

```dax
VAR Result = IF(
    ISBLANK([Profit Growth]),
    BLANK(),
    IF(
        [Profit Growth] > 0,
        GreenCircle & " " & FORMAT([Profit Growth], "0.0%"),
        RedCircle   & " " & FORMAT([Profit Growth], "0.0%")
    )
)
RETURN Result
```

## Pattern 2 — Arrow Indicators (Up/Down)

Use for directional trends, period-over-period comparisons.

```dax
TrendIndicator :=
VAR UpArrow   = UNICHAR(9650)  -- ▲
VAR DownArrow = UNICHAR(9660)  -- ▼
VAR Neutral   = UNICHAR(9651)  -- ▬
RETURN
    IF(
        [Variance] > 0,
        UpArrow   & " " & FORMAT([Variance], "+0.0%;-0.0%;0.0%"),
        IF(
            [Variance] < 0,
            DownArrow & " " & FORMAT([Variance], "+0.0%;-0.0%;0.0%"),
            Neutral   & " " & "0.0%"
        )
    )
```

## DAX Building Blocks

| Element | Purpose |
|---------|---------|
| `VAR name = <expression>` | Declares a named intermediate variable |
| `UNICHAR()` | Converts a Unicode code point to its character |
| `FORMAT(value, "0.0%")` | Formats as percentage with 1 decimal place |
| `IF(condition, true, false)` | Branching logic |
| `ISBLANK(measure)` | Returns BLANK() when the underlying measure has no data |
| `& " " &` | Concatenates the icon with a space and the formatted number |

## When to Use This Pattern

- Multi-Row Card, Card, or KPI visuals that lack the Conditional formatting option in their Format pane
- Any scenario where an icon-based indicator is more immediately scannable than a colored cell
- Consistent with [[UNICHAR]] — see that note for the full code point reference
- Contrast with [[conditional-formatting-via-dax]] — that pattern uses the Format pane's "Field value" conditional formatting to drive color; this pattern drives the icon itself as text content

## Related

- [[Conditional-Formatting-in-Multi-Row-Card-Visuals]] — concept overview
- [[Add-Conditional-Formatting-to-Multi-Row-Card]] — step-by-step workflow
- [[UNICHAR-Icon-Codes-Reference]] — quick reference for circle and arrow codes
- [[UNICHAR]] — full DAX function reference
- [[conditional-formatting-via-dax]] — color-based conditional formatting via Format pane

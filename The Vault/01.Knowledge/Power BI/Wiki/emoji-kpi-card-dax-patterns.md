---
created: 2026-08-04
updated: 2026-08-05
note_type: pattern
tags: [power-bi, dax, emoji, kpi, visual-design]
source: unknown

---

# Emoji KPI Card DAX Patterns

Using emojis inside KPI card measures to communicate status, trend, or category at a glance — without relying on conditional formatting rules that may not transfer across all visual types.

## Why Emojis in Measures?

- **No dependency on visual formatting** — the status is baked into the measure value itself
- **Transferable** — works across KPI cards, table matrices, multi-row cards, and measure grids
- **Concise** — a single character communicates what a color or icon would take up space to show

## Basic Emoji KPI Pattern

```dax
Emoji KPI Status =
VAR Rating = [Net Promoter Score]
RETURN
    SWITCH(
        TRUE(),
        Rating >= 50, "😊 " & [Net Promoter Score],
        Rating >= 0,  "😐 " & [Net Promoter Score],
        Rating < 0,   "😞 " & [Net Promoter Score],
        "—"
    )
```

## Trend Arrow Pattern

```dax
Trend Emoji :=
VAR Current = [Sales TY]
VAR Previous = [Sales LY]
VAR Delta = DIVIDE(Current - Previous, Previous)
RETURN
    SWITCH(
        TRUE(),
        Delta > 0.05,  "🚀 " & FORMAT(Delta, "0%"),
        Delta > 0,      "↗️ " & FORMAT(Delta, "0%"),
        Delta > -0.05, "↘️ " & FORMAT(Delta, "0%"),
        TRUE,          "📉 " & FORMAT(Delta, "0%")
    )
```

## Category Badge Pattern

```dax
Category Badge :=
VAR Cat = SELECTEDVALUE( Products[Category] )
RETURN
    SWITCH(
        TRUE(),
        Cat = "Electronics", "💻 " & Cat,
        Cat = "Clothing",    "👕 " & Cat,
        Cat = "Food",        "🍎 " & Cat,
        Cat = "Sports",      "⚽ " & Cat,
        Cat
    )
```

## Conditional Space Prefix

Use a leading space after the emoji so the number doesn't crowd the icon:

```dax
"✅ " & [On Time Delivery %]   -- space after emoji
"❌ " & [Late Orders]          -- space after emoji
```

## Limitations

- **Font rendering** — not all fonts render all emojis consistently across Power BI Service
- **Export** — emojis may not render in exported PDFs or Excel
- **Accessibility** — screen readers will read the emoji character; pair with text for full accessibility

## Related

- [[emoji-kpi-card-trend-icon]] — trend icon variants
- [[kpi-narrative-text-udf-pattern]] — narrative text KPI labels

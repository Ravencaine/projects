---
created: 2026-08-02
updated: 2026-08-05
source: 10 Ways to Use Emojis in Power BI
note_type: pattern
tags: [power-bi, emoji, kpi, trend, dax, format, visualization]
---

# KPI Card Trend Icon — Dynamic Emoji from Delta Sign

Add a trend emoji to KPI cards so the direction of change is visible at a glance — before the user reads the number.

## Pattern

```c
Trend Icon :=
IF([Delta] > 0, "📈", "📉")
```

```c
KPI Label :=
[Trend Icon] & " " & FORMAT([Delta], "0.0%")
```

Example output:
- `📈 +12.3%` — positive change
- `📉 -5.1%` — negative change

## Design Notes

- Emojis are text → export cleanly from any visual
- Works in KPI cards, multi-row cards, and text boxes
- Combine with conditional color formatting (green/red) for double reinforcement

## Related

- [[emoji-data-label-pattern]] — broader emoji label patterns
- [[label-variance-if-arrow-format]] — arrow + % text formatting

---
created: 2026-08-02
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: function
tags: [dax, measure, variance]
---

# Process Duration Variation

Simple subtraction of current minus previous period duration — the base variance measure.

```dax
Process Duration Variation = [Process Duration] - [Process Duration Previous Month]
```

## Sign Convention

- Negative → duration decreased (improvement)
- Positive → duration increased

Used as the input to color-switching and formatting measures.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21

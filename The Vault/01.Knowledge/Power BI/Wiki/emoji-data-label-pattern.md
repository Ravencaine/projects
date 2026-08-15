---
created: 2026-08-02
updated: 2026-08-05
source: 10 Ways to Use Emojis in Power BI
note_type: pattern
tags: [power-bi, emoji, data-labels, formatting, dax, visualization, ux]
---

# Emoji Data Label Pattern — Directional, Performance, Alerts, Rankings

Use emojis inside data labels to add instant semantic meaning — no legend or tooltip required.

## Pattern 1: Directional Change

```c
Variation Label =
IF(
    [Change %] > 0,
    "📈 " & FORMAT([Change %], "0.0%"),
    IF(
        [Change %] < 0,
        "📉 " & FORMAT([Change %], "0.0%"),
        "➖ 0%"
    )
)
```

## Pattern 2: Performance Tier

```c
Performance Label =
SWITCH(
    TRUE(),
    [Score] >= 0.8, "🟢 Good",
    [Score] >= 0.5, "🟡 Average",
    "🔴 Poor"
)
```

## Pattern 3: Semester Best/Worst

```c
Semester Label =
SWITCH(
    TRUE(),
    [Semester] = [Best Semester], "🔥 Best Semester",
    [Semester] = [Worst Semester], "🥶 Worst Semester",
    BLANK()
)
```

## Pattern 4: Alert or Insight

```c
Insight Label =
SWITCH(
    TRUE(),
    [Is_Anomaly] = TRUE(), "⚠️ Anomaly",
    [Is_Insight]  = TRUE(), "💡 Key Insight",
    BLANK()
)
```

## Pattern 5: Ranking

```c
Rank Label =
IF([Rank] = 1, "🥇 Top Result", BLANK())
```

## Design Notes

- Emojis are **text:** they export cleanly in all formats
- One emoji per label avoids clutter
- Use consistently across the report to build a **visual language**

## Related

- [[kpi-narrative-text-udf-pattern]] — narrative KPI labels
- [[emoji-kpi-card-dax-patterns]] — KPI card emoji patterns

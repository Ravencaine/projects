---
created: 2026-08-02
updated: 2026-08-05
source: 10 Ways to Use Emojis in Power BI
note_type: pattern
tags: [power-bi, emoji, chart-title, dynamic-title, ux, visualization]
---

# Dynamic Chart Title with Emoji Prefix

Prefix chart titles with an emoji as a visual anchor — users scan the report faster and understand each visual's purpose before reading.

## Static Emoji Prefixes

| Emoji | Meaning |
|-------|---------|
| 📈 | Performance / trend |
| 🏆 | Top N / leaderboard |
| 🧭 | Overview / navigation |
| 🚨 | Alert / anomaly |
| 💡 | Insight / analysis |
| 📊 | General metric |

## Dynamic Emoji in Title

```c
Title :=
"📊 Viewing data for: " & SELECTEDVALUE('Region'[Name])
```

## Design Principles

- Keep emoji consistent: if 📈 means "performance" in one chart, use it consistently everywhere
- Think of emojis as **micro-icons** — they create visual hierarchy without clutter
- Test in both light and dark mode: some emojis render differently

## Related

- [[dynamic-text-titles-in-power-bi]] — dynamic title pattern
- [[dynamic-chart-title-from-metric-dimension-selections]] — metric/dimension-aware title

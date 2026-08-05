---
created: 2026-08-02
source: 10 Ways to Use Emojis in Power BI
note_type: pattern
tags: [power-bi, emoji, axis, category, formatting, power-query]
---

# Emoji Axis Categories — Status, Risk, Timeline, Season

Embed emojis directly in axis category labels so the visual communicates its own legend.

## Application Contexts

| Context | Emojis | Example |
|---------|--------|---------|
| Risk levels | 🔴 🟡 🟢 | High / Medium / Low |
| Project phases | 🚀 🔧 🧪 ✅ | Launch / Dev / Test / Done |
| Seasons | ❄️ 🌷 ☀️ 🍂 | Winter / Spring / Summer / Fall |
| Sentiment | 😀 😐 😞 | Satisfied / Neutral / Dissatisfied |
| Customer type | 👶 💎 💤 | New / Loyal / Inactive |

## Implementation

Store emoji in a lookup table in Power Query, then merge dynamically:

```
CategoryTable:
  Category     | Emoji
  -------------|-------
  High Risk    | 🔴
  Medium Risk  | 🟡
  Low Risk     | 🟢
```

DAX or Power Query merge adds emoji to the axis label column.

## Key Benefit

Users interpret the chart instantly — no legend lookup required. Emojis act as self-documenting visual shorthand.

## Related

- [[emoji-data-label-pattern]] — emoji in data labels
- [[emoji-table-status-flags]] — emoji in table columns

---
created: 2026-08-02
updated: 2026-08-03
source: Stop Using FORMAT() in Power BI — 4 Creative Ways to Dynamically Format Numbers
note_type: atomic
tags: [dax, atomic, dynamic-format, format, number, text]
---

# Dynamic Format String: Number Stays Numeric While Display Changes

Power BI's **Dynamic Format** (modeling pane → measure → format → Dynamic) accepts a format string expression — keeping the underlying value numeric, unlike `FORMAT()` which converts to text.

**Key difference:**

- `FORMAT(value, "0.0")` → text. Cannot sum, sort numerically, or use in charts.
- Dynamic Format `SWITCH(TRUE(), ...)` → number. Fully numeric — sum, sort, filter, chart all work normally.

**When to use:** Any time you want conditional display logic (K/M/B scaling, currency symbols, directional arrows, emojis) while preserving numeric behavior.

> Concept basis for all three format patterns below. See also `auto-scale-kmbt-dynamic-format.md`, `emoji-direction-dynamic-format.md`, `emoji-status-dynamic-format.md`.

---
created: 2026-08-02
updated: 2026-08-03
source: Stop Using FORMAT() in Power BI — 4 Creative Ways to Dynamically Format Numbers
note_type: pattern
tags: [dax, pattern, dynamic-format, emoji, status, target, switch, threshold]
---

# SWITCH-Based Emoji Status Labels in Dynamic Format

Uses a SWITCH expression inside the Dynamic Format string to select emojis based on threshold logic — not just positive/negative, but relative to a target or variance bands.

**Simple two-state variant (above/below target):**
```dax
Sales vs. Target (Dynamic Format String):
    "🥳\+$#,0.00;😬 (\$#,0.00);😐\$#,0.00"
```

**Threshold-based three-state variant:**
```dax
Sales vs. Target (Dynamic Format String):
VAR _TargetPercentage = DIVIDE([Sales vs. Target], [Target])
RETURN SWITCH(
    TRUE(),
    [Sales vs. Target] > 0.05, "0.0,,M 🥳",
    [Sales vs. Target] < -0.05, "0.0,,M 😬",
    "0.0,,M 😐"
)
```

**Design:** Threshold bands (e.g., ±5% from target) determine which emoji appears. `🥳` = above target by margin, `😬` = below target by margin, `😐` = on target. The format string preserves numeric behavior — the emoji is purely display.

> For direction-based (positive/negative change) rather than target-based, see `emoji-direction-dynamic-format.md`. For threshold-free numeric scaling, see `auto-scale-kmbt-dynamic-format.md`.

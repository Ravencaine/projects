---
created: 2026-08-02
updated: 2026-08-03
source: Stop Using FORMAT() in Power BI — 4 Creative Ways to Dynamically Format Numbers
note_type: pattern
tags: [dax, pattern, dynamic-format, emoji, unicode, unichar, direction, indicator]
---

# Emoji/Unicode Direction Indicators in Dynamic Format

Embeds directional indicators (arrows, emojis) directly in the number format string so positive/negative changes are visible at a glance without needing separate label columns.

**Emoji variant (emoji in format string):**
```dax
Sales Variation (Dynamic Format String): "🔼0.0%;🔽-0.0%;0.0%"
```

**Unicode variant (for color-consistent conditional formatting):**
```dax
Sales Variation (Dynamic Format String):
    UNICHAR(9650) & " 0.0%;" & UNICHAR(9660) & " -0.0%;0.0%"
    -- UNICHAR(9650) = ▲ (up triangle)
    -- UNICHAR(9660) = ▼ (down triangle)
```

**Three-part format string structure (positive;negative;zero):**

| Part | Value | Example |
|------|-------|---------|
| Positive | > 0 | `🔼0.0%` or `▲ 0.0%` |
| Negative | < 0 | `🔽-0.0%` or `▼ -0.0%` |
| Zero | = 0 | `0.0%` (no indicator) |

**Unicode vs. emoji:** Use `UNICHAR()` for color-consistent arrows that can be paired with Power BI's conditional font color formatting. Emojis inherit the text color set by Power BI's conditional formatting, which may not match your intent.

> Combine with `emoji-status-dynamic-format.md` for threshold-based emoji selection instead of direction-based.

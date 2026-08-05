---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: function
tags: [unicode, icon, text-rendering, KPI, arrow]
related: [FORMAT, CONCATENATEX, SUBSTITUTE]
---

# UNICHAR

Returns the Unicode character corresponding to a code point. Used in DAX to render arrows, symbols, and icons inside text boxes, card visuals, and KPI labels.

## Signature

```dax
UNICHAR(<number>)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `number` | Integer | Unicode code point (1–114,111) |

## Examples

**Arrow indicators for KPI variance:**
```dax
Variance Arrow =
    IF(
        [Variance] > 0,
        UNICHAR(9650) & " " & FORMAT([Variance], "0.0%"),
        IF(
            [Variance] < 0,
            UNICHAR(9660) & " " & FORMAT([Variance], "0.0%"),
            UNICHAR(9651) & " " & "0.0%"
        )
    )
```

**Traffic light emoji via UNICHAR:**
```dax
Status Indicator =
    SWITCH(
        TRUE(),
        [Performance] > 0.9, UNICHAR(128994),  -- green circle
        [Performance] > 0.7, UNICHAR(129001),  -- yellow circle
        UNICHAR(128308)                         -- red circle
    )
```

**Dynamic header with trend:**
```dax
KPI Header =
    [KPI Name] & " " & UNICHAR(128200) & " vs Prior Period"
```

## Common Unicode Code Points

| Symbol | Code | Use |
|--------|------|-----|
| Up arrow | `9650` (▲) | Positive variance |
| Down arrow | `9660` (▼) | Negative variance |
| Neutral | `9651` (▬) | No change |
| Green circle | `128994` (🟢) | Good status |
| Yellow circle | `129001` (🟡) | Warning |
| Red circle | `128308` (🔴) | Alert |
| Checkmark | `10003` (✓) | Complete |
| Warning | `9888` (⚠) | Caution |
| Rocket | `128640` (🚀) | Launch/good trend |
| Sparkle | `10024` (✨) | Highlight |

## Notes

- Use `UNICHAR` inside `FORMAT` concatenations or directly in text boxes for dynamic icons.
- Bittar's KPI card technique combines `UNICHAR` arrows with `FORMAT` to create professional variance indicators inside card visuals.
- Unicode support in Power BI text boxes and card values is generally reliable, but test across export formats (PDF, PowerPoint) — some glyphs may render differently.
- `UNICHAR(9650)` / `9660` are triangles, not standard arrows — use them when font support for arrows is uncertain.
- As an alternative, Bittar also uses the HTML Content visual + Font Awesome CDN approach (see [[HTML-Content-Visual]]) which provides more icon options.

## Related

- [[FORMAT]] — format numbers, percentages, dates for display
- [[CONCATENATEX]] — build delimited text strings (e.g., list of alert regions)
- [[SUBSTITUTE]] — inject UNICHAR results into longer HTML strings

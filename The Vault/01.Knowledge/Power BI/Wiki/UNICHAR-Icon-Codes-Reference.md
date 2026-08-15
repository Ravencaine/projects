---
created: 2026-08-06
updated: 2026-08-06
source: Conditional Formatting in Power BI Multi-Row Card Visuals
note_type: reference
tags: [unichar, reference, icon, circles, arrows, conditional-formatting, power-bi]
---

# UNICHAR Icon Codes Reference

Quick reference for Unicode code points used in Power BI conditional formatting via DAX UNICHAR() — covering circles, arrows, and status indicators for variance, KPI, and trend display.

## Circle Indicators (Revenue / Growth / Status)

|| UNICHAR Code | Glyph | Name | Use |
||-------------|-------|------|-----|
| Green circle | `11044` | 🟢 | Environmental symbol | Positive growth / on target |
| Red circle | `128308` | 🔴 | Red circle | Negative growth / alert |
| Yellow circle | `129001` | 🟡 | Yellow circle | Warning / partial target |
| White circle (neutral) | `9675` | ○ | Circle | Neutral / no change |
| Black circle | `9679` | ● | Filled circle | Default / unclassified |

## Arrow Indicators (Variance / Trend)

|| UNICHAR Code | Glyph | Name | Use |
||-------------|-------|------|-----|
| Up arrow | `9650` | ▲ | Black up-pointing triangle | Positive variance |
| Down arrow | `9660` | ▼ | Black down-pointing triangle | Negative variance |
| Neutral flat | `9651` | ▬ | Black horizontal rectangle | No change |
| Up-pointing small | `9651` | ▬ | — | Neutral (alternative) |
| Rightwards arrow | `8594` | → | Arrow right | No change / flat trend |
| Heavy right arrow | `10148` | ➤ | — | Positive / forward movement |
| Heavy left arrow | `10094` | ◀ | — | Negative / backward movement |

## Emoji Status Indicators (Rich)

|| UNICHAR Code | Glyph | Name | Use |
||-------------|-------|------|-----|
| Checkmark | `10003` | ✓ | Check mark | Complete / achieved |
| Ballot X | `10007` | ✗ | Ballot X | Not achieved / error |
| Warning sign | `9888` | ⚠ | Warning | Caution / attention needed |
| Rocket | `128640` | 🚀 | Rocket | Launch / strong positive |
| Sparkles | `10024` | ✨ | Sparkles | Highlight / new |

## Implementation Examples

### Basic circle indicator
```dax
IF([Metric] > 0, UNICHAR(11044), UNICHAR(128308))
```

### Arrow with formatted percentage
```dax
IF(
    [Variance] > 0,
    UNICHAR(9650) & " " & FORMAT([Variance], "+0.0%"),
    UNICHAR(9660) & " " & FORMAT([Variance], "+0.0%")
)
```

### Three-state (up / flat / down)
```dax
SWITCH(
    TRUE(),
    [Variance] > 0,  UNICHAR(9650) & " " & FORMAT([Variance], "+0.0%"),
    [Variance] < 0,  UNICHAR(9660) & " " & FORMAT([Variance], "+0.0%"),
    UNICHAR(9651)   & " " & "0.0%"
)
```

## Notes

- **11044** (🟢) is preferred over 128994 for the green circle — more widely supported in Power BI text rendering
- **9650/9660** (triangles) are more reliably rendered than Unicode arrow characters — use these over ←↑→↓
- Test icon rendering in PDF and PowerPoint export — some glyphs may not render in all export formats
- For a full reference of all DAX UNICHAR applications beyond icons, see [[UNICHAR]]

## Related

- [[UNICHAR]] — full DAX function reference (examples, parameters, related functions)
- [[UNICHAR-based-Conditional-Formatting-Pattern]] — the pattern using these codes in Power BI visuals
- [[Conditional-Formatting-in-Multi-Row-Card-Visuals]] — concept overview
- [[Add-Conditional-Formatting-to-Multi-Row-Card]] — step-by-step workflow

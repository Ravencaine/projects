---
created: 2026-08-14
source: 4 ways to use error bars in Power BI - small feature, big impact.md
note_type: reference
tags: [error-bars, power-bi, reference]
---

# Error Bar Configuration Reference

All configuration options for Power BI error bars, with their effects.

## Quick Reference

### Enable / Disable
| Setting | Effect |
|---------|--------|
| Enable = On | Error bar appears on the selected series |
| Enable = Off | No error bar |

### Type
| Type | Description |
|------|-------------|
| **By Field** | Upper and Lower bounds are measures you specify |
| **By Percentage** | Bounds are percentages of the series value (e.g., 10% means ±10% of value) |
| **Fixed Value** | A single fixed value added/subtracted from the series |

### Relationship (By Field mode only)
| Setting | Effect |
|---------|--------|
| **Absolute** | Bounds are absolute values on the axis |
| **Percentage** | Bounds are percentages of the series value |
| **Number** | Bounds are a number added/subtracted from the series value |

### Bar Settings
| Setting | Options | Effect |
|---------|---------|--------|
| Bar on/off | On / Off | Toggle the connecting line |
| Match series color | On / Off | Inherit series color or use custom |
| Bar color | Any color | Custom color for the connecting line |
| Width | 1–10px | Thickness of the connecting line |
| Border size | 0–10px | Thickness of the outer border |
| Border color | Any color | Border around the bar |

### Marker Settings
| Setting | Options | Effect |
|---------|---------|--------|
| Markers on/off | On / Off | Toggle end-cap markers |
| Shape | Filled circle, hollow circle, dash, diamond, square, triangle, X, asterisk | Marker shape |
| Size | 1–20px | Marker size |
| Color | Any color | Marker fill color |
| Border on/off | On / Off | Toggle marker border |
| Border color | Any color | Border color |
| Border width | 1–5px | Border thickness |

## Common Patterns

### Vertical flag (lower bound at 0)
- Type: By Field
- Upper bound: conditional measure (BLANK at non-target positions)
- Lower bound: `Dummy0` (returns 0)
- Bar: on, custom color, width 1
- Markers: off

### Rounded bar cap
- Type: By Percentage
- Upper bound: 0%
- Lower bound: 100%
- Bar: off
- Markers: on, filled circle, size 8–12px, match bar color

### Whisker line
- Type: By Field
- Relationship: Absolute
- Upper bound: MAX
- Lower bound: MIN
- Bar: on, width 1, border 0
- Markers: on, dash shape, size 5–7px

## Notes

- Error bars attach to a specific series on the chart — the series does not need to be visible
- Set the series transparency to 100% to use it as an invisible anchor
- Multiple error bars can be added to the same series for different configurations
- The error bar draws nothing for any category where both bounds return BLANK()

## Related

- [[Error-Bar-Data-Flags]]
- [[Error-Bar-Rounded-Bars]]
- [[Error-Bar-Dumbbell-Chart]]
- [[Error-Bar-Boxplot]]

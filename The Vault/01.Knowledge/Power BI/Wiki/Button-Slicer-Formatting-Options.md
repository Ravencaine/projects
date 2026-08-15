---
created: 2026-08-06
updated: 2026-08-06
source: Button Slicer Level Up Your Power BI Reports!
note_type: reference
tags: [button-slicer, formatting, power-bi, quick-reference]
---

# Button Slicer Formatting Options

Quick reference for all formatting controls available on a Button Slicer (New Card visual in slicer mode).

## Quick Reference

### Size & Style

| Control | Options |
|---------|---------|
| Shape | Rectangle, Rounded rectangle, Ellipse, Custom shape |
| Background | Color, gradient, or transparent |
| Border | On/off, color, width |
| Font | Family, size, color, bold/italic |

### Colors

| Control | Description |
|---------|-------------|
| Button colors | Set per-state (Default, Hover, Pressed, Selected) |
| Borders | Independent border per state |
| Gradients | Linear or solid fill options |
| Conditional formatting | Threshold-based rules for fill, font, image |

### Call Out Values

| Control | Description |
|---------|-------------|
| Add data field | Select any field from the data model |
| Image URL field | Display images alongside text |
| Label field | Add a second line of text (description/subtitle) |

### State-Specific Formatting

| State | Typical Use |
|-------|-------------|
| **Default** | Base appearance of all buttons |
| **Hover** | Slightly lighter fill, 1px accent border |
| **Pressed** | Darker fill while button is being clicked |
| **Selected** | Accent color fill, white font, no border |

### Images

| Setting | Value |
|---------|-------|
| Image fit | Normal, Fit, Fill, Constrain |
| Position | Left, Right, Top, Bottom |
| Image area size | Percentage of button size |
| Space between image and callout | Pixel value |
| Hover saturation | Reduce on hover for feedback effect |

## Notes

- The New Card visual is a **preview feature:** must be enabled via File → Options → Preview features.
- Image URL columns require **Data category → Image URL** set in the model view.
- For the official Microsoft documentation on the New Card visual, see: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-new-card

## Related

- [[Button-Slicer]] — concept overview
- [[Create-a-Button-Slicer]] — step-by-step setup
- [[Conditional-Button-Slicer]] — conditional formatting pattern
- [[New-Power-BI-Slicer-Features]] — general slicer reference

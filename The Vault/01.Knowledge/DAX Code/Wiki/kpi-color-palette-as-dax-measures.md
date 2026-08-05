---
created: 2026-08-02
source: One UDF, All Your KPI Colors 🎨: 3 Steps in Power BI
note_type: pattern
tags: [dax, pattern, color, kpi, theme, design-system]
---

# KPI Color Palette: Colors as DAX Measures (Theme-Agnostic)

Store hex color values in dedicated DAX measures rather than hardcoding in themes or UDFs.

**Baseline palette** (Bittar):
| Measure | Purpose |
|---------|---------|
| `_Color Dark Green` | positive font color |
| `_Color Light Green` | positive background |
| `_Color Dark Red` | negative font color |
| `_Color Light Red` | negative background |
| `_Color Text Secondary` | neutral/zero font |

**Why measures over theme:**
- Copy/paste between projects via DAX Studio or Tabular Editor
- UDF stays theme-agnostic — swap the color measures, keep the same UDF
- One palette change propagates across all UDFs and measures

> For named color sets (e.g. accent palettes), add measures per shade: `_ColorAccent1Dark`, `_ColorAccent4Dark`, etc.

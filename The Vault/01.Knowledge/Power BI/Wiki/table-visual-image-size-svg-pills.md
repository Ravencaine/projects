---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: snippet
tags: [powerbi, snippet, table-visual, svg, image-size]
---

# Table Visual Image Size for SVG Pills

When rendering SVG pills in a table visual, the visual's image size must match the UDF's canvas constants.

**Required settings:**
| Property | Value | Must match |
|----------|-------|------------|
| Height | `28 px` | `UDF_SVGPillCanvas` → `canvasHeight = 28` |
| Width | `200 px` | `UDF_SVGPillCanvas` → `canvasWidth = 200` |

**Location:** Table visual → Values → Grid → Image size

If the visual size and UDF canvas constants are mismatched, the pill will be cropped or misaligned. Update both locations together when customizing pill dimensions.

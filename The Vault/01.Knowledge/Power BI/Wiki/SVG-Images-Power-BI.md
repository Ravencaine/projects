---
created: 2026-08-05
source: 5 Powerful Ways Import Images Power BI (Boniface Muchendu)
note_type: atomic
tags: [power-bi, svg, dax, image, scalable, dynamic]
---

# SVG Images in Power BI

Embedding SVG (Scalable Vector Graphics) XML directly in a DAX measure, setting the Image URL data category, and rendering crisp scalable images that adapt to any size without quality loss.

## Why SVG

SVG is resolution-independent — it scales to any size without pixelation. Unlike raster images (PNG/JPG), SVG stores drawing instructions (vector paths) rather than pixel grids. This makes it ideal for:

- Icons and logos that need to scale
- Dynamic shapes that can be recoloured via DAX
- Custom KPI indicators and status icons

## Steps

### 1. Obtain or create SVG code

Export from Figma, Illustrator, or write manually. The SVG XML looks like:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" fill="#2C6D6A"/>
</svg>
```

### 2. Create the DAX measure

```dax
SVG Circle = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='40' fill='#2C6D6A'/></svg>"
```

Note the prefix: `data:image/svg+xml;utf8,` — this is what Power BI uses to identify SVG content.

### 3. Set data category

Select the measure → **Modelling ribbon → Data category → Image URL**

### 4. Add to visual

Drag the measure into a Table or Matrix visual. Power BI renders the SVG.

## Dynamic SVG with DAX

The power of SVG in Power BI is that the XML can be built with DAX:

```dax
SVG Dynamic Status =
VAR _color = IF([Sales Target Met], "#2C6D6A", "#D8404A")
RETURN
"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='40' fill='" & _color & "'/></svg>"
```

This creates a dynamic circle that changes colour based on whether a sales target was met — something impossible with raster images.

## Known Limitations

- Complex SVGs with external references (images, fonts) may not render correctly
- SVG must be valid XML — malformed SVG will not display
- Some older visual types do not support image URL rendering

## Related

- [[SVG-in-Power-BI-Key-Concepts]]
- [[Binary-Base64-Image-Model]]
- [[Image-URL-Data-Category]]

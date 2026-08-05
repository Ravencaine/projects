---
created: 2026-08-05
updated: 2026-08-05
source: 5 Powerful Ways Import Images Power BI (Boniface Muchendu)
note_type: atomic
tags: [power-bi, image, base64, binary, model, offline, binarytotext]
---

# Binary/Base64 in Model

Storing images as base64 strings directly in the Power BI model — ensuring images are always available offline, embedded in the PBIX, without requiring an internet connection.

## Overview

1. Collect images in a local folder
2. Use the **Folder** connector in Power Query to load all files
3. Convert binary to base64 via `Binary.ToText(... BinaryFormat.Base64)`
4. Prefix with the MIME type: `data:image/png;base64,` + base64 string
5. Set the column's data category to **Image URL**
6. Display in a table visual

## Power Query Steps

```m
// Step 1: Get files from folder
Source = Folder.Files("C:\YourImageFolder"),

// Step 2: Filter to image files
Filtered = Table.SelectRows(Source, each [Extension] = ".png" or [Extension] = ".jpg"),

// Step 3: Convert binary to base64 string
Base64Column = Table.AddColumn(
    Filtered,
    "Base64",
    each "data:image/png;base64," & Binary.ToText([Content], BinaryFormat.Base64)
)

// Step 4: Set data category to Image URL in the model view
```

## Key Requirements

| Requirement | Detail |
|-----------|--------|
| Data category | Set the base64 column to **Image URL** in Model view (not in Power Query) |
| MIME prefix | Must include `data:image/png;base64,` or `data:image/jpeg;base64,` |
| Column limit | Power BI column has a ~32,767 character limit — large images may exceed this |

## The Character Limit Problem

Large high-resolution images produce very long base64 strings. Power BI truncates strings that exceed the column limit, resulting in broken images. Solutions:

- Resize images to smaller dimensions before encoding
- Use a thumbnail/scaled-down version
- Prefer [[Web-Image-URL-Measure]] for large image sets

## When to Use

- Small images: logos, icons, profile thumbnails, status badges
- Offline-first reports where internet is unreliable
- Reports that must be fully self-contained

## Related

- [[Binary-ToText-Base64-Power-Query]]
- [[Image-URL-Data-Category]]
- [[SVG-Images-Power-BI]]

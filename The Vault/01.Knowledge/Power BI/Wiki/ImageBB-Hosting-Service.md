---
created: 2026-08-05
source: 5 Powerful Ways Import Images Power BI (Boniface Muchendu)
note_type: reference
tags: [power-bi, image, hosting, imagebb, url, web-image]
---

# ImageBB — Image Hosting Service

ImageBB (imagebb.com) is a free image hosting service that generates direct URLs for images, making them usable in Power BI via the [[Web-Image-URL-Measure]] method.

## Workflow

1. Upload the image to [imagebb.com](https://imagebb.com)
2. ImageBB generates multiple URL formats — copy the **direct URL** (typically ends in the image filename with extension)
3. Paste the direct URL into a DAX measure, set the data category to **Image URL**, and add to a table visual

## URL Format

```
https://i.ibb.co/<hash>/<filename>.png
```

Or the older format:

```
https://image.ibb.co/j6RzvG/<filename>.png
```

The URL must end in the image file extension (`.png`, `.jpg`) for Power BI to recognise it as an image URL.

## Advantages

- Free with no account required for basic use
- No local storage needed — images are hosted externally
- Fast rendering via CDN

## Limitations

- Requires internet connectivity
- Free tier images may expire or be deleted by the host (uploaded images are subject to imagebb.com's retention policy)
- For permanent reports, prefer embedding images in the PBIX or using a dedicated cloud storage service

## Related

- [[Web-Image-URL-Measure]]
- [[Binary-Base64-Image-Model]]

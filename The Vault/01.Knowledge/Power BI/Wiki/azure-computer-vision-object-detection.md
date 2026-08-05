---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [azure-computer-vision, object-detection, api, bounding-box, image-analysis]
---

# Azure Computer Vision — Detect Objects

Identifies objects in an image and returns their locations as bounding box coordinates.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Computer Vision |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/vision/v3.1/objects` |
| Method | POST |
| Input | Image URL or binary image data |
| Output | `{ "objects": [{ "object": "...", "confidence": 0.95, "rectangle": { "x": 100, "y": 50, "w": 200, "h": 150 } }] }` |

## Response Fields

| Field | Description |
|-------|-------------|
| object | Object label (e.g., "person", "laptop", "chair") |
| confidence | Model confidence (0.0–1.0) |
| rectangle | Bounding box: x, y (top-left corner), w (width), h (height) in pixels |

## Power Query Consideration

Object detection returns a list of objects per image. In Power Query, invoke the function, then expand the resulting record list. Each row represents one detected object — images with multiple objects produce multiple rows.

## Use Cases

- Count objects in retail shelf photos
- Detect people in surveillance footage
- Audit product placements in marketing images

## Related

- [[azure-computer-vision-image-description]]
- [[azure-custom-vision]]
- [[ai-insights-vision-power-bi]]

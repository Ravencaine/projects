---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [azure-computer-vision, describe-image, api, image-analysis, captioning]
---

# Azure Computer Vision — Describe Image

Returns a human-readable caption describing the content of an image, plus a list of tags describing objects, colours, and actions in the image.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Computer Vision |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/vision/v3.1/describe` |
| Method | POST |
| Input | Image URL or binary image data |
| Output | `{ "description": { "captions": [{ "text", "confidence" }], "tags": [...] }, "tags": [...] }` |

## Power Query Custom Function (URL-based)

```m
(imageUrl as text) =>
let
    url = "https://<resource>.cognitiveservices.azure.com/vision/v3.1/describe",
    body = "{ ""url"": """ & imageUrl & """ }",
    response = Json.Document(Web.Contents(url, [
        Headers = [
            #"Ocp-Apim-Subscription-Key" = "YOUR-KEY-HERE",
            #"Content-Type" = "application/json"
        ],
        Content = Text.ToBinary(body)
    ])),
    caption = response[description][captions]{0}[text]
in
    caption
```

## Use Cases

- Auto-caption product photos for accessibility
- Categorise image libraries by visual content
- Tag clothing images for retail inventory analysis

## Related

- [[azure-computer-vision-object-detection]]
- [[azure-custom-vision]]
- [[ai-insights-vision-power-bi]]

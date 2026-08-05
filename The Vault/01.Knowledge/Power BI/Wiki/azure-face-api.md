---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [azure-face-api, api, age, emotion, glasses, hair, mask, facial-analysis]
---

# Azure Face API — Detect Facial Attributes

Detects faces in images and returns attributes: age, emotion, glasses, hair colour, mask wearing.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Face |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/face/v1.0/detect` |
| Method | POST |
| Input | Image URL or binary image data |
| Output | Array of face objects with attributes |

## Attributes

| Attribute | Values |
|-----------|--------|
| age | Integer (estimated age) |
| gender | male, female, unknown |
| emotion | anger, contempt, disgust, fear, happiness, neutral, sadness, surprise (scores 0–1) |
| glasses | NoGlasses, ReadingGlasses, Sunglasses, SwimmingGoggles |
| hair | bald, invisible, hairColor (array of { color, confidence }) |
| mask | noMask, faceMask, faceMaskWithFaceMouth, faceMaskWithFaceNose |
| faceRectangle | { top, left, width, height } |

## Power Query Custom Function

```m
(imageUrl as text) =>
let
    url = "https://<resource>.cognitiveservices.azure.com/face/v1.0/detect?returnFaceAttributes=age,gender,emotion,glasses,hair,mask",
    body = "{ ""url"": """ & imageUrl & """ }",
    response = Json.Document(Web.Contents(url, [
        Headers = [
            #"Ocp-Apim-Subscription-Key" = "YOUR-KEY-HERE",
            #"Content-Type" = "application/json"
        ],
        Content = Text.ToBinary(body)
    ]))
in
    response
```

## Notes

- Face API requires a separate **Face** resource (not the same as Computer Vision)
- Returns an **array** of faces — images with multiple faces produce multiple result rows
- Privacy and consent requirements apply — only use on images where individuals have consented to facial analysis

## Related

- [[responsible-ai-six-principles]]
- [[pii-detection]]

---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [custom-vision, workflow, training, tagging, publish, prediction]
---

# Custom Vision Workflow — Build → Train → Publish

Step-by-step process for building a Custom Vision model and integrating it into Power BI.

## Steps

### 1. Create Project

Custom Vision portal (customvision.ai) → New Project:
- Name: descriptive (e.g., `clothing-classifier`)
- Project type: **Classification**
- Classification type: **Multiclass** (one tag per image) or **Multilabel** (multiple tags per image)
- Domain: select appropriate domain (General, Food, Retail, etc.) or leave as None

### 2. Upload Images

Upload images in groups. For each group:
- Select all images of the same type (e.g., all dress photos)
- Add a tag (e.g., "dress")
- Repeat for all categories

Minimum recommended: 50 images per tag for reasonable accuracy.

### 3. Train

Click **Train** → select **Quick Train** or **Advanced Train**:
- Quick Train: faster, less accurate
- Advanced Train: longer, better accuracy

### 4. Evaluate

Review Precision, Recall, and AP from the Performance tab.

### 5. Publish Iteration

Click **Publish** → name the iteration → note:
- **Prediction URL** (used in Power BI)
- **Prediction Key** (used in Power BI)

### 6. Integrate in Power BI

Call the published endpoint from a Power Query custom function:

```m
(imageUrl as text) =>
let
    url = "https://<region>.api.cognitivecustomvision.com/v3.0/projects/<project-id>/classify/iterations/<iteration-name>/url",
    body = Json.Document("{ ""url"": """ & imageUrl & """ }"),
    headers = [
        #"Prediction-Key" = "YOUR-KEY-HERE",
        #"Content-Type" = "application/json"
    ],
    response = Json.Document(Web.Contents(url, [
        Headers = headers,
        Content = Text.ToBinary(body)
    ]))
in
    response
```

## Related

- [[azure-custom-vision]]
- [[custom-vision-evaluation-metrics]]
- [[anonymous-image-access-power-bi]]

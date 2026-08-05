---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [azure-custom-vision, image-classification, supervised, training, power-bi]
---

# Azure Custom Vision — Supervised Image Classification

Train a custom image classifier on your own labelled photos — then call it from Power BI via a REST API.

## Definition

Custom Vision is a supervised image classification service. Unlike Computer Vision (pretrained), Custom Vision lets you upload your own images, label them with categories, and train a model to recognise those categories.

## Key Points

- **Supervised**: requires labelled training images (you tell the model "this is a dog", "this is a cat")
- **Publish to a prediction endpoint** to get an API URL and prediction key
- Prediction endpoint called from Power BI the same way as Computer Vision APIs
- Iteration-based: train → evaluate → retrain → repeat

## Workflow

1. Create a Custom Vision project (classification, multiclass)
2. Upload images grouped by tag
3. Apply tags to each image
4. Train the model
5. Evaluate precision/recall on the test set
6. Publish the iteration
7. Get prediction URL and key
8. Call from Power Query custom function

## Related

- [[custom-vision-workflow]]
- [[custom-vision-evaluation-metrics]]
- [[improving-custom-vision-prediction-feedback]]

---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [custom-vision, prediction-feedback, retrain, training-set, improve]
---

# Improving Custom Vision from Prediction Feedback

Custom Vision's prediction endpoint can send incorrect predictions back to the training set for targeted retraining.

## Purpose

The Prediction API captures every image sent to the published model. Flagging incorrect predictions and re-adding them to the training set with the correct tag improves the model iteratively.

## Process

1. **Capture predictions**: send images to the published prediction endpoint
2. **Flag incorrect predictions**: manually or via user feedback identify misclassifications
3. **Add to training set**: upload flagged images to the correct Custom Vision project with the right tag
4. **Retrain**: train a new iteration
5. **Evaluate**: check Precision/Recall improvement
6. **Publish new iteration**: replace the previous prediction endpoint

## Key Points

- Custom Vision portal → Performance tab → Prediction count shows how many images the model has seen
- Images with prediction counts > 0 are already in the model's experience
- The feedback loop is especially valuable for edge cases the model hasn't seen enough of
- Retrain regularly — models drift as the data distribution changes over time

## Related

- [[azure-custom-vision]]
- [[custom-vision-workflow]]
- [[custom-vision-evaluation-metrics]]

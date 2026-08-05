---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [azure-cognitive-services, overview, categories, ai-services]
---

# Azure Cognitive Services Overview

Microsoft's family of pretrained AI APIs for vision, speech, language, and decision — accessible from Power BI via Power Query custom functions.

## Definition

Azure Cognitive Services is a collection of cloud-based AI APIs that provide pretrained models for common AI tasks. They require no training data and no ML expertise — just an Azure subscription and an API key.

## Service Categories

| Category | Services | Power BI use case |
|----------|---------|------------------|
| **Language** | Language Detection, Key Phrase Extraction, Sentiment Analysis, NER, Entity Linking, PII Detection | Analyse text in Power Query |
| **Vision** | Computer Vision (Describe Image, OCR, Tagging), Custom Vision, Face API | Analyse images via URL in Power BI |
| **Speech** | Speech-to-Text, Text-to-Speech, Translation | Transcribe audio, translate content |
| **Decision** | Content Moderator, Anomaly Detector | Moderate content, detect anomalies in streams |

## Key Points

- All services are **pretrained**: no training data required
- Accessed via **REST API** with an endpoint URL and subscription key
- In Power BI: called via **Power Query custom functions** (Advanced Editor)
- Cognitive Services are charged per transaction (free tier available)
- Requires **Azure subscription**: costs apply beyond free tier limits
- **Power BI Premium** or per-capacity licensing may be required for AI Insights in the Power BI Service

## Related

- [[create-cognitive-services-resource-azure]]
- [[language-detection-api]]
- [[sentiment-analysis-api]]

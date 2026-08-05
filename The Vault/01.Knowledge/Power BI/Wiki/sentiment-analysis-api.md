---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [cognitive-services, sentiment-analysis, api, power-query, positive-negative-neutral]
---

# Sentiment Analysis API — Detect Sentiment

Returns a sentiment score (0.0–1.0) indicating whether the text is positive, negative, or neutral. Supports per-sentence breakdown.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Text Analytics |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/sentiment` |
| Method | POST |
| Input | `{ "documents": [{ "id": "...", "language": "en", "text": "..." }] }` |
| Output | `{ "documents": [{ "sentiment": "positive|negative|neutral", "confidenceScores": { "positive", "negative", "neutral" } }] }` |

## Power Query Custom Function

```m
(text as text, lang as text) =>
let
    url = "https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/sentiment",
    body = "{ ""documents"": [{ ""id"": ""1"", ""language"": """ & lang & """, ""text"": """ & Text.Replace(text, """", "\""") & """ }] }",
    headers = [
        #"Ocp-Apim-Subscription-Key" = "YOUR-KEY-HERE",
        #"Content-Type" = "application/json"
    ],
    response = Json.Document(Web.Contents(url, [
        Headers = headers,
        Content = Text.ToBinary(body)
    ])),
    sentiment = response[documents]{0}[sentiment],
    scores = response[documents]{0}[confidenceScores]
in
    [ Sentiment = sentiment, Score = scores[positive] ]
```

## Interpretation

| Score | Sentiment |
|-------|-----------|
| 0.75–1.00 | Positive |
| 0.25–0.75 | Mixed / Neutral |
| 0.00–0.25 | Negative |

## Related

- [[azure-cognitive-services-overview]]
- [[language-detection-api]]
- [[word-cloud-visual]]

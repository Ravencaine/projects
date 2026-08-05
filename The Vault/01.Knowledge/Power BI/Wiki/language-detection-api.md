---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [cognitive-services, language-detection, api, power-query, multilingual]
---

# Language Detection API — Detect Language

Detects the language of a text string and returns a confidence score. Used in Power Query to route multilingual text for further analysis.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Text Analytics |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/languages` |
| Method | POST |
| Auth | Ocp-Apim-Subscription-Key header |
| Input | `{ "documents": [{ "id": "...", "text": "..." }] }` |
| Output | `{ "documents": [{ "detectedLanguage": { "name", "iso6391Name", "confidenceScore" } }] }` |

## Power Query Custom Function

```m
(text as text) =>
let
    url = "https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/languages",
    body = "{ ""documents"": [{ ""id"": ""1"", ""text"": """ & text & """ }] }",
    headers = [
        #"Ocp-Apim-Subscription-Key" = "YOUR-KEY-HERE",
        #"Content-Type" = "application/json"
    ],
    response = Json.Document(Web.Contents(url, [
        Headers = headers,
        Content = Text.ToBinary(body)
    ])),
    result = response[documents]{0}[detectedLanguage]
in
    result[confidenceScore]
```

## Use Cases

- Route hotel reviews to language-specific sentiment analysis
- Filter multilingual datasets for specific language analysis
- Detect language before applying region-specific NLP

## Related

- [[azure-cognitive-services-overview]]
- [[power-query-custom-function-text-analytics]]
- [[sentiment-analysis-api]]

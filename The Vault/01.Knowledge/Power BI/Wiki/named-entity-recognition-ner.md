---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [cognitive-services, ner, named-entity-recognition, api, power-query, entities]
---

# Named Entity Recognition (NER) — Extract Entities

Identifies and categorises entities (people, organisations, locations, quantities) in text.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Text Analytics |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/entities/recognition/general` |
| Method | POST |
| Input | `{ "documents": [{ "id": "...", "language": "en", "text": "..." }] }` |
| Output | `{ "documents": [{ "entities": [{ "text", "category", "subcategory", "confidenceScore" }] }] }` |

## Entity Categories

| Category | Examples |
|----------|---------|
| Person | Mary-Jo Diepeveen, the CEO |
| Organisation | Microsoft, Packt Publishing |
| Location | Amsterdam, Netherlands |
| Quantity | 3 days, 50% off |
| DateTime | yesterday, 2024-01-01 |
| Event | COVID-19 pandemic |

## Power Query Custom Function

```m
(text as text, lang as text) =>
let
    url = "https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/entities/recognition/general",
    body = "{ ""documents"": [{ ""id"": ""1"", ""language"": """ & lang & """, ""text"": """ & Text.Replace(text, """", "\""") & """ }] }",
    response = Json.Document(Web.Contents(url, [
        Headers = [
            #"Ocp-Apim-Subscription-Key" = "YOUR-KEY-HERE",
            #"Content-Type" = "application/json"
        ],
        Content = Text.ToBinary(body)
    ])),
    entities = response[documents]{0}[entities]
in
    entities
```

## Related

- [[entity-linking]]
- [[azure-cognitive-services-overview]]

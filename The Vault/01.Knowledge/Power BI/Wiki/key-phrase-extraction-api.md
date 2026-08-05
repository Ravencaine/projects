---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [cognitive-services, key-phrase-extraction, api, power-query, topics]
---

# Key Phrase Extraction API — Extract Key Phrases

Returns the most important topics from a text document. Used to surface themes in reviews, support tickets, or social media posts.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Text Analytics |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/keyPhrases` |
| Method | POST |
| Input | `{ "documents": [{ "id": "...", "language": "en", "text": "..." }] }` |
| Output | `{ "documents": [{ "keyPhrases": ["...", "..."] }] }` |

## Power Query Custom Function

```m
(text as text, lang as text) =>
let
    url = "https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/keyPhrases",
    body = "{ ""documents"": [{ ""id"": ""1"", ""language"": """ & lang & """, ""text"": """ & Text.Replace(text, """", "\""") & """ }] }",
    headers = [
        #"Ocp-Apim-Subscription-Key" = "YOUR-KEY-HERE",
        #"Content-Type" = "application/json"
    ],
    response = Json.Document(Web.Contents(url, [
        Headers = headers,
        Content = Text.ToBinary(body)
    ])),
    phrases = response[documents]{0}[keyPhrases]
in
    Text.Combine(phrases, ", ")
```

## Use Cases

- Surface themes from hotel reviews ("cleanliness", "staff", "location")
- Identify trending topics in support tickets
- Extract topics from article headlines for categorisation

## Related

- [[azure-cognitive-services-overview]]
- [[power-query-custom-function-text-analytics]]
- [[language-detection-api]]

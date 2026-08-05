---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [power-query, custom-function, cognitive-services, text-analytics, m-code]
---

# Power Query Custom Function — Text Analytics API

Build a reusable Power Query M function to call Azure Cognitive Services Text Analytics from any table.

## Purpose

A custom function wraps the REST API call in M code. Invoking it on a table column applies the API to every row — returning sentiment, key phrases, or language for each text entry.

## Structure

```m
// Saved as: DetectLanguage(text as text) =>
(text as text) =>
let
    url = "https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/languages",
    body = "{ ""documents"": [{ ""id"": ""1"", ""text"": """ & text & """ }] }",
    response = Json.Document(Web.Contents(url, [
        Headers = [
            #"Ocp-Apim-Subscription-Key" = "YOUR-KEY-HERE",
            #"Content-Type" = "application/json"
        ],
        Content = Text.ToBinary(body)
    ])),
    result = response[documents]{0}[detectedLanguage][name]
in
    result
```

## Invocation

1. In Power Query: Add Column → Invoke Custom Function
2. Select the function name
3. Map the text column to the function's text parameter
4. Power BI calls the API for each row (respects privacy settings)

## Privacy Risk — CRITICAL

> See [[privacy-risk-custom-function-public]]

Custom functions that call external APIs may expose your data to the API provider. Always:
1. Set data source privacy to **Public** for the Cognitive Services endpoint
2. Understand that your text data is transmitted to Azure
3. Never call APIs on PII without explicit consent

## Related

- [[privacy-risk-custom-function-public]]
- [[language-detection-api]]
- [[sentiment-analysis-api]]

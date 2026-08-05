---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [power-automate, http-request, azure-qa, rest-api, cloud-flow]
---

# Power Automate HTTP Request to Q&A Endpoint

A Power Automate cloud flow that receives a question from Power Apps, calls the Azure Q&A prediction endpoint, and returns the answer.

## Prerequisites

- Azure Q&A knowledge base (deployed with prediction endpoint)
- Power Automate license
- Power Apps trigger (When a flow is invoked from a Power App)

## Flow Structure

```
Power Apps (triggerText) → HTTP action → Response to Power Apps
```

## HTTP Action Configuration

| Parameter | Value |
|-----------|-------|
| Method | POST |
| URI | `https://<resource>.cognitiveservices.azure.com/language/:query-knowledgebases/projects/<project-name>/generat答案` |
| Headers | `Ocp-Apim-Subscription-Key: <key>` |
| | `Content-Type: application/json` |
| Body | `{ "question": "<triggerText()>", "top": 1 }` |

## Response Handling

The HTTP response body contains:

```json
{
  "answers": [{
    "answer": "The best route is...",
    "confidenceScore": 0.87
  }]
}
```

Parse the JSON response in Power Automate using `body('HTTP')?['answers'][0]['answer']` and return to Power Apps.

## Related

- [[power-apps-faq-app]]
- [[azure-question-answering-knowledge-base]]

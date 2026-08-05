---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [power-apps, power-automate, azure-qa, integration, pipeline]
---

# Power Apps + Power Automate + Q&A Integration Pattern

Three-component pipeline: Power Apps collects the question → Power Automate calls Azure Q&A → Power Apps displays the answer.

## Architecture

```
User types question
       ↓
Power Apps (TextInput) → User clicks Ask Button
       ↓
Power Automate (cloud flow, triggered by Power Apps)
       ↓
HTTP POST to Azure Q&A prediction endpoint
       ↓
Azure Q&A returns answer JSON
       ↓
Power Automate parses answer
       ↓
Returns answer to Power Apps
       ↓
Power Apps (Label) displays answer
```

## Key Points

- Power Apps cannot call REST APIs directly — requires Power Automate as the HTTP bridge
- Power Automate is the integration layer — it holds the API key securely, not Power Apps
- The flow is stateless — each question triggers a new HTTP call
- Latency: typically 1–3 seconds end-to-end depending on Q&A knowledge base size

## Security Notes

- Store the Q&A subscription key in Power Automate's secure parameters, not in plain text
- Consider using Azure Key Vault connector for enterprise key management
- The Q&A knowledge base URL should be treated as a secret (it reveals your project name)

## Related

- [[power-apps-faq-app]]
- [[power-automate-http-request-qa-endpoint]]
- [[azure-question-answering-knowledge-base]]

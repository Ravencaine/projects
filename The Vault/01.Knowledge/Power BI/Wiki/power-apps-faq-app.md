---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [power-apps, canvas-app, faq, text-input, button, label, question-answering]
---

# Power Apps FAQ App — Canvas App with Q&A Integration

A simple Power Apps canvas app with a text input field, submit button, and label that displays answers from the Azure Q&A endpoint.

## Prerequisites

- Azure Q&A knowledge base (deployed)
- Power Apps license
- Power Automate (for HTTP request connector)

## Steps

### 1. Create Canvas App

Power Apps → Create → Canvas App → Blank app → Phone or Tablet layout

### 2. Add Controls

- **TextInput** control: named `QuestionInput` — user types question here
- **Button** control: named `AskButton` — triggers the flow
- **Label** control: named `AnswerLabel` — displays the answer

### 3. Configure Button OnSelect

```powerapps
Set(QuestionText, QuestionInput.Text);
QAFlow.Run(QuestionText)
```

### 4. Configure Flow (Power Automate)

Create a cloud flow triggered by Power Apps, then add an HTTP action:

- **Method**: POST
- **URI**: Q&A prediction endpoint URL
- **Headers**: `Ocp-Apim-Subscription-Key: <your-key>`, `Content-Type: application/json`
- **Body**:
```json
{ "question": "<triggerText()>" }
```

Return the answer from HTTP response body to Power Apps.

### 5. Configure AnswerLabel

```
AnswerLabel.Text = QAFlow.Run(QuestionInput.Text)
```

## Related

- [[azure-question-answering-knowledge-base]]
- [[power-automate-http-request-qa-endpoint]]
- [[power-apps-automate-qa-integration]]

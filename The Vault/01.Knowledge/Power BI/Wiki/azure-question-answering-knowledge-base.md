---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [azure-question-answering, language-studio, knowledge-base, faq, power-apps]
---

# Azure Question Answering — Create Knowledge Base

Build a FAQ knowledge base using Azure Language Studio's Question Answering feature, then wire it into a Power Apps canvas app.

## Prerequisites

- Azure subscription
- Azure Language resource (QnA Maker is now unified into Language Service)

## Steps

### 1. Create Language Resource

Azure Portal → Create Language resource → choose **Question Answering** → Create

### 2. Create a Knowledge Base

Azure Language Studio (language.azure.com) → Question Answering → Create new project:

1. **Add sources**: paste FAQ content, upload a document, or add URLs
2. **Review and finish**: let the service parse Q&A pairs
3. **Edit pairs**: review, merge, delete, or add new Q&A pairs manually

### 3. Test the Knowledge Base

Use the Test pane in Language Studio — type questions and verify answers.

### 4. Deploy the Knowledge Base

Deploy to a staging/production slot — this generates a **prediction endpoint**.

### 5. Get the Endpoint

In the Language resource: Keys and Endpoint → note:
- **Endpoint URL**
- **Key**

## Related

- [[power-apps-faq-app]]
- [[power-automate-http-request-qa-endpoint]]
- [[power-apps-automate-qa-integration]]

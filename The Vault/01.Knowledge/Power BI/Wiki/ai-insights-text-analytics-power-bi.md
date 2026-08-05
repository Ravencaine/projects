---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [ai-insights, text-analytics, power-bi, power-query, button]
---

# AI Insights Text Analytics — Power BI AI Insights Button

The AI Insights button in Power Query Editor provides a GUI for Cognitive Services text analytics without writing M code.

## Prerequisites

- Power BI Desktop (latest version)
- Azure Text Analytics resource (endpoint + key)
- Power BI Premium per-capacity or per-user license (AI Insights requires Premium in the service)

## Steps

1. Get Data → connect to your text data source
2. Open Power Query Editor
3. Select the column containing text
4. Click **AI Insights** button (in the toolbar, last icon)
5. Navigate: **Text Analytics** folder
6. Choose a function:
   - Detect Language
   - Extract Key Phrases
   - Score Sentiment
   - Translate Text
7. Enter parameters:
   - Column to analyse
   - Text Analytics resource endpoint and key
8. Click **Invoke**
9. Power Query creates a custom column with the result
10. Expand the result column as needed

## Notes

- AI Insights is a GUI wrapper around Power Query custom functions — it produces the same M code under the hood
- Requires **Premium license** in Power BI Service to refresh in the cloud
- Works locally in Power BI Desktop without Premium

## Related

- [[power-query-custom-function-text-analytics]]
- [[azure-cognitive-services-overview]]

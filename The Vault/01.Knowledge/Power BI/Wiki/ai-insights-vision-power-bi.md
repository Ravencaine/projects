---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [ai-insights, vision, power-bi, computer-vision, custom-vision, image-url]
---

# AI Insights Vision — Power BI AI Insights Button

The AI Insights button for Vision in Power Query Editor provides a GUI for Computer Vision and Custom Vision image analysis.

## Prerequisites

- Azure Computer Vision or Custom Vision resource
- Images accessible via URL (Azure Blob Storage with SAS or publicly accessible URLs)
- Power BI Desktop (local); Premium capacity for cloud refresh

## Steps

1. Get Data → connect to table containing image URLs
2. Open Power Query Editor
3. Select the column containing image URLs
4. Click **AI Insights** → **Vision** folder
5. Choose a function:
   - **Tag Image** (Computer Vision): returns tags describing image content
   - **Describe Image** (Computer Vision): returns a caption
   - **Classify Image** (Custom Vision): returns your custom categories
6. Enter:
   - **Image URL column** (or full URL text)
   - **Subscription key** and **Endpoint** for the relevant Cognitive Services resource
7. Click **Invoke**
8. Power Query creates a custom column with the result
9. Expand or parse the result as needed

## Notes

- Works the same as Text Analytics AI Insights — it generates the M code under the hood
- Requires images to be accessible via URL — local files need to be uploaded to Blob Storage first

## Related

- [[ai-insights-text-analytics-power-bi]]
- [[azure-computer-vision-image-description]]
- [[anonymous-image-access-power-bi]]

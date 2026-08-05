---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [anonymous-image-access, azure-blob-storage, sas, url, power-bi]
---

# Anonymous Image Access for Power BI — Azure Blob SAS URL

Images hosted in private Azure Blob Storage require SAS (Shared Access Signature) tokens for anonymous Power BI access. Power BI cannot access private blobs directly.

## Purpose

Azure Cognitive Services and Custom Vision require image URLs. If images are stored in private Blob Storage, the URL alone is not enough — a SAS token grants time-limited anonymous read access.

## How It Works

A SAS token is appended to a Blob Storage URL, giving read access for a limited time without authentication:

```
https://<account>.blob.core.windows.net/<container>/<blob>?sv=2021-06-08&ss=b&srt=co&sp=r&se=2025-01-01T00:00:00Z&st=2024-01-01T00:00:00Z&spr=https&sig=<signature>
```

## Steps

1. Azure Portal → Storage Account → Containers
2. Select the container with images
3. Access Control (IAM) → add Public read (blob only) OR generate a SAS URL
4. To generate SAS URL:
   - Select the blob → Generate SAS
   - Permissions: Read
   - Expiry: set appropriate date
   - Copy the full URL with SAS token
5. Use the SAS URL in Power Query custom functions for Computer Vision / Custom Vision calls

## Related

- [[azure-blob-storage-sas-image-urls]]
- [[ai-insights-vision-power-bi]]
- [[improving-custom-vision-prediction-feedback]]

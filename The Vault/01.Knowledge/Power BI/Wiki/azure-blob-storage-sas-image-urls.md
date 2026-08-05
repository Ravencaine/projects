---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [azure-blob-storage, sas-token, image-url, power-bi, power-query]
---

# Azure Blob Storage — Generate SAS URL for Images

Generate a Shared Access Signature (SAS) token for Azure Blob Storage so Power BI can access images via URL for Computer Vision / Custom Vision analysis.

## Prerequisites

- Azure Storage Account
- A container with uploaded images
- Owner, Storage Account Contributor, or Storage Blob Data Owner role

## Steps

### Option 1: Generate SAS for a Single Blob

1. Azure Portal → Storage Account → Containers
2. Navigate to the container
3. Click the specific blob (image file)
4. Generate SAS → configure:
   - **Permissions**: Read
   - **Expiry**: set date (e.g., 1 year)
   - **Protocol**: HTTPS only
5. Click Generate SAS token and URL
6. Copy the **Blob SAS URL**: this is the URL to use in Power Query

### Option 2: Generate SAS for an Entire Container

1. Azure Portal → Storage Account → Containers
2. Select the container
3. Settings → Shared Access Signature
4. Allowed services: Blob
5. Allowed resource types: Object
6. Permissions: Read
7. Expiry: set date
8. Copy the container SAS URL + append the blob name

## Format

```
https://<account>.blob.core.windows.net/<container>/<blob-name>?sv=2021-06-08&ss=b&srt=co&sp=r&se=<expiry>&st=<start>&spr=https&sig=<signature>
```

## Related

- [[anonymous-image-access-power-bi]]
- [[ai-insights-vision-power-bi]]

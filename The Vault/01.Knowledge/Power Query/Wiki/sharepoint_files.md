---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["sharepoint", "m-function"]
---


# SharePoint.Files

Returns a table containing a row for each document found at the specified SharePoint site, url, and subfolders. Each row contains properties of the folder or file and a link to its content. options may be specified to control the following options: ApiVersion: A number (14 or 15) or the text "Auto" that specifies the SharePoint API version to use for this site. When not specified, API version 14 is used. When Auto is specified, the server version will be automatically discovered if possible, otherwise version defaults to 14. Non-English SharePoint sites require at least version 15. --- PAGE 396 ---

## Signature

```m
SharePoint.Files(url as text, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| url | text | |
| optional options | nullable record | |

## Returns

table


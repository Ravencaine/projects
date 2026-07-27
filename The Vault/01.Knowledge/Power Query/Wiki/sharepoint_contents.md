---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["sharepoint", "m-function"]
---


# SharePoint.Contents

Returns a table containing a row for each folder and document found at the specified SharePoint site, url. Each row contains properties of the folder or file and a link to its content. options may be specified to control the following options: ApiVersion: A number (14 or 15) or the text "Auto" that specifies the SharePoint API version to use for this site. When not specified, API version 14 is used. When Auto is specified, the server version will be automatically discovered if possible, otherwise version defaults to 14. Non-English SharePoint sites require at least version 15. Implementation: Optional. Specifies which version of the SharePoint connector to use. Accepted values are "2.0" or null. If the value is "2.0", the 2.0 implementation of the SharePoint connector is used. If the value is null, the original implementation of the SharePoint connector is used. Last updated on 04/03/2026 --- PAGE 395 ---

## Signature

```m
SharePoint.Contents(url as text, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| url | text | |
| optional options | nullable record | |

## Returns

table


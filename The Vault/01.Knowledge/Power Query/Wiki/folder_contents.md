---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["folder", "m-function"]
---


# Folder.Contents

Returns a table containing a row for each folder and file found in the folder path. Each row contains properties of the folder or file and a link to its content. The options parameter is currently intended for internal use only. --- PAGE 357 ---

## Signature

```m
Folder.Contents(path as text, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| path | text | |
| optional options | nullable record | |

## Returns

table


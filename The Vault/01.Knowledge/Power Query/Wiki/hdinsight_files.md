---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["hdinsight", "m-function"]
---


# HdInsight.Files

Returns a table containing a row for each blob file found at the container URL, account, from an Azure storage vault. Each row contains properties of the file and a link to its content. --- PAGE 364 ---

## Signature

```m
HdInsight.Files(account as text, containerName as text) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| account | text | |
| containerName | text | |

## Returns

table


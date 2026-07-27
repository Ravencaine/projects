---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["azurestorage", "m-function"]
---


# AzureStorage.Tables

Returns a navigational table containing a row for each table found at the account URL, account, from an Azure storage vault. Each row contains a link to the azure table. An optional record parameter, options, may be provided to specify additional properties. The record can contain the following fields: Timeout: A duration that controls how long to wait before abandoning the request to the server. The default value is source-specific. --- PAGE 325 ---

## Signature

```m
AzureStorage.Tables(account as text, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| account | text | |
| optional options | nullable record | |

## Returns

table


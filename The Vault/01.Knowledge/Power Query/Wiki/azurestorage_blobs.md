---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["azurestorage", "m-function"]
---


# AzureStorage.Blobs

Returns a navigational table containing a row for each container found at the account URL, account, from an Azure storage vault. Each row contains a link to the container blobs. options may be specified to control the following options: BlockSize: The number of bytes to read before waiting on the data consumer. The default value is 4 MB. RequestSize: The number of bytes to try to read in a single HTTP request to the server. The default value is 4 MB. ConcurrentRequests: The ConcurrentRequests option supports faster download of data by specifying the number of requests to be made in parallel, at the cost of memory utilization. The memory required is (ConcurrentRequest * RequestSize). The default value is 16. --- PAGE 322 ---

## Signature

```m
AzureStorage.Blobs(account as text, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| account | text | |
| optional options | nullable record | |

## Returns

table


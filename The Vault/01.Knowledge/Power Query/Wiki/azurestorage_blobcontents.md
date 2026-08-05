---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["azurestorage", "m-function"]
---


# AzureStorage.BlobContents

Returns the content of the blob at the URL, url, from an Azure storage vault. options may be specified to control the following options: BlockSize: The number of bytes to read before waiting on the data consumer. The default value is 4 MB. RequestSize: The number of bytes to try to read in a single HTTP request to the server. The default value is 4 MB. ConcurrentRequests: The ConcurrentRequests option supports faster download of data by specifying the number of requests to be made in parallel, at the cost of memory utilization. The memory required is (ConcurrentRequest * RequestSize). The default value is 16. --- PAGE 321 ---

## Signature

```m
AzureStorage.BlobContents(url as text, optional options as nullable record) as
binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| url | text | |
| optional options | nullable record | |

## Returns

binary


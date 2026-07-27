---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["salesforce", "m-function"]
---


# Salesforce.Reports

Returns the reports on the Salesforce account provided in the credentials. The account will be connected through the provided environment loginUrl. If no environment is provided then the account will connect to production (https://login.salesforce.com ). An optional record parameter, options, may be provided to specify additional properties. The record can contain the following fields: ApiVersion: The Salesforce API version to use for this query. When not specified, API version 29.0 is used. Timeout: A duration that controls how long to wait before abandoning the request to the server. The default value is source-specific. --- PAGE 392 ---

## Signature

```m
Salesforce.Reports(optional loginUrl as nullable text, optional options as
nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| optional loginUrl | nullable text | |
| optional options | nullable record | |

## Returns

table


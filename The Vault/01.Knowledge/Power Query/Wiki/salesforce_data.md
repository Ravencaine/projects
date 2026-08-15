---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [salesforce, m-function]
---


# Salesforce.Data

Returns the objects on the Salesforce account provided in the credentials. The account will be connected through the provided environment loginUrl. If no environment is provided then the account will connect to production (https://login.salesforce.com ). An optional record parameter, options, may be provided to specify additional properties. The record can contain the following fields: CreateNavigationProperties: A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false). ApiVersion: The Salesforce API version to use for this query. When not specified, API version 29.0 is used. Timeout: A duration that controls how long to wait before abandoning the request to the server. The default value is source-specific. --- PAGE 391 ---

## Signature

```m
Salesforce.Data(optional loginUrl as any, optional options as nullable record) as
table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| optional loginUrl | any | |
| optional options | nullable record | |

## Returns

table


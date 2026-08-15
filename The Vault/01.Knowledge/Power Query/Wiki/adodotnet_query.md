---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [adodotnet, m-function]
---


# AdoDotNet.Query

Returns the result of running query with the connection string connectionString using the ADO.NET provider providerName. connectionString can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, options, may be provided to specify additional properties. The record can contain the following fields: CommandTimeout: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes. SqlCompatibleWindowsAuth: A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true. --- PAGE 318 ---

## Signature

```m
AdoDotNet.Query(
providerName as text,
connectionString as any,
query as text,
optional options as nullable record
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| providerName | text | |
| connectionString | any | |
| query | text | |
| optional options | nullable record | |

## Returns

table


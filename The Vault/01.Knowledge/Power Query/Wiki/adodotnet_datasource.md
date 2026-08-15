---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [adodotnet, m-function]
---


# AdoDotNet.DataSource

Returns the schema collection for the ADO.NET data source with provider name providerName and connection string connectionString. connectionString can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, options, may be provided to specify additional properties. The record can contain the following fields: CommandTimeout: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes. SqlCompatibleWindowsAuth: A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true. TypeMap --- PAGE 317 ---

## Signature

```m
AdoDotNet.DataSource(
providerName as text,
connectionString as any,
optional options as nullable record
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| providerName | text | |
| connectionString | any | |
| optional options | nullable record | |

## Returns

table


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [oledb, m-function]
---


# OleDb.Query

Returns the result of running query with the connection string connectionString using OLE DB. connectionString can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, options, may be provided to specify additional properties. The record can contain the following fields: ConnectionTimeout: A duration that controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent. CommandTimeout: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes. SqlCompatibleWindowsAuth: A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true. --- PAGE 385 ---

## Signature

```m
OleDb.Query(
connectionString as any,
query as text,
optional options as nullable record
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| connectionString | any | |
| query | text | |
| optional options | nullable record | |

## Returns

table


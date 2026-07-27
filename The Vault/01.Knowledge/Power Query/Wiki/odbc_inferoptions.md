---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["odbc", "m-function"]
---


# Odbc.InferOptions

Returns the result of trying to infer SQL capbabilities with the connection string connectionString using ODBC. connectionString can be text or a record of property value pairs. Property values can either be text or number. Example Return the inferred SQL capabilities for a connection string. Usage Power Query M Odbc.InferOptions("dsn=your_dsn") Output record Last updated on 04/02/2026 --- PAGE 381 ---

## Signature

```m
Odbc.InferOptions(connectionString as any) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| connectionString | any | |

## Returns

record


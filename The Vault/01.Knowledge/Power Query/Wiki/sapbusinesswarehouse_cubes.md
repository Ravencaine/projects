---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["sapbusinesswarehouse", "m-function"]
---


# SapBusinessWarehouse.Cubes

Returns a table of InfoCubes and queries grouped by InfoArea from an SAP Business Warehouse instance at server server with system number systemNumberOrSystemId and Client ID clientId. An optional record parameter, optionsOrLogonGroup, may be specified to control the following options: Last updated on 04/03/2026 --- PAGE 393 ---

## Signature

```m
SapBusinessWarehouse.Cubes(
server as text,
systemNumberOrSystemId as text,
clientId as text,
optional optionsOrLogonGroup as any,
optional options as nullable record
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| server | text | |
| systemNumberOrSystemId | text | |
| clientId | text | |
| optional optionsOrLogonGroup | any | |
| optional options | nullable record | |

## Returns

table


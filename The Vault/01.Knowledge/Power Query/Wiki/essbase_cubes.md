---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["essbase", "m-function"]
---


# Essbase.Cubes

Returns a table of cubes grouped by Essbase server from an Essbase instance at APS server url. An optional record parameter, options, may be specified to control the following options: CommandTimeout: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes. --- PAGE 350 ---

## Signature

```m
Essbase.Cubes(url as text, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| url | text | |
| optional options | nullable record | |

## Returns

table


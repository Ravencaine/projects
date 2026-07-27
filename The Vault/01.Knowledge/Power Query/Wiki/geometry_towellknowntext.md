---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["geometry", "m-function"]
---


# Geometry.ToWellKnownText

Translates a structured geometric point value into its Well-Known Text (WKT) representation as defined by the Open Geospatial Consortium (OGC), also the serialization format used by many databases including SQL Server. --- PAGE 885 ---

## Signature

```m
Geometry.ToWellKnownText(input as nullable record, optional omitSRID as nullable
logical) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | nullable record | |
| optional omitSRID | nullable logical | |

## Returns

nullable text


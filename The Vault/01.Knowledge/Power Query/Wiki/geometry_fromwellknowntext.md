---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [geometry, m-function]
---


# Geometry.FromWellKnownText

Translates text representing a geometric value in Well-Known Text (WKT) format into a structured record. WKT is a standard format defined by the Open Geospatial Consortium (OGC) and is the typical serialization format used by databases including SQL Server. --- PAGE 884 ---

## Signature

```m
Geometry.FromWellKnownText(input as nullable text) as nullable record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | nullable text | |

## Returns

nullable record


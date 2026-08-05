---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["geography", "m-function"]
---


# Geography.FromWellKnownText

Translates text representing a geographic value in Well-Known Text (WKT) format into a structured record. WKT is a standard format defined by the Open Geospatial Consortium (OGC) and is the typical serialization format used by databases including SQL Server. --- PAGE 881 ---

## Signature

```m
Geography.FromWellKnownText(input as nullable text) as nullable record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | nullable text | |

## Returns

nullable record


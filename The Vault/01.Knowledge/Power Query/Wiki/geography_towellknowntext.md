---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["geography", "m-function"]
---


# Geography.ToWellKnownText

Translates a structured geographic point value into its Well-Known Text (WKT) representation as defined by the Open Geospatial Consortium (OGC), also the serialization format used by many databases including SQL Server. --- PAGE 882 ---

## Signature

```m
Geography.ToWellKnownText(input as nullable record, optional omitSRID as nullable
logical) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | nullable record | |
| optional omitSRID | nullable logical | |

## Returns

nullable text


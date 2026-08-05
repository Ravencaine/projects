---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["json", "m-function"]
---


# Json.FromValue

Produces a JSON representation of a given value value with a text encoding specified by encoding. If encoding is omitted, UTF8 is used. Values are represented as follows: Null, text and logical values are represented as the corresponding JSON types Numbers are represented as numbers in JSON, except that #infinity, -#infinity and #nan are converted to null Lists are represented as JSON arrays Records are represented as JSON objects Tables are represented as an array of objects Dates, times, datetimes, datetimezones, and durations are represented as ISO-8601 text Binary values are represented as base-64 encoded text Types and functions produce an error Example Convert a complex value to JSON. Usage Power Query M Text.FromBinary(Json.FromValue([A = {1, true, "3"}, B = #date(2012, 3, 25)])) Output "{""A"":[1,true,""3""],""B"":""2012-03-25""}" Last updated on 03/24/2026 --- PAGE 374 ---

## Signature

```m
Json.FromValue(value as any, optional encoding as nullable number) as binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional encoding | nullable number | |

## Returns

binary


---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["duration", "m-function"]
---


# Duration.ToText

Returns a textual representation in the form "day.hour:mins:sec" of the given duration value, duration. duration: A duration from which the textual representation is calculated. format: [Optional] Deprecated, will raise an error if not null. Example Convert #duration(2, 5, 55, 20) into a text value. Usage Power Query M Duration.ToText(#duration(2, 5, 55, 20)) Output "2.05:55:20" Last updated on 03/24/2026 --- PAGE 632 --- #duration 09/16/2025 Syntax #duration( days as number, hours as number, minutes as number, seconds as number ) as duration About Creates a duration value from numbers representing days, hours, minutes, and (fractional) seconds. --- PAGE 633 --- Error handling functions Article • 07/15/2024 These functions can be used to trace or construct errors. ﾉ Expand table Name Description Diagnostics.ActivityId Returns an opaque identifier for the currently-running evaluation. Diagnostics.CorrelationId Returns an opaque identifier to correlate incoming requests with outgoing ones. Diagnostics.Trace Writes a trace message, if tracing is enabled, and returns value. Error.Record Returns an error record from the provided text values for reason, message, detail, and error code. Feedback Was this page helpful?  Yes  No Provide product feedback | Ask the community --- PAGE 634 ---

## Signature

```m
Duration.ToText(duration as nullable duration, optional format as nullable text) as
nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| duration | nullable duration | |
| optional format | nullable text | |

## Returns

nullable text


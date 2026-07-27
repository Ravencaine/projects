---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["diagnostics", "m-function"]
---


# Diagnostics.Trace

Writes a trace message, if tracing is enabled, and returns value. An optional parameter delayed specifies whether to delay the evaluation of value until the message is traced. traceLevel can take one of the following values: TraceLevel.Critical TraceLevel.Error TraceLevel.Warning TraceLevel.Information TraceLevel.Verbose Example Trace the message before invoking Text.From function and return the result. Usage Power Query M Diagnostics.Trace(TraceLevel.Information, "TextValueFromNumber", () => Text.From(123), true) Output "123" Last updated on 03/24/2026 --- PAGE 637 ---

## Signature

```m
Diagnostics.Trace(
traceLevel as number,
message as anynonnull,
value as any,
optional delayed as nullable logical
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| traceLevel | number | |
| message | anynonnull | |
| value | any | |
| optional delayed | nullable logical | |

## Returns

any


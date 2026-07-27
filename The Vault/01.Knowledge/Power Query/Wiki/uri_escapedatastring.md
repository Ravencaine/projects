---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["uri", "m-function"]
---


# Uri.EscapeDataString

Encodes special characters in the input data according to the rules of RFC 3986. Example Encode the special characters in "+money$". Usage Power Query M Uri.EscapeDataString("+money$") Output "%2Bmoney%24" Last updated on 03/24/2026 --- PAGE 1292 ---

## Signature

```m
Uri.EscapeDataString(data as text) as text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| data | text | |

## Returns

text


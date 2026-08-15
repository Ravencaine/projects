---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [uri, m-function]
---


# Uri.BuildQueryString

Assemble the record query into a URI query string, escaping characters as necessary. Example Encode a query string which contains some special characters. Usage Power Query M Uri.BuildQueryString([a = "1", b = "+$"]) Output "a=1&b=%2B%24" Last updated on 03/24/2026 --- PAGE 1290 ---

## Signature

```m
Uri.BuildQueryString(query as record) as text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| query | record | |

## Returns

text


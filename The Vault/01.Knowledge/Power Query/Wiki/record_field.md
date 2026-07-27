---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.Field

Returns the value of the specified field in the record. If the field is not found, an error is raised. Example Find the value of field "CustomerID" in the record. Usage Power Query M Record.Field([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID") Output 1 Last updated on 03/24/2026 --- PAGE 889 ---

## Signature

```m
Record.Field(record as record, field as text) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |
| field | text | |

## Returns

any


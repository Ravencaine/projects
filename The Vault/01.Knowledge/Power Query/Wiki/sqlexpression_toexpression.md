---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["sqlexpression", "m-function"]
---


# SqlExpression.ToExpression

Converts the provided sql query to M code, with the available identifiers defined by environment. This function is intended for internal use only. --- PAGE 1306 ---

## Signature

```m
SqlExpression.ToExpression(sql as text, environment as record) as text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| sql | text | |
| environment | record | |

## Returns

text


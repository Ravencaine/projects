---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["activedirectory", "m-function"]
---


# ActiveDirectory.Domains

Returns a list of Active Directory domains in the same forest as the specified domain or of the current machine's domain if none is specified. --- PAGE 315 ---

## Signature

```m
ActiveDirectory.Domains(optional forestRootDomainName as nullable text) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| optional forestRootDomainName | nullable text | |

## Returns

table


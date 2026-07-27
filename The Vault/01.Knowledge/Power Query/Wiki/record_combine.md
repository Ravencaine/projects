---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.Combine

Combines the records in the given records. If the records contains non-record values, an error is returned.

## Signature

```m
Record.Combine(records as list) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| records | list | |

## Returns

record

### Example 1

Create a combined record from the records.

```m
Record.Combine({
[CustomerID = 1, Name = "Bob"],
[Phone = "123-4567"]
})
```

// Output
```
[CustomerID = 1, Name = "Bob", Phone = "123-4567"]
```


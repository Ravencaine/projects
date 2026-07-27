---
created: 2026-07-27
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "errors"]
---


# Error Handling with Try

Errors occur when operators or functions encounter error conditions. The `try` expression converts errors into values, allowing graceful handling without crashing the query.

## Key Points

- `try` returns a record: `{[HasError] = true/false, [Value] = ..., [Error] = ...}`
- When no error occurs: `HasError = false`, `Value` contains the result
- When an error occurs: `HasError = true`, `Error[Message]` contains the error message
- Errors can be raised explicitly with the `error` keyword
- Errors propagate up the call stack until handled by `try`

## Examples

```m
let
    UnitPrice = if Units = 0 then error "No Units"
                else Revenue / Units,
    Result = try Number.ToText(UnitPrice),
    Output = if Result[HasError]
             then "Error: " & Result[Error][Message]
             else "Unit Price: " & Text.From(Result[Value])
in
    Output
```

## Related

- [[m_if_expressions]] — often combined with try for conditional logic
- [[error_record]] — Error.Record for creating custom errors

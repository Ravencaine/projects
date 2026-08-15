---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [error, m-function]
---


# Error.Record

Returns an error record from the provided text values for reason, mesage, detail, and error code. reason: The high-level cause of the error. message: (Optional) A description of the error. detail: (Optional) Additional detailed information about the error. parameters: (Optional) A list of values that provide additional context for the error, typically used for diagnostics or programmatic handling. errorCode: (Optional) An identifier for the error.

## Signature

```m
Error.Record(
reason as text,
optional message as nullable text,
optional detail as any,
optional parameters as nullable list,
optional errorCode as nullable text
) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| reason | text | |
| optional message | nullable text | |
| optional detail | any | |
| optional parameters | nullable list | |
| optional errorCode | nullable text | |

## Returns

record

### Example 1

Handle a divide by zero error.

```m
let
input = 100,
divisor = 0,
result = try if divisor = 0 then
error Error.Record(
"DivideByZero",
"You attempted to divide by zero."
)
else
input / divisor
in
result
```

// Output
```
[
HasError = true,
Error =
[
Reason = "DivideByZero",
Message = "You attempted to divide by zero.",
Detail = null,
Message.Format = null,
Message.Parameters = null,
ErrorCode = null
]
]
```

### Example 2

Handle an entry with a non-existent customer ID error. If no error occurs, indicate a successful entry.

```m
let
CustomerId = 12345,
result = try if CustomerId > 9999 then
error Error.Record(
"CustomerNotFound",
Text.Format("Customer ID #{0} wasn't found.", {CustomerId}),
"Customer doesn't exist.",
{
Text.Format("Invalid ID = #{0}", {CustomerId}),
"Valid IDs: https://api.contoso.com/customers"
},
"ERR404"
)
else CustomerId
in
result
```

// Output
```
[
HasError = true,
Error = [
Reason = "CustomerNotFound",
Message = "Customer ID 12345 wasn't found.",
Detail = "Customer doesn't exist.",
Message.Format = "Customer ID 12345 wasn't found.",
Message.Parameters = {
"Invalid ID = 12345",
"Valid IDs: https://api.contoso.com/customers"
},
ErrorCode = "ERR404"
]
]
Last updated on 12/18/2025
Expression functions
08/11/2025
These functions allow the construction and evaluation of M code.
ﾉ Expand table
Name Description
Expression.Constant Returns the M source code representation of a constant value.
Expression.Evaluate Returns the result of evaluating an M expression.
Expression.Identifier Returns the M source code representation of an identifier.
```


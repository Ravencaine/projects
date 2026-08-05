---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["expression", "m-function"]
---


# Expression.Identifier

Returns the M source code representation of an identifier name.

## Signature

```m
Expression.Identifier(name as text) as text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| name | text | |

## Returns

text

### Example 1

Get the M source code representation of an identifier.

```m
Expression.Identifier("MyIdentifier")
```

// Output
```
"MyIdentifier"
```

### Example 2

Get the M source code representation of an identifier that contains a space.

```m
Expression.Identifier("My Identifier")
```

// Output
```
"#""My Identifier"""
Function values
Article • 10/25/2023
These functions create and invoke other M functions.
Name Description
Function.From Takes a unary function function and creates a new function
with the type functionType that constructs a list out of its
arguments and passes it to function.
Function.Invoke Invokes the given function using the specified and returns the
result.
Function.InvokeAfter Returns the result of invoking function after duration delay
has passed.
Function.InvokeWithErrorContext This function is intended for internal use only.
Function.IsDataSource Returns whether or not function is considered a data source.
Function.ScalarVector Returns a scalar function of type scalarFunctionType that
invokes vectorFunction with a single row of arguments and
returns its single output.
Feedback
Was this page helpful?  Yes  No
```


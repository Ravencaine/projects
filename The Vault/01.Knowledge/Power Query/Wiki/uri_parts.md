---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [uri, m-function]
---


# Uri.Parts

Returns the parts of the input absoluteUri as a record, containing values such as Scheme, Host, Port, Path, Query, Fragment, UserName and Password.

## Signature

```m
Uri.Parts(absoluteUri as text) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| absoluteUri | text | |

## Returns

record

### Example 1

Find the parts of the absolute URI "www.adventure-works.com".

```m
Uri.Parts("www.adventure-works.com")
```

// Output
```
[
Scheme = "http",
Host = "www.adventure-works.com",
Port = 80,
Path = "/",
Query = [],
Fragment = "",
UserName = "",
Password = ""
]
```

### Example 2

Decode a percent-encoded string.

```m
let
UriUnescapeDataString = (data as text) as text => Uri.Parts("http://contoso?
a=" & data)[Query][a]
in
UriUnescapeDataString("%2Bmoney%24")
```

// Output
```
"+money$"
Value functions
09/04/2025
These functions evaluate and perform operations on values.
ﾉ Expand table
Name Description
Value.Alternates Expresses alternate query plans.
Value.Compare Returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater
than the second.
Value.Equals Returns whether two values are equal.
Value.Expression Returns an abstract syntax tree (AST) that represents the value's expression.
Value.VersionIdentity Returns the version identity of a value.
Value.Versions Returns a navigation table containing the available versions of a value.
Value.NativeQuery Evaluates a query against a target.
Value.NullableEquals Returns a logical value or null based on two values.
Value.Optimize If value represents a query that can be optimized, returns the optimized query.
Otherwise returns value.
Value.Type Returns the type of the given value.
Arithmetic operations
ﾉ Expand table
Name Description
Value.Add Returns the sum of the two values.
Value.Divide Returns the result of dividing the first value by the second.
Value.Multiply Returns the product of the two values.
Value.Subtract Returns the difference of the two values.
Parameter types
ﾉ Expand table
Name Description
Value.As Returns the value if it is compatible with the specified type.
Value.Is Determines whether a value is compatible with the specified type.
Value.ReplaceType Replaces the value's type.
ﾉ Expand table
Implementation Description
Action.WithErrorContext This function is intended for internal use only.
DirectQueryCapabilities.From This function is intended for internal use only.
Embedded.Value Accesses a value by name in an embedded mashup.
Excel.ShapeTable This function is intended for internal use only.
Module.Versions Returns a record of module versions for the current module and its
dependencies.
Progress.DataSourceProgress This function is intended for internal use only.
SqlExpression.SchemaFrom This function is intended for internal use only.
SqlExpression.ToExpression This function is intended for internal use only.
Value.Firewall This function is intended for internal use only.
Value.ViewError This function is intended for internal use only.
Value.ViewFunction This function is intended for internal use only.
Variable.Value Returns the value of the specified variable.
Variable.ValueOrDefault Returns the value of the specified variable or the default value if the
variable is not defined.
Metadata
ﾉ Expand table
Name Description
Value.Metadata Returns a record containing the input’s metadata.
Name Description
Value.RemoveMetadata Removes the metadata on the value and returns the original value.
Value.ReplaceMetadata Replaces the metadata on a value with the new metadata record provided and
returns the original value with the new metadata attached.
Lineage
ﾉ Expand table
Name Description
Graph.Nodes This function is intended for internal use only.
Value.Lineage This function is intended for internal use only.
Value.Traits This function is intended for internal use only.
```


---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: [m-language, types]
---


# M Type System

M has a rich type system. Types themselves are values (`type` values). The language includes primitive types, structured types (list, record, table, function), nullable types, and custom types defined with the `type` keyword.

## Key Points

- **Primitive types**: number, logical, text, time, date, datetime, datetimezone, duration, binary, null, any
- **Structured types**: list, record, table, function
- **Nullable**: `nullable type` allows null values
- **Type values**: written as `type text`, `type number`, `type nullable number`
- Types are inferred or explicitly declared with `as`
- `Type.*` functions inspect and manipulate types at runtime

## Examples

```m
type text        // the type of all text values
type number      // the type of all numbers
type nullable number  // number or null
type [A = text, B = number]  // record type with fields A and B
```

## Related

- [[m_primitive_types]] — all primitive types
- [[type_functions]] — Type.Is, Type.ClosedRecord, etc.

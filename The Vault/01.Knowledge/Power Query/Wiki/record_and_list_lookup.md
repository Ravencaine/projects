---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: pattern
tags: [m-language, lookup]
---


# Record Field Lookup and List Item Access

M provides two primary access patterns: record field lookup with `[]` or `[[]]` and list item access with `{}` or `{}?`.

## Record Lookup

| Operator | Meaning | Returns |
|----------|---------|---------|
| `record[FieldName]` | Field by name | The field's value |
| `record[[fieldname]]` | Field by name | Record containing the field |

## List Item Access

| Operator | Meaning | Returns |
|----------|---------|---------|
| `list{0}` | Item at zero-based index 0 | First item |
| `list{-1}` | Last item | Last item |
| `list{n}?` | Safe item access | Item or null |

## Examples

```
// Record field lookup
[Name = "Alice", Age = 30][Name]    // "Alice"
[Name = "Alice", Age = 30][[age]]   // [Age = 30]

// List item access
{"a", "b", "c"}{0}      // "a"
{"a", "b", "c"}{-1}     // "c"
{"a", "b", "c"}{10}?    // null (out of range)
```

## Related

- [[m_operators]] — lookup operators
- [[record_field]] — Record.Field

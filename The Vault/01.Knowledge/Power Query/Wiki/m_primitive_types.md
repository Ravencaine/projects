---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: [m-language, types]
---


# M Primitive Types

M defines 14 primitive types. Each has a literal syntax and a set of defined operations.

## Key Points

| Type | Literal Example | Notes |
|------|----------------|-------|
| number | `3.14`, `-1` | IEEE 754 double-precision |
| logical | `true`, `false` | |
| text | `"hello"` | Unicode strings |
| time | `#time(12, 30, 0)` | |
| date | `#date(2025, 7, 27)` | |
| datetime | `#datetime(2025, 7, 27, 12, 0, 0)` | |
| datetimezone | `#datetimezone(2025, 7, 27, 12, 0, 0, -5, 0)` | |
| duration | `#duration(1, 2, 30, 0)` | days, hours, minutes, seconds |
| binary | `#binary({0x00, 0xFF})` | |
| null | `null` | absence of value |
| any | — | union of all types |
| type | `type text` | type values |
| function | `(x) => x + 1` | function values |
| table | — | no literal syntax |

## Related

- [[m_type_system]] — type system overview
- [[quoted_identifier_syntax]] — literal syntax

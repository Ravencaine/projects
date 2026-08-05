---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "fundamentals"]
---


# M Language Is Functional and Case-Sensitive

M is a functional, case-sensitive language similar to F#. Every expression evaluates to a single value. Functions are first-class values.

## Key Points

- M is **case-sensitive**: `Text.Proper` and `Text.proper` are different
- M is **functional**: queries are composed of expressions that evaluate to values
- M is **dynamically typed**: types are inferred at runtime
- M uses **let expressions** to build up complex expressions in smaller steps
- M is **mostly pure**: side effects are limited to data access and error handling

## Related

- [[m_evaluation_model]] — how M evaluates expressions
- [[m_functions_as_values]] — functions as first-class values

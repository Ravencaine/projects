---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: gotcha
tags: ["power-query", "power-bi", "text", "case"]
---


# Text Comparison Is Case-Sensitive in M; Power BI Normalizes on Load

M's text comparison operators are **always case-sensitive**. "Foo" and "foo" are never equal in M expressions. However, when data is loaded into Power BI Desktop's data model, text values are **normalized**: the data model treats "Foo", "foo", and "FOO" as the same value regardless of capitalization.

## Expected Behaviour

In Power Query M:
```
"Foo" = "foo"   // false — M is case-sensitive
"Foo" = "FOO"   // false — M is case-sensitive
```

## Actual Behaviour

When the same data is loaded into Power BI Desktop's column, the data model treats these as equal. A DAX query or relationship using "Foo" will match rows containing "foo" or "FOO".

## Why It Happens

M is a functional language specification where case sensitivity is a defined behaviour. Power BI Desktop's data model uses a different comparison model that normalizes case for storage and matching.

## How to Handle It

- Use `Comparer.OrdinalIgnoreCase` in Power Query for case-insensitive matching
- Be aware this only affects the Power Query layer — the data model still normalizes
- Use `Comparer.Ordinal` for explicit case-sensitive comparison

## Related

- [[comparer_equals]] — Comparer.Ordinal, Comparer.OrdinalIgnoreCase

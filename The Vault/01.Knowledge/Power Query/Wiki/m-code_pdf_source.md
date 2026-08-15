---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: source
tags: [power-query, m-language, microsoft, documentation]
---


# Power Query M Language Reference

Official Microsoft documentation for the Power Query M formula language, covering the complete language specification, tutorials, function references, and format string guides.

> **Type:** documentation
> **Author:** Microsoft
> **Published:** 2025
> **URL:** https://learn.microsoft.com/en-us/powerquery-m/
> **Routed to:** Power Query

## Summary

The Microsoft Power Query M Language Reference is the authoritative documentation for M — a functional, case-sensitive language used to define data mashup queries in Power Query, Power BI, Excel, and Analysis Services. The reference covers the language specification, value types, operators, the standard library of 700+ functions, format strings, and enumeration constants.

## Key Claims

- M is a **mostly pure, higher-order, dynamically typed functional language** similar to F#
- Every expression evaluates to a single value; functions are first-class values
- M uses **lazy evaluation** for lists, records, and let expressions; eager evaluation for primitives and operators
- The standard library contains **700+ functions** across 126 categories
- M supports rich literal syntax: numbers, text, dates, times, durations, binaries, lists, records, and tables
- The type system includes primitive types, structured types, nullable types, and custom types

## Notable Details

- Text comparison in M is **always case-sensitive**: "Foo" ≠ "foo" in expressions
- When data loads into Power BI's data model, case is **normalized** on the data model layer, creating a disconnect
- Lists and records use **lazy evaluation**: expressions inside them are not evaluated until accessed
- Operators have **operand-dependent meaning**: `+` does number addition, text concatenation, and date arithmetic depending on types
- `#table()` has no direct literal form — tables are always constructed via functions
- The `meta` operator attaches metadata records to any value without changing its value
- `try` expressions convert errors into values: `{[HasError] = true/false, [Value] = ..., [Error] = ...}`

## Extracted Notes

**Atomic notes (16):**
- [[m_language_is_functional_and_case_sensitive]] — `atomic` — M is functional and case-sensitive
- [[expressions_vs_values]] — `atomic` — expressions vs values distinction
- [[lazy_vs_eager_evaluation]] — `atomic` — lazy vs eager evaluation strategies
- [[m_standard_library]] — `atomic` — the M standard library
- [[m_let_expressions]] — `atomic` — let expression syntax and semantics
- [[m_if_expressions]] — `atomic` — if/then/else conditionals
- [[m_error_handling_with_try]] — `atomic` — error handling with try
- [[m_functions_as_values]] — `atomic` — functions as first-class values
- [[m_metadata]] — `atomic` — metadata with meta operator
- [[m_sections]] — `atomic` — sections as modularity mechanism
- [[m_lexical_structure]] — `atomic` — token/lexical grammar
- [[m_operators]] — `atomic` — operators overview
- [[m_type_system]] — `atomic` — M's type system
- [[m_primitive_types]] — `atomic` — all 14 primitive types
- [[m_evaluation_model]] — `atomic` — M's evaluation model
- [[culture_and_text_formatting]] — `atomic` — culture-aware text formatting

**Reference notes (7):**
- [[m_consolidated_grammar]] — `reference` — complete M grammar
- [[m_operator_behaviour]] — `reference` — operator behaviours by type
- [[standard_numeric_format_strings]] — `reference` — standard number format specifiers
- [[custom_numeric_format_strings]] — `reference` — custom number format patterns
- [[standard_date_and_time_format_strings]] — `reference` — standard date/time formats
- [[duration_support]] — `reference` — duration arithmetic and accessors
- [[m_function_reference_index]] — `reference` — 711 functions across 126 categories

**Gotcha notes (3):**
- [[pq_text_case_sensitive_vs_power_bi_normalization]] — `gotcha` — case-sensitive M vs normalizing Power BI model
- [[lazy_list_record_evaluation_gotcha]] — `gotcha` — lazy list/record evaluation
- [[m_operators_operand_dependent_meaning]] — `gotcha` — operators have context-dependent meaning

**Pattern notes (2):**
- [[m_query_structure_let_in]] — `pattern` — let…in query structure
- [[record_and_list_lookup]] — `pattern` — record/list access patterns

**Snippet notes (2):**
- [[table_literal_syntax]] — `snippet` — #table() literal syntax
- [[quoted_identifier_syntax]] — `snippet` — #"identifier with spaces" syntax

**Function notes (711):** All M library functions across 126 categories. Index: [[m_function_reference_index]].

## Metadata

| Field | Value |
|-------|-------|
| Source file | m-code.pdf |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~167,000 |
| Notes extracted | 741 (16 atomic + 7 reference + 3 gotcha + 2 pattern + 2 snippet + 1 source + 711 function) |

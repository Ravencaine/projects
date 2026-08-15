---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: reference
tags: [m-language, specification, grammar]
---


# M Language Specification — Consolidated Grammar

The M consolidated grammar defines the complete formal grammar of the Power Query M language, including all grammar rules for values, expressions, types, patterns, and programs.

## Quick Reference

```
program            ::= document
document           ::= section | document section
section            ::= section-heading section-body
section-heading    ::= [ shared ] identifier
section-body       ::= section-member... end-of-file
section-member     ::= section-library | let-expression | declaration
section-library    ::= identifier "=" expression
declaration        ::= identifier [ type-annotation ] "=" expression
let-expression     ::= "let" let-clause... "in" expression
let-clause         ::= identifier "=" expression
expression         ::= if-expression | let-expression | function-expression | ...
if-expression      ::= "if" expression "then" expression "else" expression
function-expression ::= parameter-list "=>" expression
parameter-list     ::= "(" [ identifier [ "as" type ] ... ] ")"
primary            ::= literal | identifier | "(" expression ")"
                    | primary "." identifier | primary "(" arguments ")"
                    | primary "[" field-name "]" | primary "{" expression "}"
                    | primary "???" expression | primary "meta" expression
```

## Key Grammar Points

- **Identifiers**: `[a-zA-Z_][a-zA-Z0-9_]*` or `#"..."` for quoted form
- **Comments**: `// ...` or `/* ... */`
- **Literals**: numbers, text, dates, times, durations, binaries
- **Keywords**: `let`, `in`, `if`, `then`, `else`, `error`, `try`, `otherwise`, `each`, `section`, `shared`, `type`, `as`, `nullable`, `optional`

## Related

- [[m_lexical_structure]] — token-level grammar
- [[m_evaluation_model]] — evaluation semantics

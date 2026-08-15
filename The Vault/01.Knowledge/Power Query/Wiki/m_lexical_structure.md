---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: [m-language, specification]
---


# M Lexical Structure

The lexical structure defines the valid textual representations in M: identifiers, keywords, literals, operators, comments, and escape sequences.

## Key Points

- **Identifiers**: alphanumeric + underscore, optionally quoted with `#"..."`
- **Keywords**: reserved words (let, in, if, then, else, error, try, otherwise, as, each, section, shared, type, nullable, optional)
- **Literals**: numbers, text in double quotes, dates/times/durations with `#` prefix
- **Comments**: `//` single-line, `/* */` delimited (do not nest)
- **Escape sequences**: `#(cr)`, `#(lf)`, `#(tab)`, `#(000D)` for Unicode codepoints

## Examples

```m
// Standard identifier
myVariable

// Quoted identifier (allows spaces, reserved words)
#"Variable with spaces"

// Escape sequences
"Line1#(lf)Line2"   // line feed between words
"Tab#(tab)separated" // tab between words
```

## Related

- [[m_consolidated_grammar]] — full grammar reference

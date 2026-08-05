---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "modularity"]
---


# Sections (Modularity)

Sections provide a modularity mechanism in M, allowing shared definitions to be grouped and named. Sections are not yet fully leveraged by Power Query's UI but are part of the M specification.

## Key Points

- A section is a collection of name/value pairs at the document level
- Sections use the keyword `section` followed by a name and body
- Section members are accessed via qualified names: `SectionName.MemberName`
- Sections enable library-like sharing across a document
- Power Query UI does not expose sections directly (as of 2025)

## Examples

```m
section MyLibrary
    Add = (x, y) => x + y;
    Multiply = (x, y) => x * y;
in
    MyLibrary.Add(3, 4)  // 7
```

## Related

- [[m_standard_library]] — library values in sections

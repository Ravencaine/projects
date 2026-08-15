---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, text, extraction, left, right, mid]
note_type: pattern

---

# Text Extraction Patterns in DAX

Using LEFT, RIGHT, MID, FIND, and SEARCH together to parse and extract text.

## Purpose

Real-world data often arrives in inconsistent formats. Combining text functions lets you extract meaningful values from messy strings.

## Extract Between Delimiters

```dax
-- Extract text between two characters (e.g., "User: John Doe" → "John Doe")
Extract Between :=
VAR __Start = FIND( ": ", [RawText], 1, BLANK() ) + 2
VAR __End = LEN( [RawText] )
RETURN
MID( [RawText], __Start, __End - __Start + 1 )
```

## Extract First and Last Words

```dax
First Name :=
VAR __Space = FIND( " ", [FullName], 1, BLANK() )
RETURN
LEFT( [FullName], __Space - 1 )

Last Name :=
VAR __Space = FIND( " ", [FullName], 1, BLANK() )
VAR __Len = LEN( [FullName] )
RETURN
MID( [FullName], __Space + 1, __Len - __Space )
```

## Reverse Extract (from Right)

```dax
-- Extract after last "/" in a file path
Filename :=
VAR __LastSlash = FIND( "/", SUBSTITUTE( [Path], "/", "|", LEN([Path]) - LEN(SUBSTITUTE([Path], "/", "")) ) )
RETURN
RIGHT( [Path], LEN( [Path] ) - __LastSlash )
```

## Notes

- Always use `FIND(..., BLANK())` to return BLANK() instead of an error when text is not found
- `SUBSTITUTE()` with a high replacement count lets you find the Nth occurrence of a character
- For complex parsing, consider doing it in Power Query instead — it is more robust for messy data

## Related

- [[FIND]]
- [[SEARCH]]
- [[left-right-mid]]
- [[replace-substitute]]
- [[no-calculate-dax-pattern]]

---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, text, count, occurrences, substring]
note_type: pattern

---

# Counting Occurrences in DAX

Counting how many times a character or substring appears in a text field.

## Pattern

```dax
Count Occurrences :=
VAR __Text = [RawText]
VAR __Search = [SearchChar]
VAR __Len = LEN( __Text )
VAR __LenNoChar = LEN( SUBSTITUTE( __Text, __Search, "" ) )
RETURN
__Len - __LenNoChar
```

## Count Words

```dax
Word Count :=
VAR __Text = SUBSTITUTE( [Text], " ", "" )
RETURN
LEN( [Text] ) - LEN( __Text ) + 1
```

## Notes

- Works by comparing string length before and after removing the target character
- For case-insensitive counting, wrap in LOWER()

## Related

- [[text-extraction-patterns-in-dax]]
- [[FIND]]

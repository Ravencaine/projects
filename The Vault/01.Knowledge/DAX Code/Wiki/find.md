---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "text", "find", "case-sensitive"]
note_type: function

---

# FIND — Case-sensitive Text Search

Returns the starting position of a substring within a text string. Case-sensitive.

## Signature

```dax
FIND( <FindText>, <WithinText>, [<StartPosition>], [<NotFoundValue>] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| FindText | Text | The text to search for. Case-sensitive. |
| WithinText | Text | The text to search within. |
| StartPosition | Number | Starting position (1-based). Optional. Default: 1. |
| NotFoundValue | Number | Value to return if not found. Optional. Default: error. |

## Returns

The 1-based position of the found text, or NotFoundValue if supplied.

## Examples

```dax
-- Find position of "Quick" in a sentence
Position := FIND( "Quick", [Sentence], 1, BLANK() )
-- Returns BLANK() if not found (safe form)

-- Find second occurrence
SecondPos := FIND( "a", [Text], FIND( "a", [Text] ) + 1, BLANK() )
```

## Notes

- **Case-sensitive:** "quick" ≠ "Quick". Use `SEARCH()` for case-insensitive matching.
- **Wildcards not supported:** use `SEARCH()` or `CONTAINSSTRING()` instead.
- Returns an error if the text is not found and NotFoundValue is not provided.
- Returns BLANK() if NotFoundValue is set to BLANK() — always use `FIND(..., BLANK())` for safe handling.

## Related

- [[SEARCH]] — case-insensitive version
- [[CONTAINSSTRING]] — substring detection with wildcards
- [[left-right-mid]] — extract text by position

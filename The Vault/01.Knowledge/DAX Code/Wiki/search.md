---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, text, search, case-insensitive]
note_type: function

---

# SEARCH — Case-insensitive Text Search

Returns the starting position of a substring within a text string. Case-insensitive.

## Signature

```dax
SEARCH( <FindText>, <WithinText>, [<StartPosition>], [<NotFoundValue>] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| FindText | Text | The text to search for. Case-insensitive match. |
| WithinText | Text | The text to search within. |
| StartPosition | Number | Starting position (1-based). Optional. |
| NotFoundValue | Number | Value to return if not found. Optional. |

## Returns

The 1-based position of the found text, or NotFoundValue.

## Examples

```dax
-- Case-insensitive find
Position := SEARCH( "quick", [Sentence], 1, BLANK() )
-- Returns 5 for "The quick brown fox..."

-- Wildcard support: use * to match any characters
StartsWithThe := SEARCH( "the*", [Sentence], 1, BLANK() )
```

## Notes

- **Case-insensitive:** "quick" = "QUICK" = "Quick"
- **Supports wildcards:** `*` matches any sequence; `?` matches any single character
- Use `FIND()` when case-sensitivity is required
- Always use `SEARCH(..., BLANK())` to return BLANK() instead of an error

## Related

- [[FIND]] — case-sensitive version
- [[CONTAINSSTRING]] — substring detection
- [[left-right-mid]] — extract by position

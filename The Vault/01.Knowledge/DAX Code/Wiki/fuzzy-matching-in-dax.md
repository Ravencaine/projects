---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "text", "fuzzy-match", "similarity", "approximate"]
note_type: pattern

---

# Fuzzy Matching in DAX

Finding approximate string matches when exact matching fails.

## Levenshtein Distance Approach

```dax
Levenshtein Distance :=
VAR __s = [String1]
VAR __t = [String2]
-- DAX has no native recursion; use a pre-computed lookup table
-- This is impractical for large datasets in DAX alone
RETURN
-- For production: build a fuzzy match table in Power Query
```

## Practical Fuzzy Match in Power BI

```dax
Similarity Score :=
VAR __s = LOWER( [Name1] )
VAR __t = LOWER( [Name2] )
VAR __Len1 = LEN( __s )
VAR __Len2 = LEN( __t )
VAR __Match =
    SUMX(
        GENERATESERIES( 1, MIN( __Len1, __Len2 ) ),
        IF( MID( __s, [Value], 1 ) = MID( __t, [Value], 1 ), 1, 0 )
    )
RETURN
DIVIDE( __Match, MAX( __Len1, __Len2 ) )
```

## Notes

- True fuzzy matching (Levenshtein distance) requires Power Query or an external tool
- DAX can approximate character-by-character similarity for short strings
- Use Power Query's FuzzyMerge for production fuzzy matching

## Related

- [[text-extraction-patterns-in-dax]]
- [[counting-occurrences-in-dax]]

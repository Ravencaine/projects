---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, fuzzy-matching, text, string-comparison]
---

# Fuzzy Matching — Levenshtein Distance

## Purpose

Fuzzy matching identifies strings that are **approximately, but not exactly, equal**: handling typos, abbreviations, alternate spellings, and formatting inconsistencies.
DAX has no native fuzzy functions (unlike Power Query's `Table.FuzzyGroup`),
so Deckler implements fuzzy matching entirely in DAX.

Three approaches are covered:

| Method | Algorithm | Strength |
|--------|-----------|----------|
| **Fuzzy** (custom) | Hybrid: prefix search + threshold scoring | Best accuracy |
| **Jaccard Similarity** | Character-level intersection ÷ union | Simpler, threshold-based |
| **Levenshtein Distance** | Count insertions, deletions, substitutions | Classic edit-distance metric |

## Formula — Full Custom Fuzzy Match

```dax
Fuzzy =
    VAR __MatchWord            = MAX( 'Clients'[Client Name] )
    VAR __CleanMatchThreshold  = 4
    VAR __KillThreshold        = 3
    VAR __FuzzyThreshold1      = .4
    VAR __FuzzyThreshold2      = .8

    VAR __WordSearchTable =
        GENERATE(
            'Projects',
            VAR __Word   = [Project]
            VAR __Result =
                ADDCOLUMNS(
                    GENERATESERIES( 3, LEN( __Word ), 1 ),
                    "Search",    LEFT( __Word, [Value] ),
                    "Original",  __Word
                )
            RETURN __Result
        )

    VAR __Table =
        FILTER(
            ADDCOLUMNS(
                __WordSearchTable,
                "Match", SEARCH( [Search], __MatchWord, , BLANK() )
            ),
            NOT( ISBLANK( [Match] ) )
        )

    VAR __Max   = MAXX( __Table, [Value] )
    VAR __Match = MAXX( FILTER( __Table, [Value] = __Max ), [Search] )

    VAR __Proposed =
        IF(
            LEN( __Match ) > LEN( __MatchWord ),
            SWITCH( TRUE(),
                COUNTROWS( FILTER( __Table, [Value] = __Max ) ) > 1, "No Match 1",
                LEN( __Match ) > LEN( __MatchWord ),                     "No Match 2",
                LEN( __Match ) = LEN( __MatchWord ),                    __Match,
                LEN( __Match ) / LEN( __MatchWord ) > __FuzzyThreshold1
                    && SEARCH( __Match, __MatchWord, , 0 ) = 1,        __Match,
                LEN( __Match ) / LEN( __MatchWord ) > __FuzzyThreshold2,__Match,
                "No Match 3"
            ),
            SWITCH( TRUE(),
                __Match = "Blue Cross" | __Match = "Blue Cross ", __Match,
                LEN( __Match ) / LEN( __MatchWord ) > __FuzzyThreshold1
                    && SEARCH( __Match, __MatchWord, , 0 ) <> 1,       "No Match 4",
                __Match
            )
        )

    VAR __Clean1 =
        IF(
            RIGHT( __Proposed, 1 ) = "(",
            LEFT( __Proposed, LEN( __Proposed ) - 1 ),
            __Proposed
        )

    VAR __Result =
        IF(
            RIGHT( __Clean1, 1 ) = " ",
            LEFT( __Clean1, LEN( __Clean1 ) - 1 ),
            __Clean1
        )

    RETURN __Result
```

## Formula — Levenshtein Distance

```dax
Levenshtein distance =
    VAR __FuzzyThreshold = 8
    VAR __MatchWord =
        ADDCOLUMNS(
            GENERATESERIES( 1, LEN( MAX( 'Clients'[Client Name] ) ), 1 ),
            "__Char", MID( MAX( 'Clients'[Client Name] ), [Value], 1 )
        )

    VAR __Table =
        ADDCOLUMNS(
            DISTINCT( 'Projects'[Project] ),
            "__JS",
                VAR __SearchWord  = [Project]
                VAR __SearchTable =
                    ADDCOLUMNS(
                        GENERATESERIES( 1, LEN( __SearchWord ), 1 ),
                        "__Char", MID( __SearchWord, [Value], 1 )
                    )
                VAR __Result =
                    IF(
                        COUNTROWS( __SearchTable ) > COUNTROWS( __MatchWord ),
                        COUNTROWS( EXCEPT( __SearchTable, __MatchWord ) ),
                        COUNTROWS( EXCEPT( __MatchWord, __SearchTable ) )
                    )
                RETURN __Result
        )

    VAR __Max   = MINX( __Table, [__JS] )
    VAR __Result =
        IF(
            __Max <= __FuzzyThreshold,
            MAXX( FILTER( __Table, [__JS] = __Max ), [Project] ),
            BLANK()
        )

    RETURN __Result
```

## Formula — Jaccard Similarity

```dax
Jaccard Similarity =
    VAR __FuzzyThreshold = .2
    VAR __MatchWord =
        ADDCOLUMNS(
            GENERATESERIES( 1, LEN( MAX( 'Clients'[Client Name] ) ), 1 ),
            "__Char", MID( MAX( 'Clients'[Client Name] ), [Value], 1 )
        )

    VAR __Table =
        ADDCOLUMNS(
            DISTINCT( 'Projects'[Project] ),
            "__JS",
                VAR __SearchWord  = [Project]
                VAR __SearchTable =
                    ADDCOLUMNS(
                        GENERATESERIES( 1, LEN( __SearchWord ), 1 ),
                        "__Char", MID( __SearchWord, [Value], 1 )
                    )
                VAR __Intersect = COUNTROWS( INTERSECT( __SearchTable, __MatchWord ) )
                VAR __Union     = COUNTROWS( UNION( __SearchTable, __MatchWord ) )
                VAR __Result    = DIVIDE( __Intersect, __Union, 0 )
                RETURN __Result
        )

    VAR __Max   = MAXX( __Table, [__JS] )
    VAR __Result =
        IF(
            __Max >= __FuzzyThreshold,
            MAXX( FILTER( __Table, [__JS] = __Max ), [Project] ),
            BLANK()
        )

    RETURN __Result
```

## How the Fuzzy Algorithm Works

The custom **Fuzzy** measure uses a **prefix blowout strategy**:

1. `GENERATESERIES( 3, LEN( __Word ), 1 )` — for each project name, generate
   rows with the first 3, 4, 5… letters (minimum 3 characters).
2. `LEFT( __Word, [Value] )` — truncate the project name to each prefix length.
3. `SEARCH( [Search], __MatchWord, , BLANK() )` — case-insensitive search for
   each prefix in the client name.
4. `MAXX( __Table, [Value] )` — find the **longest matching prefix**; longer
   matches = closer strings.

The Levenshtein Distance is a true edit-distance measure: it converts both
strings to single-character tables and counts how many rows differ using `EXCEPT`.
`__FuzzyThreshold = 8` means strings are considered a match if they differ by
8 or fewer character positions.

## Components

| Component | Role |
|-----------|------|
| `GENERATESERIES` | Expand project names into prefix rows |
| `LEFT` | Truncate to each prefix length |
| `SEARCH` | Case-insensitive substring search |
| `EXCEPT` | Find character differences (Levenshtein) |
| `INTERSECT / UNION` | Jaccard numerator and denominator |
| `MAXX / MINX` | Pick the best-scoring candidate |

## Notes

- The **custom Fuzzy measure** outperformed both Jaccard and Levenshtein in
  testing — it had more matches with fewer false positives.
- Levenshtein's `__FuzzyThreshold` should be **dynamic** (proportional to word
  length) for better accuracy across short and long strings.
- Jaccard counts intersecting characters **only in the same position**; this
  performed better in practice than order-agnostic intersection.
- Use the `__KillThreshold` and `__CleanMatchThreshold` to short-circuit
  obviously bad matches early.

## Related

- [[dax-index-pattern-deckler]] — GENERATESERIES + string table patterns
- [[disconnected-tables-deckler]] — SELECTCOLUMNS optimization for large tables

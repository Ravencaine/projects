---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, table, index, rank, sort, calculated-table]
---

# DAX Index Pattern (Row Number)

## Purpose

DAX has **no native row-number** function. Before Deckler's approach, generating
a sorted, stable row index in DAX was considered impossible because DAX functions
cannot guarantee sort order. The solution: use `CONCATENATEX` + `PATHITEM` to
build a deterministic sort path, then extract sequential indices from it.

This pattern works as both a **calculated table** (generate an indexed table) and
inside **measures** (via table variables).

## Formula — Unsorted Index Table

```dax
DAX Index Table =
    VAR __Table = 'Index'
    VAR __Path  = CONCATENATEX( __Table, [Product], "|" )
    VAR __Result =
        ADDCOLUMNS(
            SELECTCOLUMNS(
                GENERATESERIES( 1, COUNTROWS( __Table ), 1 ),
                "Index", [Value]
            ),
            "Product", PATHITEM( __Path, [Index] )
        )
    RETURN __Result
```

**Output:**

| Index | Product |
|-------|---------|
| 1 | Orange |
| 2 | Banana |
| 3 | Apple |
| … | … |

## Formula — Alphabetically Sorted Index Table

```dax
DAX Index Sorted Table =
    VAR __Table = 'Index'
    VAR __Path  = CONCATENATEX( __Table, [Product], "|", [Product], ASC )
    VAR __Result =
        ADDCOLUMNS(
            SELECTCOLUMNS(
                GENERATESERIES( 1, COUNTROWS( __Table ), 1 ),
                "Index", [Value]
            ),
            "Product", PATHITEM( __Path, [Index] )
        )
    RETURN __Result
```

**Output:**

| Index | Product |
|-------|---------|
| 1 | Apple |
| 2 | Banana |
| 3 | Coconut |
| … | … |

## Formula — Handles Duplicates (Stable Ranking)

```dax
DAX Index Duplicates Sorted Table =
    VAR __Table = UNION( 'Index', 'Index' )
    VAR __Path  = CONCATENATEX( __Table, [Product], "|", [Product], ASC )
    VAR __Result =
        ADDCOLUMNS(
            SELECTCOLUMNS(
                GENERATESERIES( 1, COUNTROWS( __Table ), 1 ),
                "Index", [Value]
            ),
            "Product", PATHITEM( __Path, [Index] )
        )
    RETURN __Result
```

Duplicate rows get sequential indices: Apple×2 → index 1 and 2, Banana×2 → 3 and 4.

## Formula — Two-Column Table with Numeric Sort

```dax
DAX Index Table 2 =
    VAR __Table =
        ADDCOLUMNS( 'Index', "Value", RANDBETWEEN( 10, 100 ) )
    VAR __Path =
        CONCATENATEX( __Table, [Product] & "~" & [Value], "|", [Value], DESC )
    VAR __Result =
        ADDCOLUMNS(
            SELECTCOLUMNS(
                GENERATESERIES( 1, COUNTROWS( __Table ), 1 ),
                "Index", [Value]
            ),
            "Product",
                VAR __Item   = PATHITEM( __Path, [Index] )
                VAR __Result = MID( __Item, 1, FIND( "~", __Item ) - 1 )
                RETURN __Result,
            "Value",
                VAR __Item   = PATHITEM( __Path, [Index] )
                VAR __Result =
                    MID( __Item, FIND( "~", __Item ) + 1, LEN( __Item ) - FIND( "~", __Item ) )
                RETURN __Result
        )
    RETURN __Result
```

Sorts rows by `Value` descending, then returns both the `Product` and `Value`
columns by splitting the combined `Product~Value` path items.

## How the Pattern Works

```
Step 1: CONCATENATEX
  Products → "Orange|Banana|Apple|Grapes|Kiwi|..."

Step 2: GENERATESERIES
  [1, 2, 3, 4, 5, ...] (one row per product)

Step 3: PATHITEM( __Path, Index )
  Row 1 → PATHITEM( path, 1 ) → "Orange"
  Row 2 → PATHITEM( path, 2 ) → "Banana"
  ...
```

`CONCATENATEX` preserves the original row order (or the sorted order if
`[Column], ASC/DESC` is specified). `PATHITEM` then plucks each element back
out by its numeric position — this is the same PATH family technique used for
hierarchical string parsing.

## Notes

- `CONCATENATEX( ..., [Column], ASC/DESC )` is the **sorting lever**: omit
  the sort parameters to preserve original order; add them to sort.
- **Duplicates**: `UNION` creates duplicate rows; each gets its own sequential
  index — no rank collisions.
- **Multi-column sort**: concatenate columns with a delimiter (e.g., `~`) and
  use `MID`/`FIND` to split them back out.
- This pattern is the foundation for **row-number ranking**, **dense ranking**,
  and **percentile calculations** that require positional information.

## Related

- [[fuzzy-matching-levenshtein-dax]] — GENERATESERIES + string table techniques
- [[reverse-year-to-date-dax]] — row-to-row comparison using ALL()

---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: function
tags: [ranking, ordering, top-n, sort]
related: [CALCULATE, ALL, SWITCH]
---

# RANKX

Returns the ranking of a number in a list of numbers. Used to identify the top-N items for conditional formatting or filtering.

## Signature

```dax
RANKX(<table>, <expression>[, <value>[, <order>[, <ties>]]])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `table` | Table | Table or table expression to rank over |
| `expression` | Scalar | Expression evaluated for each row of `table` |
| `value` | Scalar (optional) | Rank this specific value (defaults to evaluating `expression` in the current row context) |
| `order` | Enum (optional) | `0`/`DESC` = descending (largest is rank 1), `1`/`ASC` = ascending |
| `ties` | Enum (optional) | `DENSE` or `SKIP` (default `SKIP`) |

## Examples

**Rank industries by vacancy rate (Bittar pattern):**
```dax
No.1 Ranking =
CALCULATE(
    RANKX(
        ALL('Vacant Positions'[NAICS Industry]),
        [Vacancy Rate],
        ,
        DESC,
        DENSE
    ),
    REMOVEFILTERS()
)
```

**Rank within current filter context:**
```dax
Regional Rank =
    RANKX(
        ALLEXCEPT('Sales'[Region]),
        [Total Sales]
    )
```

**Use rank to drive conditional formatting:**
```dax
Top Performer Flag =
    IF(
        CALCULATE(
            RANKX(ALL('Salesperson'), [Total Sales]) <= 3,
            REMOVEFILTERS()
        ),
        "Top 3",
        "Others"
    )
```

## Notes

- `RANKX` is an iterator — it evaluates `expression` for every row in `table`. For large tables, it can be slow. Use `ALLEXCEPT` to reduce the evaluated set.
- In Bittar's bubble chart articles, `RANKX` with `ALL(...)` and `REMOVEFILTERS()` is used to identify the top-3 industries by vacancy rate — those top-3 then get red coloring via `SWITCH`.
- `DENSE` rank (1, 2, 2, 3) is usually preferred over `SKIP` (1, 2, 2, 4) for conditional formatting.
- When used in a CALCULATE with REMOVEFILTERS, RANKX gives the rank across all values regardless of any active slicer.
- To rank within a category, wrap with CALCULATE and use the category column in a filter argument.

## Related

- [[CALCULATE]] — wrap RANKX to remove slicer filters for absolute ranking
- [[ALL]] / [[ALLEXCEPT]] — control which rows RANKX evaluates
- [[SWITCH]] — use RANKX output to drive color assignments
- [[REMOVEFILTERS]] — clear slicer filters for full-context ranking

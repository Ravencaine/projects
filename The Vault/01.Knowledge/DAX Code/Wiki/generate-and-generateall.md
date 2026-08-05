---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table-manipulation]
---

# GENERATE and GENERATEALL

Returns the Cartesian product of table1 with the table resulting from evaluating table2 in the context of each row in table1.

## Signature

```dax
GENERATE(<table1>, <table2>)
GENERATEALL(<table1>, <table2>)
```

## Parameters

| Term | Definition |
|------|------------|
| `table1` | Any table expression (the base table) |
| `table2` | A table expression evaluated in the context of each row from table1 |

## Differences

| | GENERATE | GENERATEALL |
|---|---|---|
| table2 returns empty | Row from table1 is **dropped** | Row from table1 is **kept** with null columns |
| Duplicate handling | Columns combined by position | Same |

## Examples

```dax
-- All color/year combinations
GENERATE(
    VALUES('Product'[Color]),
    SUMMARIZECOLUMNS('Date'[Year])
)

-- Include all colors even if no sales
GENERATEALL(
    VALUES('Product'[Color]),
    CALCULATETABLE(
        SUMMARIZECOLUMNS('Date'[Year], "Sales", SUM(Sales[Amount])),
        'Product'[Color] = EARLIEST('Product'[Color])
    )
)
```

## Notes

- All column names from table1 and table2 must be **different** or an error is returned
- Table2 is evaluated independently for each row in table1 — this is different from CROSSJOIN which produces all combinations
- GENERATEALL is useful when you want to keep rows from table1 even when table2 has no data

## Related

- [[crossjoin]]
- [[table-manipulation-functions-overview]]
- [[union-intersect-except]]

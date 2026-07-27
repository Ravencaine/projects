---
created: 2026-07-26
source: dax.pdf
note_type: pattern
tags: [dax, pattern, lookup, related, cross-table]
---

# LOOKUPVALUE and RELATED: Cross-Table Lookups

Use LOOKUPVALUE when relationships don't exist or can't be used.

## RELATED: Across Active Relationships

```dax
-- In a calculated column, use RELATED to get values from related tables
Tax = 'Sales'[Net Amount] * RELATED('Tax Rate'[Rate])
```

RELATED requires an active relationship between tables. The column must be on the many side.

## LOOKUPVALUE: When No Relationship Exists

```dax
LOOKUPVALUE(
    <result_column>,
    <search_column1>, <search_value1>,
    [<search_column2>, <search_value2>],
    ...
    [<alternateResult>]
)
```

Returns a value from a column in a different table (or the same table) without requiring a relationship.

```dax
-- Lookup the tax rate for a given category
Tax Rate = LOOKUPVALUE(
    'Tax Rate'[Rate],
    'Tax Rate'[Category], 'Sales'[Category]
)

-- Multiple conditions
Effective Rate = LOOKUPVALUE(
    'Rate Table'[Effective Rate],
    'Rate Table'[Product Category], 'Sales'[Category],
    'Rate Table'[Year], 'Date'[Year],
    BLANK()  -- alternate result if no match
)
```

## LOOKUPWITHTOTALS

Advanced lookup that can work with aggregated data:

```dax
LOOKUPWITHTOTALS(
    <result_column>,
    <search_column1>, <search_value1>,
    ...
    [<alternateResult>]
)
```

Use when you need to lookup from a table that has been summarized or aggregated.

## LOOKUP: Legacy Function

LOOKUP exists for compatibility but LOOKUPVALUE is preferred:
- LOOKUPVALUE is clearer and more flexible
- LOOKUPVALUE supports multiple search conditions more naturally

## Comparison

| Function | Use Case |
|----------|----------|
| RELATED | Value from related table (active relationship, many-to-one) |
| LOOKUPVALUE | Value from any table (no relationship needed) |
| VLOOKUP-equivalent | LOOKUPVALUE with single condition |

## Related

- [[related]]
- [[lookupvalue]]

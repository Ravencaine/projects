---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, lookup, no-calculate]
note_type: pattern

---

# Lookup Values in DAX (No CALCULATE)

Replacing VLOOKUP/RELATED-style lookups with explicit FILTER + MAXX/MINX when there is no active relationship.

## Purpose

When two tables have no direct relationship in the data model, DAX cannot use RELATED(). The No CALCULATE approach uses `FILTER()` + `MAXX()` / `MINX()` to find matching rows explicitly.

## Structure

```dax
Lookup Value =
MAXX(
    FILTER( 'LookupTable', 'LookupTable'[Key] = 'FactTable'[Key] ),
    'LookupTable'[Value]
)
```

## Examples

```dax
-- Find the product category for each sale
Category =
MAXX(
    FILTER( 'Product', 'Product'[ProductID] = 'Sales'[ProductID] ),
    'Product'[Category]
)
```

## Notes

- `MAXX()` returns the maximum of an expression — but when the expression is a single column, it returns the value from the matching row
- Use `MINX()` similarly for single-value extraction
- This pattern is scan-based and can be slow on large tables — use only when no relationship exists
- If a relationship exists, use `RELATED()` instead — it is column-based and much faster

## Related

- [[no-calculate-dax-pattern]]
- [[Iterators in DAX SUMX, AVERAGEX, RANKX and How They Use Row & Filter Context]]

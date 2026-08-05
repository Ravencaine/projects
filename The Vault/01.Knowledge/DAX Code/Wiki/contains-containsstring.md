---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# CONTAINS and CONTAINSSTRING

Test whether values or substrings exist within data.

## CONTAINS

```dax
CONTAINS(<table>, <columnName>, <value>[, <columnName>, <value>]…)
```

Returns TRUE if all specified column/value pairs exist in the table.

```dax
CONTAINS('Reseller', 'Reseller'[ResellerKey], 123)
CONTAINS('Sales', 'Sales'[ProductKey], [ProdKey], 'Sales'[CustomerKey], [CustKey])
```

## CONTAINSSTRING

```dax
CONTAINSSTRING(<within_text>, <find_text>)
```

Returns TRUE if `find_text` is found within `within_text`.

- **Case-insensitive**, kanatype-insensitive, width-insensitive
- **Accent-sensitive** (e.g., "á" ≠ "a")
- Supports wildcards: `?` (any char), `*` (any sequence), `~` to escape

```dax
CONTAINSSTRING('Product'[Name], "bike")         -- case-insensitive
CONTAINSSTRING('Product'[Name], "b?ke")           -- wildcard
CONTAINSSTRING('Log'[Message], "ERROR*")          -- starts with ERROR
```

## CONTAINSSTRINGEXACT

Case-sensitive version of CONTAINSSTRING.

```dax
CONTAINSSTRINGEXACT('User'[Email], "admin@company.com")
```

## Notes

- CONTAINS checks column values (row existence); CONTAINSSTRING checks text content
- CONTAINS is commonly used in security/RLS patterns
- CONTAINSSTRING is useful for dynamic filtering and text matching
- Not supported in DirectQuery mode for calculated columns or RLS rules

## Related

- [[search-find]]
- [[filter]]

---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# CONCATENATE and CONCATENATEX

Join text strings together.

## CONCATENATE

```dax
CONCATENATE(<text1>, <text2>)
```

Joins exactly two text strings. Only accepts two arguments (unlike Excel's 255).

```dax
CONCATENATE('Customer'[FirstName], 'Customer'[LastName])
```

## CONCATENATEX

```dax
CONCATENATEX(<table>, <expression>[, <delimiter>[, <orderBy_expression>[, <order>]]])
```

Iterates over a table and concatenates the expression result for each row.

| Term | Definition |
|------|------------|
| `table` | Table to iterate |
| `expression` | Text expression per row |
| `delimiter` | (Optional) Separator string |
| `orderBy_expression` | (Optional) Sort key |
| `order` | (Optional) 0/DESC = descending, 1/ASC = ascending |

## Examples

```dax
-- Full name
Full Name = CONCATENATE('Customer'[FirstName], " " & 'Customer'[LastName])

-- Comma-separated list of product names
Product List =
CONCATENATEX(
    FILTER('Product', 'Product'[Category] = "Bikes"),
    'Product'[Name],
    ", ",
    'Product'[Name],
    ASC
)
```

## Notes

- CONCATENATE takes exactly two arguments — nest or use `&` for more
- CONCATENATEX is an iterator — expression is evaluated per row
- Use `&` operator for simple concatenation: `'A'[X] & " - " & 'A'[Y]`
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[exact]], [[lower]], [[upper]]

## Related

- [[exact]]
- [[lower]]
- [[upper]]

---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "order-by", "sort", "dax-studio"]
note_type: function

---

# ORDERBY — Row Ordering in Iterators

Specifies the sort order for an iterator function result.

## Signature

```dax
CONCATENATEX( <Table>, <Expression>, <Delimiter>, ORDERBY( <Column>, <Order> ) )
```

## Examples

```dax
Sorted Names := CONCATENATEX(
    'Products',
    'Products'[Name],
    ", ",
    'Products'[Name], ASC
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Column | Column | Column to sort by. |
| Order | ASC/DESC | Sort order. Default: ASC. |

## Notes

- `ORDERBY()` must appear inside the iterator function, not after
- Use `SKIP()` to exclude specific rows from ordering
- DAX does not support ORDER BY outside of specific functions

## Related

- [[CONCATENATEX]]
- [[skip-keyword]]

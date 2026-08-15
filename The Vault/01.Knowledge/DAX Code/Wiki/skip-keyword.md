---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, skip, orderby, iterator]
note_type: function

---

# SKIP — Exclude from Sort

Excludes specific rows from ORDER BY ordering without removing them from the result.

## Signature

```dax
CONCATENATEX(
    'Table',
    'Table'[Column],
    ", ",
    ORDERBY( 'Table'[Column], ASC ),
    SKIP( 'Table'[ExcludeFlag] = TRUE )
)
```

## Notes

- SKIP keeps excluded rows in the result but removes them from the sort order
- Useful for sorting items while keeping blanks or placeholders in position

## Related

- [[ORDERBY]]
- [[CONCATENATEX]]

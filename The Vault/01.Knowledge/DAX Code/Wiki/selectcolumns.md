---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "table", "select", "column"]
note_type: function

---

# SELECTCOLUMNS — Column Selection

Adds or selects columns from a table expression.

## Signature

```dax
SELECTCOLUMNS( <Table>, [<Name1>], <Expression1>, [<Name2>], <Expression2>, ... )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Table | Table | Source table. |
| Name | Text | Output column name. |
| Expression | Any | Column expression. |

## Examples

```dax
-- Rename and project columns
Compact :=
SELECTCOLUMNS(
    'Sales',
    "SaleID", 'Sales'[ID],
    "Amount", 'Sales'[Amount]
)

-- Create a lookup table
Lookup :=
SELECTCOLUMNS(
    'Product',
    "Key", 'Product'[ProductID],
    "Label", 'Product'[Name]
)
```

## Notes

- Adds columns rather than removing them
- Useful for renaming columns and creating projection tables
- Combined with FILTER() for context-aware column selection

## Related

- [[GENERATESERIES]]
- [[ADDCOLUMNS]]

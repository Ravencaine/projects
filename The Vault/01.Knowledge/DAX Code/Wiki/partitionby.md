---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "partition", "group", "orderby"]
note_type: function

---

# PARTITIONBY — Iterator Grouping

Defines groups within an iterator for independent ordering.

## Signature

```dax
<IteratorFunction>(
    <Table>,
    <Expression>,
    ORDERBY( <Column>, <Order>, PARTITIONBY( <Column> ) )
)
```

## Examples

```dax
Row Number Per Category :=
ADDCOLUMNS(
    'Sales',
    "__RN",
    RANKX(
        ALL( 'Sales'[Category] ),
        CALCULATE( COUNTROWS( 'Sales' ) ),
        ,
        ASC
    )
)
```

## Notes

- `PARTITIONBY()` groups rows for separate ranking/ordering within each group
- Similar to SQL's `PARTITION BY` clause
- DAX natively supports `PARTITIONBY` inside `ORDERBY` in newer versions

## Related

- [[ORDERBY]]
- [[RANKX]]

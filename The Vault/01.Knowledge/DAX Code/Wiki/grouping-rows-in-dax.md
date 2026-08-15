---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, grouping, summarize, table]
note_type: pattern

---

# Grouping Rows in DAX

Using SUMMARIZECOLUMNS and GROUPBY to create grouped aggregations.

## SUMMARIZECOLUMNS

```dax
Sales by Category :=
SUMMARIZECOLUMNS(
    'Product'[Category],
    "Total Sales", SUM( 'Sales'[Amount] ),
    "Order Count", COUNTROWS( 'Sales' )
)
```

## GROUPBY for Complex Aggregations

```dax
Grouped Sales :=
GROUPBY(
    'Sales',
    'Sales'[Category],
    "Total", SUMX( CURRENTGROUP(), 'Sales'[Amount] )
)
```

## Notes

- SUMMARIZECOLUMNS is preferred for most use cases
- GROUPBY is needed when the aggregation expression is complex

## Related

- [[SUMMARIZECOLUMNS]]
- [[GROUPBY]]
- [[the-measure-totals-problem-in-dax]]

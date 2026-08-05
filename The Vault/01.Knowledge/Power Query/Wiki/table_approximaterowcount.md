---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.ApproximateRowCount

Returns the approximate number of rows in the table, or an error if the data source doesn't support approximation.

## Signature

```m
Table.ApproximateRowCount(table as table) as number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

number

### Example 1

Estimate the number of distinct combinations of city and state in a large table, which can be used as a cardinality estimate for the columns. Cardinality estimates are important enough that various data sources (such as SQL Server) support this particular approximation, often using an algorithm called HyperLogLog.

```m
Table.ApproximateRowCount(Table.Distinct(Table.SelectColumns(sqlTable, {"city",
"state"})))
```

// Output
```
number
```


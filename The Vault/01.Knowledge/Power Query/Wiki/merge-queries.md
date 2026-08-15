---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, merge, join, combine-tables]
---

# Merge Queries

Combine data from two tables based on key columns — analogous to SQL JOIN or VLOOKUP.

## Purpose

Relate denormalized lookup tables (e.g., product categories, customer details) to a fact table without duplicating data in the model.

## Components

- `Table.NestedJoin`
- `Table.ExpandTableColumn`

## Structure

```m
Table.NestedJoin(
    leftTable,
    {"LeftKeyCol"},
    rightTable,
    {"RightKeyCol"},
    "joinedTable",
    JoinKind.LeftOuter  // or other JoinKind
)
```

Expand the nested column after joining:

```m
Table.ExpandTableColumn(
    Source,
    "joinedTable",
    {"Col1", "Col2"},
    {"Expanded.Col1", "Expanded.Col2"}
)
```

## Join Kinds

| Kind | Behaviour |
|------|-----------|
| `LeftOuter` | All left rows, matching right rows |
| `RightOuter` | All right rows, matching left rows |
| `FullOuter` | All rows from both tables |
| `Inner` | Only matching rows |
| `LeftAnti` | Rows in left with no match in right |
| `RightAnti` | Rows in right with no match in left |

## Example

```m
// Join Sales to Customer table on CustomerID
Table.NestedJoin(
    Sales,
    {"CustomerID"},
    Customer,
    {"CustomerID"},
    "Customer",
    JoinKind.LeftOuter
)
```

## Related

- [[Remove-Duplicates]] — deduplicate key columns before joining
- [[Group-By]] — aggregate fact table before merging large tables

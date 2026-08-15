---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.AddRankColumn

Appends a column named newColumnName to the table with the ranking of one or more other columns described by comparisonCriteria. The RankKind option in options can be used by advanced users to pick a more-specific ranking method. Example Add a column named "RevenueRank" to the table which ranks the "Revenue" column from highest to lowest. Usage Power Query M Table.AddRankColumn( Table.FromRecords({ [CustomerID = 1, Name = "Bob", Revenue = 200], [CustomerID = 2, Name = "Jim", Revenue = 100], [CustomerID = 3, Name = "Paul", Revenue = 200], [CustomerID = 4, Name = "Ringo", Revenue = 50] }), "RevenueRank", {"Revenue", Order.Descending}, [RankKind = RankKind.Competition] ) Output Power Query M --- PAGE 956 --- Table.FromRecords({ [CustomerID = 1, Name = "Bob", Revenue = 200, RevenueRank = 1], [CustomerID = 3, Name = "Paul", Revenue = 200, RevenueRank = 1], [CustomerID = 2, Name = "Jim", Revenue = 100, RevenueRank = 3], [CustomerID = 4, Name = "Ringo", Revenue = 50, RevenueRank = 4] }) Related content Comparison criteria Last updated on 04/03/2026 --- PAGE 957 ---

## Signature

```m
Table.AddRankColumn(
table as table,
newColumnName as text,
comparisonCriteria as any,
optional options as nullable record
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| newColumnName | text | |
| comparisonCriteria | any | |
| optional options | nullable record | |

## Returns

table


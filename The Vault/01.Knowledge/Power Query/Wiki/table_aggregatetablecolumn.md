---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.AggregateTableColumn

Aggregates tables in table[column] into multiple columns containing aggregate values for the tables. aggregations is used to specify the columns containing the tables to aggregate, the aggregation functions to apply to the tables to generate their values, and the names of the aggregate columns to create. Example Aggregate table columns in [t] in the table {[t = {[a=1, b=2, c=3], [a=2,b=4,c=6]}, b = 2]} into the sum of [t.a], the min and max of [t.b], and the count of values in [t.a]. Usage Power Query M Table.AggregateTableColumn( Table.FromRecords( { [ t = Table.FromRecords({ [a = 1, b = 2, c = 3], [a = 2, b = 4, c = 6] }), b = 2 ] }, type table [t = table [a = number, b = number, c = number], b = number] ), "t", { {"a", List.Sum, "sum of t.a"}, {"b", List.Min, "min of t.b"}, {"b", List.Max, "max of t.b"}, --- PAGE 958 --- {"a", List.Count, "count of t.a"} } ) Output Table.FromRecords({[#"sum of t.a" = 3, #"min of t.b" = 2, #"max of t.b" = 4, #"count of t.a" = 2, b = 2]}) Last updated on 03/24/2026 --- PAGE 959 ---

## Signature

```m
Table.AggregateTableColumn(
table as table,
column as text,
aggregations as list
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| column | text | |
| aggregations | list | |

## Returns

table


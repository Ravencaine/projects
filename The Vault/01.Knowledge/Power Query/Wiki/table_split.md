---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.Split

Splits table into a list of tables where the first element of the list is a table containing the first pageSize rows from the source table, the next element of the list is a table containing the next pageSize rows from the source table, and so on. Example Split a table of five records into tables with two records each. Usage Power Query M let Customers = Table.FromRecords({ [CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Cristina", Phone = "232-1550"], [CustomerID = 5, Name = "Anita", Phone = "530-1459"] }) in Table.Split(Customers, 2) Output Power Query M { Table.FromRecords({ [CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"] }), Table.FromRecords({ [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Cristina", Phone = "232-1550"] }), --- PAGE 1126 --- Table.FromRecords({ [CustomerID = 5, Name = "Anita", Phone = "530-1459"] }) } Last updated on 03/24/2026 --- PAGE 1127 ---

## Signature

```m
Table.Split(table as table, pageSize as number) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| pageSize | number | |

## Returns

list


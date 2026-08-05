---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.Buffer

Buffers a table in memory, isolating it from external changes during evaluation. Buffering is shallow. It forces the evaluation of any scalar cell values, but leaves non-scalar values (records, lists, tables, and so on) as-is. table: The table to buffer in memory. options: (Optional) The following options record values can be used: BufferMode: The buffer mode that describes the type of buffering to be performed. This option can be either BufferMode.Eager or BufferMode.Delayed. Using this function might or might not make your queries run faster. In some cases, it can make your queries run more slowly due to the added cost of reading all the data and storing it in memory, as well as the fact that buffering prevents downstream folding. If the data doesn't need to be buffered but you just want to prevent downstream folding, use Table.StopFolding instead. Example Load all the rows of a SQL table into memory, so that any downstream operations are no longer able to query the SQL server. Usage Power Query M let Source = Sql.Database("SomeSQLServer", "MyDb"), MyTable = Source{[Item="MyTable"]}[Data], BufferMyTable = Table.Buffer(MyTable) in BufferMyTable --- PAGE 963 --- Output table Last updated on 04/03/2026 --- PAGE 964 ---

## Signature

```m
Table.Buffer(table as table, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| optional options | nullable record | |

## Returns

table


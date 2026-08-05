---


title: "Power Query Advanced Editor"
created: 2026-07-28
updated: 2026-08-02
tags: [power-query, reference]
note_type: reference
description: "Power Query Advanced Editor — viewing and editing the M language code behind each query step. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Query: Advanced Editor

Displays and allows editing of the underlying **M language** (Power Query Formula Language) code that defines the query.

## Access

```
Power Query → Advanced Editor
```

## What It Shows

Each transformation step in the query is represented as a line of M code:

```m
Source = Csv.Document(File.Contents("C:\data\nyse.csv"), [Delimiter=","]),
PromotedHeaders = Table.PromoteHeaders(Source),
ChangedType = Table.TransformColumnTypes(PromotedHeaders, {{"Symbol", type text}, ...})
```

## Practical Uses

- **Debug**: see exactly what each step does
- **Optimize**: remove unnecessary intermediate steps
- **Share**: copy the M code for reuse
- **Customize**: write M expressions not available via the ribbon

## M Language Notes

- Case-sensitive
- Functions follow the `Table.FunctionName` pattern
- Each step output becomes the input for the next step
- Comments start with `//`

## Source Reference

Chapter 8, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

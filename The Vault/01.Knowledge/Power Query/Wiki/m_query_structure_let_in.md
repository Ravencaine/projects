---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: pattern
tags: ["m-language", "query-structure"]
---


# M Query Structure — let…in

Every M query in Power Query follows the let…in pattern. Build a pipeline of named steps, then output the final result after `in`.

## Purpose

Structure complex data transformations into readable, named steps.

## Components

1. `let` keyword opens the expression
2. Named steps each define a transformation
3. Steps reference previous steps by name
4. `in` keyword declares the output step
5. The named step after `in` is the query's result

## Structure

```
let
    Source = DataSource(...),
    #"Step Name" = Table.TransformColumns(Source, ...),
    Filtered = Table.SelectRows(#"Step Name", each [Column] > 0),
    Output = Table.SelectColumns(Filtered, {"Column1", "Column2"})
in
    Output
```

## Example

```
let
    Orders = Table.FromRecords({
        [OrderID = 1, Item = "fishing rod", Price = 100.0],
        [OrderID = 2, Item = "1 lb. worms", Price = 5.0]
    }),
    Capitalized = Table.TransformColumns(Orders, {"Item", Text.Proper})
in
    Capitalized
```

## Related

- [[m_let_expressions]] — let expression semantics

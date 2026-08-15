---
created: 2026-08-09
updated: 2026-08-09
source: "Easily Remove Blank Rows in a Table using Power Query(.pbix included).md"
source_url: "https://medium.com/@shashanka.shekhar02/easily-remove-blank-rows-in-a-table-using-power-query-pbix-included-780c4bd164a8"
author: "[[Shashanka Shekhar]]"
site: https://medium.com/@shashanka.shekhar02
published: 2026-08-03
source_type: article
kb_routing: Power Query
tags: [power-query, remove-blanks, table-selectrows, beginner]
level: Beginner
---

# Remove Blank Rows in Power Query

Shashanka Shekhar · Medium · 2026-08-03

## What this article covers

Use `Table.SelectRows` with a custom filter condition in the Advanced Editor to remove blank rows from a table in Power Query. The filter checks one reference column; rows where that column is null or empty are removed. Steps: Advanced Editor → replace M code with filter → Close & Apply.

## Key technique

```m
Table.SelectRows(Source, each ([Column2] <> "" and [Column2] <> null))
```

Removes any row where Column2 is empty or null. After filtering, promote the first remaining row to headers.

## Level

Beginner

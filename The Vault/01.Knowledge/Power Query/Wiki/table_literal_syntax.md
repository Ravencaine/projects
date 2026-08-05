---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: snippet
tags: ["m-language", "table"]
---


# Table Literal Syntax — #table()

Tables in M have no direct literal syntax. Use `#table()` to construct tables from column names and row lists.

## Code

```
// Basic #table
#table(
    {"Column1", "Column2"},
    {
        {1, "one"},
        {2, "two"},
        {3, "three"}
    }
)

// With type declaration
#table(
    type table [ID = Int64.Type, Name = Text.Type],
    {
        {1, "Alice"},
        {2, "Bob"}
    }
)

// Empty table with schema
#table(type table [Name = Text.Type, Age = Int64.Type], {{}})
```

## When to Use

- Creating small reference tables inline in a query
- Defining expected schema with `type table [...]`
- Generating test data without a data source

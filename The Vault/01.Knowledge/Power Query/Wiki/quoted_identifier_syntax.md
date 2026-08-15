---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: snippet
tags: [m-language, identifiers]
---


# Quoted Identifier Syntax — #"Name with Spaces"

M identifiers cannot contain spaces normally. The `#"..."` syntax allows spaces, reserved words, and arbitrary text as identifier names.

## Code

```
// Standard identifier
StepName = Table.Distinct(Source)

// Quoted identifier with spaces
#"Step With Spaces" = Table.Distinct(Source),
#"Filtered Rows" = Table.SelectRows(#"Step With Spaces", each [Status] = "Active"),
#"Renamed Columns" = Table.RenameColumns(#"Filtered Rows", {{"Old", "New"}})

// Quoted identifier for reserved words
#"and" = 1,
#"or" = 2,
#"if" = 3
```

## When to Use

- Creating readable step names in the Power Query Advanced Editor
- Using M keywords as variable names
- Making queries self-documenting with descriptive step names

## Notes

- Power Query's UI automatically quotes step names with spaces using `#"Step Name"` format

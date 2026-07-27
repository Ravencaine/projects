---
created: 2026-07-26
source: dax.pdf
note_type: reference
tags: [dax, reference, syntax]
---

# DAX Syntax

DAX syntax rules govern how formulas, references, and expressions are written.

## Quick Reference

### Formula Structure

- Calculated column: `= <expression>`
- Measure: `MeasureName := <expression>`
- Every formula must begin with `=` (calculated columns/measures)
- DAX query statements do not require leading `=`

### Table and Column References

- **Fully qualified**: `TableName[ColumnName]` — table name in single quotes if it contains spaces: `'Table Name'[Column]`
- **Unqualified**: `[ColumnName]` — table name is implied (safe in calculated columns, ambiguous in measures)
- **Fully qualified table**: `TableName` — used in table functions: `ALL(TableName)`

### Measure References

Measures are always fully qualified with table: `[TableName][MeasureName]` or `TableName[MeasureName]`. Fully qualified measure references break if the home table changes.

### Naming Rules

- Table names: must be unique within the model. Single quotes required if the name contains spaces or special characters.
- Column names: must be unique within a table. Brackets required for names with spaces.
- Measure names: must be unique within the model.

### Function Syntax

DAX functions follow: `FunctionName(arg1, arg2, ...)` — arguments separated by commas.

- Commas are used as argument separators
- Parentheses are required, even for zero-argument functions
- Optional arguments are shown in `[brackets]` in documentation

### Whitespace and Case

- DAX is **not case-sensitive** — `SUM`, `Sum`, `sum` are equivalent
- Whitespace is ignored: line breaks and spaces are equivalent to a single space
- Comments: `--` for single-line

## Notes

- There are no named ranges in DAX — always reference columns or tables directly
- DAX formulas cannot reference individual cells (unlike Excel)
- The formula bar and DAX Editor provide AutoComplete for functions, tables, and columns
- AutoComplete does not add closing parentheses — you must match them manually
- Up to 64 levels of function nesting are supported in calculated columns

## Related

- [[dax-operators]] — reference
- [[dax-overview]] — atomic

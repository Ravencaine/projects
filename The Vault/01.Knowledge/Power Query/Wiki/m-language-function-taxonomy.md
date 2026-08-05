---
created: 2026-08-02
updated: 2026-08-02
source: Mastering M Language and DAX Functions in Power BI A Comprehensive Guide with Real-World Use Cases.md
note_type: reference
tags: [power-query, reference, m, function-taxonomy, table-functions, text-functions, date-functions]
---

# M Language Function Taxonomy

M Language is a functional, case-sensitive language used exclusively in Power Query Editor for ETL (Extract, Transform, Load). Every step creates a new table — M is immutable with no side effects. Functions are grouped by the type of data they operate on.

## Function Categories

### 1. Table Functions (Core ETL)
Manipulate tables: filter, add columns, group, join, sort.

- `Table.SelectColumns` — choose specific columns
- `Table.SelectRows` — filter rows by condition
- `Table.AddColumn` — create custom columns
- `Table.Group` — aggregate data (like SQL GROUP BY)
- `Table.Distinct` — remove duplicate rows
- `Table.TransformColumns` — change column types or values
- `Table.NestedJoin` / `Table.Combine` — merge or append tables

### 2. Text Functions
Handle and format strings.

- `Text.Proper` — title case
- `Text.Trim` — remove leading/trailing whitespace
- `Text.Combine` — concatenate strings
- `Text.Replace` — substitute text
- `Text.Split` — split by delimiter
- `Text.Length` — character count

### 3. Date, DateTime, Duration, Time Functions
Date/time arithmetic and extraction.

- `Date.AddDays`, `Date.FromText`, `DateTime.LocalNow`
- `Duration.Days`, `Time.From`

### 4. List Functions
Work with lists (arrays).

- `List.Sum`, `List.Distinct`, `List.Transform`
- `List.Contains`, `List.Count`

### 5. Record Functions
Handle record structures (key-value pairs).

- `Record.Field`, `Record.ToTable`, `Record.HasFields`

### 6. Number Functions
Math on numbers.

- `Number.Round`, `Number.FromText`, `Number.Random`

### 7. Logical Functions
Boolean logic.

- `Logical.From`, `if…then…else` (built-in)

### 8. Specialized Categories
- **Accessing Data**: `Excel.Workbook`, `Sql.Database`, `Web.Contents`
- **Binary/Uri/Web**: File handling, HTTP calls
- **Type Functions**: `Type.Is`, `Value.Type` (data type checks)
- **Custom Functions & Combinators**: Reusable parameterized logic
- **Comparer/Join Types**: Advanced merges (Inner, Left Anti, etc.)

## Architecture Note

M operates in Power Query during the ETL stage. It can fold queries back to the source (where the data engine supports it), improving performance. DAX operates after data is loaded, in the data model.

## Related

- [[m-language-real-world-use-cases]] — `pattern`
- [[dax-function-taxonomy]] — `reference`
- [[dax-real-world-use-cases]] — `pattern`

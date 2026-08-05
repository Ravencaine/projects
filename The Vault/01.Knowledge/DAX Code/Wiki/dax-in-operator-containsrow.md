---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [in-operator, containsrow, filter, or-conditions, syntax]
---

# DAX IN Operator and CONTAINSROW

The `IN` operator tests whether a value exists in a set of values, replacing verbose `OR` chains with clean, readable syntax.

## Purpose

Checking whether a column value matches one of several specific values (e.g., `Item = "Banana" | Item = "Pickle"`) is common but verbose. The `IN` operator (and its functional equivalent `CONTAINSROW`) provides a compact, readable alternative.

## IN Operator Syntax

```dax
<column> IN { <value1>, <value2>, ... }
```

The curly braces `{ }` create a **table constructor**: a single-column table of literal values.

## CONTAINSROW Equivalent

```dax
CONTAINSROW( { <value1>, <value2>, ... }, <column> )
```

`IN` and `CONTAINSROW` are functionally identical. Use `IN` in filter expressions; use `CONTAINSROW` inside functions that require a table expression.

## Structure

```dax
-- IN in a filter context
FILTER( 'Table', 'Table'[Item] IN { "Banana", "Pickle" } )

-- CONTAINSROW inside a function that expects a table
FILTER( 'Table', CONTAINSROW( { "Banana", "Pickle" }, [Item] ) )
```

## Examples

**Using IN to filter for Banana or Pickle rows:**
```dax
IN Operator =
VAR __Table = { "Banana", "Pickle" }
VAR __Result = FILTER( 'Table', CONTAINSROW( __Table, [Item] ) )
RETURN
    __Result
```

**Using a derived IN table (more flexible):**
```dax
IN Operator =
VAR __Table =
    FILTER(
        'Table',
        'Table'[Item] = "Banana" | 'Table'[Item] = "Pickle"
    )
VAR __SelectedColumns = SELECTCOLUMNS( __Table, "__Item", [Item] )
VAR __Values = DISTINCT( __SelectedColumns )
VAR __Result = FILTER( 'Table', [Item] IN __Values )
RETURN
    __Result
```
This builds the IN set dynamically from the data itself, rather than hardcoding literals. `__Values` has 2 rows (1 Banana, 1 Pickle) even though `__Table` has 4 rows.

## IN vs Multiple OR Conditions

```dax
-- Verbose
FILTER( 'Table', 'Table'[Item] = "Banana" | 'Table'[Item] = "Pickle" )

-- Clean IN equivalent
FILTER( 'Table', 'Table'[Item] IN { "Banana", "Pickle" } )
```

## Related

- [FILTER](/wiki/filter.md) — the function that most often contains `IN`
- [Table Constructor Pattern](/wiki/table-constructor-pattern-in-dax.md) — `{ }` syntax for creating inline tables
- [CONTAINSROW](/wiki/containsrow.md) — functional equivalent of the `IN` operator
- [No CALCULATE Banana Pattern](/wiki/no-calculate-banana-pattern.md) — IN is commonly used in the filter step

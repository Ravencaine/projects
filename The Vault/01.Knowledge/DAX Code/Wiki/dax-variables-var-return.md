---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: atomic
tags: [dax-concepts, variables, var, readability, debugging]
---

# DAX Variables (VAR/RETURN)

Named intermediate values declared inside a DAX expression that avoid repetition, improve readability, and enable step-by-step debugging.

## Definition

A `VAR` declares a named value or table expression inside a DAX measure or calculated column. `RETURN` marks where the final result expression begins. Everything between `VAR` and `RETURN` is evaluated once and stored by name.

```dax
VAR <name> = <expression>
VAR <name> = <expression>
...
RETURN
    <final expression referencing VAR names>
```

## Key Points

- **Avoid repetition**: if the same sub-expression appears twice, store it in a `VAR` and reference it by name instead of recomputing it. This also improves performance by eliminating duplicate evaluation.
- **Named steps aid debugging**: because each `VAR` is a named, inspectable value, you can temporarily swap the `RETURN` expression to display any intermediate variable. This is the foundation of the No CALCULATE debugging workflow.
- **Naming convention**: prefix variable names with `__` (double underscore) following Microsoft's internal DAX query convention. This avoids collisions with reserved words like `Table`, `Date`, `Value`, etc.
- **`__Result` convention**: put the final computed value in a `VAR __Result` (or `_Result`) and return that. Keeps the `RETURN` line clean and makes debugging trivial.
- **DAX queries use double underscore internally**: when you copy a DAX query from the Performance Analyzer, you see `__DS0Core`, `__DS0PrimaryWindowed`, etc. This is why the double-underscore convention is used.

## Examples

**Without variables (repetitive, harder to follow):**
```dax
Min Plus Max Total Cost Not Pickle =
MINX(
    FILTER( 'Table', 'Table'[Item] <> "Pickle" ),
    [Total Cost]
)
+
MAXX(
    FILTER( 'Table', 'Table'[Item] <> "Pickle" ),
    [Total Cost]
)
```
The same `FILTER` expression is written twice — error-prone and redundant.

**With variables (clean, debuggable):**
```dax
Min Plus Max Total Cost No Pickle =
VAR __Table = FILTER( 'Table', 'Table'[Item] <> "Pickle" )
VAR __Min = MINX( __Table, [Total Cost] )
VAR __Max = MAXX( __Table, [Total Cost] )
VAR __Result = __Min + __Max
RETURN
    __Result
```

Both produce the same result. The variable version:
1. Evaluates the filtered table once (performance benefit)
2. Breaks the logic into named steps (readability benefit)
3. Allows swapping `RETURN __Result` for `RETURN COUNTROWS(__Table)` to debug (debugging benefit)

## Related

- [No CALCULATE Banana Pattern](/wiki/no-calculate-banana-pattern.md) — the primary pattern that uses variables
- [TOCSV Debugging Pattern](/wiki/dax-debugging-tocsv.md) — using `VAR` for debugging table contents
- [FILTER](/wiki/filter.md) — the function most often stored in a table `VAR`

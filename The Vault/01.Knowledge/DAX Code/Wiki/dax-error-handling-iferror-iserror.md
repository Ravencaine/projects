---

created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: ["dax", "pattern", "error", "iferror", "iserror", "error-handling"]

---

# DAX Error Handling — IFERROR and ISERROR

DAX does not fail silently — errors break visuals. DAX provides `ERROR()`, `IFERROR`, and `ISERROR` to manage error generation and handling, similar to try/catch in other languages.

## Purpose

Catch DAX errors (division by zero, type mismatches, invalid context) and return fallback values or alternate logic to keep visuals rendering cleanly.

## Structure

**Raise a custom error:**

```dax
Error = ERROR( "Something bad happened" )
```

**Detect and handle an error:**

```dax
IsError =
IF(
    ISERROR( ERROR( "Something bad happened" ) ),
    "Something bad happened",
    "Everything is good"
)
```

**Try/catch pattern with IFERROR:**

```dax
IfError =
IFERROR(
    ERROR( "Something bad happened" ),
    "Something bad happened"
)
```

**Safe division — preferred over IFERROR for divide-by-zero:**

```dax
IfError 2 = IFERROR( 100 / 1, 0 )   // returns 100
IfError 3 = IFERROR( 100 / 0, 0 )   // returns 0
```

## Notes

- `IFERROR(expression, fallback)` — evaluates `expression`; if it errors, returns `fallback`.
- `ISERROR(expression)` — returns TRUE/FALSE without suppressing the error.
- Performance impact: both functions carry a performance penalty. Prefer built-in error-tolerant functions where possible:
  - `DIVIDE(numerator, denominator, 0)` — handles division by zero natively
  - `SELECTEDVALUE`, `LOOKUPVALUE`, `FIND`, `SEARCH` — all have error-tolerant modes
- Do NOT use `ERROR()` in production code; it is for demonstration and debugging only.
- Nesting `IFERROR` is possible but signals a design problem — consider restructuring the logic.

## Related

- [[dax-debugging-with-evaluateandlog-and-tocsv]]
- [[divide]]

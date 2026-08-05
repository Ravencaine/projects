---
created: 2026-07-27
updated: 2026-08-02
source: "Stop Repeating Yourself in DAX: The Power of Variables (VAR)"
note_type: atomic
tags: [dax, variables, var, readability, performance]
---

# VAR in DAX: Readability and Performance

DAX VAR statements name intermediate calculation results, making DAX both faster (no re-evaluation) and more readable (self-documenting logic).

## Definition

```dax
VAR <Name> = <Expression>
RETURN <Result>
```

VAR captures the result of Expression once. Any reference to Name in the RETURN clause reuses that cached result — the engine does not re-evaluate.

## Key Points

- **Readability:** Naming intermediates (VAR Profit = ..., VAR LY_Sales = ...) makes DAX self-documenting
- **Performance:** An expression referenced twice inline evaluates twice; wrapped in VAR it evaluates once
- **Defensive DAX:** VAR enables explicit intermediate checks (zero test, BLANK test) before final calculation
- **Scope:** VAR names are only visible inside their own RETURN block — they do not leak to other measures
- **Context:** VAR does NOT create a new CALCULATE context; expressions inside VAR evaluate in the current filter context

## Examples

**Without VAR (duplication + slow):**

```dax
Profit Margin % =
DIVIDE (
    SUM(Sales[Revenue]) - SUM(Sales[Cost]),
    SUM(Sales[Revenue])
)
```

**With VAR (single evaluation):**

```dax
Profit Margin % =
VAR Profit = SUM(Sales[Revenue]) - SUM(Sales[Cost])
RETURN
    DIVIDE ( Profit, SUM(Sales[Revenue]), BLANK() )
```

**Growth % with LY comparison (two references to profit):**

```dax
Growth % =
VAR Profit    = SUM(Sales[Revenue]) - SUM(Sales[Cost])
VAR Profit_LY = CALCULATE(Profit, SAMEPERIODLASTYEAR(Calendar[Date]))
RETURN
    DIVIDE(Profit - Profit_LY, Profit_LY, BLANK())
```

Profit is calculated once, reused in both measures.

**Defensive pattern (explicit zero check):**

```dax
Safe Conversion Rate =
VAR Visits      = SUM(Sales[Visits])
VAR Conversions = SUM(Sales[Conversions])
VAR HasData     = NOT ISBLANK(Visits) && NOT ISBLANK(Conversions)
VAR Result      = IF(Visits > 0 && HasData, DIVIDE(Conversions, Visits, 0), BLANK())
RETURN
    Result
```

## Related

- [[measure-branching-pattern]] — VAR enables clean branching
- [[pattern-2-defensive-dax]] — VAR for error handling

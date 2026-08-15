---
created: 2026-08-06
updated: 2026-08-06
source: Controlling Format Strings in Calculation Groups
note_type: atomic
tags: [calculation-groups, dax, format-string, SELECTEDMEASUREFORMATSTRING, SELECTEDMEASURENAME, tabular]
---

# Format String Expression in Calculation Groups

Each calculation item has two DAX properties: the *Expression* (controls the calculated value) and the *Format String Expression* (controls the display format). The format string expression uses [[SELECTEDMEASUREFORMATSTRING]] to read the current format and can override it conditionally — for example, applying a percentage format to a YOY% calculation item regardless of the underlying measure's format.

<!-- one-line description: Format String Expression property on calculation items — overrides measure format dynamically using SELECTEDMEASUREFORMATSTRING() as the base -->

## How It Works

The Format String Expression is a DAX expression that returns a format string (e.g., `"#,0.00%"`). It runs in the same filter context as the calculation item's Expression, so it has access to:
- The current measure's name via `SELECTEDMEASURENAME()`
- The current measure's existing format via `SELECTEDMEASUREFORMATSTRING()`
- Any column values from the filter context

## Key Pattern

```dax
VAR MeasureName = SELECTEDVALUE(Metric[Metric], SELECTEDMEASURENAME())
VAR SkipConversion = (SEARCH("#", MeasureName, 1, 0) > 0)
                       || (SEARCH("%", MeasureName, 1, 0) > 0)
VAR CurrencyFormat = SELECTEDVALUE('Currency'[Currency Format], "#,0.00")
RETURN
    IF(
        SkipConversion,
        SELECTEDMEASUREFORMATSTRING(),  // preserve existing format
        CurrencyFormat                  // apply currency format
    )
```

## SELECTEDMEASUREFORMATSTRING() Behaviour

- Returns the format string of the measure currently being evaluated
- If another calculation item with higher precedence has already set a format, `SELECTEDMEASUREFORMATSTRING()` returns that overridden format — useful for chaining
- Returns blank if no format string is defined on the measure

## Precedence and Format String Expression

Format String Expression follows the same precedence rules as the main Expression. The CG with the **highest** precedence value applies first — both its Expression and its Format String Expression. This has a practical implication: when a high-precedence CG's Format String Expression runs, the lower-precedence CG's column values may still be in the filter context.

This is intentional — it allows the high-precedence CG (e.g., Currency Conversion) to inspect which measure is selected and conditionally apply a format string based on that context.

## Gotchas

- Not all Power BI visuals fully support custom format strings — custom visuals in particular may not honour the Format String Expression (as of 2021; Microsoft announced a fix but it was not resolved by 2021)
- `SELECTEDMEASUREFORMATSTRING()` captures the format string **after** any higher-precedence CG has already applied its format string — be aware of precedence ordering when chaining
- Format strings must be valid DAX format strings (e.g., `"#,0.00"`, `"0.00%"`, `"€#,0.00"`)
- If the measure has no format string defined, `SELECTEDMEASUREFORMATSTRING()` returns blank — always provide a fallback

## Relationship to Other CG Properties

- `multipleOrEmptySelectionExpression` and `noSelectionExpression` (new in 2025) control what happens when 0 or ≥2 CG items are active — these also support a paired `formatStringDefinition`
- Format String Expression applies per-calculation-item and is part of the standard CG item definition
- Both use `SELECTEDMEASUREFORMATSTRING()` to read the base format

## Related

- [[Calculation-Group-Multiple-Selection-Pattern]] — `multipleOrEmptySelectionExpression` with paired `formatStringDefinition`
- [[Calculation-Group-No-Selection-Default-Pattern]] — `noSelectionExpression` with paired `formatStringDefinition`
- [[Controlling-Calculation-Group-Selection]] — overview of all three new selection properties
- [[SELECTEDMEASUREFORMATSTRING]] — function reference
- [[SELECTEDMEASURENAME]] — function reference

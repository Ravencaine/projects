---
created: 2026-08-06
updated: 2026-08-06
source: Controlling Format Strings in Calculation Groups
note_type: pattern
tags: [calculation-groups, dax, format-string, currency-conversion, tabular, SELECTEDMEASUREFORMATSTRING, SELECTEDMEASURENAME]
---

# Currency Conversion Format String Pattern

DAX pattern for using the *Format String Expression* on a Currency Conversion calculation item — conditionally applies currency-specific format strings while preserving the original format for non-currency measures (those containing "#" or "%" in the name).

<!-- one-line description: Format String Expression for a Currency Conversion CG — SELECTEDMEASURENAME to detect currency vs ratio measures, SELECTEDVALUE to pull the right format string from the Currency table -->

## Context

Currency Conversion calculation groups apply exchange rates to monetary measures. The conversion value is controlled by the CG's main Expression; the *Format String Expression* controls how that converted value is displayed — which should differ per currency (e.g., "€#,0.00" vs "£#,0.00").

## Pattern

```dax
// Format String Expression on the "Report Currency" calculation item:

VAR MeasureName =
    SELECTEDVALUE(Metric[Metric], SELECTEDMEASURENAME())

VAR SkipConversion =
    (SEARCH("#", MeasureName, 1, 0) > 0)
        || (SEARCH("%", MeasureName, 1, 0) > 0)

VAR CurrencyFormat =
    SELECTEDVALUE('Currency'[Currency Format], "#,0.00")

RETURN
    IF(
        SkipConversion,
        SELECTEDMEASUREFORMATSTRING(),  // ratio/count measures: keep original format
        CurrencyFormat                  // monetary measures: apply currency format
    )
```

## How It Works

| Variable | Purpose |
|----------|---------|
| `MeasureName` | Gets the current measure name — from Metric CG if active, otherwise from the report measure |
| `SkipConversion` | Detects ratio and count measures (contain "#" or "%") — these should not be converted |
| `CurrencyFormat` | Looks up the format string from the Currency table for the selected currency |
| `RETURN` | If SkipConversion is true → preserve original format; otherwise → use currency format |

## Why SELECTEDVALUE with Default?

```dax
SELECTEDVALUE(Metric[Metric], SELECTEDMEASURENAME())
```

- `SELECTEDVALUE(Metric[Metric])` returns blank if Metric CG is not in the visual or has no selection
- The second argument (`SELECTEDMEASURENAME()`) acts as the fallback — useful when the Metric CG column is not in the visual but another CG or direct measure selection is active

## Precedence Consideration

The Currency Conversion CG typically has **higher precedence** than the Metric CG (e.g., Metric = 10, Currency = 20). This means Currency's Format String Expression runs while Metric's column is still in the filter context — so `SELECTEDVALUE(Metric[Metric])` can read the Metric selection at this point.

If the precedence were reversed, Metric's format would have already been applied and `SELECTEDMEASUREFORMATSTRING()` would return Metric's format, not the raw measure format.

## Related DAX Functions

| Function | Role |
|----------|------|
| `SELECTEDMEASURENAME()` | Gets the name of the measure currently being evaluated |
| `SELECTEDMEASUREFORMATSTRING()` | Gets the format string of the current measure (before or after CG modification) |
| `SELECTEDVALUE(column, default)` | Gets the selected value from the Metric CG, or falls back to the report measure name |
| `SEARCH(substring, text, start, not_found)` | Finds a substring in the measure name |
| `IF(condition, true, false)` | Branches between original format and currency format |

## Related Notes

- [[Format-String-Expression-in-Calculation-Groups]] — concept overview
- [[Calculation-Group-No-Selection-Default-Pattern]] — currency conversion noSelectionExpression pattern (separate property)
- [[Controlling-Calculation-Group-Selection]] — overview of all three selection properties

---
created: 2026-08-06
updated: 2026-08-06
source: Controlling empty or multiple selections in calculation groups
note_type: pattern
tags: [calculation-groups, dax, no-selection, default-behaviour, currency-conversion, tabular]
---

# Calculation Group No-Selection Default Pattern

DAX pattern for `noSelectionExpression` — applies a default calculation when the calculation group column has **no active filters** at all. Used to set "always-on" behaviour unless a specific calculation item is explicitly selected.

<!-- one-line description: noSelectionExpression — apply a default CG item automatically when no CG filters are active, e.g. currency conversion that runs unless explicitly disabled -->

## Core Concept

`noSelectionExpression` fires when the calculation group column has **no filters** applied — not just no items selected, but no filters at all (direct, indirect, or cross-filter). This is distinct from `multipleOrEmptySelectionExpression`, which intercepts when the CG is filtered but produces 0 or ≥2 visible items.

Use case: a "background" calculation that should run automatically on every measure unless the user explicitly overrides it with a specific calculation item.

## Pattern 1 — Currency Conversion (Full Example)

The canonical use case from SQLBI: convert amounts to original currency unless a "No conversion" calculation item is selected.

```dax
// TMDL — add inside calculationGroup block:
calculationGroup
    precedence: 60

    noSelectionExpression = ``
        IF(
            ISCROSSFILTERED('Currency'),
            CALCULATE(
                VAR SelectedCurrency = SELECTEDVALUE('Currency'[Currency Code], "USD")
                VAR MeasureName      = SELECTEDMEASURENAME()
                VAR SkipConversion   = CONTAINSSTRING(MeasureName, "#")
                                         || CONTAINSSTRING(MeasureName, "%")
                RETURN
                    IF(
                        SkipConversion || SelectedCurrency = "USD",
                        SELECTEDMEASURE(),
                        VAR DailyAmount =
                            CALCULATETABLE(
                                SUMMARIZECOLUMNS(
                                    'Date'[Date],
                                    Currency[Currency Code],
                                    "@Amount",       SELECTEDMEASURE(),
                                    "@ExchangeRate", VALUES(ExchangeRate[Exchange])
                                ),
                                ExchangeRate[FromCurrency] = "USD",
                                USERELATIONSHIP(
                                    ExchangeRate[ToCurrency],
                                    'Currency'[Currency Code]
                                )
                            )
                        VAR Result =
                            SUMX(DailyAmount, [@Amount] * [@ExchangeRate])
                        RETURN
                            Result
                    )
            ),
            SELECTEDMEASURE()
        )
    ``

    formatStringDefinition =
        IF(
            ISCROSSFILTERED('Currency'),
            VAR MeasureName      = SELECTEDMEASURENAME()
            VAR SkipConversion   = CONTAINSSTRING(MeasureName, "#")
                                     || CONTAINSSTRING(MeasureName, "%")
            RETURN
                IF(
                    SkipConversion,
                    SELECTEDMEASUREFORMATSTRING(),
                    SELECTEDVALUE(
                        'Currency'[Currency Format],
                        SELECTEDMEASUREFORMATSTRING()
                    )
                ),
            SELECTEDMEASUREFORMATSTRING()
        )

    calculationItem 'No conversion' = SELECTEDMEASURE()
```

**How it works:**
1. When the Currency table is cross-filtered (i.e., sliced by currency), `noSelectionExpression` intercepts and converts all measures to the original currency
2. `ISCROSSFILTERED('Currency')` short-circuits the conversion when Currency is not in the report — avoids unnecessary calculation overhead
3. The "No conversion" calculation item returns `SELECTEDMEASURE()` unchanged — a user can explicitly disable conversion by selecting it
4. `precedence: 60` ensures this CG runs after other CGs with lower precedence

## Pattern 2 — Percentage Formatting Override

Apply a percentage format to ratio measures when no CG item is selected:

```dax
noSelectionExpression = ``
    VAR MeasureName = SELECTEDMEASURENAME()
    RETURN
        IF(
            CONTAINSSTRING(MeasureName, "%"),
            SELECTEDMEASURE(),
            CALCULATE(
                SELECTEDMEASURE(),
                'Percentage CG'[Name] = "As Percentage"
            )
        )
    ``
```

## Pattern 3 — "Always Show Original" Default

For a Time Intelligence CG: when nothing is selected, default to "Original" (no transformation):

```dax
noSelectionExpression = ``
    VAR NoSelectionItem = "Original"
    RETURN
        CALCULATE(
            SELECTEDMEASURE(),
            'Time Intelligence'[Name] = NoSelectionItem
        )
    ``
```

## Key DAX Functions Used

| Function | Purpose |
|----------|---------|
| `ISCROSSFILTERED(column)` | Detect if the table/column is cross-filtered — short-circuit when not needed |
| `SELECTEDMEASURENAME()` | Get the name of the measure currently being evaluated |
| `SELECTEDVALUE(column, default)` | Get the single selected value or a default |
| `CONTAINSSTRING()` | Check measure name for patterns (e.g., "%" for ratio measures) |
| `CALCULATETABLE(SUMMARIZECOLUMNS(...))` | Virtual table: iterate dates × currencies to compute converted amount |
| `USERELATIONSHIP()` | Activate an inactive relationship for the conversion calculation |
| `SUMX()` | Aggregate the converted daily amounts |
| `SELECTEDMEASURE()` | Refer to the currently evaluating measure |
| `SELECTEDMEASUREFORMATSTRING()` | Get the current measure's format string |
| `SELECTEDVALUE(table[column], default)` | Get selected format string or fallback |

## Gotchas

- `noSelectionExpression` ≠ `multipleOrEmptySelectionExpression`. No selection = no filters on the CG column. Empty selection = filter active but returns zero rows. They are intercepted by different properties.
- `ISCROSSFILTERED` optimisation is important: without it, the expression evaluates every measure reference even when the Currency table is not in the report
- The "No conversion" calculation item pattern is powerful: gives users a way to explicitly disable the automatic behaviour
- Requires compatibility level **1605** minimum

## Related

- [[Controlling-Calculation-Group-Selection]] — concept overview and property reference
- [[Calculation-Group-Multiple-Selection-Pattern]] — `multipleOrEmptySelectionExpression` pattern
- [[TMDL-Syntax-Calculation-Group-Properties]] — full TMDL syntax reference
- [[SELECTEDMEASURE]] — SELECTEDMEASURE() usage in calculation groups

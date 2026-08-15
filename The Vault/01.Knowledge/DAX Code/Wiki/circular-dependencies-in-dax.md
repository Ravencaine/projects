---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, error, circular-dependency, measure]
note_type: pattern

---

# Circular Dependencies in DAX

Resolving the error when two or more measures reference each other in a loop.

## Error Message

"Circular dependency detected: [Measure A] depends on [Measure B] which depends on [Measure A]"

## Common Causes

1. Two measures that reference each other's output
2. A calculated column referencing a measure that references that column
3. Accidental bi-directional dependency through calculated columns

## Resolution

```dax
-- Wrong: circular
-- [Profit] = [Revenue] - [Cost]
-- [Cost] = [Price] * [Quantity] - [Profit]  -- CIRCULAR

-- Right: resolve dependencies one level up
-- [Cost] = [Price] * [Quantity] - [Profit]
-- [Profit] = [Revenue] - [Cost]  -- works
```

## Prevention

- Always reference base columns, not aggregate measures
- Separate data (base calculations) from display (ratios, percentages)

---

## Deckler Extension — CALCULATE in Calculated Columns (ch16)

Circular dependencies also occur in **calculated columns**, especially with `CALCULATE`. The error is triggered by the interplay between CALCULATE's context transition and DAX's dependency ordering:

**Produces a circular dependency error:**
```dax
Val1 = CALCULATE( MAX( 'Table'[Value] ), 'Table'[Index] > 1 )
Val2 = CALCULATE( MAX( 'Table'[Value] ), 'Table'[Index] > 1 )
-- Error: Circular dependency detected (creating the second column)
```

**Workaround 1 — Replace CALCULATE with FILTER + MAXX:**
```dax
Val3 = MAXX(
    FILTER(
        'Table',
        [Index] > 1 && [Index] = EARLIER( 'Table'[Index] )
    ),
    [Value]
)
-- No error
```

**Workaround 2 — Wrap the filter with ALL:**
```dax
Val5 = CALCULATE(
    MAX( 'Table'[Value] ),
    ALL( 'Table' ),
    'Table'[Index] > 1
)
-- No error
```

**Rule:** Avoid `CALCULATE` in calculated columns unless you know the filter argument won't cause context transition loops. `ALL()` strips row context and prevents the cycle.

**Source:** DAX for Humans (Greg Deckler, ch16) — dax4humans_ch16_circular.txt

## Related

- [[handling-errors-in-dax]]
- [[no-calculate-dax-pattern]]

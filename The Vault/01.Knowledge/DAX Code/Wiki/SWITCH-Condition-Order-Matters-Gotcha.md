---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: gotcha
tags: [dax, isinscope, isatlevel, switch, condition-order, gotcha, conditional-formatting, level-detection]
---

# SWITCH Condition Order Gotcha

**Type:** Gotcha · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

When ISINSCOPE or ISATLEVEL returns TRUE for **all ancestor levels simultaneously**, putting the wrong condition first in SWITCH silently produces wrong results — no error, no warning.

## What happens

At the month level, ISINSCOPE returns TRUE for:
- `ISINSCOPE('Date'[Year Month])` → TRUE ✓
- `ISINSCOPE('Date'[Year Quarter])` → TRUE ✓
- `ISINSCOPE('Date'[Year])` → TRUE ✓

If the SWITCH tests year first, the year branch fires for every month cell too — producing the wrong color for every non-grand-total cell.

## Example of wrong order

```dax
-- WRONG: year branch fires for month cells too
SWITCH(
    TRUE,
    ISINSCOPE('Date'[Year]),              -- fires at MONTH level too
        <year-level rule>,
    ISINSCOPE('Date'[Year Quarter]),
        <quarter-level rule>,
    ISINSCOPE('Date'[Year Month])
        <month-level rule>
)
```

## Correct order: most specific first

```dax
-- CORRECT: most specific wins at each level
SWITCH(
    TRUE,
    ISINSCOPE('Date'[Year Month]) || ISINSCOPE('Date'[Year Month Short]),
        <month-level rule>,              -- fires first at month level
    ISINSCOPE('Date'[Year Quarter]),
        <quarter-level rule>,            -- fires first at quarter level
    ISINSCOPE('Date'[Year])
        <year-level rule>                -- fires only at year level
)
```

## Why this is silent

DAX evaluates the SWITCH without error and returns a color — just not the right one. The cells get formatted, but incorrectly. The only way to catch it is visual inspection of the output.

## Mitigation

Always test all three levels in a matrix before assuming correctness. Add a comment at the top of each branch indicating its level.

## Related

- [[SWITCH-Specificity-Ordering]] — the pattern that prevents this gotcha
- [[ISINSCOPE-Per-Level-Conditional-Formatting]] — correctly ordered example

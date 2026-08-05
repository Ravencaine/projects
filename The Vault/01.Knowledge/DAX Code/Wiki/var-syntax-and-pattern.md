---
created: 2026-08-01
updated: 2026-08-02
source: "Stop Repeating Yourself in DAX - The Power of Variables (VAR).md"
note_type: atomic
tags: [dax, var, return, syntax, pattern, beginner]
---

# VAR / RETURN: Syntax and Pattern

`VAR` stores an expression's result in a named variable; `RETURN` delivers the final result using those variables.

## Syntax

```dax
VAR <variable_name> = <expression>
RETURN
    <final_expression>
```

## Rules

- Multiple `VAR` blocks can be chained (each on its own line)
- Variables are evaluated once, in order, before `RETURN` executes
- A variable can reference previously defined variables
- Variable scope is **measure-local**: it does not persist outside the measure
- A variable named the same as a measure does **not** shadow the measure

## Basic Scalar Example

```dax
Profit Margin % =
VAR Revenue = SUM ( Sales[Revenue] )
VAR Cost    = SUM ( Sales[Cost] )
VAR Profit  = Revenue - Cost
RETURN
DIVIDE ( Profit, Revenue )
```

## Returning Multiple Values

A single `RETURN` can only return one value — but it can be a table or a concatenated string:

```dax
Performance Summary =
VAR Actual = SUM ( Sales[Revenue] )
VAR Target  = SUM ( Targets[TargetAmount] )
VAR LY      = CALCULATE ( SUM ( Sales[Revenue] ), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
VAR Growth  = DIVIDE ( Actual - LY, LY )
RETURN
FORMAT ( Actual, "$#,##0" ) & " | " &
FORMAT ( Growth, "0%" )
```

## Named Variables vs Inline Literals

**Good:** named variables make intent clear
```dax
VAR LY = CALCULATE ( SUM ( Sales[Revenue] ), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
```

**Bad:** inline literals require parsing
```dax
DIVIDE ( Actual - CALCULATE ( SUM(Sales[Revenue]), SAMEPERIODLASTYEAR('Date'[Date]) ), LY )
```

## Variable Naming Conventions

Use descriptive names that describe the **value**, not the calculation:

```
Good:  Revenue, Cost, LYRevenue, TargetAchievement
Bad:   Var1, Result2, Temp3
```

## Self-Documenting Pattern

```dax
Revenue vs Target % =
VAR Revenue = [Total Revenue]
VAR Target  = [Total Target]
VAR Gap     = Revenue - Target
RETURN
DIVIDE ( Gap, Target )
```

The variable names make the logic readable without comments.

## Related

- [[var-performance-benefit]] — why VAR improves performance
- [[var-table-variables]] — VAR with table expressions
- [[var-calculate-filter-composition]] — VAR + CALCULATE
- [[var-anti-patterns-limits]] — when not to use VAR

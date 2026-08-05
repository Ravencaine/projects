---
created: 2026-07-30
updated: 2026-08-02
source: "dax4humans_ch16_calculate_trouble.txt"
note_type: gotcha
tags: [calculate, keepfilters, nested-calculate, filter-context, arbitrary]
---

# CALCULATE Nested KEEPFILTERS — Arbitrary Override Rules

Nested CALCULATE functions follow counterintuitive precedence rules. Inner CALCULATE's filter overrides outer CALCULATE's filter, and KEEPFILTERS changes this to intersection — but only for the specific filter it's applied to.

## Expected Behaviour

You might expect one of:
1. Two CALCULATE filter arguments conflict and return BLANK (mutual exclusion)
2. Outer CALCULATE's filter replaces inner CALCULATE's filter (overwrite)

## Actual Behaviour

Neither. CALCULATE has a built-in rule: **the innermost CALCULATE's filter always wins**, regardless of nesting depth. Adding KEEPFILTERS changes this to an **intersection** of the two filters, but only for the KEEPFILTERS-wrapped clause.

```dax
Days in February ? =
  CALCULATE(
    CALCULATE(
      COUNTROWS( 'Dates1' ),
      'Dates1'[Month] = "February"
    ),
    'Dates1'[Month] = "January"      -- outer CALCULATE filter
  )
```

Returns **85** (days in February), not blank. The innermost CALCULATE's `"February"` filter overrides the outer `"January"` filter.

## Why It Happens

CALCULATE evaluates its arguments in a specific internal order that is not exposed to the user. The innermost CALCULATE's filter expression is evaluated last and takes precedence. This is an internally-defined rule, not documented as a general principle.

Adding KEEPFILTERS modifies this:

```dax
Days in February ?? =
  CALCULATE(
    CALCULATE(
      COUNTROWS( 'Dates1' ),
      KEEPFILTERS( 'Dates1'[Month] = "January" | 'Dates1'[Month] = "February" )
    ),
    'Dates1'[Month] = "April" | 'Dates1'[Month] = "February"
  )
```

Returns **85** again. KEEPFILTERS changes the outer filter to an **intersection** with the inner filter. Since `"February"` is the only common value between the two filter clauses, the result is still February rows only.

## Filter Modifier Functions (the "mini-language")

DAX has 7 filter modifier functions usable only inside CALCULATE:

| Function | Behaviour |
|----------|-----------|
| `REMOVEFILTERS` | Removes all filters |
| `ALL` | Removes filters, returns all values |
| `ALLEXCEPT` | Removes filters except specified columns |
| `ALLNOBLANKROW` | Removes filters, keeps blank row |
| `KEEPFILTERS` | Intersects with existing filter instead of replacing |
| `USERELATIONSHIP` | Activates an inactive relationship |
| `CROSSFILTER` | Changes cross-filter direction |

Their interactions when nested are combinatorial and largely undocumented.

## How to Handle It

1. **Avoid deeply nested CALCULATE**: if you need to layer logic, use variables or separate measures composed with `+` or `DIVIDE`.
2. **Isolate the filter logic**: put each filter in its own CALCULATE at the same level, then combine results.
3. **Use KEEPFILTERS deliberately**: only when you specifically want intersection behaviour.
4. **Debug with EVALUATEANDLOG**: log intermediate filter context to understand what CALCULATE is actually applying.

```dax
-- Instead of nested CALCULATE, use variables at the same level:
VAR __FebCount  = CALCULATE(COUNTROWS('Dates'), 'Dates'[Month]="February")
VAR __JanFilter = CALCULATE(__FebCount, 'Dates'[Month]="January")
-- Result depends on what you actually need — write it explicitly
```

## Related

- [[calcuate-the-calculate-counterculture]] — why to avoid complex CALCULATE nesting
- [[calculate-internal-context-transition]] — context transition inside CALCULATE
- [[filter]] — intersection vs. replace semantics

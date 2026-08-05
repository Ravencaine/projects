---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: snippet
tags: [dax, user-defined-function, testing, validation, measure, calculated-column]
---

# Test DAX UDF from Multiple Calling Contexts

Minimum test cases to validate a UDF before trusting it in production. The VAL/EXPR class of bug only surfaces when the calling context changes — so test from multiple contexts before production does.

## Test Cases

### Test 1 — As a Measure (Filter Context)

```dax
MEASURE Sales[Test_UDF_Measure] =
    Finance.NetRevenue( SUM(Sales[Amount]) )
```

Place on a card visual filtered by Product Category, Year, and Region.

### Test 2 — As a Calculated Column (Row Context + Context Transition)

```dax
-- Calculated column on Sales table:
Column =
    Finance.NetRevenue( Sales[Amount] )
```

Add the column to a table visual alongside other measures. Compare totals to Test 1.

### Test 3 — As an Iterator (SUMX)

```dax
MEASURE Sales[Test_UDF_Iterator] =
    SUMX(
        Sales,
        Finance.NetRevenue( Sales[Amount] )
    )
```

Compare to Test 1. If they differ, the function has a context sensitivity issue.

### Test 4 — As a Visual Calculation (if applicable)

```dax
-- In a visual calculation:
RunningTotal = RUNNINGSUM( Finance.NetRevenue( SUM(Sales[Amount]) ) )
```

## Validation Checklist

| Test | Expected Result | Red Flag |
|------|-----------------|----------|
| Measure vs Calculated Column | Same total | Different totals → VAL/EXPR issue |
| Measure vs Iterator | Same total | Different totals → context handling issue |
| Filtered vs Unfiltered | Appropriate ratio | Unchanged → function ignores context |

## When to Flag for Review

If any red flag fires:
1. Review parameter evaluation modes (VAL vs EXPR)
2. Check whether CALCULATE inside the function body is changing context unexpectedly
3. Add explicit context handling before declaring the function production-ready

See [[val-vs-expr-parameter-evaluation]] for the root cause of most context-class bugs.

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[val-vs-expr-parameter-evaluation]] — gotcha
- [[dax-udf-adoption-workflow]] — workflow

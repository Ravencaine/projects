---
created: 2026-08-01
updated: 2026-08-02
source: "The DAX concepts that actually save you time in Power BI.md"
note_type: atomic
tags: [dax, mistakes, beginner, fundamentals]
---

# DAX Common Mistakes: The Ones That Still Show Up

The mistakes Daniel Olatunji sees most often — and how to avoid them.

## Mistake 1: Calculated Columns for Things That Should Be Measures

The biggest model-bloater. Calculated columns:
- Store values physically → consumes memory
- Don't recalculate on filter interaction → wrong tool for dynamic values

**Fix:** If it changes when someone clicks a slicer → measure.

## Mistake 2: Repeated Sub-Calculations Without VAR

Writing the same sub-calculation three or four times inside one formula:

```c
// BAD: SAMEPERIODLASTYEAR evaluated 2× in one formula
YoY Growth % =
DIVIDE(
    [Total Sales] - CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date])),
    CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))
)
```

**Fix:** Use VAR — calculated once, reused cleanly.

## Mistake 3: Nine Nested IFs Instead of SWITCH

```c
// BAD: unreadable, hard to debug
Status =
IF(Score >= 90, "A",
IF(Score >= 80, "B",
IF(Score >= 70, "C",
IF(Score >= 60, "D", "F"))))

// GOOD: SWITCH with TRUE()
Status =
SWITCH(
    TRUE(),
    Score >= 90, "A",
    Score >= 80, "B",
    Score >= 70, "C",
    Score >= 60, "D",
    "F"
)
```

## Mistake 4: Forgetting DIVIDE

```c
// BAD: breaks when denominator = 0
Margin = [Profit] / [Revenue]

// GOOD: returns blank or 0 when Revenue = 0
Margin = DIVIDE([Profit], [Revenue], BLANK())
```

One empty category can crash an entire visual.

## Mistake 5: No Date Table

Time intelligence functions (`SAMEPERIODLASTYEAR`, `DATESYTD`, `TOTALYTD`) **only work correctly against a marked, continuous date table**.

Without it:
- `SAMEPERIODLASTYEAR` gives wrong or blank results
- `TOTALYTD` accumulates incorrectly
- Everything downstream behaves unexpectedly

**Requirements for a date table:**
- One row per date (continuous, no gaps)
- Date column marked as a date table
- At least the full range of dates in your data

## Checklist

- ☐ Calculated column? → confirm it needs a fixed stored value
- ☐ Repeated sub-calculation? → extract to VAR
- ☐ Nested IF × 3+? → convert to SWITCH
- ☐ Division without DIVIDE? → replace `/` with `DIVIDE(..., BLANK())`
- ☐ Time intelligence without date table? → create and mark date table first

## Related

- [[measures-vs-calculated-columns]] — Mistake 1
- [[var-dax-reading-complexity]] — Mistake 2
- [[dax-functions-shortlist]] — SWITCH (Mistake 3), DIVIDE (Mistake 4)

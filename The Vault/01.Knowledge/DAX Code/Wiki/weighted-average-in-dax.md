---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "statistics", "weighted-average", "averagex"]
note_type: pattern

---

# Weighted Average in DAX

Calculating a weighted average where each value contributes proportionally to its weight.

## Purpose

Simple AVERAGE treats all rows equally. Weighted average assigns importance to each row via a weight column.

## Structure

```dax
Weighted Average :=
DIVIDE(
    SUMX( 'Table', 'Table'[Value] * 'Table'[Weight] ),
    SUMX( 'Table', 'Table'[Weight] )
)
```

## Examples

```dax
-- Average score weighted by hours studied
Avg Score =
DIVIDE(
    SUMX( 'StudentScores', 'StudentScores'[Score] * 'StudentScores'[Hours] ),
    SUM( 'StudentScores'[Hours] )
)

-- Weighted profit margin by sales amount
Weighted Margin =
DIVIDE(
    SUMX( 'Sales', 'Sales'[Profit] ),
    SUM( 'Sales'[SalesAmount] )
)
```

## Notes

- Use `DIVIDE()` instead of `/` to handle division by zero
- Weight can be any numeric column — quantity, hours, sales amount, etc.
- Can be filtered contextually (e.g., weighted average per product category)

## Related

- [[no-calculate-dax-pattern]]
- [[regression-analysis-in-dax]]

---

## Deckler Extension — No CALCULATE vs Quick Measure (ch5)

The Power BI Quick Measure "Weighted average by category" produces an unnecessarily complex formula:

```dax
Grade weighted by Weight per Item =
VAR __CATEGORY_VALUES = VALUES('Grades'[Item])
RETURN
    DIVIDE(
        SUMX(
            KEEPFILTERS(__CATEGORY_VALUES),
            CALCULATE(SUM('Grades'[Grade]) * SUM('Grades'[Weight]))
        ),
        SUMX(
            KEEPFILTERS(__CATEGORY_VALUES),
            CALCULATE(SUM('Grades'[Weight]))
        )
    )
```

The No CALCULATE approach is dramatically simpler:

```dax
Weighted average =
    VAR __Numerator   = SUMX( 'Grades', [Grade] * [Weight] )
    VAR __Denominator = SUMX( 'Grades', [Weight] )
    VAR __Result      = DIVIDE( __Numerator, __Denominator, 0 )
    RETURN __Result
```

**Why it works:** SUMX iterates row-by-row over `'Grades'`, multiplies each row's Grade by its Weight, then sums — no CALCULATE needed because row context is already established.

**Deckler's point:** This comparison is a canonical example of the "No CALCULATE" philosophy in action. The simpler formula is easier to read, debug, and extend.

**Source:** DAX for Humans (Greg Deckler, ch5) — dax4humans_ch5_weighted_avg.txt

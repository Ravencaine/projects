---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: function
tags: [safe-division, division, null-handling, division-by-zero]
related: [IFERROR, CALCULATE, SUM]
---

# DIVIDE

Performs division and returns an alternate result if the denominator is zero or blank. The preferred DAX function for safe division.

## Signature

```dax
DIVIDE(<numerator>, <denominator>[, <alternateResult>])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `numerator` | Scalar | The dividend |
| `denominator` | Scalar | The divisor |
| `alternateResult` | Scalar (optional) | Value to return when `denominator` = 0 or BLANK (default: BLANK) |

## Returns

The result of `numerator / denominator`, or `alternateResult` if `denominator` is 0 or BLANK.

## Examples

**Safe division for rate metrics:**
```dax
Vacancy Rate =
    DIVIDE(
        SUM('Positions'[Vacancies]),
        SUM('Positions'[Payroll Employees]),
        0
    )
```

**Percentage with zero guard:**
```dax
Completion % =
    DIVIDE(
        [Completed Steps],
        [Total Steps],
        BLANK()
    )
```

**Chained in a calculation:**
```dax
Conversion Rate =
    DIVIDE(
        [Orders],
        [Visitors],
        0
    )
```

## Notes

- Use `DIVIDE` instead of the `/` operator in DAX. The `/` operator returns `INFINITY` when dividing by zero, which propagates through aggregations and can corrupt visuals.
- `DIVIDE` with no `alternateResult` returns `BLANK()` — this causes the visual to show blank instead of an error, which is usually the desired behavior.
- Pass `0` as `alternateResult` when you want to show `0` instead of blank for new categories with no denominator.
- Behind the scenes, `DIVIDE` is optimised for evaluation — it uses a single storage engine query, making it faster than `IFERROR(<a>/<b>, <alt>)`.
- In Bittar's articles, `DIVIDE` appears in rate calculations (vacancy rates, completion percentages).

## Related

- [[IFERROR]] — general-purpose error catching (less efficient than DIVIDE for division)
- [[CALCULATE]] — wrap DIVIDE in CALCULATE to modify filter context
- [[SUM]] — aggregate numerators and denominators before dividing

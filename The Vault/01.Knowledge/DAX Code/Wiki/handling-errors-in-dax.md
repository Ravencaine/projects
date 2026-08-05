---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "error-handling", "iferror", "try", "validation"]
note_type: pattern

---

# Handling Errors in DAX

Managing errors gracefully in DAX measures and calculated columns.

## IFERROR Pattern

```dax
Safe Ratio :=
IFERROR(
    DIVIDE( [Revenue], [Units] ),
    BLANK()
)
```

## Validation Before Calculation

```dax
Validated Sales :=
IF(
    AND( [Units] > 0, [Price] > 0 ),
    [Units] * [Price],
    BLANK()
)
```

## Notes

- `IFERROR(value, fallback)` catches any error and returns the fallback
- Prefer explicit validation (IF with conditions) over catching errors after the fact
- `ISERROR()` and `ERROR()` exist but are rarely needed in measures

## Related

- [[DIVIDE]]
- [[no-calculate-dax-pattern]]

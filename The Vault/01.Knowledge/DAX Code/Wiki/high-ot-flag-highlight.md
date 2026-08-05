---
created: 2026-08-04
updated: 2026-08-05
note_type: atomic
tags: [dax, overtime, highlight, flag, employee-data]
source: unknown

---

# High OT Flag for Highlight (DAX)

A measure that returns a binary or categorical flag indicating whether an employee has exceeded overtime thresholds — used for conditional formatting, highlighting, and alert logic.

## Basic Binary Flag

```dax
High OT Flag =
IF(
    [Overtime Hours] > [OT Threshold],
    1, 0
)
```

## Threshold from a Parameter Table

```dax
High OT Flag :=
VAR Threshold = SELECTEDVALUE('Parameters'[OT Threshold], 40)
RETURN
    IF(
        [Overtime Hours] > Threshold,
        "🔴 High OT",
        "✅ Normal"
    )
```

## Percentage of Standard Hours

```dax
OT % of Standard Hours :=
VAR StandardHours = [Standard Weekly Hours]
VAR OTHours = [Overtime Hours]
RETURN
    DIVIDE(OTHours, StandardHours)
```

## Conditional Formatting Background Color

Apply via **Field → Cell Elements → Background Color**:

```dax
OT Highlight Color :=
SWITCH(
    TRUE(),
    [OT % of Standard Hours] > 0.5, "#FF6B6B",  -- >50% OT: red
    [OT % of Standard Hours] > 0.25, "#FFD93D",  -- >25% OT: amber
    TRUE, "#6BCB77"                              -- normal: green
)
```

## Related

- [[high-ot-employees-last-7-days]] — identifying high-OT employees over a period
- [[graph-title]] — using OT flags in visual titles

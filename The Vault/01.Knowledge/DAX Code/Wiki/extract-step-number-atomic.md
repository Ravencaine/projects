---
created: 2026-08-02
source: The Same-Day Trap: Calculating "Days in Status" in Power BI
note_type: atomic
tags: [dax, atomic, value, left, find, extract, step, number, status]
---

# Extract Step Number from Status Name: VALUE(LEFT(FIND(".", status)-1))

Converts the numeric prefix of a status name (e.g., "2. Discussion") into a comparable integer for use as a sort key in date-tie scenarios.

```dax
Step_Number =
IFERROR(
    VALUE(
        LEFT(
            'opportunity_status'[status],
            FIND(".", 'opportunity_status'[status]) - 1
        )
    ),
    0  -- fallback: no period or blank status
)
```

**How it works:**
1. `FIND(".", status)` → position of the period (e.g., "2. Discussion" → 2)
2. `LEFT(status, pos - 1)` → extracts the substring before the period ("2")
3. `VALUE(...)` → converts to integer (2) for numeric comparison
4. `IFERROR(..., 0)` → handles statuses without a numeric prefix

**Use case:** Pair with `same-day-status-trap-min-date.md` to break ties when multiple status rows share the same date. Compare `Step_Number > _currentStep` as the secondary sort key.

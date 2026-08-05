---
created: 2026-08-02
updated: 2026-08-03
source: The Same-Day Trap: Calculating "Days in Status" in Power BI
note_type: pattern
tags: [dax, pattern, days-in-status, status-duration, minx, filter, datediff, same-day, tiebreaker]
---

# Days in Status: MINX + FILTER + OR(Date Future, SameDate + Step Higher) Tie-Breaker

Calculates how many days each status row represents, correctly handling same-day status transitions using a step number as a chronological tie-breaker.

**Calculated column:**
```dax
days_in_status =
VAR _currentID    = sheet1[opportunity_id]
VAR _currentDate  = sheet1[start_date]
VAR _currentStep  = sheet1[Step_Number]

-- Virtual table: all future statuses for this ID
VAR _futureSteps =
    FILTER(
        sheet1,
        sheet1[opportunity_id] = _currentID && (
            -- Date strictly in the future
            sheet1[start_date] > _currentDate ||
            -- OR same date, but step number is higher (tie-breaker)
            (sheet1[start_date] = _currentDate && sheet1[Step_Number] > _currentStep)
        )
    )

VAR _nextDate = MINX(_futureSteps, sheet1[start_date])

RETURN
    IF(
        ISBLANK(_nextDate),
        DATEDIFF(_currentDate, TODAY(), DAY),      -- open/latest status
        DATEDIFF(_currentDate, _nextDate, DAY)      -- closed status
    )
```

**Logic walkthrough (same-day transition on March 16):**

| Row | Status | Step | Date | Next Date found | Days |
|-----|--------|------|------|----------------|------|
| "2. Discussion" | 2 | Mar 16 | Mar 16 (step 7 > 2) | 0 |
| "7. Did not proceed" | 7 | Mar 16 | Jul 14 (next date) | 120 |

**Key insight:** The `OR(future_date, same_date AND step_higher)` clause is the tie-breaker — it tells DAX which row is chronologically first on the same day by comparing the embedded step number.

**Active status behavior:** `TODAY()` for open rows means Days in Status auto-increments on each refresh — ideal for live dashboards.

---
created: 2026-08-02
updated: 2026-08-02
source: The Same-Day Trap: Calculating "Days in Status" in Power BI
note_type: snippet
tags: [dax, snippet, overdue, flag, status, latest, days, threshold, filter]
---

# Overdue Flag: `_isLatestStatus + IN + days_in_status > N`

Flags rows that are the latest status for their ID, in an active status, and have exceeded a day threshold — for highlighting stalled opportunities.

```dax
Overdue_in_Status =
VAR _currentID    = sheet1[opportunity_id]
VAR _currentDate   = sheet1[start_date]
VAR _currentStep   = sheet1[Step_Number]
VAR _days          = 30

-- Reuse same future-steps logic from days_in_status
VAR _futureSteps =
    FILTER(
        sheet1,
        sheet1[opportunity_id] = _currentID && (
            sheet1[start_date] > _currentDate ||
            (sheet1[start_date] = _currentDate && sheet1[Step_Number] > _currentStep)
        )
    )

VAR _nextDate       = MINX(_futureSteps, sheet1[start_date])
VAR _isLatestStatus = ISBLANK(_nextDate)

VAR _activeStatuses = {
    "1. Preparation",
    "2. Discussion with Prospect",
    "3. Submitted",
    "4. Accepted"
}

RETURN
    IF(
        _isLatestStatus = TRUE() &&
        sheet1[status] IN _activeStatuses &&
        sheet1[days_in_status] > _days,
        TRUE(),
        FALSE()
    )
```

**Three conditions all must be TRUE:**
1. `_isLatestStatus` — no future step exists for this ID → this is the current status
2. `status IN _activeStatuses` — only flag specific statuses as "overdue-eligible"
3. `days_in_status > _days` — threshold exceeded

**Design:** Use in conditional formatting (background or text color) on the status column or a dedicated alert icon.

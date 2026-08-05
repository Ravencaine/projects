---
created: 2026-08-02
updated: 2026-08-03
source: The Same-Day Trap: Calculating "Days in Status" in Power BI
note_type: gotcha
tags: [dax, gotcha, same-day, date, status, datediff, timestamp]
---

# Same-Day Status Trap: MIN(Date) > CurrentDate Fails on Identical Dates

When multiple status changes occur on the same date, a naive `MIN(date) > current_date` filter silently returns incorrect results — it cannot establish chronological order between identical timestamps.

**Broken pattern:**
```dax
_nextDate = MINX(
    FILTER(sheet1,
        sheet1[opportunity_id] = _currentID &&
        sheet1[start_date] > _currentDate   -- silently ignores same-day transitions
    ),
    sheet1[start_date]
)
```

**Root cause:** Identical dates are treated as simultaneous events. DAX has no tie-breaker to determine which status came first.

**Symptom:** Opportunities that move status on the same day (e.g., "2. Discussion" → "7. Did not proceed" on March 16) show incorrect Days in Status — often zero or wildly inflated.

**Fix:** Add a secondary sort key that resolves ties. See `days-in-status-step-tiebreaker.md` and `extract-step-number-atomic.md`.

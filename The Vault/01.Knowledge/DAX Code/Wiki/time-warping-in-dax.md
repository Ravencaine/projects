---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "time", "warp", "projection", "scenario"]
note_type: pattern

---

# Time Warping in DAX

Projecting a measure onto a different time axis — for example, mapping all events to "Day 1, Day 2, Day N" of their lifecycle rather than calendar dates.

## Purpose

When events start at different times, calendar-aligned reporting produces messy, sparse visuals. Time warping normalizes each event's lifecycle to a common starting point.

## Pattern

```dax
Time Warped Sales :=
VAR __EventDate = [EventStartDate]
VAR __CalendarDate = MAX( 'Dates'[Date] )
VAR __DayNumber = DATEDIFF( __EventDate, __CalendarDate, DAY ) + 1
RETURN
IF( __DayNumber >= 1, [Sales], BLANK() )
```

## Use Case: Product Launch Analysis

```dax
Days Since Launch :=
DATEDIFF( [LaunchDate], MAX( 'Dates'[Date] ), DAY ) + 1

Sales Normalized :=
SUMX(
    FILTER(
        'Products',
        [Days Since Launch] >= 1
    ),
    [Sales]
)
```

## Notes

- Useful for product launches, marketing campaigns, employee onboarding cohorts
- Always filter to `DayNumber >= 1` to exclude pre-event dates

## Related

- [[no-calculate-time-intelligence-pattern]]
- [[offset-based-date-calculations]]
- [[rollup]]

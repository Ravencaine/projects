---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "streak", "consecutive", "sequence", "iteration"]
note_type: pattern

---

# Streak Detection in DAX

Identifying consecutive runs of TRUE values or repeating patterns in a sequence.

## Purpose

Detect streaks of consecutive days with sales, login streaks, winning streaks, etc.

## Pattern: Current Streak Length

```dax
Current Streak :=
VAR __CurrentDate = MAX( 'Dates'[Date] )
VAR __ConsecutiveDays =
    SUMX(
        GENERATESERIES( 0, 365 ),
        VAR __TestDate = __CurrentDate - [Value]
        VAR __HasValue = NOT( ISBLANK( CALCULATE( [Sales], 'Dates'[Date] = __TestDate ) ) )
        RETURN
        IF( __HasValue, 1, BLANK() )
    )
RETURN
__ConsecutiveDays
```

## Pattern: Longest Streak

```dax
Longest Streak :=
MAXX(
    SUMMARIZECOLUMNS(
        'Dates',
        "Streak", [Current Streak]
    ),
    [Streak]
)
```

## Notes

- Performance-critical: limit the maximum streak search length with GENERATESERIES
- For binary flags (did event happen or not), use a 1/0 column
- Combine with RANKX for nth-largest streak

## Two Approaches to Streak Detection

### Approach 1: GENERATESERIES (backward-looking)

The pattern above uses `GENERATESERIES` to look backward from the current date, testing each prior day for a value. Best when:
- You want the **current streak** (days ending at today)
- You have a maximum known streak length to bound the search
- Performance matters — GENERATESERIES has a fixed iteration count

### Approach 2: Gaps and Islands / Rank Subtraction (forward-looking)

Use the [[dax-gaps-and-islands-pattern]] when:
- You want the **longest streak ever** (not current streak)
- Gaps and multiple islands exist in the data
- You need **all streaks per entity** (not just one per entity)
- Duplicate rows exist per entity-date pair

The Gaps and Islands approach is:
- More general: handles multiple islands and gaps of any length
- More complex: requires nested SUMMARIZE + RANKX + EARLIER
- Slower: no bounded iteration, scans all dates per entity

## DAX Gaps and Islands Pattern (Nayan, 2025)

The complete six-VAR implementation for longest streak per entity, handling duplicate rows and multiple islands:

```dax
MaxConsecutiveDays =
VAR _DistinctDates =
    ADDCOLUMNS(
        SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
        "Rank", RANKX(
            FILTER(
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
            ),
            LessonStreaks[date],
            ,
            ASC
        ),
        "Island", LessonStreaks[date] - RANKX(
            FILTER(
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
            ),
            LessonStreaks[date],
            ,
            ASC
        )
    )

VAR _Streaks =
    ADDCOLUMNS(
        SUMMARIZE(_DistinctDates, LessonStreaks[user_id], [Island]),
        "StreakLength", COUNTROWS(
            FILTER(_DistinctDates,
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id]) &&
                [Island] = EARLIER([Island])
            )
        )
    )

VAR _result = MAXX(_Streaks, [StreakLength])
RETURN
_result
```

Key steps:
1. `SUMMARIZE` deduplicates duplicate user-date pairs
2. `RANKX` assigns chronological rank per user
3. `date − Rank` produces the island grouping key
4. `SUMMARIZE` groups by user + island key
5. `COUNTROWS` counts days per island
6. `MAXX` returns the longest streak

See [[dax-gaps-and-islands-pattern]] for the full pattern with walkthrough and performance notes.

## Related

- [[dax-index-pattern-deckler]]
- [[dax-gaps-and-islands-pattern]] — full six-VAR pattern (Nayan, 2025)
- [[gaps-and-islands-theory]] — conceptual foundation: islands, gaps, per-user worked example
- [[rank-subtraction-grouping-trick]] — the key insight: date − RANKX(date) = island ID
- [[dax-vs-generateseries-streak-comparison]] — side-by-side: when to use each approach

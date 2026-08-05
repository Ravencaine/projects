---
created: 2026-08-01
updated: 2026-08-02
source: "Gaps and Islands Solving Consecutive Active Days in Power BI.md"
note_type: pattern
tags: [dax, pattern, gaps-and-islands, streak-detection, rankx, summarize]
---

# DAX Gaps and Islands Pattern

Detect the longest consecutive run of a condition per entity — e.g., longest streak of active days per user, longest winning streak per salesperson, longest consecutive login run per device.

## Purpose

Given a fact table with event rows (possibly duplicate per entity-date), return the maximum count of consecutive rows where a condition is true for each entity. Handles gaps of any length and multiple islands per entity.

## Components

- `SUMMARIZE` — deduplicate to one row per entity-date (handles duplicate events per day)
- `ADDCOLUMNS` — add Rank and Island columns
- `RANKX` — chronological rank per entity (partitioned by entity, ordered ASC by date)
- Date subtraction — creates the island grouping key
- `FILTER` + `COUNTROWS` — counts rows per island
- `MAXX` — returns the maximum streak length

## Structure

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

## Step-by-Step Walkthrough

1. **Deduplicate**: `SUMMARIZE` collapses multiple lesson completions per user per day into one row
2. **Rank**: `RANKX` assigns 1, 2, 3… to each distinct date per user (chronological)
3. **Island key**: subtract Rank from Date: consecutive dates keep the same result; a gap breaks it
4. **Group by island**: `SUMMARIZE` groups by user + island key
5. **Count streak**: `COUNTROWS` + `FILTER` counts days in each island
6. **Return max**: `MAXX` picks the largest streak length

## Usage

- Place this as a measure in a table visual grouped by user_id to produce a leaderboard
- Works in card visuals when sliced by a single user
- For Top N leaderboard: wrap in `RANKX(ALL(user_id), [MaxConsecutiveDays])`

## Performance Considerations

- The nested `SUMMARIZE` inside `RANKX` is expensive on large tables — the inner SUMMARIZE runs once per outer row
- On datasets with millions of rows, consider pre-computing the island key as a calculated column in the fact table
- Alternative for large datasets: use `GENERATESERIES` approach (see [[streak-detection-in-dax]]) which can be bounded

## Related

- [[gaps-and-islands-theory]] — conceptual foundation
- [[rank-subtraction-grouping-trick]] — the key insight that powers this pattern
- [[streak-detection-in-dax]] — compares GENERATESERIES (bounded, faster) vs Gaps and Islands (unbounded, more general)
- [[earlier]] — EARLIER function used inside RANKX to partition by entity
- [[summarizecolumns]] — alternative to SUMMARIZE for deduplication

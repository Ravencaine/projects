---
created: 2026-08-01
updated: 2026-08-02
source: "Gaps and Islands Solving Consecutive Active Days in Power BI.md"
source_url: "https://medium.com/microsoft-power-bi/gaps-and-islands-solving-consecutive-active-days-in-power-bi-f409b3679559"
note_type: source
tags: [power-bi, dax, gaps-and-islands, streak-detection, maven-analytics]
---

# Gaps and Islands: Solving Consecutive Active Days in Power BI

> **Type:** article / tutorial
> **Author:** Md Mizanur Rahman Nayan
> **Published:** 2025-10-06
> **Source:** Maven Analytics Monthly Data Drill — Streak Leaderboard challenge
> **URL:** https://medium.com/microsoft-power-bi/gaps-and-islands-solving-consecutive-active-days-in-power-bi-f409b3679559
> **Level:** Beginner | **Category:** DAX | **Tags:** Tutorial, DAX

## Summary

A practical walkthrough of the Gaps and Islands pattern in DAX, applied to finding the longest consecutive active day streak per user from a language learning platform (~900K lesson completions). The challenge: users complete multiple lessons per day (duplicate user-date pairs) and have gaps in activity. Solution uses rank subtraction to create island grouping keys.

## The Problem

Dataset: ~900,000 lesson completions with user_id, date, lesson_id.
- One user can complete multiple lessons per day → duplicate user-date pairs
- Users are not active every day → gaps in the date sequence
- Goal: find the longest streak of consecutive active days per user

## Gaps and Islands Theory

- **Island:** consecutive sequence of data points (e.g., 5 consecutive active days)
- **Gap:** missing data between islands (e.g., 3 days with no activity)
- The key insight: subtract a sequential rank from the date → every date in the same streak gets the same result → that result IS the island ID

## The 6-Step Algorithm

1. **Deduplicate:** `SUMMARIZE(LessonStreaks, user_id, date)` — one row per user per day
2. **Rank:** `RANKX(FILTER(SUMMARIZE...), date, ASC)` — sequential rank per user per active day
3. **Island key:** `date - Rank` — same result for all consecutive days = island ID
4. **Build virtual table:** `ADDCOLUMNS` with both Rank and Island columns
5. **Count streak length:** `SUMMARIZE` by user_id + Island, COUNTROWS
6. **Max streak:** `MAXX(_Streaks, [StreakLength])`

## Complete DAX Solution

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

## Key Design Decisions

- `EARLIER(LessonStreaks[user_id])` captures the outer row's user_id while iterating through the inner FILTER context
- SUMMARIZE inside FILTER creates a per-user filtered table for each row's rank calculation
- No GENERATESERIES needed — this approach handles arbitrary-length streaks without a predefined maximum
- RANKX ASC + date subtraction: works because rank N on date D means D - N is constant within a streak but increases when a gap exists

## Extracted Notes

Links to notes derived from this source:

- [[gaps-and-islands-theory]] — `atomic` — conceptual foundation: island, gap, per-user worked example
- [[rank-subtraction-grouping-trick]] — `atomic` — core DAX insight: date − RANKX(date) = island ID
- [[earlier-captures-outer-row-context]] — `atomic` — EARLIER escapes nested iterator shadowing
- [[dax-gaps-and-islands-pattern]] — `pattern` — full six-VAR DAX pattern for longest streak per entity
- [[streak-leaderboard-top-n-users]] — `pattern` — combine with outer RANKX for ranked leaderboards
- [[dax-vs-generateseries-streak-comparison]] — `comparison` — GENERATESERIES vs Gaps and Islands: when to use each
- [[streak-detection-in-dax]] — extended with full Gaps and Islands implementation

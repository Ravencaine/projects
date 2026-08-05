---
created: 2026-08-01
updated: 2026-08-02
source: "Gaps and Islands Solving Consecutive Active Days in Power BI.md"
note_type: pattern
tags: [dax, pattern, gaps-and-islands, streak-detection, leaderboard, top-n, rankx]
---

# Streak Leaderboard — Top-N Users by Longest Consecutive Active Days

Combining the Gaps and Islands streak algorithm with RANKX to rank all users by their longest active streak — producing a leaderboard suitable for gamification, competitions, or engagement reporting.

## The Problem

Given a user activity table, rank all users by their maximum consecutive active day streak, descending — showing the top performers (longest streaks) at the top.

## Pattern: Ranked Streak Leaderboard

```dax
Streak Leaderboard :=
ADDCOLUMNS(
    SUMMARIZE(
        ADDCOLUMNS(
            ADDCOLUMNS(
                -- Step 1: Deduplicated user-date pairs
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                -- Step 2: Sequential rank per user
                "Rank", RANKX(
                    FILTER(
                        SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                        LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
                    ),
                    LessonStreaks[date], , ASC
                ),
                -- Step 3: Island grouping key
                "Island", LessonStreaks[date] - RANKX(
                    FILTER(
                        SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                        LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
                    ),
                    LessonStreaks[date], , ASC
                )
            ),
            -- Step 4: One row per user + island, with streak length
            LessonStreaks[user_id],
            [Island]
        ),
        "StreakLength", COUNTROWS(
            FILTER(
                ADDCOLUMNS(
                    SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                    "Rank", RANKX(
                        FILTER(
                            SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                            LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
                        ),
                        LessonStreaks[date], , ASC
                    ),
                    "Island", LessonStreaks[date] - RANKX(
                        FILTER(
                            SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                            LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
                        ),
                        LessonStreaks[date], , ASC
                    )
                ),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id]) &&
                [Island] = EARLIER([Island])
            )
        )
    ),
    -- Step 5: Rank users by streak length, descending
    "StreakRank", RANKX(
        ADDCOLUMNS(
            SUMMARIZE(
                ADDCOLUMNS(
                    SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                    "Rank", RANKX(
                        FILTER(
                            SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                            LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
                        ),
                        LessonStreaks[date], , ASC
                    ),
                    "Island", LessonStreaks[date] - RANKX(
                        FILTER(
                            SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                            LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
                        ),
                        LessonStreaks[date], , ASC
                    )
                ),
                LessonStreaks[user_id], [Island]
            ),
            "StreakLength", COUNTROWS(
                FILTER(
                    ADDCOLUMNS(
                        SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                        "Rank", RANKX(
                            FILTER(
                                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
                            ),
                            LessonStreaks[date], , ASC
                        ),
                        "Island", LessonStreaks[date] - RANKX(
                            FILTER(
                                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
                            ),
                            LessonStreaks[date], , ASC
                        )
                    ),
                    LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id]) &&
                    [Island] = EARLIER([Island])
                )
            )
        ),
        [StreakLength],
        ,
        DESC
    )
)
```

> **Performance note:** This pattern nests the Gaps and Islands logic three times (per-row island key, streak length count, and outer RANKX). For large datasets, pre-compute as a calculated table.

## Simpler Version: Rank Users by Max Streak Length

If you already have the `MaxConsecutiveDays` measure from [[dax-gaps-and-islands-pattern]], the leaderboard simplifies to:

```dax
StreakLeaderboardRank :=
VAR _UserMaxStreaks =
    SUMMARIZECOLUMNS(
        LessonStreaks[user_id],
        "MaxStreak", [MaxConsecutiveDays]
    )
RETURN
RANKX(
    _UserMaxStreaks,
    [MaxStreak],
    ,
    DESC
)
```

Use this as a column or measure alongside `MaxConsecutiveDays` in a table visual filtered to the top N.

## Related

- [[dax-gaps-and-islands-pattern]] — the underlying streak detection algorithm
- [[rank-subtraction-grouping-trick]] — the key grouping technique
- [[streak-detection-in-dax]] — alternative GENERATESERIES-based approach

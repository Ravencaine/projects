---
created: 2026-08-01
updated: 2026-08-02
source: "Gaps and Islands Solving Consecutive Active Days in Power BI.md"
note_type: atomic
tags: [dax, rankx, gaps-and-islands, grouping, streak-detection]
---

# Rank Subtraction Grouping Trick

The core DAX insight behind Gaps and Islands streak detection: subtracting a chronological rank from a date value produces a constant that identifies all members of the same island.

## Definition

Given a deduplicated list of `(entity, date)` rows sorted chronologically:

```
Islands Grouping Key = date − RANKX(date ASC)
```

All dates belonging to the same island share the same grouping key value, because the date and its rank advance in lockstep for consecutive dates. A gap causes the rank to lag behind the date, breaking the key value and starting a new island.

## Why It Works

Consider user 8226413 over May 1–7 with a gap on May 2–4:

| date | RANKX (ASC) | date − Rank | Island |
|------|-------------|-------------|--------|
| May 1 | 1 | May1 − 1 = May0 | A |
| May 5 | 2 | May5 − 2 = May3 | B |
| May 6 | 3 | May6 − 3 = May3 | B |
| May 7 | 4 | May7 − 4 = May3 | B |

- May 5, 6, 7 are consecutive: rank increments by 1 each day, date increments by 1 → difference stays constant (May3)
- The gap (May 2–4) caused the rank to stay flat at 1 while the date jumped from May1 to May5: May5 − 2 = May3, a new value → new island

The constant value (e.g., `May3`) becomes the **island identifier** used in a subsequent `GROUP BY` to count rows per island.

## Key Requirements

1. **Deduplication first**: deduplicate to one row per entity-date before ranking, otherwise duplicate dates receive different ranks and produce incorrect island values
2. **Chronological rank**: `RANKX(..., ASC)` ranks oldest date as 1; DESC would invert the logic
3. **Partition by entity**: rank must be scoped per entity (user_id), not global, using `FILTER(SUMMARIZE(...), entity = EARLIER(entity))`

## DAX Implementation

```dax
"Island", LessonStreaks[date] - RANKX(
    FILTER(
        SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
        LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
    ),
    LessonStreaks[date],
    ,
    ASC
)
```

The inner `SUMMARIZE` deduplicates; the `FILTER` inside `RANKX` partitions by user; the subtraction produces the island key.

## Related

- [[gaps-and-islands-theory]] — conceptual foundation for why islands form
- [[dax-gaps-and-islands-pattern]] — complete pattern using this trick
- [[streak-detection-in-dax]] — compares this approach to GENERATESERIES (bounded)

---
created: 2026-08-01
updated: 2026-08-02
source: "Gaps and Islands Solving Consecutive Active Days in Power BI.md"
note_type: atomic
tags: [dax, gaps-and-islands, streak-detection, consecutive, theory]
---

# Gaps and Islands Theory

A framework for identifying and grouping consecutive sequences in ordered data, particularly useful for streak detection in time-series event data.

## Definition

Gaps and Islands is a theory for partitioning ordered data into groups based on the presence or absence of a condition across consecutive positions:

- **Island:** A maximal consecutive sequence where a condition holds true. In user activity data, an island is a run of consecutive active days.
- **Gap:** The period between two islands where the condition is false. In user activity data, a gap is a stretch of inactive days.

An island ends when the condition breaks; a new island begins when the condition resumes.

## Key Points

- Islands are defined relative to a specific condition (e.g., "user was active on this date")
- The condition must be evaluated per entity (per user, per device, etc.) — not globally
- Gaps can be of any length; the island detection algorithm handles this automatically
- Duplicate rows for the same entity-date pair must be deduplicated first (using `SUMMARIZE` or `DISTINCT`) or they inflate the streak count incorrectly

## Per-User Worked Example

For user 8226413 (Aeris Stone) over May 1–23:

| Period | Dates | Condition | Label |
|--------|-------|-----------|-------|
| 1 | May 1 | Active | Island A (1 day) |
| 2 | May 2–4 | Inactive | Gap 1 |
| 3 | May 5–7 | Active | Island B (3 days) |
| 4 | May 8–20 | Inactive | Gap 2 |
| 5 | May 21–23 | Active | Island C (3 days) |

Three islands, two gaps. The longest streak for this user is 3 days (Island B or Island C).

## Why It Matters

Without Gaps and Islands theory, naive streak detection produces incorrect results by:
- Treating a gap as part of the streak (counting inactive days)
- Merging two separate streaks into one if there is any missing data in between

The rank-subtraction trick (see [[rank-subtraction-grouping-trick]]) provides a DAX implementation of this theory that handles gaps of arbitrary length.

## Related

- [[rank-subtraction-grouping-trick]] — the DAX technique that implements island grouping
- [[dax-gaps-and-islands-pattern]] — the complete DAX pattern for longest streak
- [[streak-detection-in-dax]] — the two approaches: GENERATESERIES (bounded) vs Gaps and Islands (unbounded)

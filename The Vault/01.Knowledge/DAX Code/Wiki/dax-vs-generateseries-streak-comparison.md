---
created: 2026-08-01
updated: 2026-08-02
source: "Gaps and Islands Solving Consecutive Active Days in Power BI.md"
note_type: comparison
tags: [dax, comparison, streak-detection, generateseries, gaps-and-islands]
---

# DAX Streak Detection: GENERATESERIES vs Gaps and Islands

Two fundamentally different approaches to detecting consecutive runs in DAX. Choose based on what you need: the current (ongoing) streak or the longest ever streak.

## At a Glance

| | GENERATESERIES (backward-looking) | Gaps and Islands (forward-looking) |
|---|---|---|
| Direction | Looks backward from today | Scans all historical dates |
| Output | Current streak only | Longest streak ever |
| Multiple islands | Not supported | Fully supported |
| Handles gaps | Bounded iteration | Handles any gap length |
| Performance | Bounded (fixed iteration count) | Scans all dates per entity |
| Max streak | Must specify a bound | Unlimited |

## Approach 1: GENERATESERIES (Backward-Looking)

Tests each day going backward from the current date until a gap is hit. Best for **current/live streaks** where you know the maximum possible length.

```dax
Current Streak :=
VAR __CurrentDate = MAX('Dates'[Date])
VAR __ConsecutiveDays =
    SUMX(
        GENERATESERIES(0, 365),          -- bound: max 365 days
        VAR __TestDate = __CurrentDate - [Value]
        VAR __HasValue = NOT(ISBLANK(CALCULATE([Sales], 'Dates'[Date] = __TestDate)))
        RETURN IF(__HasValue, 1, BLANK())
    )
RETURN __ConsecutiveDays
```

**Best for:**
- Live/current streak metrics (days of consecutive sales, login streaks)
- Bounded scenarios where you know the maximum streak length
- Performance-sensitive scenarios (fixed iteration count)

**Weakness:** Cannot identify past streaks that ended before today.

## Approach 2: Gaps and Islands (Forward-Looking)

Scans all historical dates per entity, groups consecutive dates into islands via rank subtraction, and returns the maximum island size. Best for **historical longest-streak** queries.

See [[dax-gaps-and-islands-pattern]] for the full pattern.

**Best for:**
- Longest streak ever leaderboards
- Datasets with multiple islands per entity
- Unknown maximum streak length
- When duplicate rows exist per entity-date pair (SUMMARIZE handles this)

**Weakness:** More complex; scans all dates (no natural bound); slower on very large datasets.

## When to Use Each

| Scenario | Recommended Approach |
|----------|--------------------|
| "How many days has this customer been active consecutively?" | GENERATESERIES |
| "What is each user's longest active streak ever?" | Gaps and Islands |
| "Build a top-10 streak leaderboard from historical data" | Gaps and Islands |
| "Days of consecutive sales for a live dashboard" | GENERATESERIES |
| "Multiple inactivity gaps exist in the data" | Gaps and Islands |

## Combining Both

For a full leaderboard showing both current and longest-ever streak:

```dax
Current Streak := [GENERATESERIES-based current streak measure]
Longest Streak := [Gaps-and-Islands-based longest streak measure]
Top 10 Leaderboard := RANKX(ALL(user_id), [Longest Streak])
```

## Related

- [[streak-detection-in-dax]] — original pattern note with both approaches
- [[dax-gaps-and-islands-pattern]] — full six-VAR Gaps and Islands pattern
- [[rank-subtraction-grouping-trick]] — the core DAX insight powering Gaps and Islands
- [[generateseries-and-datatable]] — GENERATESERIES function reference

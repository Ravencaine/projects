---
created: 2026-08-01
updated: 2026-08-02
source: "We Replaced 47 Excel Files With One Power BI Model. Here's What Actually Happened.md"
note_type: atomic
tags: [power-bi, migration, parallel-run, validation, trust, cutover]
---

# Power BI Parallel Run Protocol

## Why Parallel Run Matters

Running both Excel and Power BI simultaneously (1–2 weeks) before cutover:
- Proves Power BI is ready
- Finds remaining issues before they become crises
- Builds user confidence
- Creates paper trail for trust

## Parallel Run Rules

```
1. Everyone must check BOTH systems daily
2. Report any discrepancies immediately
3. Make decisions based on Power BI, verify with Excel
4. Track which system you trust more (anonymous survey)
```

## What Discrepancies Actually Were

| Category | Example | Outcome |
|----------|---------|---------|
| Excel errors | Manual adjustment made 3 weeks ago, wrong | Power BI correct |
| Power BI bugs | Region name mismatch ("West Coast" vs "Western Region") | Fixed mapping |
| Source data issues | Excel had yesterday's snapshot; Power BI = real-time | Documented the difference |
| Power BI bugs | Filter logic error, data refresh failure | Fixed within 24 hrs |

**Week 1 findings:** 17 discrepancy reports. 9 = Excel errors. 5 = Power BI issues. 3 = source data inconsistencies.

## The Trust Survey

End of parallel run question: "Which system do you trust more?"

| Result | % |
|--------|---|
| Power BI | 67% |
| Excel | 18% |
| Not sure | 15% |

Post-parallel run: "Ready to switch to Power BI only?"
- Yes: 81%
- No: 8%
- Need more time: 11%

## Month-End Close Stress Test

The real parallel-run test: month-end close.

**Before Power BI:** Finance took until 2:00 PM.

**With Power BI:** Done by 9:47 AM. Reports auto-updated as journal entries posted.

**Lesson:** Month-end close = the ultimate readiness test.

## The Cutover Email Template

```
Subject: Excel Files Moving to Read-Only Status — [Date] 8:00 AM

Effective [Date] at 8:00 AM, the following Excel files will be set to read-only:

[List of N files]

All reporting will be done through Power BI.

Excel files will remain accessible for 90 days as reference, then archived.

If you have questions, contact [name].
```

## Post-Cutover Support Trajectory

```
Week 1:  23 support requests (how-to, bugs, feature requests)
Week 2:  12 support requests
Week 3:   5 support requests
Week 4:   2 support requests
Month 2+: < 2 requests per week
```

By week 4, people had adapted. The drop from 23 → 2 = the adaptation curve.

## Escalation Plan

```
Severity 1 (report down):     Respond < 30 min, fix < 2 hrs
Severity 2 (wrong numbers):  Respond < 1 hr, fix < 4 hrs
Severity 3 (minor bug):      Respond < 4 hrs, fix next day
Severity 4 (feature request): Log, prioritize in sprint
```

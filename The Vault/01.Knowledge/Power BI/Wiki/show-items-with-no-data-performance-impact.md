---
created: 2026-08-01
updated: 2026-08-02
source: "How I Reduced a Power BI Visual from 23 Seconds to 8 Seconds A Real Performance Tuning Case Study.md"
note_type: atomic
tags: [power-bi, visual-settings, performance, cross-join, show-items-with-no-data]
---

# Show Items with No Data: Hidden Performance Killer

A single visual field well setting can generate 1,000+ Storage Engine queries and push 88.7% of execution time into the Formula Engine — without any DAX or data model issues.

## What It Is

"Show items with no data" is a per-field setting in Power BI visuals (available in the field well for categorical/grouping fields). When enabled, the visual displays category values even when no data exists for the current filter context.

## Why It Hurts Performance

When enabled, Power BI must:
1. Enumerate **every possible category combination** across all grouping fields
2. Cross-join the combinations with the fact data
3. Evaluate every measure against all combinations
4. Return blanks for combinations with no data

This generates a `__DS0PrimaryShowAllCompat` block in the auto-generated DAX containing nested `GENERATEALL` statements with `OR(NOT(ISBLANK()))` conditions across all measures.

The result:
- Hundreds or thousands of Storage Engine queries (in this case: **1,033 SE queries for 17 rows**)
- 88.7% of execution time in the Formula Engine
- Visual load times measured in seconds instead of milliseconds

## The Fix

Disable **"Show items with no data"** on any grouping field where it is not explicitly needed by the business requirement.

## When It Might Be Needed

- Cross-filter scenarios where "0" is a meaningful value (not just missing data)
- Compliance reports that must show all possible categories regardless of presence
- Auditing visuals that require a complete category list

When needed, consider pre-aggregating the categories in the data model instead of relying on this visual setting.

## Related

- [[ds0-primary-showallcompat-auto-generated-dax]] — what the generated DAX looks like
- [[power-bi-performance-diagnosis-workflow]] — how to find this kind of bottleneck
- [[performance-tuning-assumption-gotcha]] — DAX assumed first; visual settings rarely suspected

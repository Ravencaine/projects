---
created: 2026-07-27
updated: 2026-08-02
source: "Why I Stopped Writing 'Best Practice' DAX Posts"
note_type: atomic
tags: [dax, documentation, pattern, trade-offs, conditional]
---

# DAX Documentation Philosophy: Pattern + Condition

DAX pattern documentation should always include the conditions under which the pattern applies, not just the pattern itself. "Best practice" without context is misleading.

## The Problem with "Best Practice"

"Best practice" without context leads to:

- Using SUMX everywhere (bad advice: SUM is often correct)
- Never nesting CALCULATEs (sometimes necessary for different purposes)
- Always using VAR (adds noise in simple measures)
- Using SAMEPERIODLASTYEAR unconditionally (breaks with non-continuous date tables)

## The Pattern + Condition Template

Every DAX pattern note in this vault should document:

1. **Pattern Name**: what it does
2. **Scenario**: when to use it
3. **Trade-offs**: what you give up
4. **When to Use**: explicit conditions
5. **When NOT to Use**: explicit conditions

## Example: SAMEPERIODLASTYEAR

| Field | Value |
|-------|-------|
| Pattern | SAMEPERIODLASTYEAR |
| Scenario | Period-over-period comparison on a continuous date table |
| Trade-offs | Breaks on non-contiguous date selections; requires PARALLELPERIOD in that case |
| When to Use | Date table is continuous (no gaps), user selects a contiguous date range |
| When NOT to Use | Date table has gaps, user uses non-standard date range selections |

## Example: SUMX vs SUM

| Field | SUM (aggregator) | SUMX (iterator) |
|-------|------------------|----------------|
| Scenario | Sum a single column | Row-level computation required |
| Trade-offs | Faster (no row iteration) | Slower but handles row-level logic |
| When to Use | Expression is a single column reference | Expression requires per-row calculation |
| When NOT to Use | Expression needs row-level multiplication/conditional | Expression is just a single column |

## Implication for This Vault

> Every pattern note should include "When to Use" and "When NOT to Use" sections. Gotcha notes should include the specific condition that triggers the failure.

## Related

- [[dax-performance-5000-measures-source]] — pattern documentation example
- [[measure-branching-pattern]] — includes scenario and trade-offs

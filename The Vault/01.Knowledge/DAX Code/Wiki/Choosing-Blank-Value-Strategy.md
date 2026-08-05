---
created: 2026-08-05
source: Blank Values in Power BI Reports (Boniface Muchendu)
note_type: comparison
tags: [dax, comparison, blank, isblank, card-visual, quick-fix]
---

# Choosing a Blank Value Strategy

Three approaches to handling blank values in Power BI: `+ 0`, New Card Visual, and DAX `IF`. Each suits different situations.

## Comparison

| Approach | Ease | No DAX | Chart-safe | Custom text | Applies to |
|----------|------|--------|------------|-------------|-----------|
| `+ 0` on measure | Instant | ✗ | ✗ | ✗ (returns 0) | All visuals |
| New Card Visual setting | Easy | ✓ | ✓ | ✓ | Card (New Card) only |
| `IF` measure | Moderate | ✗ | ✓ | ✓ | All visuals |

## When to Use Each

| Situation | Recommended approach |
|-----------|---------------------|
| Card visual, no DAX preferred | New Card Visual — "Show blank value as" |
| Quick numeric card, zero = blank | `+ 0` — instant, no new measure |
| Chart with blanks that should not plot as zero | DAX `IF` — keeps value blank in chart |
| Custom display text (N/A, —, null) | DAX `IF` — any text in the fallback |
| Measure that can legitimately return 0 | Use `IF(ISBLANK(...), ...)` explicitly — implicit form treats 0 as blank |

## Key Trade-off

`+ 0` is the fastest but converts blanks to zeros in all visuals. If your charts need to omit blank periods rather than show them as zero, use the DAX `IF` approach and apply the measure only to card visuals.

## Related

- [[Plus-Zero-Blanks-Atomic]]
- [[IF-Implicit-Blank-Check-Pattern]]
- [[New-Card-Visual-Blank-Setting]]

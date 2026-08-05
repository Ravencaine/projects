---
created: 2026-07-27
updated: 2026-08-02
source: "The 5 DAX Patterns Senior Analysts Use"
note_type: pattern
tags: [dax, measure-branching, architecture, hierarchy]
---

# Pattern 1: Measure Branching

See [[measure-branching-pattern]] for the full pattern description.

**Summary:** Complex calculations are decomposed into base measures (raw calculations), intermediate measures (business rules applied), and KPI measures (final business-facing metrics). Derivatives reference base measures, not duplicated logic.

## Quick Reference

```dax
-- Level 0: base
_Revenue Raw = SUM(Sales[Revenue])

-- Level 1: business rule applied
Revenue = CALCULATE([_Revenue Raw], Sales[IsReturn] = FALSE)

-- Level 2: time intelligence
Revenue LY = CALCULATE([Revenue], SAMEPERIODLASTYEAR(Calendar[Date]))

-- Level 3: KPI
Revenue vs LY % = DIVIDE([Revenue] - [Revenue LY], [Revenue LY], 0)
```

## Related

- [[measure-branching-pattern]] — full pattern
- [[measure-library-architecture-pattern]] — library organization

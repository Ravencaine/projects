---
created: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, text, normalize, trim, unichar]
---

# NormalizeLabel — Trim + Clean Invisible Characters

Strips leading/trailing whitespace and replaces common invisible characters that break LOOKUPVALUEs and groupings.

```dax
DEFINE
    FUNCTION NormalizeLabel =
        ( s : STRING ) =>
        TRIM(
            SUBSTITUTE(
                SUBSTITUTE(s, UNICHAR(160), " "),   -- non-breaking space
                UNICHAR(9), " "                     -- tab
            )
        )
```

**Handles:**
- `UNICHAR(160)` — non-breaking space (common in Excel/HTML copy-paste)
- `UNICHAR(9)` — tab character
- `TRIM` — leading/trailing whitespace

**Usage:**
```dax
-- Clean category for grouping
Clean Category = NormalizeLabel(Sales[CategoryName])

-- Safe lookup (avoid mismatches from hidden chars)
Region Code = LOOKUPVALUE(
    Regions[Code],
    Regions[Name], NormalizeLabel(Sales[RegionName])
)
```

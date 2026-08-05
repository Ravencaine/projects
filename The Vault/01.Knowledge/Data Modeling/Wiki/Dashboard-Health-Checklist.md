---
created: 2026-08-05
source: 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)
note_type: workflow
tags: [data-cleaning, data-quality, checklist, power-bi, pre-publish]
---

# Dashboard Health Checklist

Five questions to answer before publishing any Power BI dashboard. If the answer to any question is "No," step away from the Publish button.

## The Checklist

- [ ] **1. Duplicates purged?** — Have all duplicate records been removed or accounted for? Run `COUNTROWS` vs `DISTINCTCOUNT` on key ID columns.
- [ ] **2. Date formats standardised?** — Are all date columns in a consistent, unambiguous format (ISO `YYYY-MM-DD` preferred)?
- [ ] **3. Blanks handled?** — Have all blank values been accounted for, replaced with a default, or the row dropped?
- [ ] **4. Categories normalised?** — Are all text categories consistent (no `Mumbai` vs `MUMBAI` vs `Bombay` for the same city)?
- [ ] **5. Outliers reviewed?** — Have you scanned min/max values for every numeric column? Does any value look like a data entry error?

## How to Run the Checks

| Check | Tool |
|-------|------|
| Duplicates | Power Query: Remove Duplicates; DAX: `COUNTROWS` vs `DISTINCTCOUNT` |
| Date formats | Power Query: Detect Data Type + locale setting |
| Blank values | Power Query: Replace Errors / Replace Nulls; DAX: `ISBLANK` measure |
| Category consistency | Power Query: `Text.Trim`, `Text.Upper`, dimension lookup merge |
| Outliers | Power BI: sort numeric columns by min/max in Data view |

## The Mantra

> "Can I actually trust the data behind this visual?" — DigitalBYKewat

## Related

- [[Duplicate-Records-Detection-Removal]]
- [[Inconsistent-Date-Formats-ISO]]
- [[Missing-Values-Handling-Strategy]]
- [[Inconsistent-Categories-Normalisation]]
- [[Ignoring-Outliers-Detection-Action]]

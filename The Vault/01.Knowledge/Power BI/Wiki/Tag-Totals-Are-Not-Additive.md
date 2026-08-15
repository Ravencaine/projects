---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Framework for Tagging and Classification in Power BI
source_url: https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
note_type: gotcha
tags: [powerbi, data-modeling, tagging, totals, aggregation, gotcha]
---

# Tag Totals Are Not Additive

Users expect tag totals to add up across categories (Logistics = 71 units, Compliance = 10 units, therefore combined = 81 units). In a tagging model, this assumption is wrong — the combined total is not the sum of individual tag totals.

## Expected Behaviour

Given:
- Tag A (Logistics): 71 units
- Tag B (Compliance): 10 units

User expects: Combined = 71 + 10 = **81 units**

## Actual Behaviour

Combined total is **not 81 units**. The overlap between tags means some services are counted in both categories. Adding the two numbers together double-counts the shared services.

The model is behaving correctly. The total is not additive across tags.

## Why It Happens

The tagging model intentionally allows entities to belong to multiple tags. The same entity contributes to every applicable tag view. This overlap means tag-level totals share data — they are not independent partitions that can be summed.

## How to Handle It

**Do not add tag totals.** Instead:
- Present individual tag totals as independent slices
- Use `Show Values As: No Calculation` or rely on single-tag context
- For cross-tag analysis, use a dedicated measure that explicitly handles overlap (e.g., `DISTINCTCOUNT` on entity key, or a Venn diagram visual)

**Frame for users:**
> *"Each tag shows what data relates to that topic. Tags answer 'what belongs here?' — not 'what is unique to this category?' View individual tag totals in isolation; do not sum across tags."*

**Visual/design mitigations:**
- Use KPI cards per tag rather than a table summing across tags
- Add a note or tooltip explaining the non-additive nature
- Use conditional formatting that only shows values within single-tag context

## Related Gotchas

- [[Tags-Equal-Lens-Not-Partition]] — the conceptual framing behind this behaviour
- [[why-totals-look-wrong-in-dax-and-how-to-fix-them]] — general DAX totals issue (if it exists in DAX Code KB)

---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Framework for Tagging and Classification in Power BI
source_url: https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
note_type: atomic
tags: [powerbi, data-modeling, tagging, classification, interpretation]
---

# Tags = Lens, Not Partition

Each tag in a tagging model represents a **perspective on the data**, not a distinct subset of it. Tags are overlapping lenses — they answer "what data relates to this topic?" not "what share of the data belongs exclusively to this topic?"

## Definition

In a tagging model, a single entity (service, product, document) can belong to multiple tags simultaneously. This means the same underlying data can appear in multiple tag selections — and should. Tags are additive in coverage, not exclusive in partitioning.

## Key Points

- Tags are **non-mutually-exclusive** classifications — an entity can appear in every applicable tag view simultaneously
- A service tagged *Logistics* AND *Compliance* belongs to both views — this is correct, not double-counting
- Selecting one tag returns all entities with that tag applied, regardless of what other tags they carry
- Results are best interpreted **within the context of a selected tag**, not **across multiple tags**

## Examples

| Scenario | Tag A (Logistics) | Tag B (Compliance) |
|---------|-------------------|--------------------|
| Service belongs to A only | ✓ included | ✗ excluded |
| Service belongs to B only | ✗ excluded | ✓ included |
| Service belongs to A + B | ✓ included | ✓ included |

The same service appearing in both views is correct behavior — not a data quality problem.

## How to Communicate This to Users

> *"Think of tags like coloured lenses. The same data viewed through a blue lens and a red lens is still the same data — you're just highlighting different aspects of it."*

## Related

- [[Tag-Totals-Are-Not-Additive]]
- [[Tagging-Bridge-Table-Pattern]]

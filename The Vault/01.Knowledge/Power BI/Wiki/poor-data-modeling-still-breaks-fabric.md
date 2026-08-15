---
created: 2026-08-13
source: "5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)"
source_url: "https://medium.com/powerbi-microsoft-fabric/5-mistakes-beginners-make-in-microsoft-fabric-and-how-to-avoid-them-269ac1739472"
note_type: gotcha
tags: [microsoft-fabric, data-modeling, star-schema, dax, power-bi]
---

# Poor Data Modeling Still Breaks Fabric Reports

The promise of a unified platform does not eliminate the need for good data modeling. Beginners in Fabric make the same modeling mistakes they made in standalone Power BI.

## Expected Behaviour

Beginners expect that Fabric's modern platform handles performance and correctness automatically — the lakehouse and Direct Lake will compensate for bad model design.

## Actual Behaviour

A flat table loaded directly into Power BI from a Fabric Lakehouse produces the same slow, bloated semantic model as a flat Excel import in standalone Power BI.

Fabric does not auto-optimize your data model. DAX still runs in the same engine. Relationships still matter. Measure granularity still determines whether your calculations are correct.

## Why It Happens

The lakehouse gives you somewhere to put your data — it does not tell you how to structure it. Without medallion discipline and dimensional modeling, you end up with:

- **Flat tables** — no separation of fact and dimensions
- **Missing relationships** — unlinked tables that should be connected
- **Overused calculated columns** — row-level computations instead of measures

## How to Handle It

Apply the same modeling principles used in any Power BI project:

- Use a **star schema** — central fact table, dimension tables around it
- Separate **Fact and Dimension tables** — do not combine them
- Create **measures not calculated columns** — aggregate in DAX, not at row level
- Define **relationships** explicitly — do not rely on auto-detection

Fabric's OneLake and Direct Lake do not replace dimensional modeling — they just make correct models faster to query.



See [[star-schema-fact-table-dimension-tables-in-powerpivot]] for the foundational star schema principles.



See [[measures-vs-calculated-columns]] for when to use measures vs calculated columns.

## Related

- [[star-schema-fact-table-principles]] — foundational star schema principles
- [[medallion-architecture]] — the layer discipline that forces good modeling
- [[fabric-is-a-complete-data-platform]] — why the platform exists
- [[data-model-5-common-problems-fixes]] — the five common beginner mistakes

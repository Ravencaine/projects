---
created: 2026-08-01
updated: 2026-08-02
source: "When a Simple Variance Measure Breaks Power BI Lessons from Cross-Fact DAX.md"
note_type: atomic
tags: [dax, treatas, virtual-relationship, cross-fact, filter-propagation]
---

# Cross-Fact TREATAS Virtual Relationships

## Problem

Two fact tables from different systems (`fctPayrollVehicles` + `LN Eq Rev`) have no physical relationship. Power BI cannot naturally compare them.

## TREATAS Solution

```c
Vehicle Eq Hours =
CALCULATE(
    SUM('LN Eq Rev'[Quantity]),
    TREATAS(
        SUMMARIZE(
            fctPayrollVehicles,
            fctPayrollVehicles[Vehicle],
            fctPayrollVehicles[Job_Number]
        ),
        'LN Eq Rev'[Equipment Serial Code],
        'LN Eq Rev'[Project]
    )
)
```

**What it does:** Treat Vehicle + Job pairs from payroll as filters on the equipment table — even without a physical relationship.

## Filter Flow

```
Payroll Context (Vehicle + Job)
        │
        │  TREATAS
        ▼
LN Eq Rev
filtered by: Equipment Serial Code + Project
```

## Use Cases

- Cross-system reconciliation
- Comparing operational systems (ERP vs CRM vs custom)
- Bridging datasets with different schemas

## Anti-Pattern

Do NOT build a many-to-many bridge table just to join two fact tables. TREATAS virtual relationships are cheaper and cleaner.

## Key Constraint

TREATAS requires the target column to have the same cardinality as the source — if SUMMARIZE produces more unique combinations than the target column can hold, results are undefined.

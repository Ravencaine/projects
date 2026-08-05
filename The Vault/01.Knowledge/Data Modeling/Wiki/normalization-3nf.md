---


title: "Normalization and Third Normal Form (3NF)"
created: 2026-07-28
updated: 2026-08-02
tags: [data-modeling, concept]
note_type: pattern
description: "Database normalization — eliminating redundant fields, Third Normal Form (3NF), eliminating transitive dependencies. From Dunlop Chapter 4."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Normalization and 3NF

## Why Normalize

The core principle of relational database design: **avoid repeating fields**. Normalization divides large tables into smaller, related tables to minimize redundancy.

## Normalization Example

Before (repeating fields):
```
employees: Name, DeptOffice, DeptPhone, DeptManager, DeptBudget
```

After (normalized — office data removed):
```
employees: Name, DeptCode
departments: DeptCode, Office, Phone, Manager, Budget
```

Dept info stored once per department, not once per employee.

## Third Normal Form (3NF)

Defined by E.F. Codd. A table is in 3NF when:
1. It is in Second Normal Form (2NF) — no partial dependencies on composite keys
2. **Every non-key field depends on the primary key, and only the primary key**: eliminating transitive dependencies

### Transitive Dependency

```
Field A → Field B → Field C

A (PK) determines B, and B determines C — but C should only depend on A.
If B changes, C could become inconsistent. This is a transitive dependency.
```

### 3NF Rule

> Each field in a table must depend on the primary key, and **only** the primary key.

## Why 3NF Matters

- **No update anomalies**: changing a department's manager requires one update, not N employee rows
- **No insertion anomalies**: new departments can exist without employees
- **No deletion anomalies**: removing the last employee doesn't accidentally delete department info

## Source Reference

Chapter 4, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

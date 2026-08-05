---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling!.md"
note_type: atomic
tags: [power-bi, data-modeling, relationships, one-to-many, many-to-many, beginner]
---

# Relationship Types: One-to-Many, Many-to-Many, and More

Relationships are the invisible bridges that let Power BI look up customer details from a sales table. Four types exist.

## 1. One-to-Many (Use This 90% of the Time) ⭐

**Pattern:** One record on one side connects to many records on the other side.

**Model view indicator:** "1" on the dimension side, "*" on the fact side.

**Example:**
```
Customers (1) ──────────── (*) Orders
```

One customer appears once in the Customers table. That same customer can have unlimited orders in the Orders table.

This is the standard. Start here. It works in almost every business scenario.

## 2. Many-to-One (Same Thing, Different Direction)

Identical to one-to-many — just viewed from the opposite direction. Power BI labels it "Many-to-one (*:1)" in some dialogs. Same behaviour, same performance.

## 3. Many-to-Many — The Danger Zone ⚠️

**Pattern:** Multiple records on both sides can match multiple records on the other side.

**Example:** Sales territories
- Robert covers California, Oregon, Washington
- California has three salespeople covering it

There is no clear "one" side. Direct many-to-many relationships cause **row duplication**: the same sale gets counted multiple times when filtering by territory.

**The symptom:** Every measure shows 2-10x the correct total.

**The solution:** Use a bridge/assignment table:
```
Salespeople (1) ──── (*) SalespersonTerritory (*) ──── (1) Territories
```

Each relationship is one-to-many. No many-to-many. Correct counts.

## 4. One-to-One — Merge Instead

**Pattern:** Both sides have exactly one matching record.

**Example:** Employee details split across two source systems (HR and Payroll).

In most cases: just merge these into one table in Power Query. Simpler is better.

**Valid reasons to keep separate:**
- Security: sensitive salary data restricted
- Large text fields separated for performance
- Connecting to two separate source databases

## Filter Direction

Filter direction (shown as arrows on relationship lines) determines which table's filters flow to which. Single direction: from dimension to fact (correct). Bidirectional: filters flow both ways — causes ambiguity and row duplication problems.

**Rule:** Keep filter direction single, pointing from dimension to fact.

## Related

- [[fact-table-vs-dimension-table]] — which side is "one" and which is "many"
- [[data-model-5-common-problems-fixes]] — diagnosing and fixing many-to-many symptoms (inflated numbers)
- [[excel-flat-table-problems]] — why you need relationships in the first place

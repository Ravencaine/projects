---
created: 2026-08-13
source: 5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)
note_type: pattern
tags: [star-schema, data-modeling, microsoft-fabric, fact-table, dimension-table, one-lake]
---

# Star Schema in Fabric

<!-- Source: Anurodh Kumar, "5 Mistakes Beginners Make in Microsoft Fabric", 2026-05-03 -->

## Purpose

Even in Fabric, data modelling still matters. Beginners often create flat tables and ignore relationships — Fabric's convenience does not eliminate the need for a proper star schema.

## The Anti-Pattern (Flat Tables)

```
❌ One big table: SalesID, Product, Category, Customer, Region, Salesperson, Date, Amount, Cost, Tax, ...
```

Problems:
- All attributes repeated per row — massive storage waste
- No reuse across facts — CustomerName stored separately in every fact
- Slicers behave unexpectedly
- Measures return wrong totals

## Star Schema Pattern

```
FactSales
├── SalesKey (PK)
├── ProductKey (FK → DimProduct)
├── CustomerKey (FK → DimCustomer)
├── DateKey (FK → DimDate)
└── Amount

DimProduct
├── ProductKey (PK)
├── ProductName
├── Category
└── Subcategory

DimCustomer
├── CustomerKey (PK)
├── CustomerName
├── Region
└── Segment

DimDate
├── DateKey (PK)
├── Year
├── Month
└── Quarter
```

## Components

- **Fact table** — transactions at the atomic grain (one row per sale)
- **Dimension tables** — descriptive attributes for slicing/filtering
- **Surrogate keys** — integer PKs for joins
- **One-to-many relationships** — each dimension joins to the fact

## In Fabric / OneLake

The Gold layer in the medallion architecture is where the star schema lives:

| Layer | What Lives Here |
|-------|----------------|
| Bronze | Raw source files — flat or unstructured |
| Silver | Cleansed data — may still be denormalised |
| Gold | Star schema — fact + dims ready for BI |

Power BI connects to Gold via **Direct Lake**, reading the fact and dimension tables directly from OneLake shortcuts.

## Related

- [[star-schema-fact-table-principles]] — Data Modeling: fact table design rules
- [[dim-date-dax-calendar]] — Data Modeling: DAX date dimension
- [[medallion-architecture-raw-cleansed-dimensional]] — where star schema fits in medallion
- [[End-to-End-Fabric-Pipeline]] — Power BI: Fabric pipeline context
- [[Medallion-Architecture-Fabric]] — how Gold layer hosts the star schema

---
title: "From Messy Power BI Relationships to a Clean Fleet Analytics Model"
source: "https://medium.com/microsoft-power-bi/from-messy-power-bi-relationships-to-a-clean-fleet-analytics-model-d9ae82bb323c"
author:
  - "[[Mark Chen]]"
published: 2026-03-17
created: 2026-07-29
description: "Lessons from building a real-world Equipment–Operator–Project data model"
Processed: "Unprocessed"
---
## Lessons from building a real-world Equipment–Operator–Project data model

Operational datasets often look deceptively simple at first glance.  
A few tables for equipment transactions, payroll, and assignments — connect them together in Power BI and start building dashboards.

But once the model grows, things begin to break:

- circular relationships appear
- many-to-many relationships creep in
- calculated columns become unpredictable
- totals stop making sense

This article walks through a practical modeling journey for a **fleet analytics dataset** containing:

- ~1,000 pieces of equipment
- 2–3 years of daily operational data
- payroll for operators
- revenue and cost transactions per machine

The goal: build a model that can answer questions like:

- Which machines are most profitable?
- Which operators generate the most revenue?
- Which projects consume the most equipment resources?

Along the way we’ll look at several modeling techniques that dramatically improve stability and clarity.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## The Starting Point: A Typical Operational Model

Many operational Power BI models begin like this:

```c
dimOperator
   ├── dimEmployee
   ├── dimEquipment
   └── dimRegion
fctPayroll
fctEquipmentTransactions
```

At first this feels natural.  
But one table — `dimOperator` — is doing too many things at once.

It contains:

```c
operator attributes
equipment assignments
region information
```

This creates multiple relationship paths such as:

```c
Region → Equipment → Operator → Employee → Payroll
Region → Equipment → Transactions
```

Power BI now has **multiple ways to propagate filters**, which leads to:

- ambiguous relationships
- circular dependency errors
- incorrect aggregations

The core lesson:

> *Dimensions should rarely connect directly to other dimensions.*

## Step 1 — Separate Dimensions from Relationships

The first improvement is separating **entities** from **relationships**.

Instead of one overloaded table, create three logical structures.

## Dimensions

```c
dimEquipment
dimEmployee
dimRegion
dimDate
```

Each dimension describes a single entity.

Example:

EquipmentID  
Model  
Fleet  
Region

## Bridge / Assignment Table

```c
fctOperatorAssignment
```

EmployeeCodeEquipmentIDE101EQ01E101EQ02

This table represents **relationships**, not attributes.

Employees can operate multiple machines — so duplicates are expected.

## Step 2 — Treat Assignments as Facts

Operator assignments are not static attributes.

They represent an operational relationship:

```c
Operator ↔ Equipment
```

So instead of modeling them as a dimension, treat them as a **fact table**.

```c
dimEmployee
     │
fctOperatorAssignment
     │
dimEquipment
```

This simple change removes most relationship ambiguity.

## Step 3 — Build a Hub-and-Spoke Model

In fleet analytics, **equipment naturally becomes the hub**.

Nearly every operational signal connects to machines:

- revenue
- fuel usage
- maintenance
- operators
- payroll
- projects

So the model becomes:

```c
dimEquipment
           │   │   │
           │   │   │
fctEquipmentTransactions ---*
           │                │
       fctFuel--------------*               
           │                │
    fctMaintenance----------*---------dimDate
           │                │
 fctOperatorAssignment------*
           │                │
        dimEmployee         │
           │                │
       fctPayroll-----------*
```

This is a classic **hub-and-spoke star schema**.

Facts connect to dimensions — not to other facts.

## Step 4 — Handling Many-to-Many Relationships

Operators often work on multiple machines during the same pay period.

This means payroll cannot simply store one machine per row.

Instead of forcing a relationship, allocate payroll dynamically.

Conceptually:

```c
Payroll → Employee
Employee → Assignment
Assignment → Equipment
```

Payroll is distributed across machines using **DAX measures**, not columns.

Example concept:

```c
Allocated Payroll =
Payroll Hours / Machines Operated
```

This keeps totals correct without creating many-to-many fact relationships.

## Step 5 — The Operational Triangle

In many equipment-heavy industries, activity revolves around three entities:

```c
Operator
Equipment
Project
```

Add time and you get the operational grain:

```c
Operator + Equipment + Project + Date
```

This forms the **operational triangle**.

```c
dimOperator
                 │
                 │
dimProject ── fctOperations ── dimEquipment
                 │
                 │
               dimDate
```

This structure enables powerful analysis:

- revenue per machine per project
- operator productivity by project
- equipment utilization across jobs

## Step 6 — Optional: Consolidated Activity Fact

If multiple fact tables share the same grain (`Equipment + Date`), they can be consolidated into a single operational table.

Example:

Equipment  
Date  
Revenue  
Fuel  
Maintenance  
PayrollHours

This enables extremely simple calculations.

```c
Machine Profit =
Revenue
- Fuel
- Maintenance
- Payroll
```

However, consolidation is optional.  
For many models, separate fact tables remain perfectly manageable.

## Step 7 — Performance Considerations

At the scale of this dataset:

```c
1,000 equipment
~3 years daily data
≈ 1 million equipment-day rows
```

Power BI handles this easily.

Typical model size:

```c
50–150 MB
```

Performance problems at this scale usually come from:

- complex relationship paths
- unnecessary bidirectional filters
- calculated columns replacing proper modeling

Not from row volume.

## Key Modeling Principles

After working through the redesign, several principles emerge.

## 1\. Dimensions describe entities

```c
Equipment
Employee
Project
Date
```

## 2\. Relationships belong in fact tables

```c
OperatorAssignment
```

## 3\. Avoid dimension-to-dimension relationships

Use facts as controlled bridges.

## 4\. Keep grains consistent

Examples:

```c
Equipment + Date
Employee + Date
```

Avoid mixing grains within the same table.

## 5\. Push complexity into measures, not relationships

Measures are easier to control and maintain.

## What This Model Enables

Once the structure is clean, the analytics layer becomes powerful.

Examples:

## Fleet Profitability

Equipment  
Revenue  
Cost  
Profit

## Operator Productivity

| Operator | Hours | Revenue Generated |

## Project Equipment Utilization

| Project | Machine Hours | Revenue |

## Final Model Overview

The resulting architecture becomes surprisingly elegant:

```c
dimEquipment
              │  │  │
              │  │  │
fctEquipmentTransactions--------*
              │                 │
          fctFuel---------------*
              │                 │
       fctMaintenance-----------*---------dimDate
              │                 │
    fctOperatorAssignment-------*
              │                 │
         dimEmployee            │
              │                 │
        fctPayroll--------------*
```

This structure is very similar to the models used in **large fleet, mining, and construction BI systems**.

![](99.System/Attachments/1!WrW_g8ZPBAqY6xGwWOs8yg.png.webp)

## Final Thoughts

Many Power BI modeling problems are not DAX problems — they are **data modeling problems**.

The biggest improvements often come from:

- separating entities from relationships
- clarifying grain
- simplifying relationship paths

Once those are in place, the model becomes easier to reason about, easier to maintain, and far more powerful analytically.

Sometimes the best optimization isn’t a clever formula — it’s a **cleaner model**.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----d9ae82bb323c---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Model

**Tags:** Tutorial, Data Model
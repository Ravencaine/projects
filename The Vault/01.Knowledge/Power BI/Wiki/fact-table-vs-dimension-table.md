---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling!.md"
note_type: atomic
tags: [power-bi, data-modeling, fact-table, dimension-table, beginner, star-schema]
---

# Fact Table vs Dimension Table

Every table in a Power BI model is either a fact table or a dimension table. Understanding which is which is the foundation of everything that follows.

## Fact Tables: The "What Happened" Tables

Fact tables store measurable business events — the transactions, actions, and measurements you want to count or sum.

**Characteristics:**
- Mostly numbers and IDs (very little text)
- Many rows (thousands to millions)
- Each row is one event or transaction
- Grows over time as new events occur
- Contains the data you want to aggregate

**Examples:**
- Sales transactions: each row = one order
- Call records: each row = one call
- Inventory snapshots: each row = one state measurement

**Key question:** Does each row represent a transaction or event? If yes → fact table.

**What you measure from fact tables:**
- Total revenue: `SUM(Sales[Amount])`
- Number of orders: `COUNTROWS(Sales)`
- Average call duration: `AVERAGE(Calls[Duration])`

Fact tables answer "How much?" and "How many?"

## Dimension Tables: The Who, What, When, Where Tables

Dimension tables contain descriptive information that gives context to your facts.

**Characteristics:**
- Mostly text and categories
- Fewer rows (dozens to thousands)
- Relatively stable (changes infrequently)
- Contains attributes you filter and group by
- Provides the "story" around the numbers

**Examples:**
- Customer dimension: who bought
- Product dimension: what was sold
- Date dimension: when it happened
- Geography dimension: where it happened

Dimension tables answer "Who?", "What?", "When?", "Where?", and "Why?"

## The Four Questions

| Question | Answer | Table Type |
|----------|--------|------------|
| Does each row = a transaction/event? | Yes | Fact |
| Will this table grow significantly over time? | Yes (new rows daily) | Fact |
| Am I measuring this or describing something? | Measuring | Fact |
| Mostly numbers or mostly text? | Numbers | Fact |

| Question | Answer | Table Type |
|----------|--------|------------|
| Does each row = a transaction/event? | No | Dimension |
| Will this table grow significantly over time? | No (slow-changing) | Dimension |
| Am I measuring this or describing something? | Describing | Dimension |
| Mostly numbers or mostly text? | Text | Dimension |

## A Real Scenario

| Data | Rows | Type | Reason |
|------|------|------|--------|
| Sales transactions | 2M (adds 5K/day) | Fact | Event, rapidly growing |
| Products catalog | 500 | Dimension | Stable, descriptive |
| Stores | 150 | Dimension | Stable, descriptive |
| Customer list | 50,000 | Dimension | Descriptive even at large size |
| Daily inventory snapshot | 75K/day | Fact | State at a point in time |

## Related

- [[star-schema-vs-snowflake-schema]] — how to arrange fact and dimension tables
- [[relationship-types-one-to-many-many-to-many]] — fact tables are always the "many" side
- [[data-model-5-testing-checks]] — testing that fact/dimension relationships work correctly

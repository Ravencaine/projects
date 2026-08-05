---
created: 2026-08-01
updated: 2026-08-02
source: "Unlocking Python Inside Power BI How I Solved the Cumulative Value Challenge (and What I Learned Along the Way).md"
note_type: atomic
tags: [power-query, python, formula-firewall, gotcha, intermediate]
---

# Formula Firewall: Why Python Scripts Only Work on Direct Queries

Power BI's Formula Firewall blocks Python scripts when they run inside a **referenced query**: only direct queries support Python execution.

## The Scenario: Referencing a Query for a Clean Pipeline

Intuitive approach: create a separate query that **references** the source table, run Python there, keeping the original clean.

```m
// New query referencing StackedData
Cumulative = StackedData  // reference
// Then run Python script step...
```

Power BI response:

> **Formula.Firewall: Query 'Cumulative' (step 'Run Python script') references other queries or steps, so it may not directly access a data source. Please rebuild this data combination.**

## Why the Formula Firewall Blocks This

The Formula Firewall enforces Power BI's **privacy level** settings. When a query references another query and then runs Python, Power BI cannot guarantee data isolation — the Python script might expose data from the referenced query to the environment Power BI considers untrusted.

Python scripts are treated as a potential data source in their own right, so the Firewall treats them as a query that touches multiple privacy contexts.

## The Fix: Run Python on the Source Table Directly

The Python script must run directly inside the **source query**: not in a downstream reference:

```
StackedData (source query)
  → Run Python script here  ← directly in source
  → Changed Type
  → ... downstream steps
```

This works because the source query only touches its own privacy context. Everything downstream (including the new `Cumulative Value` column) is visible to all subsequent steps automatically.

**Trade-off:** the Python transformation modifies the source table in place. In practice this is cleaner — everything downstream sees the enriched table without needing a separate reference.

## When Referencing Is Still Useful

Referencing is still good for:
- Creating a copy before a destructive transformation (reference first, then transform)
- Isolating two different transformation paths from the same source
- Debugging (reference → inspect intermediate state)

But if Python is needed, the script must live in the source query itself.

## Related

- [[python-script-in-power-query]] — step-by-step for running Python in Power Query
- [[python-data-types-power-query]] — data types lost after expansion; always add Changed Type

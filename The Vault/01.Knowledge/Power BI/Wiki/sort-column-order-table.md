---
created: 2026-08-02
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: pattern
tags: [powerbi, pattern, sorting, column, data-model]
---

# Sort Column Order Table

A lookup table created in Power Query (or Excel) to impose a custom sort order on a categorical column, connected to the data model via a relationship.

## Use Case

The native column order in a dimension table does not match the desired display order (e.g., process steps: Application → Screening → Interview → Offer → Onboarding).

## Implementation

1. Create a table with two columns: the categorical value and a numeric sort key
2. Load it into Power BI and connect it to the dimension table via the categorical column
3. Sort the dimension column by the numeric column in the model view or via "Sort by Column"

## Why a Relationship

Connecting the sort table to the data model ensures the sort order persists across all visuals that use the dimension — no need to set sort order per visual.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21

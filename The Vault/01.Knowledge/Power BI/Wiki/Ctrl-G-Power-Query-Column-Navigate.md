---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: atomic
tags: [power-query, productivity, shortcut]
---

# Ctrl+G: Navigate Columns in Power Query

Press Ctrl+G in Power Query to jump directly to any column by name — eliminating slow horizontal scrolling through wide tables.

## Definition

Power Query Editor supports a column navigator (Ctrl+G) that shows a searchable list of all columns in the current table. Selecting a column name instantly scrolls to it and selects it.

## Key Points

- Works in **Transform** tab → any table with many columns
- Opens a column picker/search box — type to filter
- Instantly navigates to the column and selects it
- Particularly valuable for tables with 20+ columns (e.g., wide fact tables, booking/staging tables)
- Replaces manual horizontal scrolling or searching visually
- Applies to the currently loaded/transformed table view

## Example

**Workflow:**
1. Go to Transform → select a wide table (e.g., Bookings)
2. Press **Ctrl+G**
3. Type `StayDate` or `GuestKey`
4. Click the column → instantly scrolls to and selects it

## Related

- [[Power-Query-Parameters-Environment-Switch]] — Power Query parameter patterns
- [[Test-Mode-Parameters-Development]] — Power Query development patterns

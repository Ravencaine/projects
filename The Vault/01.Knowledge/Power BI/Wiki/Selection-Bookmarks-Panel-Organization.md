---
created: 2026-08-05
updated: 2026-08-05
source: 4 Tips Work Efficiently Power BI (Isabelle Bittar)
note_type: atomic
tags: [power-bi, selection-panel, bookmarks, navigation, organization]
---

# Selection and Bookmarks Panel Organization

Renaming and grouping all report elements in the Selection panel, and organizing bookmarks into named groups — essential as reports grow beyond ~10 elements.

## Definition

The **Selection panel** (View → Selection) lists every visual, shape, text box, and button on the report canvas. The **Bookmarks panel** (View → Bookmarks) lists navigation and state bookmarks. Both become hard to manage without a consistent naming and grouping convention.

## Why It Matters

- Double-clicking an element in the Selection panel selects it on the canvas — no hunting for tiny shapes
- Bookmark groups make navigation state management faster in large reports
- Grouped elements hide/show together when toggling bookmarks
- A clean Selection panel signals professional report hygiene

## Naming Convention

| Element type | Pattern | Example |
|-------------|---------|---------|
| Visual | `[Section] [Type]` | `Sales Bar Chart`, `KPI Card` |
| Shape/background | `[Section] Background` | `Header Background` |
| Text box | `[Section] [Content]` | `Title Text`, `Footer Note` |
| Button | `[Action] Button` | `Drillthrough Button` |
| Group | `[Section] Group` | `Filter Panel Group` |

## Grouping Elements

1. Select multiple elements in the Selection panel (Ctrl+click)
2. Right-click → **Group**
3. Rename the group with a descriptive name
4. Groups collapse/expand in the Selection panel — use this to keep sections tidy

## Bookmark Groups

1. Create bookmarks for each navigation state
2. In the Bookmarks pane: click **Add** for each state
3. Rename bookmarks with a consistent prefix (e.g., `Nav - Dashboard`, `Nav - Report`)
4. As the count grows, group them visually by naming convention — Power BI doesn't have bookmark folders, so naming prefixes serve the same purpose

## Best Practice

- Rename elements **before** adding bookmarks — renaming breaks bookmark references if done after
- Review and clean up the Selection panel before publishing — it is visible to anyone who downloads the PBIX

## Related

- [[Organizing-Measures-Display-Folders]]
- [[Parameter-File-No-Hard-Coding]]

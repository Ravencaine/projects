---
created: 2026-08-05
updated: 2026-08-05
source: 4 Tips Work Efficiently Power BI (Isabelle Bittar)
note_type: atomic
tags: [power-bi, measure, display-folder, model, organization]
---

# Organizing Measures in Display Folders

Creating a centralized `\_Measures` table to group all measures, then organizing them into a display folder hierarchy with subfolders — keeping the model view clean and navigable.

## Definition

A display folder is a virtual folder in the Power BI Model view that groups fields visually without affecting the data model. Isabelle's approach: create an empty table that becomes a measures group, then assign every measure to a display folder.

## Why a `\_Measures` Table

Measures must belong to a table in the model. Storing all measures in a single `\_Measures` table (prefixed with `_` so it sorts first alphabetically) keeps them visually separated from data columns.

## Steps

### 1. Create the empty table

1. **Home → Enter Data** → create a table with any single column
2. Rename the table to `\_Measures` (or `\_ *Measures`)
3. Load the table — it now appears in the model with one column

### 2. Create the first measure in the group

1. Right-click the table → **Create a measure**
2. Write any simple expression (e.g., `Total = 1`)
3. The table is now a measures group — you can delete the original column

### 3. Delete the column

- Right-click the column in the data view → **Delete from model**
- The column disappears; the table remains as an empty container

### 4. Assign display folders

1. Switch to **Model view**
2. Select the measure → open the **Properties pane**
3. Find **Display folder** and type: `Average Score` or `Average Score\Visualization`
4. Use `\` (backslash) to create subfolders

## Subfolder Naming Convention

| Display folder value | Result |
|---------------------|--------|
| `Average Score` | Folder named "Average Score" |
| `Average Score\Visualization` | Subfolder "Visualization" inside "Average Score" |
| `KPIs\Financial` | Subfolder "Financial" inside "KPIs" |

## Benefits

- All measures visible in one place regardless of which data table they reference
- Clean model view — data columns separated from measures
- Subfolders mirror business domains or report sections

## Related

- [[Selection-Bookmarks-Panel-Organization]]
- [[Reusable-Project-Assets]]

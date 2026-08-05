---
created: 2026-08-02
updated: 2026-08-05
source: Enhancing Accessibility Developing Translated Views in Multilingual Power BI Reports.md
note_type: pattern
tags: [powerbi, field-parameters, internationalization, localization, axis]
---

# Language Field Parameter for Axis Translation

A field parameter that exposes both language columns of a dimension table (e.g. `AgeGroups[EN]` and `AgeGroups[FR]`) as switchable fields, with a `Language` column linked to the `Languages` table to sync axis labels with the language slicer.

## Purpose

Visual axis labels (the values on the X or Y axis) cannot be translated using the ID-based measure pattern — they are determined by the column values themselves, not by DAX measures. A language-aware field parameter solves this: when the user switches the language slicer, the field parameter's `Language` relationship causes Power BI to display the correct language column on the axis automatically.

## Structure

### 1. Dimension table with bilingual columns

Load from Excel (or Power Query):

| AgeGroupEN | AgeGroupFR | Order |
|------------|------------|-------|
| 15-24 | 15-24 | 1 |
| 25-54 | 25-54 | 2 |
| 55+ | 55+ | 3 |

### 2. Create field parameter

```
TR AgeGroups = {
    ("Age Groups (EN)", NAMEOF('AgeGroups'[AgeGroupEN]), 0),
    ("Age Groups (FR)", NAMEOF('AgeGroups'[AgeGroupFR]), 1)
}
```

Add a `Language` column to the field parameter table and connect it to `Languages[Language]`.

### 3. Assign to visual axis

Replace the visual's axis field with the new `TR AgeGroups` field parameter.

### 4. Sort by order

Configure the field parameter to sort by the `Order` column from the source dimension table.

## How It Works

- The `Languages[Language]` column added to the field parameter table creates an implicit relationship to the `Languages` table.
- When the language slicer changes, the relationship activates the row whose `Language` column matches — this selects the EN or FR column.
- The visual axis displays the correct language values without any measure on the axis.

## Key Rules

- Requires one field parameter per axis that needs translation.
- The `Language` column on the field parameter table is the sync mechanism — it must connect to `Languages[Language]`.
- Sorting: use the `Order` column from the source dimension table to maintain logical sort order across languages.
- Works for any dimension table with bilingual columns — repeat the pattern per table.

## Variations

- **Three or more languages:** Add additional columns (DE, ES, etc.) to the dimension table and extend the field parameter tuples.
- **Disconnected translation table:** For axis values that don't come from a dimension table, use a dedicated translation table with `OriginalValue`, `Language`, `TranslatedValue` columns and a `MAXX(FILTER(...))` pattern in a measure.

## Related

- [[selected-language-measure]]
- [[translation-id-based-dax-measures]]
- [[multilingual-report-translated-views]]

---
created: 2026-08-02
updated: 2026-08-05
source: Enhancing Accessibility Developing Translated Views in Multilingual Power BI Reports.md
note_type: workflow
tags: [powerbi, internationalization, localization, field-parameters, dax, accessibility]
---

# Multilingual Report — Translated Views

Build a bilingual (or multilingual) Power BI report where users can switch between languages via a slicer. Visual titles, text boxes, and axis labels all update dynamically.

## Prerequisites

- A Power BI report with data and basic visuals already built in one language.
- Excel parameters file (or Power Query tables) with translation columns for each dimension table and a translations lookup table.
- Power BI Desktop with field parameters feature (May 2022+).

## Steps

### 1. Identify translatable elements

Review all visuals and identify every text element that needs translation:

- Visual titles and subtitles
- Text boxes and labels
- Axis values (category labels)
- Tooltips

Categorise by whether the element comes from a data column or is hardcoded text.

### 2. Create dimension tables with bilingual columns

For each dimension table that feeds axis values, add translated columns (e.g. `AgeGroupEN`, `AgeGroupFR`). Include an `Order` column for custom sort order.

Load into Power BI and connect to the fact table alongside the original column.

### 3. Create the Translations table

Prepare a lookup table with columns: `ID`, `Language`, `Text`. One row per element per language.

| ID | Language | Text |
|----|----------|------|
| 1 | en | Dashboard Title |
| 1 | fr | Titre du Tableau de Bord |
| 2 | en | By Gender |
| 2 | fr | Par Genre |
| ... | ... | ... |

Load into Power BI as a disconnected table (no relationships).

### 4. Create the Languages table

A simple lookup table providing the language codes used in the slicer:

| Language |
|----------|
| en |
| fr |

Load into Power BI. This table drives the slicer and the `Selected language` measure.

### 5. Create the Selected Language measure

```dax
Selected language =
    IF(
        SELECTEDVALUE(Languages[Language]) = "",
        "en",
        SELECTEDVALUE(Languages[Language])
    )
```

### 6. Create translation measures (one per text element)

Template:

```dax
TR <Element> =
VAR translation_id = <N>
RETURN
    CALCULATE(
        FIRSTNONBLANK(Translations[Text], 1),
        FILTER(
            Translations,
            Translations[ID] = translation_id &&
            Translations[Language] = [Selected language]
        )
    )
```

Assign each measure to its visual title, subtitle, or text box.

### 7. Create language field parameters for axes

For each axis that needs translation:

1. Create a field parameter exposing both language columns:
   ```
   TR <Dimension> = {
       ("Label (EN)", NAMEOF('<Table>'[<ColEN>]), 0),
       ("Label (FR)", NAMEOF('<Table>'[<ColFR>]), 1)
   }
   ```
2. Add a `Language` column to the field parameter table and connect it to `Languages[Language]`.
3. Replace the visual axis field with the new field parameter.
4. Sort by the `Order` column from the source dimension table.

### 8. Add the language slicer

Insert a slicer visual bound to `Languages[Language]`. This is the user's language toggle. Place it prominently on the report page.

### 9. Test

Toggle between languages and verify all titles, subtitles, text boxes, and axis labels update correctly.

## Variations

- **Three or more languages:** Extend the `Languages` table, add columns to each dimension table, extend field parameter tuples, and add rows to the `Translations` table.
- **HTML Content visual for titles:** Use the HTML Content custom visual instead of native text boxes for titles — it supports HTML and performs better on heavy reports.
- **Translation table in SharePoint/Excel Online:** Store the translations file externally and refresh on schedule, so translators can update without republishing the report.

## Related

- [[selected-language-measure]]
- [[translation-id-based-dax-measures]]
- [[language-field-parameter-for-axis-translation]]

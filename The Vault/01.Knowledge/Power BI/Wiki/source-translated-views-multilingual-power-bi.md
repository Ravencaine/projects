---
created: 2026-08-02
source: Enhancing Accessibility Developing Translated Views in Multilingual Power BI Reports.md
note_type: source
tags: [powerbi, internationalization, localization, tutorial, field-parameters]
---

# Source: Enhancing Accessibility — Developing Translated Views in Multilingual Power BI Reports

> Author: Isabelle Bittar
> Published: 2023-06-01
> URL: https://medium.com/@isabittar/enhancing-accessibility-developing-translated-views-in-multilingual-power-bi-reports-5ca20d41217a

## Introduction

Power BI has no native automatic translation feature. Using field parameters (May 2022+) and DAX, a report can be built to let users switch between languages within the report itself.

## Step 1: Load and Prepare Data

Load the data into Power BI and apply minor transformations in Power Query.

## Step 2: Build the Initial View

Build all visuals in one language (e.g. English) first. Identify all text elements that will need translation.

## Step 3: Create Dimension Tables with Bilingual Columns

For each dimension table feeding axis values, add translated columns:

| AgeGroupEN | AgeGroupFR | Order |
|------------|------------|-------|
| 15-24 | 15-24 | 1 |
| 25-54 | 25-54 | 2 |
| 55+ | 55+ | 3 |

Load into Power BI and connect to the fact table.

## Step 4: Create the Translations Table

A disconnected lookup table (no relationships to the data model):

| ID | Language | Text |
|----|----------|------|
| 1 | en | Dashboard Title |
| 1 | fr | Titre du Tableau de Bord |
| 2 | en | By Gender |
| 2 | fr | Par Genre |
| ... | ... | ... |

## Step 5: DAX Language Table and Translation Measures

**Languages table:**

| Language |
|----------|
| en |
| fr |

**Selected Language measure:**

```c
Selected language =
VAR selected_language = SELECTEDVALUE(Languages[Language])
VAR value_to_return =
    IF(
        selected_language = "",
        "en",
        selected_language
    )
RETURN value_to_return
```

**Translation measure (template):**

```c
TR By Gender =
VAR translation_id = 4
VAR translated_text =
    CALCULATE(
        FIRSTNONBLANK(Translations[Text], 1),
        FILTER(
            Translations,
            Translations[ID] = translation_id &&
            Translations[Language] = [Selected language]
        )
    )
RETURN translated_text
```

Apply to visual titles via **Title → Dynamic title → Field value** and to text boxes via the field property. The HTML Content custom visual is recommended for heavy reports.

## Step 6: Field Parameters for Axis Translation

For each axis requiring translation:

1. Create a field parameter exposing both language columns:
   ```
   TR AgeGroups = {
       ("Age Groups (EN)", NAMEOF('AgeGroups'[AgeGroupEN]), 0),
       ("Age Groups (FR)", NAMEOF('AgeGroups'[AgeGroupFR]), 1)
   }
   ```
2. Add a `Language` column to the field parameter table and connect it to `Languages[Language]`.
3. Replace the visual axis with the field parameter.
4. Sort by the `Order` column.

## Step 7: Insert the Language Slicer

Insert a slicer bound to `Languages[Language]`. This is the user's language toggle. Test that all titles, subtitles, text boxes, and axes update correctly for each language.

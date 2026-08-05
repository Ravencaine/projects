---
created: 2026-08-02
source: Enhancing Accessibility Developing Translated Views in Multilingual Power BI Reports.md
note_type: pattern
tags: [powerbi, dax, internationalization, localization, translations]
---

# Translation ID-Based DAX Measures

One DAX measure per translatable text ID that uses `CALCULATE + FILTER` over a `Translations` table to return the text in the currently selected language.

## Purpose

Power BI has no native translation feature. This pattern creates a separate measure for each translatable element (titles, subtitles, text boxes, labels). Each measure reads a row from the `Translations` table where `ID` matches and `Language` matches `[Selected language]`. The result is a dynamically translated string that updates when the user changes the language slicer.

## Structure

```dax
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

Generic template:

```dax
TR <Element Name> =
VAR translation_id = <N>
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

## How It Works

1. `translation_id` — a hardcoded integer identifying which row in the `Translations` table holds this text.
2. `CALCULATE(FIRSTNONBLANK(...), FILTER(...))` — evaluates FIRSTNONBLANK under a modified filter context where both `ID` and `Language` must match.
3. `FIRSTNONBLANK(Translations[Text], 1)` — returns the text value for the matching row.
4. The measure returns blank if no matching row is found.

## Translations Table Structure

| ID | Language | Text |
|----|----------|------|
| 1 | en | Dashboard Title |
| 1 | fr | Titre du Tableau de Bord |
| 4 | en | By Gender |
| 4 | fr | Par Genre |

The `Languages` table provides the slicer values:

| Language |
|----------|
| en |
| fr |

## Key Rules

- One measure per translatable element — the ID is the only thing that changes.
- The `Translations` table does not need to be connected to the data model (no relationships required).
- Applied to visual titles via **Title → Dynamic title → Field value** and to text boxes via the field property.
- The HTML Content custom visual can render these measures with HTML support, useful for heavy reports.

## Related

- [[selected-language-measure]]
- [[language-field-parameter-for-axis-translation]]
- [[multilingual-report-translated-views]]

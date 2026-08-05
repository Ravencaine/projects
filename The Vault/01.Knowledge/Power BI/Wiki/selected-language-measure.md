---
created: 2026-08-02
updated: 2026-08-05
source: Enhancing Accessibility Developing Translated Views in Multilingual Power BI Reports.md
note_type: pattern
tags: [powerbi, dax, internationalization, localization, measure]
---

# Selected Language Measure

A DAX measure that reads the user's current language selection from a `Languages` table and defaults to English ("en") if no selection is active.

## Purpose

Acts as the central selector for the entire multilingual reporting system. Every translation measure references this measure to determine which language column to pull from the `Translations` table. It must be placed in every formula that returns translated text.

## Structure

```dax
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

## How It Works

1. `SELECTEDVALUE(Languages[Language])` — reads the active value from the language slicer (connected to the Languages table).
2. `IF(selected_language = "", "en", selected_language)` — if no slicer selection is made (blank), defaults to English.
3. The returned string ("en", "fr", etc.) is passed to translation measures via the `CALCULATE + FILTER` pattern.

## Key Rules

- The `Languages` table must have a `Language` column with ISO codes or keys matching the `Translations` table.
- This measure must be referenced in every translation measure — it is the single source of truth for which language is active.
- A slicer on `Languages[Language]` drives the selection. The slicer itself is the user's language toggle.

## Related

- [[translation-id-based-dax-measures]]
- [[language-field-parameter-for-axis-translation]]
- [[multilingual-report-translated-views]]

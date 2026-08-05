---
created: 2026-07-27
updated: 2026-08-02
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: pattern
tags: [many-to-many, bridge-table, survey-data, power-bi, data-modeling]
---

# Many-to-Many Bridge Table Pattern

A data modelling pattern that resolves survey response many-to-many relationships cleanly using an intermediate bridge table — avoiding the performance cost of Power BI's native many-to-many relationship option.

## Purpose

Survey data has a natural many-to-many structure: one respondent can choose multiple answers, and one answer can be chosen by multiple respondents. Naively joining survey_responses → dim_survey_options directly causes duplicate respondent counts. Power BI's native many-to-many option works but adds engine burden. A bridge table keeps the relationship one-to-one and COUNTX efficient.

## Components

- `fact_survey_responses` — one row per respondent per survey
- `bridge_survey_options` — one row per respondent per selected answer
- `dim_survey_options` — one row per distinct answer option
- `COUNTX(bridge_survey_options, 1)` or `COUNTX(bridge_survey_options[AnswerKey], DISTINCT(...))` — clean count

## Structure

```
fact_survey_responses
  RespondentKey (FK)
  SurveyKey (FK)
  → bridge_survey_options
      RespondentKey (FK)
      AnswerKey (FK)
      → dim_survey_options
          AnswerKey (PK)
          AnswerName
```

## Why Not Power BI Native Many-to-Many?

The native many-to-many relationship exists and works, but:
- Adds computation overhead on cross-filter evaluation
- Can produce unexpected results in aggregate visuals when context is ambiguous
- Requires careful handling in measures (DISTINCTCOUNT is often needed to de-duplicate)
- A bridge table makes the relationship explicit and COUNTX unambiguous

## Related

- [[surrogate-keys-vs-composite-keys]] — keys used on bridge table
- [[star-schema-vs-snowflake-schema]] — the schema pattern this fits into

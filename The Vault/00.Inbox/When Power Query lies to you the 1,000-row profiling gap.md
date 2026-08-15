---
title: "When Power Query lies to you: the 1,000-row profiling gap"
source: "https://medium.com/microsoft-power-bi/when-power-query-lies-to-you-the-1-000-row-profiling-gap-a994bcf2079e"
author:
  - "[[Lin]]"
published: 2026-03-25
created: 2026-08-09
description: "Zero errors in the editor. A failed refresh by morning. The sampling default that has been hiding bad data in plain sight"
Processed: "Unprocessed"
---
## Zero errors in the editor. A failed refresh by morning. The sampling default that has been hiding bad data in plain sight

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*y3HEgTD2Ub9ZXwHuNLZH7w.png)

The editor said clean. The full dataset disagreed

You check the Column Quality bar before publishing. Zero errors. You hit publish, the scheduled refresh runs overnight, and by morning there’s a failure email: `DataFormat.Error: We couldn't convert to Number`. The editor said everything was fine. It wasn't - it just never looked past row 1,000.

The questions this solves:

- Why does Power Query show 0% errors in the editor when my scheduled refresh fails with a type conversion error?
- What does “Column profiling based on entire dataset” actually change, and why isn’t it the default?
- How do I stop a single “N/A” value from taking down a refresh for 200,000 rows?
- Where in the Applied Steps pane does the error-handling step need to go?

> Study guide coverage: This article targets the Prepare data domain of the [Power BI Data Analyst study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300), the topic is Profile, clean, and shape data in Power Query Editor

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

Here’s the two-step fix, before the explanation.

```c
// Before — no error handling; crashes on the first unconvertible value
Table.TransformColumnTypes(Source, {{"SalesAmount", type number}})

// After — replace bad values with null first, then cast
Table.TransformColumnTypes(
    Table.ReplaceErrorValues(Source, {{"SalesAmount", null}}),
    {{"SalesAmount", type number}}
)
```

Wrap `Table.ReplaceErrorValues` around your source before `Table.TransformColumnTypes` runs. Any value that can't become a number becomes null instead of a crash. The refresh completes.

## The problem nobody names

[*The Column Quality, Column Distribution, and Column Profile*](https://learn.microsoft.com/en-us/power-query/data-profiling-tools) views in Power Query Editor are genuinely useful. But they share a default most analysts never notice: they profile the first 1,000 rows of your dataset, not all of them.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lEtvlEJBM47ae0FfuwZzVg.png)

Default scope can hide errors in larger datasets

That default sits in the status bar at the bottom of the editor. When you open Column Quality, it reads “Column profiling based on top 1,000 rows.”

> To switch it, go to **View** and toggle **Column profiling based on entire dataset**. One click. The catch: this setting doesn’t save with the `.pbix` file. It resets every time you reopen Power Query Editor. It's a session-level display toggle, not a query property.

That’s where the gap opens. Your source has 200,000 rows. Rows 1 through 1,000 are clean. Row 47,382 has “N/A” in a column your query expects to be numeric, entered manually in the source system six months ago. Power Query Editor shows 0% errors, 0% empty, 100% valid. You publish.

![](https://miro.medium.com/v2/resize:fit:1274/format:webp/1*vCngk_S-nPnVnCeHsew6bw.png)

Profiling is capped at the first 1,000 rows by default

The scheduled refresh in the Power BI service doesn’t use the editor’s sampling logic. It runs the full query against the full dataset. When `Table.TransformColumnTypes` hits "N/A" and tries to convert it to `type number`, it throws `DataFormat.Error` and stops. The entire refresh fails, not just that row. The dataset stays on the previous version with no partial load and no row-level warning.

The deeper issue is step ordering. `Table.TransformColumnTypes` is not forgiving: it doesn't skip problem rows or coerce values, it errors out. Without an error-handling step before it, there's nothing to absorb the failure when it eventually runs against data the editor never showed you.

## Friction analysis

*What teams do today vs the corrected approach*

## How the engine actually handles this

The friction table points to a specific ordering problem in the Applied Steps pane. Understanding why it works this way makes the fix feel obvious rather than arbitrary.

When the Power BI service runs a scheduled refresh, it executes the M query from the first Applied Step to the last, against the full live data source, with no sampling. `Table.TransformColumnTypes` tells the Mashup Engine to reinterpret every value in the named column as the declared type. If a value can't be coerced - "N/A", "TBD", an empty string - the engine raises an error on that cell. Because there's no error boundary around it, the error propagates up and terminates the entire query.

`Table.ReplaceErrorValues` intercepts at the row level, before the type cast runs. It scans the column for any value that would produce an error and substitutes the replacement you specify. The Mashup Engine then runs `Table.TransformColumnTypes` on a column that contains no unconvertible values. Nulls cast cleanly to `type number` as null.

Order is everything here. `ReplaceErrorValues` must wrap the source, not the output of `TransformColumnTypes`. By the time `TransformColumnTypes` has failed, there's nothing left to replace.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*P0-z7izKMz0WNRW-FlGTGw.png)

Default preview vs. full dataset error handling

## Performance impact

Operational impact of adding the `*ReplaceErrorValues*` guard

One more constraint worth naming before moving on: `Table.ReplaceErrorValues` substitutes null, not zero. If your downstream measures use `SUM` or `AVERAGE`, null rows are excluded from the aggregation, which is usually what you want. If a business rule says "N/A" means zero, add a `Table.ReplaceValue` step after the null substitution, targeting null values in that column specifically.

## Your next steps

- ☐ **Today — audit profiling scope:** Open any published report with numeric or date columns from a spreadsheet. In Power Query Editor, go to **View → Column quality** and switch the status bar to **Column profiling based on entire dataset**.
- ☐ **Today — find unguarded type steps:** In the Applied Steps pane, look for `Changed Type` appearing immediately after `Source`. Flag each one—those queries have no error handling.
- ☐ **This week — add the guard:** In the Advanced Editor, wrap `Table.ReplaceErrorValues` as a named step before every `Table.TransformColumnTypes` call.
```c
#"Replaced Errors" = Table.ReplaceErrorValues(
    #"Promoted Headers", {{"SalesAmount", null}}
),
#"Changed Type" = Table.TransformColumnTypes(
    #"Replaced Errors", {{"SalesAmount", type number}}
)
```
- ☐ **This week — validate in the service:** Republish and confirm the refresh completes. A successful refresh with nulls confirms the guard is working.
- ☐ **This week — surface nulls to consumers:** Add a measure or visual-level filter that flags blank values so data quality problems are visible to consumers.

## References

1. [*Microsoft Docs: Table.ReplaceErrorValues -Power Query M reference*](https://learn.microsoft.com/en-us/powerquery-m/table-replaceerrorvalues)
2. [*Prepare for Microsoft Power BI Data Analyst PL-300 exam*](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/?practice-assessment-type=certification#certification-prepare-for-the-exam)

> Follow me on [**Medium**](https://medium.com/@dataengklin88), and [**LinkedIn**](https://www.linkedin.com/in/linthedataguy/) for updates. If something here sparks a question or saves you a debugging session, that’s exactly why I write.

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----a994bcf2079e---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Model, Power Query

**Tags:** Tutorial, Data Model, Power Query
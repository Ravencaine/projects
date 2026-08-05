---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
source_url: https://www.packtpub.com/product/dax-for-humans/9781835466612
note_type: source
tags: [dax, deckler, packt, 2025, book, no-calculate]
---

# DAX for Humans (Greg Deckler, Packt 2025)

Greg Deckler's contrarian guide to DAX — teaching the language without CALCULATE as the centrepiece.

> **Type:** book
> **Author:** Greg Deckler
> **Published:** September 2025
> **URL:** https://www.packtpub.com/product/dax-for-humans/9781835466612
> **Routed to:** DAX Code

## Summary

Greg Deckler flips the conventional DAX teaching order: instead of starting with CALCULATE (the "most important and powerful function"), Deckler argues it's the source of DAX's reputation for difficulty, and that a No CALCULATE approach — FILTER + iterator (SUMX/MAXX/MINX) — is more learnable, debuggable, and maintainable. The book teaches the Banana Pattern as the foundational DAX mental model: VAR to define exclusion logic, FILTER to construct the working table, X aggregator to compute the result.

The book is structured around a single data model (Table with Item, Price, Quantity, Total Cost, Date columns) that is reused across all 21 chapters, giving the reader deep familiarity with a consistent model rather than constant context-switching. The foreword by Brian Julius describes a 30-day experiment abandoning CALCULATE entirely, which became the seed for this book's philosophy.

## Key Claims

- CALCULATE is not "the most important function in DAX" — it's a "fancy FILTER" that makes debugging harder
- The Banana Pattern (FILTER + X aggregator) can solve most DAX problems without CALCULATE
- DAX's difficulty stems from the teaching approach (starting with CALCULATE) rather than the language itself
- Integer offsets on a date table are superior to DAX's built-in time intelligence functions
- CALCULATE context transition is opaque — the "devil in the details"
- DAX can solve problems most people don't expect: Haversine distances, ATAN2, Kaplan-Meier survival curves, fuzzy text matching, SVG star ratings

## Notable Details

- **Banana data model**: All examples use a "Table" table with columns: Item (Pickle, Banana, Grapefruit), Price, Quantity, Total Cost, Date. The Banana serves as the recurring example throughout Ch1–2.
- **Chapter structure**: 21 chapters, ~42K–50K chars each. Ch1–2 = foundations. Ch3–6 = core data types (dates, text, numbers, time). Ch7–11 = business KPIs (customers, HR, projects, finance, operations). Ch12–14 = advanced (spatial, complex patterns). Ch15 = performance optimization. Ch16 = AI debugging and CALCULATE deconstruction.
- **Brian Julius foreword**: Documents Greg's 2020 "CALCUHATE" forum post and the 30-day experiment that followed.
- **No third-party dependencies**: All examples use only built-in Power BI Desktop and DAX.
- **GitHub repo**: github.com/gdeckler/DAX-For-Humans — includes .pbix files for each chapter.
- **Deckler's thesis on CALCULATE**: CALCULATE's two-argument model (expression + filter) hides context transition, making it impossible to trace intermediate values. The No CALCULATE approach exposes every step as a VAR.
- **Key gotchas covered**: TRUNC vs INT sign bug, MEDIAN even-count bug, CALCULATE context transition, circular dependencies, MOD with large numbers.
- **Functions introduced or re-examined**: ATAN2 (no native — implemented from scratch), GAMMA (no native — Lanczos approximation), TRIMMEAN (no native), UNICHAR (for SVG, barcodes, Unicode tricks), EVALUATEANDLOG (debugging), TOCSV (debugging).
- **AI chapter**: BIM file export → feed to LLM → context-aware DAX. Process pioneered by patron Brian Julius.

## Extracted Notes

Links to notes derived from this source:

### Foundational Concepts
- [[no-calculate-banana-pattern]] — `pattern` — the foundational FILTER + iterator pattern (Ch1)
- [[dax-variables-var-return]] — `atomic` — VAR/RETURN for clarity and debugging (Ch1)
- [[x-aggregators-sumx-minx-maxx]] — `pattern` — X aggregator vs scalar aggregator (Ch1)
- [[dax-context-row-filter]] — `atomic` — row context and filter context (Ch1)
- [[no-calculate-vs-calculate-deckler]] — `comparison` — CALCUHATE argument vs traditional approach (Ch2, Ch16)
- [[dax-debugging-tocsv]] — `pattern` — TOCSV for table visualization during debugging (Ch2)
- [[lookup-without-calculate-filter-maxx]] — `pattern` — lookup via FILTER + MAXX (Ch2)
- [[dax-in-operator-containsrow]] — `pattern` — IN operator and CONTAINSROW (Ch2)

### Date & Time
- [[offset-based-date-calculations-deckler]] — `pattern` — offset columns replacing time intelligence (Ch3)
- [[date-table-calendar-addcolumns]] — `pattern` — CALENDAR + ADDCOLUMNS for date tables (Ch3)
- [[period-to-date-offset-pattern]] — `pattern` — YTD/QTD/MTD/WTD via offsets (Ch3)

### Numbers
- [[trunc-vs-int-dax]] — `gotcha` — TRUNC(-2.1) = -2, INT(-2.1) = -3 (Ch5)
- [[better-mod-workaround-dax]] — `pattern` — reliable MOD for large/negative numbers (Ch5)
- [[better-median-workaround-dax]] — `pattern` — MEDIANX workaround for even-count lists (Ch5)

### Business KPIs — Customers
- [[customer-churn-rate-dax]] — `pattern` — churn rate calculation (Ch7)
- [[net-promoter-score-nps-dax]] — `pattern` — NPS formula (Ch7)
- [[customer-lifetime-value-ltv-dax]] — `pattern` — LTV/CLV calculation (Ch7)
- [[market-basket-analysis-dax]] — `pattern` — items purchased together (Ch7)

### Business KPIs — HR
- [[employee-turnover-rate-etr-dax]] — `pattern` — ETR from HireDate/TermDate (Ch8)
- [[absenteeism-rate-dax]] — `pattern` — absenteeism vs PTO/holidays (Ch8)
- [[bradford-factor-dax]] — `pattern` — S² × D absenteeism weighting (Ch8)
- [[kaplan-meier-survival-estimator-dax]] — `pattern` — survival probability estimator (Ch8)
- [[gini-coefficient-dax]] — `pattern` — pay inequality index (Ch8)
- [[human-capital-value-added-hcva-dax]] — `pattern` — profit per employee (Ch8)

### Business KPIs — Projects
- [[project-burndown-chart-dax]] — `pattern` — burndown chart DAX (Ch9)
- [[earned-value-management-evm-dax]] — `pattern` — BCWS/BCWP/SV/CV/SPI/CPI (Ch9)

### Business KPIs — Finance
- [[modified-dietz-return-dax]] — `pattern` — Modified Dietz return (Ch10)
- [[reverse-year-to-date-dax]] — `pattern` — remaining period forecast (Ch10)

### Business KPIs — Operations
- [[on-time-in-full-otif-dax]] — `pattern` — OTIF supply chain KPI (Ch11)
- [[overall-equipment-effectiveness-oee-dax]] — `pattern` — OEE = Availability × Performance × Quality (Ch11)

### Advanced Patterns
- [[atan2-dax-no-native]] — `pattern` — ATAN2 implementation from ATAN (Ch12)
- [[haversine-distance-dax]] — `pattern` — great-circle distance (Ch12)
- [[disconnected-tables-deckler]] — `pattern` — disconnected tables for custom behaviour (Ch13)
- [[inverse-slicer-pattern-dax]] — `pattern` — NOT/inverse slicer (Ch13)
- [[and-slicer-multi-select-dax]] — `pattern` — AND logic multi-select (Ch13)
- [[svg-star-rating-dax]] — `pattern` — SVG star ratings via UNICHAR (Ch13)
- [[gamma-function-in-dax]] — `pattern` — GAMMA via Lanczos (Ch14)
- [[trimmean]] — `pattern` — TRIMMEAN implementation (Ch14)
- [[fuzzy-matching-levenshtein-dax]] — `pattern` — Levenshtein distance (Ch14)
- [[dax-index-pattern-deckler]] — `pattern` — row number without native (Ch14)
- [[streak-detection-in-dax]] — `pattern` — consecutive run detection (Ch14)

### Performance & Debugging
- [[dax-debugging-evaluateandlog]] — `pattern` — EVALUATEANDLOG logging (Ch16)
- [[bim-file-ai-dax-generation]] — `workflow` — AI DAX generation via BIM file (Ch16)
- [[dax-error-handling-iferror-iserror]] — `pattern` — error handling (Ch16)
- [[circular-dependencies-in-dax]] — `gotcha` — circular dependency causes and fixes (Ch16)
- [[calculate-internal-context-transition]] — `reference` — CALCULATE deep dive (Ch16)

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX for Humans.epub |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-29 |
| Word count | ~673,000 chars (17 chapters extracted) |
| Notes extracted | ~50+ pattern/atomic/gotcha/comparison notes |
| Status | Archived, notes in DAX Code Wiki |

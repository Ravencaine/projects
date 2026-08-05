---
created: 2026-07-28
source: Beginning Big Data with Power BI and Excel 2013 (Dunlop)
source_url:
note_type: source
tags: [power-bi, excel, powerpivot, power-query, power-view, power-map, azure, hadoop, hdinsight]
---

# Beginning Big Data with Power BI and Excel 2013 (Dunlop)

> **Type:** book
> **Author:** Neil Dunlop
> **Published:** 2015
> **URL:** www.apress.com/9781484205303
> **Routed to:** Power BI

## Summary

This Apress book (2015) positions Excel and Power BI as the practical self-service BI toolkit for small and medium businesses — a middle path between raw data and enterprise-scale Hadoop infrastructure. It covers the full stack: data modeling in PowerPivot, DAX formulas, Power Query (M), Power View reports, Power Map 3D geospatial visualization, Azure HDInsight, and Excel statistics. The central thesis is that tools practitioners already know can perform many of the same analytical functions as higher-end Apache tools.

## Key Claims

- Excel + Power BI can solve most "big data" problems for organizations that don't have Netflix-scale data needs
- PowerPivot introduces a relational data model (star schema) into Excel, enabling cross-table analysis
- DAX formulas are column-oriented (unlike cell-based Excel formulas), with CALCULATE as the key filter-context function
- Power Query (M) handles ETL: web scraping, JSON APIs, CSV folder imports, data cleaning
- Power Map (3D Maps) plots Excel data on Bing Maps with time animation
- Azure HDInsight brings Hadoop as a cloud service, with Hive providing SQL queries and Power Query pulling the results into Excel
- Historical data analysis (Priestley, Playfair, John Snow's cholera map) establishes the lineage of data visualization

## Notable Details

- SQL in Excel via PowerPivot Table Import Wizard and MSQuery: equijoin syntax, aggregate functions, multi-table JOINs
- The book predates Power BI Service (cloud workspaces, dashboards) — it covers only the Excel desktop tools
- Recommended approach for self-service BI: Azure Marketplace (free demographic/economic data) → Pivot Table → Power View → Power Map
- Contoso sample database (Tinyurl.com/PowerPivotSamples) used throughout for data model examples
- HDInsight chapter notes: 2015 Azure portal screenshots may differ from current Azure portal UX

## Extracted Notes

Links to notes derived from this source:

- [[big-data-is-the-fourth-factor-of-production]] — `atomic` — data as a production factor alongside land, labor, capital
- [[apache-hadoop-hdfs-mapreduce-architecture]] — `atomic` — HDFS + MapReduce framework
- [[nosql-cap-theorem]] — `atomic` — CAP theorem fundamentals
- [[newsql-relational-architecture-sql-nosql-scalability]] — `atomic` — NewSQL as a compromise
- [[sql-plus-plus-and-n1ql]] — `atomic` — SQL++ and N1QL for JSON data
- [[pivot-tables-create-group-slicer-timeline]] — `workflow` — full Pivot Table workflow
- [[pivot-charts-from-pivot-tables]] — `pattern` — Pivot Charts visualization
- [[power-view-reports-table-matrix-bar-chart-map]] — `pattern` — Power View report types
- [[hdinsight-power-query-pivot-table-power-map-pipeline]] — `pattern` — end-to-end Azure pipeline
- [[azure-hdinsight-provision-cluster-hive-query-download-results]] — `workflow` — HDInsight setup and query
- [[power-map-install-layer-tour-bubble-heat-region-time-animation]] — `workflow` — Power Map features
- [[camden-success-story-56-percent-reduction]] — `atomic` — Brenner's 56% cost reduction via heat maps
- [[big-data-healthcare-roi]] — `atomic` — McKinsey's 12–17% healthcare savings estimate
- [[star-schema-fact-table-dimension-tables-in-powerpivot]] — `pattern` — star schema in PowerPivot
- [[powerpivot-data-model-load-access-diagram-view-relationships]] — `pattern` — PowerPivot data model setup
- [[dax-is-column-oriented]] — `atomic` — column vs. cell formula distinction
- [[calculated-column-vs-calculated-field]] — `atomic` — DAX context types
- [[dax-calculate-function]] — `function` — filter-based DAX aggregation
- [[dax-sumx-function]] — `function` — row-by-row iteration
- [[dax-left-function]] — `function` — text extraction
- [[dax-aggregate-functions-average-min-max]] — `function` — aggregate measures
- [[dax-operators]] — `reference` — full operator reference
- [[dax-year-over-year]] — `pattern` — CALCULATE + calculated field composition
- [[dax-kpi-create-key-performance-indicator]] — `workflow` — KPI creation steps
- [[sql-select-syntax-reference]] — `reference` — SQL SELECT clause reference
- [[sql-aggregate-functions]] — `reference` — COUNT, SUM, MIN, MAX, AVG
- [[sql-equijoin-vs-cartesian-product]] — `pattern` — JOIN vs. WHERE-less cross product
- [[power-query-import-multiple-csv-files-from-folder]] — `pattern` — folder import pattern
- [[power-query-group-by-single-dual-triple-field]] — `pattern` — Group By aggregations
- [[power-query-import-json-from-web-api]] — `pattern` — JSON import and multi-level expand
- [[power-query-import-tables-from-web-pages]] — `pattern` — web table scraping
- [[excel-analysis-toolpak-descriptive-statistics-histogram]] — `workflow` — ToolPak enable and use
- [[descriptive-statistics-mean-median-mode-variance-stddev]] — `reference` — statistical functions
- [[dax-68-95-99-rule]] — `reference` — Three Sigma Rule of Thumb
- [[scatter-chart-with-r-squared-trendline]] — `pattern` — Excel scatter chart + R²

## Metadata

| Field | Value |
|-------|-------|
| Source file | Beginning Big Data With Power B - Neil Dunlop.pdf |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-28 |
| Word count | ~30,000 |
| Pages | 258 |

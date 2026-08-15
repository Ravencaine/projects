---
created: 2026-07-26
updated: 2026-08-02
note_type: index
tags: [data-modeling, index]
---

# Data Modeling — Knowledge Base Index

This is the index for the Data Modeling knowledge base. 47 notes grouped by type.

| [[star-schema-fact-table-principles]] | Star Schema FACT Table Design Principles

Grain, dimension types, additive/non-additive, PK-FK, fact table types (transaction/snapshot/accumulating) |
| [[star-schema-double-timestamp-pattern]] | Double Timestamp Pattern

order_date_key + warehouse_processing_date_key; handles late arrivals without breaking historical trends |
| [[star-schema-degenerate-dimensions]] | Degenerate Dimensions

Transaction IDs stored in fact table; saves 40% storage vs separate dimension table |
| [[star-schema-late-arrival-handling]] | Late Arrival Handling

is_late_arrival flag + original_expected_date_key; auto-adjusts reports without breaking history |
| [[star-schema-denormalized-metrics]] | Denormalized Metrics — Pre-Computed Exchange Rates

Pre-denormalize exchange rates at load time; avoids join at query time for multi-currency |
| [[star-schema-multi-key-partitioning]] | Multi-Key Partitioning (Time AND Geography)

PARTITION BY (quarter, region_id) instead of date alone; 60% compute cost reduction |
| [[star-schema-zstd-encoding-clustering]] | ZSTD Encoding + Clustering (500GB to 70GB)

ZSTD column encoding; ORDER BY (customer_id, transaction_id); 86% compression, 40% faster queries |
| [[star-schema-rollup-flags-pattern]] | Rollup Flags Pattern — Replaces 20 Materialized Views

is_monthly_summary + is_regional_summary flags; dashboard query hits pre-aggregated rows; 2min to 3sec |
| [[star-schema-referential-integrity-rely]] | Referential Integrity with RELY Constraint

FOREIGN KEY with RELY; cloud warehouse planner eliminates unused joins; 12sec to 0.8sec |
| [[star-schema-grain-locking-constraint]] | Grain Locking with UNIQUE Constraint

UNIQUE (transaction_id, product_id); prevents silent duplicate counting at database level |
| [[star-schema-performance-framework]] | Star Schema Performance Framework (5-Step Summary)

5-step framework: lock grain, PK-FK, pre-aggregate, test vs flat baseline, document and monitor |
| [[star-schema-fact-tables-source]] | Star Schema FACT Tables — Source

12 real-world patterns from production fire drills; flat file 4hr to star 36min; 500GB to 70GB |
## Schema Patterns  (39 notes)

| Note | Description |
|------|-------------|
| [[Jesse Ruiz]] | Jesse Ruiz (she/they)

Data engineering and Power BI content creator on Medium, specialising in dimensional modeling for |
| [[QUESTIONS]] | Open Questions

(None yet — questions surface here after ingestion, health checks, or during note-writing.)

Open questi |
| [[advanced-dimensional-modeling-retail-product-variants-source]] | Advanced Dimensional Modeling for Retail Product Variants (Parts 1–3)

Three-part Medium series by Jesse Ruiz covering t |
| [[batch-processing-vs-stream-processing]] | Batch Processing vs Stream Processing

Two fundamental data processing paradigms distinguished by latency, complexity, a |
| [[column-pruning-bravo]] | Column Pruning with Bravo for Power BI

The process of removing unused columns from a Power BI model to reduce memory fo |
| [[composite-key-strategy-itemkey]] | Composite Key Strategy (CONCAT-based ItemKey)

A key design pattern that generates a single, unique ItemKey for every ro |
| [[conditional-joins-case-concat-matching]] | Conditional Joins via CASE/CONCAT Matching

A SQL join pattern that applies different matching column sets to different  |
| [[data-modeling-bi-trustworthy-analytics]] | In BI work, people often focus on dashboards first. |
| [[data-warehousing-bi]] | If BI is about making better decisions, data warehousing is the system that makes those decisions trustworthy and repeat |
| [[database-key-types]] | Database Key Types

Primary Key

A field (or fields) that uniquely identifies each record in a table. |
| [[degenerate-dimension-barcode-in-fact]] | Degenerate Dimension (Barcode in Fact)

A dimensional modelling pattern where a low-cardinality attribute (Barcode) is s |
| [[differential-privacy-smartnoise]] | Differential Privacy — SmartNoise

A mathematical guarantee that adding noise to individual data points prevents re-iden |
| [[dim-date-dax-calendar]] | dim_date DAX (CALENDAR + ADDCOLUMNS)

A reusable DAX expression for building a complete date dimension table in Power BI |
| [[dimension-groups-color-style-size-config]] | Dimension Groups (Color / Style / Size / Config)

The D365 F&O concept that defines which variant attributes apply to a  |
| [[duplicate-barcodes-retailshowforitem-filter]] | Duplicate Barcodes (retailshowforitem Filter)

Symptom: a barcode scan returns multiple rows in the dimension — a barcod |
| [[import-vs-directquery-performance]] | Import vs DirectQuery Performance

Summary

Import reads data from memory and is faster for most models. |
| [[incremental-refresh-pattern]] | Incremental Refresh Pattern

A Power BI configuration that limits refresh scope to recent partitions — dramatically redu |
| [[index-strategy-filtered-index-barcode]] | Index Strategy (Filtered Index on Barcode)

Index design pattern for product dimensions: standard indexes on join keys,  |
| [[is-data-cleaning-more-painful-than-building-models]] | — A Data Analyst’s Perspective from 20+ Years in the Field


When people imagine data analysis, they picture sleek dashb |
| [[lambda-kappa-architecture]] | Lambda and Kappa Architecture

Two patterns for combining batch and stream processing to serve both historical accuracy  |
| [[materialized-views-vs-regular-views-cetas]] | Materialized Views vs Regular Views (CETAS)

Performance strategy for pre-computing complex dimension views — choosing b |
| [[medallion-architecture]] | Medallion Architecture (Bronze / Silver / Gold) ⭐ extended 2026-08-13

A layered data lake organisation pattern that progressively cleanses an |
| [[missing-prices-debug-root-cause]] | Missing Prices (Debug + Root Cause)

Symptom: a variant row exists in the dimension but RetailPrice = 0 or NULL. |
| [[ml-data-formats-csv-parquet-json]] | Data Formats for ML — CSV, Parquet, JSON, Plain Text

Four common formats for storing data used in ML pipelines. |
| [[normalization-3nf]] | Normalization and 3NF

Why Normalize

The core principle of relational database design: avoid repeating fields. |
| [[performance-degradation-over-time]] | Performance Degradation Over Time

Symptom: a dimension view that took 30 seconds last month now takes 2 minutes. |
| [[power-bi-visual-performance]] | Power BI Visual Performance

Visualisation complexity directly impacts report rendering time. |
| [[powerpivot-diagram-view]] | PowerPivot Diagram View

A visual canvas in PowerPivot showing all tables in the Data Model and the relationships betwee |
| [[pricing-cte-with-row-number-deduplication]] | Pricing CTE with ROW_NUMBER Deduplication

A CTE pattern that isolates PriceDiscTable rows per item and picks a determin |
| [[remove-pii-from-datasets]] | Remove PII from Datasets

Identify and remove or mask personally identifiable information before using data in AI/ML pip |
| [[replicated-table-distribution]] | Replicated Table Distribution

A table distribution strategy for Azure Synapse dedicated SQL Pool that broadcasts a dime |
| [[role-playing-dimension]] | Role-Playing Dimension

A dimensional modelling pattern where the same dimension table is joined to a fact table multipl |
| [[shared-dimensions-multi-fact]] | Shared Dimensions with Multiple Fact Tables

Use one set of shared dimensions across all fact tables — not one dimension per fact |
| [[conformed-dimensions]] | Conformed Dimensions

Identical dimension definitions shared across fact tables, enabling cross-fact aggregation |

Shared dimensions reduce model size, speed refresh, and enable clean cross-fact reporting |
|| [[pitfall-duplicating-dimensions]] | Pitfall: Duplicating Dimensions Per Fact Table

Creates separate dimension copies per fact — bloats model, slows refresh, breaks cross-fact reports |
|| [[pitfall-consolidated-fact-tables]] | Pitfall: Consolidated (Appended) Fact Tables

Appending fact tables into one creates blank values from unmatched fact-specific keys |
|| [[implementing-star-schema-multi-fact]] | Implementing Star Schema with Multiple Fact Tables

6-step workflow: identify shared dims, import once, create relationships, test cross-fact |
| [[simple-vs-variant-products]] | Simple vs Variant Products

The two fundamental product types in a retail dimension — each requiring different join and  |
| [[handling-multiple-fact-tables-in-power-bi-source]] | Handling Multiple Fact Tables in Power BI — Source

Article by Boniface Muchendu (DataBear) on multi-fact star schema; extracted 5 notes |
| [[kimball-dimensional-modeling-case-study-baylas-2026.md]] | Kimball Dimensional Modeling Case Study — Baylas 2026

Real-world data warehouse from scratch using Kimball + medallion + ELT; covers methodology choice, three-layer architecture, common cleansing problems, dimensional decisions, and data quality philosophy |
| [[slow-power-bi-report-optimization-workflow]] | Source: Stop Building Slow Power BI Reports — A Data Pro's Checklist

> Type: article
> Author: unknown (file missing fr |
| [[star-schema-fact-table-dimension-tables-in-powerpivot]] | Star Schema: Fact Table + Dimension Tables in PowerPivot

A star schema organizes data in a central fact table surrounde |
| [[star-schema-vs-snowflake-schema]] | Star Schema vs Snowflake Schema

Summary

Star Schema is simpler and faster — single-hop joins from fact to dimension. |
| [[surrogate-keys-vs-composite-keys]] | Surrogate Keys vs Composite Keys

Using integer surrogate keys instead of multi-column composite keys dramatically reduc |
| [[union-all-pattern-simple-variant-products]] | UNION ALL Pattern (Simple + Variant Products)

A SQL pattern that combines rows from simple products and variant product |
| [[variant-complexity-problem-d365-fo]] | The Variant Complexity Problem (D365 F&O)

The challenge of building a unified product dimension when a single master pr |

| [[power-bi-informal-ontologies]] | Power BI Models as Informal Ontologies

Power BI .pbix files are informal business ontologies — 20 million semantic models waiting to be formalized |
| [[ontology-auto-generation-70-30-split]] | 70/30 Ontology Auto-Generation Split

70% of ontology extraction is automatable; 30% requires business analyst input for operational and governance rules |
| [[power-bi-formal-ontology-extraction-pipeline]] | Power BI → Formal Ontology Extraction Pipeline

Four-step pipeline: extract from .pbix, auto-generate ontology, analyst review, export to Fabric IQ |
| [[ontology-fabric-iq-export]] | Ontology → Fabric IQ Export

Exporting formal ontologies to Microsoft Fabric IQ JSON format for semantic item import |
| [[schema-drift-detection-pattern]] | Schema Drift Detection

Automatically detecting column renames, drops, and additions before AI agents act on stale data bindings |
| [[multi-dashboard-semantic-debt-analysis]] | Multi-Dashboard Semantic Debt Analysis

Detecting conflicting concept definitions across multiple Power BI dashboards and quantifying reconciliation cost |
| [[schema-drift-column-rename-loss]] | Schema Drift — Column Rename $4.6M Loss

Column rename causes AI agent to receive NULL values, resulting in $4.6M routing failure — prevented by drift detection |
| [[Data-Modeling-Mistake-Missing-Date-Table]] | Data Modeling Mistake: Missing Dedicated Date Table — Fix Pattern |

## Data Quality  (3 notes)

| Note | Description |
|------|-------------|
| [[unique-key-that-isnt-primary-key-verification.md]] | Primary Key Verification — When a Unique Key Is Not Unique

Always verify column uniqueness assumptions with COUNT(*) vs COUNT(DISTINCT); a non-unique key silently overwrites wrong rows in upsert logic |
| [[same-code-different-meanings-code-column-reliability.md]] | Same Code, Different Meanings — Code Column Reliability

Code columns can accumulate inconsistent meanings over time; exclude unreliable codes and use cleaned text as the natural key instead |
| [[flag-and-preserve-data-quality-philosophy.md]] | Flag and Preserve — Data Quality Philosophy

Never silently discard non-matching values; add is_matched flags and preserve raw values; transforms data quality from one-time cleanup into continuous improvement |

## Relationships & Cardinality  (3 notes)

| Note | Description |
|------|-------------|
| [[many-to-many-bridge-table-pattern]] | Many-to-Many Bridge Table Pattern

A data modelling pattern that resolves survey response many-to-many relationships cle |
| [[powerpivot-data-model-load-access-diagram-view-relationships]] | PowerPivot Data Model: Load from Access, Diagram View, Relationships |

A step-by-step pattern for loading multiple relate |
| [[Data-Modeling-Mistake-Broken-Relationships]] | Data Modeling Mistake: Broken Relationships — Symptoms and Fix Pattern |
| [[Data-Modeling-Mistake-Bi-Directional-Filtering]] | Data Modeling Mistake: Overusing Bi-Directional Filtering — Fix Pattern |

## Architecture  (2 notes)

| Note | Description |
|------|-------------|
| [[data-lake-vs-data-warehouse]] | Data Lake vs Data Warehouse

Two foundational storage patterns for analytical workloads — each optimised for different s |
| [[data-warehouse-architectures-inmon-kimball-datavault]] | You just landed a job as a Data Architect
| [[inmon-vs-kimball-vs-data-vault-decision-framework.md]] | Inmon vs Kimball vs Data Vault — Decision Framework

Three methodologies compared: Inmon (top-down/3NF/EDW), Kimball (bottom-up/fact–dimension), Data Vault (Hubs/Links/Satellites) — fit depends on team size, speed, source volatility, and regulation |
| [[medallion-architecture-raw-cleansed-dimensional.md]] | Medallion Architecture: Raw / Cleansed / Dimensional Layers |
| [[Medallion-Architecture-Fabric.md]] | Medallion Architecture — Fabric: OneLake Direct Lake Extension |
| [[Star-Schema-Fabric.md]] | Star Schema in Fabric: Anti-Patterns and Best Practices |

Three-layer data warehouse architecture: raw (bronze) stores source-as-is; cleansed (silver) standardizes and establishes CDC; dimensional (gold) is the Kimball fact/dimension model for BI. |
||| [[Source-Do-You-Really-Need-Medallion-Architecture.md]] | Do You Really Need Medallion Architecture? |
| [[Medallion-Architecture-Layer-Selection-Pattern.md]] | Medallion Architecture Layer Selection Pattern
| Bronze→Silver→Gold vs Landing→Curated→Analytics: driven by source schema volatility, team count, shared platform, data volume. Measure before adding layers. |
| [[Medallion-Materialization-Overhead-Gotcha.md]] | Medallion Materialization Overhead Gotcha
| Each materialized layer = ownership + maintenance + storage + monitoring boundary. Accumulation = more storage, orchestration, complexity. |
| [[Avoid-Architecture-by-Habit-Gotcha.md]] | Avoid Architecture by Habit Gotcha
| Teams implement Bronze→Silver→Gold without evaluating fit. Ask: schema change freq, team count, shared platform, need for intermediate datasets. |
| [[Semantic-Model-Replaces-Gold-Layer.md]] | Semantic Model Replaces Gold Layer Aggregates Pattern
| Power BI semantic model can calculate measures dynamically. Gold layer aggregates needed only for external tools, large datasets, cross-platform analytics. |
| [[Materialized-Views-Data-Quality-Pattern.md]] | Materialized Views for Data Quality — Curated Layer Pattern
| Fabric Lakehouse materialized views enforce NOT NULL, value constraints, positive values directly in Curated layer — eliminates separate Silver layer. |
| [[Layers-Equal-Responsibility-Boundaries.md]] | Layers = Responsibility Boundaries Atomic
| Each layer must have a distinct, unambiguous responsibility. If removing a layer hurts no one, it may not need to exist. Goal = clarity, not more layers. |
| [[cdc-column-selection-created-vs-updated-vs-etl-date.md]] | CDC Column Selection — Created vs Updated vs ETL Date

For upsert tables use updated date; for insert-only use created date; never use ETL run date — this decision propagates into every downstream load |
| [[indexing-strategy-defer-until-schema-complete.md]] | Indexing Strategy — Defer Until Schema Complete

Add indexes after schema is stabilized but before BI reporting begins; tie every decision to a concrete join or filter scenario; factor table write frequency into index count |, and you’re tasked with building the company’s brand-new data warehouse. |

| [[junk-dimension-combine-vs-separate.md]] | Junk Dimension — Combine vs Separate Decision

Combine low-cardinality related attributes into one table when always queried together; keep universal conformed dimensions (date, location) separate |
| [[bridge-tables-many-to-many-list-unpivoting.md]] | Bridge Tables — Many-to-Many and List Unpivoting

Intermediate table for many-to-many fact–dimension relationships; UNNEST comma-separated lists into rows; never assume two independent list columns are index-parallel |
| [[multi-source-merge-archive-priority-load-sequencing.md]] | Multi-Source Merge — Archive Priority and Load Sequencing

Archive version always takes priority; three-step load sequence: upsert archive, delete old active, upsert active — prevents silent double-counting |
| [[surrogate-key-pragmatism-when-to-use-natural-keys.md]] | Surrogate Key Pragmatism — When to Use Natural Keys

Use surrogate keys for low-cardinality dimensions; use natural keys (source UUID) for high-volume fact tables — avoids unnecessary lookup overhead |

## Concepts  (2 notes)

| Note | Description |
|------|-------------|
| [[power-bi-correct-granularity-and-scd]] | Correct Granularity and SCD Performance

Joining a fact table to a slowly changing dimension (SCD) table at the wrong gr |
| [[scd-type-1-price-changes]] | SCD Type 1 (Price Changes Overwrite)

A slowly changing dimension pattern where price changes overwrite the previous val |

## Author Notes  (2 notes)

| Note | Description |
|------|-------------|
| [[3-easy-data-architecture-interview-questions-source]] | 3 Easy Data Architecture Interview Questions (Conceptual)

A Medium article by Jesse Ruiz presenting three conceptual da |
| [[stop-building-slow-power-bi-reports-source]] | Stop Building Slow Power BI Reports: A Data Pro's Checklist

A Medium article by Bill Donofrio presenting a 10-point che |
| [[Author-Yadullah-Abidi]] | Yadullah Abidi

MakeUseOf contributor — PostgreSQL, database design, Docker, Python, LLM integration. |
| [[pl-line-structure-reference]] | P&L Line Structure Reference

| [[5-Data-Cleaning-Mistakes-DigitalBYKewat-source.md]] | 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)

Source note: duplicate records, inconsistent date formats, missing values, inconsistent categories, ignoring outliers — with PQ/SQL fixes and a 5-point health checklist.

| [[Author-DigitalBYKewat]] | DigitalBYKewat

Medium author focused on data cleaning and Power Query. 1 source in vault.

| [[Duplicate-Records-Detection-Removal.md]] | Duplicate Records: Detection and Removal

COUNTROWS vs DISTINCTCOUNT QA, Power Query Remove Duplicates, primary key enforcement.

| [[Inconsistent-Date-Formats-ISO.md]] | Inconsistent Date Formats: ISO Standardisation

ISO YYYY-MM-DD standard, locale settings in Power Query, format ambiguity between DD/MM and MM/DD.

| [[Missing-Values-Handling-Strategy.md]] | Missing Values: Handling Strategy

Why blanks break averages and slicers — the decision framework (replace, drop, or investigate upstream).

| [[Inconsistent-Categories-Normalisation.md]] | Inconsistent Categories: Normalisation

Text.Trim, Text.Clean, case normalisation, dimension lookup tables for legacy name mapping.

| [[Ignoring-Outliers-Detection-Action.md]] | Ignoring Outliers: Detection and Action

Min/max QA check before publishing, median vs mean, data entry error investigation.

| [[Dashboard-Health-Checklist.md]] | Dashboard Health Checklist

5-point pre-publish checklist: duplicates, date formats, blanks, categories, outliers.

| [[Data-Cleaning-Pipeline-Flow.md]] | Data Cleaning Pipeline Flow

8-step ordered pipeline: Duplicate Check → Missing Value → Standardize → Validate → Outliers → Clean → Dashboard → Decisions.

Standard account code ranges (100s-600s) and P&L section structure for corporate financial statements |

| [[source-excel-postgres-weekend-yadullah.md]] | Excel was my Database for 15 Years, and Postgres ended that in a Weekend — Source

Excel → Postgres migration; Yadullah Abidi, MakeUseOf 2026-07-29. |
||| [[postgres-constraint-enforcement.md]] | Postgres Constraint Enforcement Pattern

UNIQUE/NOT NULL/FOREIGN KEY/type constraints enforce data quality; VLOOKUP silent failure vs FK engine rejection. |
||| [[normalized-tables-vs-flat-rows.md]] | Normalized Tables vs Flat Rows Atomic

Schema design exposes duplicate/inconsistent data; same entity multiple times (spacing, case). |
||| [[excel-to-postgres-migration-workflow.md]] | Excel to Postgres Migration Workflow

Sketch schema → Docker Compose → pandas cleanup → psycopg2 insert → constraints catch bad data. |
||| [[constraints-catch-bad-data-not-bad-formatting.md]] | Constraints Catch Bad Data Not Bad Formatting Atomic

Constraints reject wrong types, orphans, duplicates — NOT inconsistent text (yes/Y/true); clean before insert. |
||| [[database-schema-first-migration.md]] | Database Schema First Migration Pattern

Design normalized schema before migration code; schema sketch is first data quality audit. |

## Sources

| Note | Description |
|------|-------------|
| [[Source-5-Mistakes-in-Power-BI-Data-Modeling]] | 5 Mistakes in Power BI Data Modeling (Anurodh Kumar, 2026-05-04) |

## Imported from Raindrop / Medium Reading List
- [[CHANGELOG|Changelog]]
- [[modscape-an-ai-powered-data-modeling-tool-i-built|Modscape: An AI-Powered Data Modeling Tool I Built]]


## Imported from Raindrop / Medium Reading List
- [[dimensional-modeling-for-retail-product-variants-b4e6c1743382|Dimensional Modeling For Retail Product Variants B4e6c1743382]]
- [[dimensional-modeling-for-retail-product-variants-pt-d02abbc97319|Dimensional Modeling For Retail Product Variants Pt D02abbc97319]]
- [[dimensional-modeling-for-retail-product-variants-pt-efd14c680c3c|Dimensional Modeling For Retail Product Variants Pt Efd14c680c3c]]
- [[graphing-unleashing-multi-dimensional-insights-in-one-power-bi-visual-a8c4e4a9b5|Graphing Unleashing Multi Dimensional Insights In One Power Bi Visual A8c4e4a9b5e4]]
- [[or-dimension-the-all-in-one-guide-to-reading-data-model-and-nailing-the-intervie|Or Dimension The All In One Guide To Reading Data Model And Nailing The Interview 4d580d8fb0af]]
- [[power-bi-introduction-to-data-modeling-0410bdb8c080|Power Bi Introduction To Data Modeling 0410bdb8c080]]
- [[power-bi-introduction-to-data-modeling-part-c48c9043280f|Power Bi Introduction To Data Modeling Part C48c9043280f]]
- [[star-schema-fact-tables-are-more-powerful-than-you-think-and-how-to-master-them-|Star Schema Fact Tables Are More Powerful Than You Think And How To Master Them Ac4739124da8]]
- [[your-power-bi-slow-10-ways-to-optimize-your-data-model-6f3cc2f98398|Your Power Bi Slow 10 Ways To Optimize Your Data Model 6f3cc2f98398]]
[[CHANGELOG]]


## Implicit Knowledge

| Note | Description |
|------|-------------|
| [[Implicit/Entities/entity-jesse-ruiz]] | Data engineering and Power BI content creator on Medium specialising in dimensional modeling for retail and D365 F&O dat |
| [[Implicit/Entities/entity-advanced-dimensional-modeling-for-retail-product-variants-parts-1-3]] | Three-part Medium series by Jesse Ruiz covering the full lifecycle of a D365 F&O retail product dimension: composite key |
| [[Implicit/Entities/entity-data-modeling-for-bi-build-trustworthy-analytics]] | Medium article by Han Xu Yang arguing that BI data modeling is about structure, meaning, and rules - not just storage -  |
| [[Implicit/Entities/entity-data-warehousing-for-bi]] | Medium article by Han Xu Yang describing the five-stage end-to-end warehouse architecture (source, ingestion, raw, trans |
| [[Implicit/Entities/entity-han-xu-yang]] | Medium author of data-modeling-bi-trustworthy-analytics and data-warehousing-bi (per @hanxuyang0826 Medium handle). Writ |
| [[Implicit/Entities/entity-beginning-big-data-with-power-bi-and-excel-2013-dunlop]] | Book by Dunlop published by Apress (2015). Source of the database-key-types definition (Chapter 4) covering primary, can |
| [[Implicit/Entities/entity-differential-privacy]] | A mathematical privacy technique that adds calibrated random noise to query results, preventing individual re-identifica |
| [[Implicit/Entities/entity-smartnoise-sdk]] | Microsoft's open-source differential privacy library providing SQL-based aggregations, Python core libraries (mockdp, py |
| [[Implicit/Entities/entity-dimdate-dax-date-dimension]] | A reusable DAX expression using CALENDAR and ADDCOLUMNS to build a complete date dimension table with DateKey, Year, Qua |
| [[Implicit/Entities/entity-dax-calendar-function]] | DAX function that generates a date table from a start to end date, the foundation of a programmatic dim_date implementat |
| [[Implicit/Entities/entity-dimension-groups-d365-fo]] | A D365 Finance and Operations concept that defines which variant attributes (Colour, Style, Size, Config) apply to a pro |
| [[Implicit/Entities/entity-retail-product-variants]] | Products with multiple dimension combinations (color, style, size, config) that require conditional matching when joinin |
| [[Implicit/Entities/entity-multiple-fact-tables-modeling]] | A Power BI data modeling pattern where fact tables at different granularities (e.g., Internet Sales, Reseller Sales) req |
| [[Implicit/Entities/entity-conformed-dimensions]] | Dimensions with identical definitions shared across multiple fact tables, enabling seamless cross-fact aggregation and c |
| [[Implicit/Entities/entity-import-mode-power-bi]] | A Power BI storage mode where data is read from memory, providing orders of magnitude faster performance than disk queri |
| [[Implicit/Entities/entity-directquery-mode-power-bi]] | A Power BI storage mode that queries the source database on every interaction, supporting unlimited data size and live d |
| [[Implicit/Entities/entity-incremental-refresh-pattern]] | A Power BI configuration that partitions large append-only tables and refreshes only recent partitions, dramatically red |
| [[Implicit/Entities/entity-append-only-tables]] | Tables where new rows are added but existing rows are never modified. Ideal candidates for incremental refresh: GA4, POS |
| [[Implicit/Entities/entity-filtered-index-sql]] | A conditional database index that excludes certain rows (e.g., empty strings), keeping the index compact and improving s |
| [[Implicit/Entities/entity-lambda-architecture]] | A data architecture pattern combining a batch layer for historical accuracy with a streaming layer for real-time approxi |
| [[Implicit/Entities/entity-kappa-architecture]] | A simplified data architecture that treats all data as streams, using a single code path for both real-time and historic |
| [[Implicit/Entities/entity-materialized-views]] | Pre-computed database views that store query results, eliminating per-query compute cost for complex dimension queries.  |
| [[Implicit/Entities/entity-cetas-create-external-table-as-select]] | A pre-computation pattern in Azure Synapse that writes query results to external tables in Delta Lake or Parquet format, |
| [[Implicit/Entities/entity-medallion-architecture]] | A three-layer data lake pattern (Bronze/Silver/Gold) that progressively cleanses and aggregates data from raw source to  |
| [[Implicit/Entities/entity-bronze-layer]] | The raw landing zone in medallion architecture that stores exact source copies append-only with no transformations, enab |
| [[Implicit/Entities/entity-silver-layer]] | The validated layer in medallion architecture where data is cleansed, deduplicated, with business rules and data types e |
| [[Implicit/Entities/entity-gold-layer]] | The aggregated layer in medallion architecture with pre-computed metrics and KPIs, denormalized for fast dashboard queri |
| [[Implicit/Entities/entity-onelake]] | Microsoft Fabric's single logical data lake that serves as the unified storage layer for all Fabric workloads, with meda |
| [[Implicit/Entities/entity-direct-lake-mode]] | Power BI storage mode that queries OneLake files directly without importing into memory, eliminating the import/refresh  |
| [[Implicit/Entities/entity-delta-lake]] | Open-source storage layer that brings ACID transactions to data lakes, underlying medallion architecture implementations |
| [[Implicit/Entities/entity-pricedisctable]] | D365 F&O price and discount table that stores price records keyed by item and dimensional attributes; mismatches between |
| [[Implicit/Entities/entity-product-variants]] | Retail product dimension rows representing specific combinations of Color, Style, and Size attributes; require matching  |
| [[Implicit/Entities/entity-dimension-groups]] | D365 F&O attribute groupings that define which dimensional combinations (Color+Style, Color+Size, etc.) are active for a |
| [[Implicit/Entities/entity-parquet-format]] | Columnar binary storage format with built-in compression (2-10x smaller than CSV), schema preservation, and optimized re |
| [[Implicit/Entities/entity-csv-format]] | Plain text comma-delimited format with no compression, best suited for small tabular datasets under 100K rows and intero |
| [[Implicit/Entities/entity-json-format]] | Key-value format with nested structure support and no compression, designed for semi-structured data and API payloads. |
| [[Implicit/Entities/entity-plain-text-format]] | Unstructured text format with no compression, used for NLP training pipelines where raw text content is the input. |
| [[Implicit/Entities/entity-semantic-debt]] | The cost of resolving conflicting definitions of the same business concept across different Power BI dashboards or model |
| [[Implicit/Entities/entity-normalization-and-3nf]] | Relational database design principle defined by E.F. Codd that divides large tables into smaller related tables to minim |
| [[Implicit/Entities/entity-transitive-dependency]] | A data dependency pattern where Field A determines Field B and Field B determines Field C, but Field C should only depen |
| [[Implicit/Entities/entity-ontology]] | A formal specification of concepts, properties, relationships, and constraints in a business domain. Power BI models enc |
| [[Implicit/Entities/entity-fabric-iq]] | Microsoft Fabric's semantic layer that consumes formal ontologies in JSON format for AI agent consumption, semantic item |
| [[Implicit/Entities/entity-stale-statistics]] | Database query optimizer statistics that become outdated as data volume grows, causing the optimizer to generate subopti |
| [[Implicit/Entities/entity-power-bi-ontology-extractor]] | Python tool that extracts semantic model components (tables, columns, relationships, hierarchies, DAX measures, RLS) fro |
| [[Implicit/Entities/entity-modelbim]] | JSON file inside a pbix archive containing the complete semantic model definition: tables, columns, relationships, hiera |
| [[Implicit/Entities/entity-power-bi-visual-performance]] | The rendering speed of individual report visuals, which degrades with visual count, row count, conditional formatting co |
| [[Implicit/Entities/entity-power-bi-performance-analyzer]] | A built-in Power BI Desktop tool that shows exact DAX query time per visual, used to benchmark before and after performa |
| [[Implicit/Entities/entity-powerpivot-diagram-view]] | A visual canvas in PowerPivot showing all tables and their relationships; arrows indicate relationship direction but are |
| [[Implicit/Entities/entity-manage-relationships-screen]] | The precise relationship editor in PowerPivot showing exact field names for each relationship, preferred over Diagram Vi |
| [[Implicit/Entities/entity-pricing-cte-with-rownumber-deduplication]] | A SQL CTE pattern that partitions PriceDiscTable rows by item and uses ROW_NUMBER ordered by fromdate to pick the latest |
| [[Implicit/Entities/entity-inventdim]] | D365 table storing dimension attribute combinations (color, style, size, config) for variants; linked to price records f |
| [[Implicit/Entities/entity-rownumber-window-function]] | SQL window function used for deduplication: PARTITION BY item groups rows, ORDER BY fromdate sequences them, and WHERE s |
| [[Implicit/Entities/entity-pii-removal-techniques]] | Methods for handling personally identifiable information before AI/ML pipelines: remove columns, pseudonymisation, gener |
| [[Implicit/Entities/entity-pii-categories]] | Three tiers of PII: direct identifiers (name, email, SSN), indirect identifiers (ZIP+birthdate), and sensitive data (hea |
| [[Implicit/Entities/entity-azure-cognitive-services-pii-detection]] | Azure service that flags PII in text data, used as part of a data pipeline before ML model training. |
| [[Implicit/Entities/entity-replicated-table-distribution]] | Azure Synapse distribution strategy that copies a full dimension table to every compute node, eliminating data movement  |
| [[Implicit/Entities/entity-role-playing-dimension]] | A dimensional modelling pattern where the same dimension table is joined to a fact table multiple times via different al |
| [[Implicit/Entities/entity-schema-drift-column-rename-failure]] | AI governance failure mode where a source column rename causes NULL values for AI agents bound to the ontology's origina |
| [[Implicit/Entities/entity-schema-drift-detection]] | Pattern that automatically compares an ontology's expected schema against the actual live database schema, blocking agen |
| [[Implicit/Entities/entity-schemamapper-powerbi-ontology]] | The core component of a schema drift detection system that maintains property-to-column bindings and compares them again |
| [[Implicit/Entities/entity-shared-dimensions-with-multiple-fact-tables]] | A dimensional modelling practice where a single dimension table is used across multiple fact tables via one-to-many rela |
| [[Implicit/Entities/entity-simple-vs-variant-products]] | The two fundamental product types in retail dimensions: simple products have a single SKU with no variants, while varian |
| [[Implicit/Entities/entity-simple-product]] | A product with a single SKU and no variant attributes; pricing resolved directly on itemid plus dataareaid. |
| [[Implicit/Entities/entity-variant-product]] | A product with multiple valid combinations in InventDimCombination, each combination being a distinct SKU with its own p |
| [[Implicit/Entities/entity-star-schema]] | The foundational data modelling pattern: a central fact table containing measures and foreign keys surrounded by denorma |
| [[Implicit/Entities/entity-fact-table]] | The central table in a star schema containing numeric measures to be aggregated and foreign keys linking to dimension ta |
| [[Implicit/Entities/entity-dimension-table]] | A denormalized table in a star schema containing descriptive attributes used to slice and filter fact table measures. |
| [[Implicit/Entities/entity-foreign-key-and-primary-key]] | The link between fact and dimension tables: a foreign key field in the fact table references the primary key of a dimens |
| [[Implicit/Entities/entity-surrogate-key]] | A system-generated unique identifier (typically integer) used as the primary key in dimension tables, preferred over nat |
| [[Implicit/Entities/entity-snowflake-schema]] | A normalised dimensional schema where dimension tables are split into normalised sub-tables (Country, Region, District,  |
| [[Implicit/Entities/entity-composite-key]] | A multi-column foreign key (e.g., CONCAT(ProductID, ColorID, SizeID)) used to join fact to dimension. Expensive in Power |
| [[Implicit/Entities/entity-union-all]] | A SQL set operation that combines result sets without deduplication. Preferred over UNION in ETL because it skips the ex |
| [[Implicit/Entities/entity-d365-fo-dynamics-365-finance-operations]] | Microsoft's ERP system with no single Products table. Product data spans 12+ interconnected tables (EcoResProduct, Inven |
| [[Implicit/Entities/entity-bi-directional-filtering]] | A Power BI relationship setting that propagates filter context both ways between tables. Causes ambiguity, row duplicati |
| [[Implicit/Entities/entity-broken-relationship]] | A missing or incorrectly configured table relationship (wrong direction, wrong cardinality, or duplicate path). The root |
| [[Implicit/Entities/entity-bridge-table]] | An intermediate table in a many-to-many relationship that splits one M:M join into two one-to-many joins. Enables clean  |
| [[Implicit/Entities/entity-powerpivot]] | Excel's in-memory data modeling engine (included in Excel 2013 Standard+). Supports loading multiple related tables from |
| [[Implicit/Entities/entity-data-lake]] | A raw data storage system storing data in native format (JSON, CSV, Parquet) with schema applied at read time. Low stora |
| [[Implicit/Entities/entity-data-warehouse]] | A structured analytical storage system with pre-modelled, processed data optimised for fast queries. Enforces schema at  |
| [[Implicit/Entities/entity-inmon-data-warehouse-approach]] | A top-down enterprise data warehousing methodology pioneered by Bill Inmon. Builds a massive centralised Enterprise Data |
| [[Implicit/Entities/entity-kimball-dimensional-modeling-approach]] | A bottom-up data warehousing methodology by Ralph Kimball. Builds dimensional star schemas directly for each business pr |
| [[Implicit/Entities/entity-data-vault-20]] | An enterprise-scale data warehousing methodology designed for agility, auditability, and parallel loading. Adds hash key |
| [[Implicit/Entities/entity-slowly-changing-dimension-scd]] | A dimension table that tracks attribute changes over time. Type 1 overwrites values in place; Type 2 adds new rows with  |
| [[Implicit/Entities/entity-scd-type-1-overwrite]] | A slowly changing dimension pattern where attribute changes overwrite the previous value in place. No history is preserv |
| [[Implicit/Entities/entity-scd-type-2-history]] | A slowly changing dimension pattern that stores multiple versions of a dimension row, each with effective date ranges. F |
| [[Implicit/Entities/entity-third-normal-form-3nf]] | A normalisation standard used by the Inmon approach. Eliminates transitive dependencies so every non-key attribute depen |
| [[Implicit/Entities/entity-schema-on-read]] | A data storage approach (used by data lakes) where structure is imposed when data is queried rather than when it is stor |
| [[Implicit/Entities/entity-schema-on-write]] | A data storage approach (used by data warehouses) where data is validated and structured before storage. Ensures quality |
| [[Implicit/Entities/entity-enterprise-data-warehouse-edw]] | The centralised normalised data repository at the core of Inmon's top-down methodology. All data is cleaned, standardise |
| [[Implicit/Entities/entity-survey-response-mm-problem]] | The inherent many-to-many structure of survey data: one respondent can select multiple answers, and one answer can be se |
| [[Implicit/Entities/entity-crossfilter-dax-function]] | A DAX function that overrides the filter direction of a relationship for a specific calculation. Enables targeted cross- |
| [[Implicit/Entities/entity-degenerate-dimension]] | A dimension attribute stored directly in the fact table rather than in a separate dimension table. Used for low-cardinal |
| [[Implicit/Entities/entity-data-swamp]] | A degraded data lake that has lost value due to lack of governance and enforced schema. Without schema-on-write controls |
| [[Implicit/Entities/entity-cross-filter-direction]] | A Power BI relationship property controlling how filter context propagates between two tables. Options are Single (defau |
| [[Implicit/Entities/entity-data-mart]] | A subset of the enterprise data warehouse focused on a specific business function or department. In Inmon's approach, da |
| [[Implicit/Entities/entity-unified-product-dimension]] | A single dimension table combining simple products and variant products via UNION ALL, with variant attribute columns (C |
| [[Implicit/Entities/entity-batch-processing]] | A data processing pattern where data is collected over a time window and processed together, offering simplicity and rel |
| [[Implicit/Entities/entity-stream-processing]] | A data processing pattern where data is processed record-by-record or in micro-batches as it arrives, enabling real-time |
| [[Implicit/Entities/entity-lakehouse-architecture]] | A hybrid architecture that combines the low-cost storage of a data lake with the data management and BI capabilities of  |
| [[Implicit/Entities/entity-pl-line-structure]] | The standard hierarchical ordering of a Profit and Loss statement: Revenue, Cost of Sales, Gross Profit, Operating Expen |
| [[Implicit/Entities/entity-account-code-ranges]] | Numeric ranges assigned to P&L categories in a chart of accounts, such as 100-199 for Revenue and 200-299 for Cost of Sa |
| [[Implicit/Entities/entity-chart-of-accounts]] | A structured list of all accounts used by an organisation for financial reporting, serving as the basis for mapping raw  |
| [[Implicit/Entities/entity-pl-mapping-table]] | A lookup table that maps each account code in the Chart of Accounts to a P&L section and line, enabling automated profit |
| [[Implicit/Entities/entity-flat-table-one-big-table]] | An anti-pattern where all data is denormalised into a single table, bypassing dimensional modeling, causing model bloat  |
| [[Implicit/Entities/entity-dimdate-date-dimension]] | A dedicated date dimension table in Power BI containing a row per date with fiscal periods, hierarchies, and working-day |
| [[Implicit/Entities/entity-directquery-mode]] | A Power BI storage mode that queries the source database directly at report runtime rather than loading data into memory |
| [[Implicit/Entities/entity-import-mode]] | A Power BI storage mode that loads all data into the in-memory Vertipaq engine, providing fast query performance by sacr |
| [[Implicit/Entities/entity-incremental-refresh]] | A Power BI data refresh strategy that only loads new or changed records since the last refresh, dramatically reducing re |
| [[Implicit/Entities/entity-bravo-for-power-bi]] | An open-source Power BI tool that analyses semantic models and highlights unused columns and inefficient data types to s |
| [[Implicit/Entities/entity-column-pruning]] | The practice of removing unused columns from Power BI tables before loading, reducing model size and memory consumption, |
| [[Implicit/Entities/entity-bi-directional-cross-filtering]] | A Power BI relationship setting that propagates filters in both directions between tables, creating ambiguity and row du |
| [[Implicit/Entities/entity-calculated-column]] | A DAX-defined column computed at model load time and stored in memory, increasing model size and failing to respond to s |
| [[Implicit/Entities/entity-dax-measure]] | A DAX expression evaluated at query time that responds to slicer and filter context, making it the preferred alternative |
| [[Implicit/Entities/entity-date-dimension-table]] | A dedicated dimension table containing one row per date, enabling Power BI time intelligence functions (YTD, MTD, prior  |
| [[Implicit/Entities/entity-time-intelligence]] | DAX functions (YTD, MTD, QTD, SAMEPERIODLASTYEAR) that enable period-over-period comparison in Power BI, requiring a pro |
| [[Implicit/Entities/entity-one-to-many-relationship]] | The standard Power BI relationship type where a single dimension row filters many fact rows, forming the backbone of sta |
| [[Implicit/Entities/entity-dashboard-health-checklist]] | A five-question pre-publish checklist for Power BI dashboards covering duplicates, date formats, blanks, category normal |
| [[Implicit/Entities/entity-data-cleaning-pipeline]] | An ordered eight-step ETL pipeline for cleaning raw data before loading into Power BI: duplicate check, missing values,  |
| [[Implicit/Entities/entity-duplicate-records]] | Identical or near-identical rows that inflate count metrics and distort revenue, profit, customer count, and inventory,  |
| [[Implicit/Entities/entity-inconsistent-date-formats]] | Mixed date string representations (e.g., MM/DD/YYYY vs DD/MM/YYYY) that cause Power BI to group transactions into wrong  |
| [[Implicit/Entities/entity-missing-values]] | Blank or NULL cells that silently break average calculations, break slicer completeness, and distort forecasting models  |
| [[Implicit/Entities/entity-inconsistent-categories]] | Mismatched text values for the same entity (e.g., Mumbai/MUMBAI/Bombay) that split bar charts into many small bars inste |
| [[Implicit/Entities/entity-outlier]] | An extreme data value (often a data entry error) that distorts the mean, warps trend lines, and biases forecasting model |
| [[Implicit/Entities/entity-iso-date-format-yyyy-mm-dd]] | The ISO 8601 date standard that unambiguously represents dates as year-month-day, recommended as the safest universal da |
| [[Implicit/Entities/entity-primary-key]] | A unique identifier column or set of columns in a source table that enforces row uniqueness and is the foundation for de |
| [[Implicit/Entities/entity-minmax-qa-check]] | A data quality technique that scans the minimum and maximum values of every numeric column before publishing a report, c |
| [[Implicit/Entities/entity-median-central-tendency]] | The middle value in a sorted dataset, used as a robust alternative to the mean when outliers are present since it is not |
| [[Implicit/Entities/entity-countrows-vs-distinctcount-qa]] | A DAX QA technique comparing total row count against distinct count of a key column to detect the presence of duplicate  |
| [[Implicit/Entities/entity-texttrim-and-textclean]] | Power Query text transformation functions that remove leading/trailing whitespace and invisible ghost characters respect |
| [[Implicit/Entities/entity-architecture-by-habit]] | An anti-pattern where teams default to medallion layers (Bronze/Silver/Gold) without evaluating whether those layers sol |
| [[Implicit/Entities/entity-bill-donofrio]] | A data practitioner and Medium author (@foodarchitects) focused on Power BI performance optimisation, authoring a 10-poi |
| [[Implicit/Entities/entity-anurodh-kumar]] | A data practitioner and Medium author (write-a-catalyst) covering foundational Power BI data modeling mistakes including |
| [[Implicit/Entities/entity-digitalbykewat]] | A Medium author (@digitalbykewat) focused on practical data analytics, Power Query transformations, and Power BI dashboa |
| [[Implicit/Entities/entity-yadullah-abidi]] | A MakeUseOf contributor covering developer tooling, databases, and productivity software, with expertise in PostgreSQL,  |
| [[Implicit/Entities/entity-text-normalization]] | The practice of standardizing text values including case, trim, and character cleaning to prevent silent aggregation spl |
| [[Implicit/Entities/entity-date-format-standardization]] | Converting dates to ISO 8601 format (YYYY-MM-DD) to eliminate regional ambiguity that causes silent mis-parsing in BI to |
| [[Implicit/Entities/entity-landing-layer]] | The initial data ingestion layer where raw data from source systems is stored as-is before any transformation. |
| [[Implicit/Entities/entity-curated-layer]] | The layer responsible for data quality enforcement, star schema creation, and data validation in a simplified lakehouse  |
| [[Implicit/Entities/entity-analytics-layer]] | The optional layer for pre-aggregated datasets optimized for reporting and analytics queries. |
| [[Implicit/Entities/entity-data-quality-constraints]] | Validation rules applied at the materialized view or curated layer level, including NOT NULL, value ranges, and required |
| [[Implicit/Entities/entity-power-bi-semantic-model]] | The Power BI layer that defines measures, relationships, and hierarchies; can replace pre-aggregated Gold layer datasets |
| [[Implicit/Entities/entity-many-to-many-relationship]] | A data relationship where one fact row can关联 multiple dimension values and vice versa, requiring a bridge table to model |
| [[Implicit/Entities/entity-microsoft-fabric]] | Microsoft's unified data platform where OneLake serves as the single logical data lake, implementing medallion layers as |
| [[Implicit/Entities/entity-missing-values-handling]] | The decision process for blank/null cells: investigate root cause, then either replace with defaults (Unknown, 0, -1) or |
| [[Implicit/Entities/entity-power-query-transforms]] | Power Query operations for handling data quality including Fill Down/Up, Replace Nulls, Replace Errors, and Remove Rows  |
| [[Implicit/Entities/entity-boniface-muchendu]] | Author and data architect at Data Bear who wrote the decision framework for medallion architecture necessity. |
| [[Implicit/Entities/entity-cdc-column]] | A database column used for change data capture to detect changed records in a data warehouse load. Options include ETL r |
| [[Implicit/Entities/entity-watermark-table]] | A control table that tracks the last successfully loaded value of a CDC column for each source table, enabling the load  |
| [[Implicit/Entities/entity-etl-run-date]] | A column recording when the load process ran. Has no business meaning since it changes every load regardless of whether  |
| [[Implicit/Entities/entity-upsert-table]] | A table where records can be modified over time and the updated date is used as the CDC column to capture those changes  |
| [[Implicit/Entities/entity-insert-only-table]] | A table where records are written once and never changed. Uses the created date as the CDC column since subsequent updat |
| [[Implicit/Entities/entity-postgres-constraints]] | Database-level enforcement of type and referential integrity including NOT NULL, UNIQUE, FOREIGN KEY, CHECK, and type co |
| [[Implicit/Entities/entity-schema-first-design]] | The practice of designing the normalized database schema before writing migration code. The schema design itself is the  |
| [[Implicit/Entities/entity-excel-to-postgres-migration-workflow]] | A five-step workflow for migrating from Excel-as-database to PostgreSQL: sketch schema, spin up Postgres in Docker, writ |
| [[Implicit/Entities/entity-flag-and-preserve]] | A data quality philosophy that preserves non-matching or suspicious source values in raw form with an is_matched flag co |
| [[Implicit/Entities/entity-deferred-indexing-strategy]] | The practice of deferring index creation until after the schema is fully stabilized but before BI reporting begins, when |
| [[Implicit/Entities/entity-inmon-enterprise-data-warehouse]] | Bill Inmon's top-down 3NF data warehouse approach where a centralized normalized warehouse feeds departmental data marts |
| [[Implicit/Entities/entity-kimball-dimensional-modeling]] | Ralph Kimball's bottom-up approach using fact and dimension tables per subject area unified through conformed dimensions |
| [[Implicit/Entities/entity-data-vault]] | Dan Linstedt's methodology using Hubs (keys), Links (relationships), and Satellites (attributes/history) in a middle-out |
| [[Implicit/Entities/entity-junk-dimension]] | A dimensional modeling pattern that combines multiple low-cardinality, related attributes into a single dimension table  |
| [[Implicit/Entities/entity-multi-source-merge-pattern]] | A data warehouse load pattern for merging the same entity from multiple source tables where archive always takes priorit |
| [[Implicit/Entities/entity-normalized-tables]] | A database design approach using separate tables for distinct entities (customers, orders, payments) with foreign key re |
| [[Implicit/Entities/entity-kimball-dimensional-modeling-case-study-baylas-2026]] | A real-world data warehouse built from scratch using Kimball methodology blended with medallion architecture and ELT pra |
| [[Implicit/Entities/entity-cleansed-layer]] | The silver layer of the medallion architecture where column names are standardized, unnecessary columns removed, CDC is  |
| [[Implicit/Entities/entity-dimensional-layer]] | The gold layer of the medallion architecture containing Kimball fact and dimension tables focused on modeling decisions  |
| [[Implicit/Entities/entity-raw-layer]] | The bronze layer of the medallion architecture storing an exact copy of source system data with no transformations. Acts |
| [[Implicit/Entities/entity-elt-pattern]] | A data loading pattern where transformation happens inside the target database using SQL rather than in a separate proce |
| [[Implicit/Entities/entity-source-excel-was-my-database-for-15-years-and-postgres-ended-that-in-a-weekend]] | Article by Yadullah Abidi documenting the journey from using Excel as a database for 15 years to migrating to PostgreSQL |
| [[Implicit/Entities/entity-postgresql]] | Relational database engine that enforces data quality rules at the engine level through constraints (UNIQUE, NOT NULL, F |
| [[Implicit/Entities/entity-unique-constraint]] | Postgres constraint that prevents duplicate values in a column, catching duplicates that Excel silently allows. |
| [[Implicit/Entities/entity-not-null-constraint]] | Postgres constraint ensuring a column cannot be empty, replacing optional Excel data validation. |
| [[Implicit/Entities/entity-foreign-key-constraint]] | Postgres constraint requiring referenced values to exist in parent table; rejects inserts if parent record missing, unli |
| [[Implicit/Entities/entity-grain]] | The atomic level of one row in a fact table; the fundamental granularity (one transaction, one line item, one event). Mu |
| [[Implicit/Entities/entity-late-arriving-data]] | Data that arrives after the reporting period has closed, such as orders placed in October reaching the warehouse in Nove |
| [[Implicit/Entities/entity-multi-key-partitioning]] | Partition strategy using two keys (time and geography/business dimension) rather than date alone, enabling partition pru |
| [[Implicit/Entities/entity-dual-timestamp-pattern]] | Pattern storing two date columns in fact table: order_date and warehouse_processing_date to separate actual sales timing |
| [[Implicit/Entities/entity-denormalized-metrics]] | Pattern of pre-denormalizing slowly changing or frequently joined metric components (like exchange rates) directly into  |
| [[Implicit/Entities/entity-rohan-dutt]] | Author of the Medium article on real-world star schema fact table design covering performance engineering patterns. |
| [[Implicit/Entities/entity-rely-constraint]] | Cloud warehouse foreign key modifier that signals the query planner to trust the constraint and eliminate unnecessary jo |
| [[Implicit/Entities/entity-zstd-encoding]] | Lossless compression algorithm (Zstandard) applied at the column level in data warehouses, balancing compression ratio w |
| [[Implicit/Entities/entity-column-clustering]] | Physical pre-sorting of rows by specified columns in cloud data warehouses, accelerating queries that filter on those co |
| [[Implicit/Entities/entity-rollup-flags-pattern]] | Fact table design pattern that stores pre-aggregated rows at multiple granularities with boolean flags indicating aggreg |
| [[Implicit/Entities/entity-natural-key]] | A key that exists in the source system data, derived from business meaning, as opposed to an artificially generated surr |
| [[Implicit/Entities/entity-primary-key-verification]] | The practice of testing assumed unique columns with COUNT(*) = COUNT(DISTINCT col) before using them as join or upsert t |
| [[Implicit/Entities/entity-scd-type-2]] | Slowly changing dimension technique that tracks historical attribute changes by inserting new rows and maintaining versi |
| [[Implicit/Entities/entity-snowflake]] | Cloud-based data warehouse platform that supports RELY constraints and advanced encoding techniques. |
| [[Implicit/Entities/entity-amazon-redshift]] | AWS cloud data warehouse that supports RELY constraints for query planner optimization. |
| [[Implicit/Entities/entity-bigquery]] | Google Cloud data warehouse that supports RELY constraints for query optimization. |
| [[Implicit/Entities/entity-assume-referential-integrity]] | Power BI model option that changes relationships from LEFT JOIN to INNER JOIN, trusting that foreign key relationships a |
| [[Implicit/Claims/claim-data-modeling-mistake-missing-date-table]] | Using raw date columns instead of a dedicated Date dimension limits time intelligence functions and breaks fiscal period |
| [[Implicit/Claims/claim-batch-processing-vs-stream-processing]] | Two fundamental data processing paradigms distinguished by latency, complexity, and cost trade-offs. Default recommendat |
| [[Implicit/Claims/claim-column-pruning-bravo]] | The process of removing unused columns from a Power BI model to reduce memory footprint and improve query performance us |
| [[Implicit/Claims/claim-composite-key-strategy-itemkey]] | A key design pattern that generates a single unique ItemKey for every row in a product dimension handling both simple pr |
| [[Implicit/Claims/claim-conditional-joins-case-concat-matching]] | A SQL join pattern that applies different matching column sets to different rows based on a dimension group value - the  |
| [[Implicit/Claims/claim-conformed-dimensions]] | Dimensions shared across fact tables with identical definitions - same attributes, keys, and business meaning - enabling |
| [[Implicit/Claims/claim-database-key-types]] | Taxonomy of database keys: primary key (unique non-null identifier), candidate key (alternative unique identifier), comp |
| [[Implicit/Claims/claim-degenerate-dimension-barcode-in-fact]] | A dimensional modelling pattern where a low-cardinality attribute (Barcode) is stored directly in the fact table rather  |
| [[Implicit/Claims/claim-d365-fo-product-dimension]] | D365 F&O product data spans 12+ interconnected tables with no single Products table. A single master product can generat |
| [[Implicit/Claims/claim-d365-fo-dimension-groups]] | Dimension groups in D365 F&O (e.g., Donated=Colour+Style+Size, DonatedNS=Colour+Style, DonatedS=Style, Retail Kit=Config |
| [[Implicit/Claims/claim-epsilon-parameter]] | The privacy budget parameter in differential privacy. Smaller epsilon values provide stronger privacy guarantees but red |
| [[Implicit/Claims/claim-delta-parameter]] | The probability parameter representing the acceptable chance of privacy violation in differential privacy systems. Set t |
| [[Implicit/Claims/claim-duplicate-barcodes]] | A data modeling error where barcode scans return multiple rows due to historical and secondary barcode records in Invent |
| [[Implicit/Claims/claim-retailshowforitem-filter]] | The solution to duplicate barcodes: filtering on retailshowforitem = 1 returns only the primary current barcode, excludi |
| [[Implicit/Claims/claim-star-schema-multi-fact]] | A clean star schema with one set of shared dimensions connected to each fact table enables accurate cross-fact reporting |
| [[Implicit/Claims/claim-shared-dimensions]] | One set of shared dimensions imported once and connected to all fact tables, avoiding duplication and enabling cross-fac |
| [[Implicit/Claims/claim-barcode-lookup]] | A POS barcode scan lookup against a dimension table that benefits from a filtered index excluding empty barcodes for fas |
| [[Implicit/Claims/claim-data-cleaning-effort]] | Studies and practitioner experience indicate that 70-80% of a data analyst's time is spent on data cleaning and preparat |
| [[Implicit/Claims/claim-batch-stream-combination]] | Lambda and Kappa architectures both combine batch and stream processing to serve both historical accuracy and real-time  |
| [[Implicit/Claims/claim-view-precomputation]] | Pre-computing complex multi-table joins as materialized views or CETAS eliminates the per-query cost of re-executing 12+ |
| [[Implicit/Claims/claim-missing-price-error]] | Symptom: variant row exists in dimension but RetailPrice equals 0 or NULL because no matching price record exists in Pri |
| [[Implicit/Claims/claim-semantic-debt-analysis]] | Analyzing multiple Power BI dashboards simultaneously to detect conflicting definitions of the same business concept acr |
| [[Implicit/Claims/claim-third-normal-form]] | A table in Third Normal Form avoids insertion, update, and deletion anomalies because every non-key field depends only o |
| [[Implicit/Claims/claim-ontology-extraction-70-30]] | Ontology extraction from Power BI models is approximately 70% automatable via parsing (entities, properties, relationshi |
| [[Implicit/Claims/claim-power-bi-informal-ontologies]] | Power BI semantic models contain rich domain knowledge (tables, relationships, hierarchies, DAX measures, business rules |
| [[Implicit/Claims/claim-ontology-to-fabric-iq-export]] | Formal ontologies generated from Power BI models can be exported to Fabric IQ JSON format containing entities, propertie |
| [[Implicit/Claims/claim-performance-degradation-over-time]] | Query performance worsens steadily over time without code changes due to three compounding factors: product catalog grow |
| [[Implicit/Claims/claim-consolidated-fact-tables]] | Stacking multiple fact tables into one via append/union creates null keys wherever fact-specific dimensions do not apply |
| [[Implicit/Claims/claim-duplicated-dimensions]] | Creating separate dimension tables for each fact table bloats model size, slows refresh, creates confusion for report au |
| [[Implicit/Claims/claim-power-bi-ontology-extraction-pipeline]] | A four-step pipeline that converts a Power BI pbix file (ZIP with model.bim JSON) into a formal ontology: Step 1 extract |
| [[Implicit/Claims/claim-visual-count-latency]] | Every visual fires its own DAX query on filter change; 20 visuals with 2-second queries can cause 40 seconds of per-inte |
| [[Implicit/Claims/claim-matrix-table-high-cardinality-rows]] | Matrix and Table visuals with high-cardinality columns load all matching rows, causing performance problems for large da |
| [[Implicit/Claims/claim-conditional-formatting-expensive]] | Background colour, font colour, and data bar rules re-evaluate per cell; a 100-row x 10-column matrix equals 1,000 rule  |
| [[Implicit/Claims/claim-scatter-plot-rendering]] | Scatter plots with many data points degrade rendering performance significantly and should be replaced with tooltips or  |
| [[Implicit/Claims/claim-null-dimension-handling]] | PriceDiscTable may have NULL inventdimid for item-level (non-variant) prices; LEFT JOIN with ISNULL prevents NULL propag |
| [[Implicit/Claims/claim-data-movement-elimination]] | When a fact table is hash-distributed, joining a dimension requires moving rows to fact nodes; replicated tables remove  |
| [[Implicit/Claims/claim-replicate-table-size-rule]] | If a dimension is under 2GB per node, Replicate distribution is almost always the correct choice for read-mostly dimensi |
| [[Implicit/Claims/claim-schema-drift-4-6m-loss]] | A Fortune 500 logistics company lost $4.6M when Warehouse_Location was renamed to FacilityID in the source database, cau |
| [[Implicit/Claims/claim-schema-drift-fail-safe]] | When schema drift is detected, agent execution is blocked, a drift report is generated with missing/new columns and cost |
| [[Implicit/Claims/claim-shared-dimensions-model-size]] | Using one Date table instead of N copies across multiple fact tables reduces model size, shortens refresh times, and pro |
| [[Implicit/Claims/claim-unified-itemkey]] | A product dimension must use one unified key pattern (CONCAT of dataareaid, itemid, and variant dimensions) so fact tabl |
| [[Implicit/Claims/claim-denormalized-dimensions]] | Dimension tables should be wide with descriptive text columns for easier filtering, in contrast to the narrow normalized |
| [[Implicit/Claims/claim-narrow-fact-tables]] | Fact tables should contain only foreign keys and measures for performance; descriptive attributes belong in dimension ta |
| [[Implicit/Claims/claim-powerpivot-auto-relationship-detection]] | PowerPivot automatically detects and creates relationships during import when foreign keys are present in the source dat |
| [[Implicit/Claims/claim-wrong-granularity-scd]] | Joining a fact table to a slowly changing dimension at the wrong granularity forces Power BI to recalculate the entire f |
| [[Implicit/Claims/claim-bi-directional-overuse-causes-duplication]] | Enabling Both directions on a Power BI relationship propagates filter context through multiple paths simultaneously, cau |
| [[Implicit/Claims/claim-union-all-over-union]] | UNION ALL combines result sets without deduplication sorting, making it significantly faster than UNION which removes du |
| [[Implicit/Claims/claim-star-schema-default-power-bi]] | Star Schema should be the default schema for 90% of Power BI projects due to single-hop joins, simpler model structure,  |
| [[Implicit/Claims/claim-snowflake-slower-4x]] | Snowflake Schema with 4-hop joins (Region to Manager to Director) is approximately 4 times slower than Star Schema's sin |
| [[Implicit/Claims/claim-composite-key-60x-memory]] | A 6-column NVARCHAR composite key at 20 characters per column consumes approximately 240 bytes per row vs 4 bytes for an |
| [[Implicit/Claims/claim-d365-no-single-products-table]] | D365 F&O stores product data across 12+ interconnected tables with no unified Products view. A single master product can |
| [[Implicit/Claims/claim-broken-relationships-wrong-totals]] | Missing or incorrectly configured relationships (wrong direction, cardinality, or duplicate path) are the root cause of  |
| [[Implicit/Claims/claim-missing-date-relationship]] | If a fact table is not connected to a Date dimension, time intelligence functions (YTD, MTD, SAMEPERIODLASTYEAR) fail si |
| [[Implicit/Claims/claim-scd-type1-overwrites-price]] | In SCD Type 1, when RetailPrice changes the value is overwritten in place. Historical prices are not preserved in the di |
| [[Implicit/Claims/claim-inmon-top-down]] | Inmon's methodology is top-down: the centralised Enterprise Data Warehouse (EDW) must be fully built in 3NF before any b |
| [[Implicit/Claims/claim-inmon-single-truth]] | The Inmon EDW eliminates duplicate records and conflicting metrics by storing every entity in exactly one place. A custo |
| [[Implicit/Claims/claim-bridge-avoids-m2m-overhead]] | A bridge table keeps relationships as one-to-one and makes COUNTX unambiguous. Power BI's native many-to-many option add |
| [[Implicit/Claims/claim-powerpivot-auto-relationship-import]] | PowerPivot imports any relationships defined in the source database (Access, SQL Server) during table import, and displa |
| [[Implicit/Claims/claim-schema-on-read-flexibility]] | Data lakes use schema-on-read to store any data format (JSON, CSV, Parquet, images, logs) without upfront structure. Thi |
| [[Implicit/Claims/claim-lake-and-warehouse-complementary]] | Modern architectures use both: data lake (ADLS, S3) for cheap raw storage and ingestion, data warehouse (Snowflake, Syna |
| [[Implicit/Claims/claim-claim-schema-on-read-vs-write]] | Data lakes use schema-on-read (structure applied at query time) while data warehouses use schema-on-write (structure enf |
| [[Implicit/Claims/claim-claim-medallion-standard-pattern]] | Medallion architecture (Bronze/Silver/Gold) is the standard Delta Lake pattern on platforms like Databricks, Fabric, and |
| [[Implicit/Claims/claim-claim-batch-first-default]] | The honest default answer for most data processing decisions is batch first; stream processing should only be adopted wh |
| [[Implicit/Claims/claim-claim-lakehouse-blurs-lines]] | Delta Lake and Lakehouse architectures blur the line between data lakes and data warehouses by adding warehouse-style AC |
| [[Implicit/Claims/claim-claim-star-schema-mandatory]] | Star schema is mandatory for performant Power BI models; importing multiple flat files and letting Power BI auto-join th |
| [[Implicit/Claims/claim-claim-surrogate-key-memory-efficiency]] | Integer surrogate keys use 4 bytes versus multi-byte string composite keys, providing significant memory savings at scal |
| [[Implicit/Claims/claim-claim-scd-wrong-granularity-recalculation]] | Joining fact tables to type-2 SCD dimension tables at the wrong granularity causes Power BI to recalculate the entire mo |
| [[Implicit/Claims/claim-claim-bridge-tables-solve-many-to-many]] | Many-to-many relationships in Power BI should be avoided in favour of bridge tables, which keep respondent-to-answer cou |
| [[Implicit/Claims/claim-claim-import-faster-than-directquery]] | DirectQuery reads from disk at query time while Import mode reads from memory, making Import faster for most Power BI wo |
| [[Implicit/Claims/claim-claim-incremental-refresh-game-changer]] | Incremental refresh only processes new or changed records since the last refresh window, dramatically reducing refresh t |
| [[Implicit/Claims/claim-claim-flat-table-breaks-calculations]] | Consolidating all data into a single flat table causes model size bloat and breaks DAX calculations that rely on proper  |
| [[Implicit/Claims/claim-claim-bi-directional-ambiguity]] | Enabling bi-directional cross-filtering on multiple relationships causes ambiguous filter context that produces incorrec |
| [[Implicit/Claims/claim-claim-measures-preferred-over-calculated-columns]] | Calculated columns are evaluated at model load time, stored in memory, and do not respond to slicers; DAX measures evalu |
| [[Implicit/Claims/claim-claim-date-table-unlocks-time-intelligence]] | Raw date columns cannot support Power BI time intelligence functions (YTD, MTD, SAMEPERIODLASTYEAR); a properly configur |
| [[Implicit/Claims/claim-claim-duplicates-distort-metrics]] | A single duplicated large transaction can overstate revenue and profit, skew customer count and average order value, and |
| [[Implicit/Claims/claim-claim-inconsistent-dates-wrong-grouping]] | Mixed date formats in a single column cause Power BI to group transactions into incorrect months or years, as demonstrat |
| [[Implicit/Claims/claim-claim-missing-values-break-calculations]] | Blank cells in numeric columns silently corrupt average calculations, produce incomplete slicer lists, and distort machi |
| [[Implicit/Claims/claim-claim-inconsistent-categories-fragment-charts]] | Unnormalised text categories (Mumbai/MUMBAI/Bombay for the same city) cause bar charts to show many small bars instead o |
| [[Implicit/Claims/claim-claim-outliers-warp-averages]] | A single extreme data entry error (e.g., a keychain priced at 20,00,000 instead of 2,000) dramatically distorts the mean |
| [[Implicit/Claims/claim-claim-medallion-habit-no-evaluation]] | Teams automatically implement Bronze/Silver/Gold layers as a default without evaluating whether those layers actually so |
| [[Implicit/Claims/claim-claim-pipeline-step-order-matters]] | Remove duplicates before calculating aggregates. Standardise formats before building relationships. Validate categories  |
| [[Implicit/Claims/claim-claim-countrows-distinctcount-detects-duplicates]] | If COUNTROWS exceeds DISTINCTCOUNT of a key column, duplicate records exist in the table; this DAX-based QA measure is a |
| [[Implicit/Claims/claim-claim-remove-duplicates-early]] | Remove Duplicates must be applied early in the Power Query pipeline, before any aggregations, joins, or calculations tha |
| [[Implicit/Claims/claim-claim-median-robust-to-outliers]] | When outliers are genuine (not data entry errors), the median should be used for central tendency instead of the mean, s |
| [[Implicit/Claims/claim-case-inconsistency-splits-aggregations]] | Text case variations like Mumbai, MUMBAI, and Bombay silently split aggregation groups into phantom segments on bar char |
| [[Implicit/Claims/claim-iso-8601-unambiguous]] | YYYY-MM-DD is the only date format that is unambiguous across all regional conventions; all others cause silent mis-pars |
| [[Implicit/Claims/claim-layer-must-have-distinct-responsibility]] | A layer is only justified when it has a distinct, unambiguous responsibility that no other layer handles; if no one is h |
| [[Implicit/Claims/claim-materialized-views-eliminate-silver]] | In Fabric Lakehouses, materialized views can enforce data quality directly in the Curated layer, eliminating the need fo |
| [[Implicit/Claims/claim-materialization-overhead-accumulation]] | Every materialized layer adds ownership, maintenance, storage, and monitoring burden; the overhead accumulates across th |
| [[Implicit/Claims/claim-semantic-model-replaces-gold-aggregates]] | Power BI semantic models can calculate measures dynamically via VertiPaq, making pre-aggregated Gold layer tables redund |
| [[Implicit/Claims/claim-list-columns-not-index-parallel]] | When a source row contains multiple comma-separated list columns, they are often independent and not aligned by index; m |
| [[Implicit/Claims/claim-boniface-muchendu-source]] | Boniface Muchendu (Data Bear) authored the decision framework article on when medallion architecture is necessary versus |
| [[Implicit/Claims/claim-code-column-reliability]] | Code or type columns can accumulate inconsistent meanings over time as different modules use the same value to represent |
| [[Implicit/Claims/claim-constraint-enforcement-pattern]] | PostgreSQL constraints cannot be bypassed, replacing manual vigilance with enforced rules that run regardless of who ent |
| [[Implicit/Claims/claim-degenerate-dimensions-save-storage]] | Storing transaction IDs as degenerate dimensions instead of creating separate dim_transaction tables saves approximately |
| [[Implicit/Claims/claim-grain-must-be-locked]] | The fact table grain must be defined and locked with a UNIQUE constraint before any other design decisions; mixed grain  |
| [[Implicit/Claims/claim-dual-timestamp-prevents-trend-spikes]] | Storing order_date and warehouse_processing_date separately prevents Black Friday backlog clears from artificially spiki |
| [[Implicit/Claims/claim-multi-key-partitioning-reduces-cost]] | Partitioning by (quarter, region_id) instead of date alone enables partition pruning on both dimensions, reducing comput |
| [[Implicit/Claims/claim-pre-denormalize-at-load-time]] | Denormalize metric components that change per transaction and are used in over 80% of queries directly into the fact tab |
| [[Implicit/Claims/claim-constraint-catches-three-data-quality-issues]] | During migration, Postgres caught duplicate emails, missing FK references, and wrong type values that Excel had silently |
| [[Implicit/Claims/claim-rely-optimizer-eliminates-joins]] | The RELY keyword signals to the cloud warehouse query planner that foreign key constraints are trusted, allowing it to e |
| [[Implicit/Claims/claim-rely-plus-pbi-0-8s]] | Using RELY constraint in the warehouse combined with Power BI Assume Referential Integrity ON reduced a flat table query |
| [[Implicit/Claims/claim-rollup-flags-replaces-20-mviews]] | Storing pre-aggregated rows with boolean flags in a single fact table eliminates the need for 20 separate materialized v |
| [[Implicit/Claims/claim-zstd-500gb-to-70gb]] | Applying ZSTD encoding to a 500GB fact table reduced storage to 70GB, a 86% reduction. |
| [[Implicit/Claims/claim-clustering-reduces-io-40]] | Pre-sorting fact table rows by frequently filtered columns (customer_id, transaction_id) reduces disk I/O by approximate |
| [[Implicit/Claims/claim-surrogate-keys-low-cardinality]] | For status, priority, and category tables with low cardinality, surrogate keys provide value that outweighs the key gene |
| [[Implicit/Claims/claim-natural-keys-high-volume-fact]] | Fact tables with stable source UUIDs and no Type 2 SCD requirements are better served by natural keys, avoiding unnecess |
| [[Implicit/Claims/claim-scd-type-2-requires-surrogate]] | When historical tracking of attribute changes is needed, surrogate keys are required because they persist through dimens |
| [[Implicit/Claims/claim-verify-primary-key-with-count]] | Source systems frequently misidentify primary keys. The only reliable verification is comparing total row count against  |
| [[Implicit/Claims/claim-blind-upsert-silently-overwrites]] | Using a column as an upsert key without verifying uniqueness results in silently overwriting the wrong source rows when  |
| [[Implicit/Edges/authored_by/jesse-ruiz--authored_by--advanced-dimensional-modeling-retail-product-variants-source]] | ****: Jesse Ruiz is the author of the Advanced Dimensional Modeling for Retail Product Variants three-part Medium series. |
| [[Implicit/Edges/authored_by/han-xu-yang--authored_by--data-modeling-bi-trustworthy-analytics]] | ****: Han Xu Yang authored the Data Modeling for BI: Build Trustworthy Analytics article on Medium. |
| [[Implicit/Edges/authored_by/han-xu-yang--authored_by--data-warehousing-bi]] | ****: Han Xu Yang authored the Data Warehousing for BI article on Medium. |
| [[Implicit/Edges/cites/dunlop-beginning-big-data--cites--database-key-types]] | ****: The Database Key Types note is sourced from Chapter 4 of Dunlop's Beginning Big Data with Power BI and Excel 2013 (Apres |
| [[Implicit/Edges/exemplifies/advanced-dimensional-modeling-retail-product-variants-source--exemplifies--d365-fo-product-dimension]] | ****: The retail product variants series exemplifies the D365 F&O product dimension complexity challenge and provides the patt |
| [[Implicit/Edges/builds_on/d365-fo-product-dimension--builds_on--composite-key-strategy-itemkey]] | ****: The composite CONCAT-based ItemKey strategy is the design response to D365 F&O's lack of a unified product table and the |
| [[Implicit/Edges/builds_on/composite-key-strategy-itemkey--builds_on--conditional-joins-case-concat-matching]] | ****: The conditional CASE/CONCAT join pattern uses the CONCAT-based ItemKey structure on both sides of the join to match vari |
| [[Implicit/Edges/builds_on/d365-fo-dimension-groups--builds_on--conditional-joins-case-concat-matching]] | ****: The CASE/CONCAT join pattern is required because dimension groups dictate different matching column sets per row. |
| [[Implicit/Edges/cites/conditional-joins-case-concat-matching--cites--advanced-dimensional-modeling-retail-product-variants-source]] | ****: The conditional-joins pattern originates from Part 2 of Jesse Ruiz's retail product variants series. |
| [[Implicit/Edges/cites/composite-key-strategy-itemkey--cites--advanced-dimensional-modeling-retail-product-variants-source]] | ****: The composite ItemKey strategy originates from Part 1 of Jesse Ruiz's retail product variants series. |
| [[Implicit/Edges/cites/degenerate-dimension-barcode-in-fact--cites--advanced-dimensional-modeling-retail-product-variants-source]] | ****: The barcode-as-degenerate-dimension pattern originates from Part 3 of Jesse Ruiz's retail product variants series. |
| [[Implicit/Edges/contradicts/data-modeling-mistake-missing-date-table--contradicts--advanced-dimensional-modeling-retail-product-variants-source]] | ****: The Date Table pattern advocates a dedicated dimension joined via a single key; the retail product variants series shows |
| [[Implicit/Edges/builds_on/database-key-types--builds_on--composite-key-strategy-itemkey]] | ****: The CONCAT-based ItemKey is a concrete composite-key implementation consistent with the Dunlop composite-key definition. |
| [[Implicit/Edges/builds_on/conformed-dimensions--builds_on--data-modeling-bi-trustworthy-analytics]] | ****: Conformed dimensions operationalise Han Xu Yang's claim that a good BI data model is defined consistently so metrics agr |
| [[Implicit/Edges/builds_on/data-warehousing-bi--builds_on--data-modeling-bi-trustworthy-analytics]] | ****: Han Xu Yang's warehousing article explicitly recaps the OLTP vs OLAP section from the data modeling for BI article. |
| [[Implicit/Edges/builds_on/batch-processing-vs-stream-processing--builds_on--data-warehousing-bi]] | ****: The batch/stream trade-off is one of the central design decisions in the five-stage warehouse architecture. |
| [[Implicit/Edges/contradicts/column-pruning-bravo--contradicts--composite-key-strategy-itemkey]] | ****: Bravo flags surrogate/composite keys as unused candidates for removal, but the composite ItemKey pattern depends on thos |
| [[Implicit/Edges/builds_on/degenerate-dimension-barcode-in-fact--builds_on--advanced-dimensional-modeling-retail-product-variants-source]] | ****: The degenerate barcode dimension pattern is presented as part of Part 3's production optimisation discussion in the reta |
| [[Implicit/Edges/exemplifies/differential-privacy--exemplifies--smartnoise]] | ****: SmartNoise implements differential privacy with SQL aggregations, Python libraries, and Azure SQL integration. |
| [[Implicit/Edges/builds_on/differential-privacy--builds_on--epsilon-parameter]] | ****: Epsilon is the core privacy budget parameter that governs differential privacy guarantees. |
| [[Implicit/Edges/builds_on/differential-privacy--builds_on--delta-parameter]] | ****: Delta represents the acceptable probability of privacy violation in differential privacy systems. |
| [[Implicit/Edges/builds_on/dim-date--builds_on--dax-calendar-function]] | ****: The dim_date pattern uses CALENDAR to generate the base date sequence. |
| [[Implicit/Edges/builds_on/dimension-groups--builds_on--retail-product-variants]] | ****: Dimension groups define which variant attributes apply to retail products, determining join matching rules. |
| [[Implicit/Edges/contradicts/duplicate-barcodes--contradicts--retailshowforitem-filter]] | ****: The duplicate barcodes error is resolved by applying the retailshowforitem = 1 filter. |
| [[Implicit/Edges/builds_on/duplicate-barcodes--builds_on--retail-product-variants]] | ****: Duplicate barcodes occur in retail product variant dimensions where multiple barcode records exist per variant. |
| [[Implicit/Edges/builds_on/star-schema-multi-fact--builds_on--conformed-dimensions]] | ****: Star schema for multi-fact models relies on conformed dimensions with identical definitions across fact tables. |
| [[Implicit/Edges/builds_on/star-schema-multi-fact--builds_on--shared-dimensions]] | ****: Star schema for multi-fact models implements shared dimensions imported once and connected to all facts. |
| [[Implicit/Edges/exemplifies/multiple-fact-tables--exemplifies--star-schema-multi-fact]] | ****: Implementing star schema is the recommended approach for managing multiple fact tables in Power BI. |
| [[Implicit/Edges/exemplifies/multiple-fact-tables--exemplifies--shared-dimensions]] | ****: Multi-fact models exemplify shared dimensions as the solution to avoid duplicating dimension tables per fact. |
| [[Implicit/Edges/builds_on/import-mode--builds_on--incremental-refresh]] | ****: Import mode is required for incremental refresh, which partitions tables to reduce refresh scope. |
| [[Implicit/Edges/builds_on/directquery-mode--builds_on--materialized-views]] | ****: DirectQuery mode benefits from materialized views to eliminate per-query compute cost on complex joins. |
| [[Implicit/Edges/builds_on/incremental-refresh--builds_on--append-only-tables]] | ****: Incremental refresh is designed for append-only tables where historical data never changes. |
| [[Implicit/Edges/exemplifies/filtered-index--exemplifies--barcode-lookup]] | ****: Filtered indexes on non-empty barcodes exemplify the performance benefit of conditional indexing for targeted lookups. |
| [[Implicit/Edges/exemplifies/lambda-architecture--exemplifies--batch-stream-combination]] | ****: Lambda architecture exemplifies combining batch and stream processing for historical accuracy and real-time speed. |
| [[Implicit/Edges/exemplifies/kappa-architecture--exemplifies--batch-stream-combination]] | ****: Kappa architecture exemplifies treating all data as streams to combine batch and stream processing. |
| [[Implicit/Edges/builds_on/materialized-views--builds_on--cetas]] | ****: CETAS serves as an alternative to native materialized views for serverless pools and Delta Lake environments. |
| [[Implicit/Edges/exemplifies/view-precomputation--exemplifies--materialized-views]] | ****: Materialized views exemplify the view precomputation pattern for eliminating per-query compute costs. |
| [[Implicit/Edges/exemplifies/view-precomputation--exemplifies--cetas]] | ****: CETAS exemplifies the view precomputation pattern for serverless and Delta Lake environments. |
| [[Implicit/Edges/builds_on/bronze-layer--builds_on--silver-layer]] | ****: Silver layer builds on Bronze layer by applying cleansing and validation transformations. |
| [[Implicit/Edges/builds_on/silver-layer--builds_on--gold-layer]] | ****: Gold layer builds on Silver layer by applying aggregation and business-ready transformations. |
| [[Implicit/Edges/exemplifies/medallion-architecture--exemplifies--one-lake]] | ****: Medallion architecture is exemplified in Microsoft Fabric via OneLake containers mapping to Bronze/Silver/Gold layers. |
| [[Implicit/Edges/builds_on/medallion-architecture--builds_on--delta-lake]] | ****: Medallion architecture builds on Delta Lake for ACID transaction support on the data lake. |
| [[Implicit/Edges/exemplifies/gold-layer--exemplifies--direct-lake-mode]] | ****: Gold layer is exposed via Direct Lake mode in Power BI for fast querying without import. |
| [[Implicit/Edges/builds_on/pricedisctable--builds_on--product-variants]] | ****: PriceDiscTable provides price records that join to product variants based on matching dimensional attributes. |
| [[Implicit/Edges/builds_on/dimension-groups--builds_on--pricedisctable]] | ****: Dimension groups define which dimensional attributes PriceDiscTable records must match for correct price resolution. |
| [[Implicit/Edges/exemplifies/missing-price-error--exemplifies--pricedisctable]] | ****: Missing prices exemplify a PriceDiscTable join failure when price dimensions do not match variant dimensions. |
| [[Implicit/Edges/builds_on/parquet-format--builds_on--csv-format]] | ****: Parquet format is a more efficient alternative to CSV for large analytical datasets with columnar storage and compressio |
| [[Implicit/Edges/exemplifies/semantic-debt--exemplifies--semantic-debt-analysis]] | ****: Multi-dashboard semantic debt analysis exemplifies how semantic debt manifests across conflicting business concept defin |
| [[Implicit/Edges/contradicts/normalization-3nf--contradicts--transitive-dependency]] | ****: 3NF is violated by transitive dependencies where non-key fields depend on other non-key fields. |
| [[Implicit/Edges/exemplifies/normalization-3nf--exemplifies--third-normal-form]] | ****: Third Normal Form exemplifies the correct application of normalization principles to eliminate update anomalies. |
| [[Implicit/Edges/exemplifies/power-bi-informal-ontologies--exemplifies--ontology]] | ****: Power BI informal ontologies exemplify how semantic models contain domain knowledge that forms the basis of a formal ont |
| [[Implicit/Edges/builds_on/ontology-extraction-70-30--builds_on--power-bi-informal-ontologies]] | ****: The 70/30 auto-generation split builds on the concept that Power BI models are informal ontologies by quantifying the ex |
| [[Implicit/Edges/builds_on/power-bi-ontology-extraction-pipeline--builds_on--power-bi-extractor]] | ****: The ontology extraction pipeline builds on the Power BI Extractor tool as Step 1 of the pipeline. |
| [[Implicit/Edges/builds_on/power-bi-ontology-extraction-pipeline--builds_on--ontology-extraction-70-30]] | ****: The pipeline builds on the 70/30 split concept by implementing it as Steps 2 and 3 of the extraction process. |
| [[Implicit/Edges/builds_on/ontology-extraction-70-30--builds_on--ontology-to-fabric-iq-export]] | ****: The Fabric IQ export pattern builds on the 70/30 split by providing the export destination for validated ontologies. |
| [[Implicit/Edges/builds_on/ontology-to-fabric-iq-export--builds_on--fabric-iq]] | ****: Ontology to Fabric IQ export targets Fabric IQ as the semantic layer for consuming formal ontologies. |
| [[Implicit/Edges/exemplifies/stale-statistics--exemplifies--performance-degradation-over-time]] | ****: Stale statistics exemplifies one of three compounding factors causing performance degradation over time. |
| [[Implicit/Edges/contradicts/cetas--contradicts--performance-degradation-over-time]] | ****: CETAS materialization contradicts on-demand view execution by pre-computing dimensions to prevent degradation. |
| [[Implicit/Edges/contradicts/consolidated-fact-tables--contradicts--duplicated-dimensions]] | ****: Consolidated fact tables contradict the approach of keeping fact tables separate with shared dimensions, while both are  |
| [[Implicit/Edges/contradicts/duplicated-dimensions--contradicts--consolidated-fact-tables]] | ****: Duplicating dimensions per fact table contradicts shared dimension design while stacking fact tables also represents a m |
| [[Implicit/Edges/exemplifies/visual-count-latency--exemplifies--power-bi-visual-performance]] | ****: Visual count per page is a specific cause of visual performance degradation |
| [[Implicit/Edges/exemplifies/matrix-table-high-cardinality-rows--exemplifies--power-bi-visual-performance]] | ****: Matrix and Table visuals with high-cardinality columns exemplify visual performance problems |
| [[Implicit/Edges/exemplifies/conditional-formatting-expensive--exemplifies--power-bi-visual-performance]] | ****: Conditional formatting re-evaluation per cell exemplifies the cost of visual-level complexity |
| [[Implicit/Edges/exemplifies/scatter-plot-rendering--exemplifies--power-bi-visual-performance]] | ****: Dense scatter plots exemplify visual rendering overhead from high data point counts |
| [[Implicit/Edges/cites/power-bi-performance-analyzer--cites--power-bi-visual-performance]] | ****: The Performance Analyzer tool is the recommended benchmarking tool for visual performance |
| [[Implicit/Edges/builds_on/powerpivot-diagram-view--builds_on--manage-relationships]] | ****: Diagram View is the initial visual canvas, but Manage Relationships provides the precise field-level view |
| [[Implicit/Edges/exemplifies/pricing-cte-row-number-deduplication--exemplifies--row-number-window-function]] | ****: The pricing CTE is a concrete application of ROW_NUMBER for deduplication |
| [[Implicit/Edges/cites/pricing-cte-row-number-deduplication--cites--pricedisctable]] | ****: PriceDiscTable is the source table for the pricing CTE pattern |
| [[Implicit/Edges/cites/pricing-cte-row-number-deduplication--cites--inventdim]] | ****: InventDim provides the variant dimension attributes joined in the pricing CTE |
| [[Implicit/Edges/builds_on/null-dimension-handling--builds_on--row-number-window-function]] | ****: ISNULL handling is a prerequisite for consistent key generation before ROW_NUMBER partitioning |
| [[Implicit/Edges/builds_on/pii-removal-techniques--builds_on--pii-categories]] | ****: PII categories inform which removal technique to apply per data type |
| [[Implicit/Edges/builds_on/azure-cognitive-services-pii-detection--builds_on--pii-removal-techniques]] | ****: PII Detection identifies PII before removal techniques are applied |
| [[Implicit/Edges/exemplifies/replicated-table-distribution--exemplifies--data-movement-elimination]] | ****: Replicated table distribution exemplifies how broadcast eliminates data movement across nodes |
| [[Implicit/Edges/builds_on/data-movement-elimination--builds_on--replicate-table-size-rule]] | ****: The 2GB per node rule of thumb determines when replicated distribution is appropriate |
| [[Implicit/Edges/exemplifies/role-playing-dimension--exemplifies--star-schema]] | ****: Role-playing dimensions are a specific application of star schema principles with multiple aliases |
| [[Implicit/Edges/exemplifies/schema-drift-4-6m-loss--exemplifies--schema-drift-column-rename-failure]] | ****: The $4.6M loss is a concrete instance of the schema drift column rename failure mode |
| [[Implicit/Edges/builds_on/schema-drift-column-rename-failure--builds_on--schema-drift-detection]] | ****: Schema drift detection is the mitigation pattern for column rename failures |
| [[Implicit/Edges/exemplifies/schema-drift-detection--exemplifies--schema-drift-fail-safe]] | ****: Fail-safe mode is the critical enforcement mechanism within the schema drift detection pattern |
| [[Implicit/Edges/cites/schema-drift-detection--cites--schema-mapper]] | ****: SchemaMapper is the component that performs the binding validation in schema drift detection |
| [[Implicit/Edges/exemplifies/shared-dimensions--exemplifies--shared-dimensions-model-size]] | ****: The shared dimensions pattern demonstrates how single-dimension reuse reduces model size |
| [[Implicit/Edges/builds_on/shared-dimensions--builds_on--star-schema]] | ****: Shared dimensions build on core star schema principles by applying conformed dimensions across multiple facts |
| [[Implicit/Edges/exemplifies/simple-vs-variant-products--exemplifies--simple-product]] | ****: Simple products are one of the two product types in the simple vs variant distinction |
| [[Implicit/Edges/exemplifies/simple-vs-variant-products--exemplifies--variant-product]] | ****: Variant products are the second product type in the simple vs variant distinction |
| [[Implicit/Edges/builds_on/simple-vs-variant-products--builds_on--unified-itemkey]] | ****: The unified ItemKey pattern resolves the fundamental tension between simple and variant products |
| [[Implicit/Edges/builds_on/variant-product--builds_on--pricedisctable]] | ****: Variant products have their own pricing rows in PriceDiscTable at the variant level |
| [[Implicit/Edges/builds_on/variant-product--builds_on--inventdim]] | ****: Variant products require InventDim to store their valid colour/style/size/config combinations |
| [[Implicit/Edges/exemplifies/star-schema--exemplifies--fact-table]] | ****: The fact table is the central component of a star schema |
| [[Implicit/Edges/exemplifies/star-schema--exemplifies--dimension-table]] | ****: Dimension tables are the surrounding components of a star schema |
| [[Implicit/Edges/exemplifies/star-schema--exemplifies--foreign-key-primary-key]] | ****: Foreign key to primary key relationships connect fact and dimension tables in a star schema |
| [[Implicit/Edges/builds_on/fact-table--builds_on--surrogate-key]] | ****: Fact tables typically use surrogate keys from dimension tables as foreign keys |
| [[Implicit/Edges/exemplifies/fact-table--exemplifies--narrow-fact-tables]] | ****: Fact tables should be narrow, containing only keys and measures for performance |
| [[Implicit/Edges/exemplifies/dimension-table--exemplifies--denormalized-dimensions]] | ****: Dimension tables should be denormalized with wide descriptive attributes |
| [[Implicit/Edges/builds_on/powerpivot-diagram-view--builds_on--powerpivot-auto-relationship-detection]] | ****: PowerPivot's auto-detection creates the relationships that Diagram View then displays |
| [[Implicit/Edges/contradicts/snowflake-schema--contradicts--star-schema]] | ****: Snowflake Schema uses normalised multi-hop joins whereas Star Schema uses single-hop joins, making Snowflake approximate |
| [[Implicit/Edges/builds_on/union-all--builds_on--variant-product]] | ****: The UNION ALL pattern combines variant product rows from InventDimCombination with simple product rows from InventTable  |
| [[Implicit/Edges/builds_on/union-all--builds_on--simple-product]] | ****: The UNION ALL pattern combines simple product rows from InventTable with variant product rows from InventDimCombination  |
| [[Implicit/Edges/exemplifies/unified-product-dimension--exemplifies--union-all]] | ****: The unified product dimension is built by applying UNION ALL to variant and simple product source tables, with variant a |
| [[Implicit/Edges/builds_on/variant-product--builds_on--d365-fo]] | ****: D365 F&O stores variant product data across 12+ interconnected tables with pricing at the variant level, not the product |
| [[Implicit/Edges/builds_on/simple-product--builds_on--d365-fo]] | ****: Simple product data in D365 F&O lives in InventTable while variant product data lives in InventDimCombination, requiring |
| [[Implicit/Edges/builds_on/unified-product-dimension--builds_on--composite-key]] | ****: The unified product dimension uses a composite ItemKey (CONCAT of dataareaid and itemid) to identify simple products, ge |
| [[Implicit/Edges/contradicts/composite-key--contradicts--surrogate-key]] | ****: Surrogate keys replace composite keys for fact-dimension joins, consuming 4 bytes per row vs up to 240 bytes for multi-c |
| [[Implicit/Edges/builds_on/surrogate-key--builds_on--composite-key]] | ****: The surrogate key is assigned at ETL time to replace the original composite business key used for source system joins. |
| [[Implicit/Edges/exemplifies/bridge-table--exemplifies--survey-response-many-to-many]] | ****: The bridge table pattern resolves survey response M:M by splitting one fact-to-dimension M:M join into two one-to-many j |
| [[Implicit/Edges/builds_on/bridge-table--builds_on--star-schema]] | ****: Bridge tables extend star schema to handle many-to-many relationships while preserving the one-to-many relationship stru |
| [[Implicit/Edges/builds_on/bridge-table--builds_on--surrogate-key]] | ****: Bridge tables use surrogate keys on both sides of the bridge to enable clean single-column joins instead of multi-column |
| [[Implicit/Edges/builds_on/diagram-view--builds_on--powerpivot]] | ****: Diagram View is the PowerPivot feature used to visually inspect auto-detected relationships after importing tables from  |
| [[Implicit/Edges/exemplifies/diagram-view--exemplifies--star-schema]] | ****: PowerPivot Diagram View displays the star schema structure with the fact table at the centre and dimension tables as spo |
| [[Implicit/Edges/builds_on/powerpivot--builds_on--star-schema]] | ****: PowerPivot automatically traverses star schema relationship chains when Pivot Tables reference fields from multiple rela |
| [[Implicit/Edges/exemplifies/data-lake--exemplifies--schema-on-read]] | ****: Data lakes apply schema-on-read, imposing structure only at query time rather than at ingestion time. |
| [[Implicit/Edges/exemplifies/data-warehouse--exemplifies--schema-on-write]] | ****: Data warehouses enforce schema-on-write, validating and structuring data before storage to ensure quality at write time. |
| [[Implicit/Edges/builds_on/data-lake--builds_on--data-warehouse]] | ****: Modern architectures feed raw data into a data lake first, then transform and curate business-level datasets into a data |
| [[Implicit/Edges/contradicts/data-swamp--contradicts--data-lake]] | ****: Without governance and schema enforcement, data lakes degrade into data swamps where bad data proliferates unchecked. |
| [[Implicit/Edges/exemplifies/data-warehouse--exemplifies--inmon-approach]] | ****: The Inmon approach builds data warehouses as normalised EDWs in Third Normal Form before slicing out departmental data m |
| [[Implicit/Edges/builds_on/inmon-approach--builds_on--third-normal-form]] | ****: Inmon's EDW uses Third Normal Form to eliminate transitive dependencies and store every entity attribute in exactly one  |
| [[Implicit/Edges/exemplifies/inmon-approach--exemplifies--enterprise-data-warehouse]] | ****: The Inmon approach requires building a centralised Enterprise Data Warehouse in 3NF before any business team can access  |
| [[Implicit/Edges/builds_on/data-mart--builds_on--inmon-approach]] | ****: In Inmon's methodology, data marts are sliced out from the normalised EDW as star schemas or cubes after the EDW is full |
| [[Implicit/Edges/contradicts/inmon-approach--contradicts--kimball-approach]] | ****: Inmon's top-down normalised approach (EDW first) directly contradicts Kimball's bottom-up dimensional approach (data mar |
| [[Implicit/Edges/builds_on/data-vault--builds_on--inmon-approach]] | ****: Data Vault 2.0 emerged as an evolution addressing Inmon's limitations around agility and parallel loading for complex en |
| [[Implicit/Edges/builds_on/data-vault--builds_on--kimball-approach]] | ****: Data Vault 2.0 builds on Kimball's business-process orientation while adding hash keys, point-in-time constructs, and sa |
| [[Implicit/Edges/builds_on/inmon-approach--builds_on--star-schema]] | ****: In Inmon's methodology, data marts sliced from the EDW are typically modelled as star schemas, making star schema the do |
| [[Implicit/Edges/exemplifies/kimball-approach--exemplifies--star-schema]] | ****: Kimball's bottom-up approach builds star schemas directly for each business process, making star schema the primary mode |
| [[Implicit/Edges/builds_on/scd-type-2--builds_on--surrogate-key]] | ****: SCD Type 2 requires a surrogate key on every dimension row (active and inactive versions) so that fact rows can join to  |
| [[Implicit/Edges/exemplifies/scd-type-1--exemplifies--slowly-changing-dimension]] | ****: SCD Type 1 is one of two main SCD patterns: attribute changes overwrite the previous value in place without preserving h |
| [[Implicit/Edges/exemplifies/scd-type-2--exemplifies--slowly-changing-dimension]] | ****: SCD Type 2 is one of two main SCD patterns: attribute changes create new dimension rows with effective date ranges to pr |
| [[Implicit/Edges/exemplifies/wrong-granularity-scd--exemplifies--scd-type-2]] | ****: The wrong granularity mistake is specific to SCD Type 2 where fact rows must join to a specific historical version, not  |
| [[Implicit/Edges/contradicts/wrong-granularity-scd--contradicts--surrogate-key]] | ****: Wrong granularity SCD occurs when a fact table lacks a point-in-time surrogate key; the correct fix is assigning a surro |
| [[Implicit/Edges/builds_on/scd-type-1--builds_on--degenerate-dimension]] | ****: In D365 F&O, RetailPrice is a Type 1 SCD attribute stored in the product dimension; pricing history lives in PriceDiscTa |
| [[Implicit/Edges/exemplifies/scd-type-1--exemplifies--role-playing-dimension]] | ****: Role-playing dimensions (OrderDate, ShipDate, DueDate all pointing to the same Date dimension) are a separate pattern fr |
| [[Implicit/Edges/exemplifies/bi-directional-filtering--exemplifies--cross-filter-direction]] | ****: Bi-directional filtering is the Cross Filter Direction setting set to Both on a Power BI relationship, propagating filte |
| [[Implicit/Edges/exemplifies/bi-directional-overuse-causes-duplication--exemplifies--bi-directional-filtering]] | ****: Setting Cross Filter Direction to Both on a relationship causes row duplication in aggregate visuals when multiple filte |
| [[Implicit/Edges/builds_on/bi-directional-filtering--builds_on--broken-relationship]] | ****: The temptation to enable bi-directional filtering usually indicates a missing relationship; fixing the missing link is t |
| [[Implicit/Edges/contradicts/crossfilter-dax--contradicts--bi-directional-filtering]] | ****: CROSSFILTER in DAX provides targeted cross-table filtering without changing the model-wide default direction, replacing  |
| [[Implicit/Edges/builds_on/cross-filter-direction--builds_on--crossfilter-dax]] | ****: CROSSFILTER is the DAX function that overrides the Cross Filter Direction relationship property for a specific calculati |
| [[Implicit/Edges/builds_on/broken-relationship--builds_on--cross-filter-direction]] | ****: A broken relationship can result from setting Cross Filter Direction incorrectly (e.g., pointing Fact to Dimension inste |
| [[Implicit/Edges/exemplifies/missing-date-relationship--exemplifies--broken-relationship]] | ****: A missing date relationship is a specific broken relationship where the fact table is not connected to a Date dimension, |
| [[Implicit/Edges/builds_on/star-schema--builds_on--fact-table]] | ****: Star Schema organises one or more fact tables at the centre with dimension tables radiating outward via single-hop forei |
| [[Implicit/Edges/builds_on/star-schema--builds_on--dimension-table]] | ****: Star Schema uses flat dimension tables with all attributes at the same level, rather than normalised sub-tables as in Sn |
| [[Implicit/Edges/builds_on/snowflake-schema--builds_on--dimension-table]] | ****: Snowflake Schema normalises dimension tables into hierarchies (Region, Manager, Director) stored as separate related tab |
| [[Implicit/Edges/builds_on/surrogate-key--builds_on--fact-table]] | ****: Fact tables should always use integer surrogate keys as foreign keys, never multi-column string composites, for memory e |
| [[Implicit/Edges/exemplifies/star-schema-default-power-bi--exemplifies--star-schema]] | ****: Star Schema should be the default for 90% of Power BI projects due to single-hop joins and superior query and refresh pe |
| [[Implicit/Edges/exemplifies/snowflake-slower-4x--exemplifies--snowflake-schema]] | ****: Snowflake Schema with 4-hop join chains (Region to Manager to Director) produces approximately 4x slower query performan |
| [[Implicit/Edges/exemplifies/union-all-over-union--exemplifies--union-all]] | ****: UNION ALL is faster than UNION in ETL because the ETL logic already guarantees no overlap between variant and simple pro |
| [[Implicit/Edges/exemplifies/composite-key-60x-memory--exemplifies--composite-key]] | ****: A 6-column NVARCHAR composite key at 20 characters per column consumes ~240 bytes per row vs 4 bytes for an integer surr |
| [[Implicit/Edges/exemplifies/d365-no-single-products-table--exemplifies--d365-fo]] | ****: D365 F&O has no single Products table; product data spans EcoResProduct, InventTable, InventDimCombination, InventDim, P |
| [[Implicit/Edges/exemplifies/broken-relationships-wrong-totals--exemplifies--broken-relationship]] | ****: Missing or incorrectly configured relationships (wrong direction, cardinality, or duplicate path) are the root cause of  |
| [[Implicit/Edges/exemplifies/scd-type1-overwrites-price--exemplifies--scd-type-1]] | ****: In SCD Type 1, when RetailPrice changes the value is overwritten in place with no historical row added; pricing history  |
| [[Implicit/Edges/exemplifies/inmon-top-down--exemplifies--inmon-approach]] | ****: Inmon's methodology is top-down: the EDW must be fully built in 3NF before data marts are sliced out for business teams. |
| [[Implicit/Edges/exemplifies/inmon-single-truth--exemplifies--inmon-approach]] | ****: The Inmon EDW provides a single source of truth by storing every entity in exactly one place, so a customer address chan |
| [[Implicit/Edges/exemplifies/bridge-avoids-m2m-overhead--exemplifies--bridge-table]] | ****: A bridge table keeps relationships as one-to-one and makes COUNTX unambiguous, avoiding the computation overhead of Powe |
| [[Implicit/Edges/exemplifies/powerpivot-auto-relationship-import--exemplifies--powerpivot]] | ****: PowerPivot imports any relationships defined in the source Access or SQL Server database during table import and display |
| [[Implicit/Edges/exemplifies/schema-on-read-flexibility--exemplifies--schema-on-read]] | ****: Schema-on-read enables data lakes to store any format (JSON, CSV, Parquet, images, logs) without upfront structure, defe |
| [[Implicit/Edges/exemplifies/lake-and-warehouse-complementary--exemplifies--data-lake]] | ****: Modern architectures use a data lake for cheap raw storage and ingestion of any data format before transformation. |
| [[Implicit/Edges/exemplifies/lake-and-warehouse-complementary--exemplifies--data-warehouse]] | ****: Modern architectures use a data warehouse for fast curated analytical queries, fed by transformation from the upstream d |
| [[Implicit/Edges/exemplifies/claim-schema-on-read-vs-write--exemplifies--data-lake]] | ****: Data lakes exemplify schema-on-read by applying structure at query time rather than at ingestion. |
| [[Implicit/Edges/exemplifies/claim-schema-on-read-vs-write--exemplifies--data-warehouse]] | ****: Data warehouses exemplify schema-on-write by enforcing structure at ingestion time. |
| [[Implicit/Edges/exemplifies/claim-medallion-standard-pattern--exemplifies--medallion-architecture]] | ****: Delta Lake on Databricks, Fabric, and Snowflake exemplifies the Bronze/Silver/Gold medallion pattern. |
| [[Implicit/Edges/builds_on/claim-medallion-standard-pattern--builds_on--delta-lake]] | ****: Delta Lake provides the ACID transaction layer that enables reliable medallion architecture reprocessing. |
| [[Implicit/Edges/exemplifies/claim-lakehouse-blurs-lines--exemplifies--lakehouse-architecture]] | ****: Lakehouse architectures exemplify the convergence of data lake storage with data warehouse governance features. |
| [[Implicit/Edges/builds_on/claim-lakehouse-blurs-lines--builds_on--delta-lake]] | ****: Delta Lake is the enabling technology behind lakehouse architecture implementations. |
| [[Implicit/Edges/contradicts/batch-processing--contradicts--stream-processing]] | ****: Batch processing trades real-time latency for simplicity, contradicting stream processing's complexity-for-speed tradeof |
| [[Implicit/Edges/builds_on/lambda-architecture--builds_on--batch-processing]] | ****: Lambda architecture builds on batch processing as one of its two parallel processing paths. |
| [[Implicit/Edges/builds_on/lambda-architecture--builds_on--stream-processing]] | ****: Lambda architecture builds on stream processing as its speed layer for near-real-time results. |
| [[Implicit/Edges/builds_on/kappa-architecture--builds_on--stream-processing]] | ****: Kappa architecture simplifies Lambda by removing the batch layer and treating all data as a stream. |
| [[Implicit/Edges/exemplifies/claim-batch-first-default--exemplifies--batch-processing]] | ****: Batch processing exemplifies the honest default for most business data processing needs, with stream added only when a r |
| [[Implicit/Edges/contradicts/claim-batch-first-default--contradicts--stream-processing]] | ****: The claim contradicts blindly adopting stream processing as the default, recommending it only when genuinely required. |
| [[Implicit/Edges/exemplifies/claim-star-schema-mandatory--exemplifies--star-schema]] | ****: Star schema is presented as the mandatory pattern that replaces the anti-pattern of auto-joined flat files. |
| [[Implicit/Edges/contradicts/claim-star-schema-mandatory--contradicts--flat-table]] | ****: The claim directly contradicts using flat tables, asserting that star schema is mandatory for performant models. |
| [[Implicit/Edges/exemplifies/claim-flat-table-breaks-calculations--exemplifies--flat-table]] | ****: Flat tables exemplify the model bloat and broken DAX calculations that star schema prevents. |
| [[Implicit/Edges/exemplifies/claim-surrogate-key-memory-efficiency--exemplifies--surrogate-key]] | ****: Integer surrogate keys exemplify the memory-efficient alternative to multi-byte string composite keys at scale. |
| [[Implicit/Edges/contradicts/claim-surrogate-key-memory-efficiency--contradicts--composite-key]] | ****: The memory efficiency claim contradicts composite key design, which consumes multi-bytes-per-character versus 4 bytes fo |
| [[Implicit/Edges/exemplifies/claim-scd-wrong-granularity-recalculation--exemplifies--slowly-changing-dimension]] | ****: SCDs exemplify the performance risk when dimension tables are joined at wrong granularity, causing full in-memory recalc |
| [[Implicit/Edges/exemplifies/claim-bridge-tables-solve-many-to-many--exemplifies--bridge-table]] | ****: Bridge tables exemplify the correct resolution for many-to-many cardinality that avoids ambiguous filter propagation. |
| [[Implicit/Edges/builds_on/dim-date--builds_on--date-table]] | ****: dim_date is the conventional naming convention for the dedicated date dimension table in Power BI. |
| [[Implicit/Edges/exemplifies/claim-import-faster-than-directquery--exemplifies--import-mode]] | ****: Import mode exemplifies the faster storage mode that loads data into memory versus reading from disk at query time. |
| [[Implicit/Edges/contradicts/claim-import-faster-than-directquery--contradicts--directquery]] | ****: The claim contradicts DirectQuery as a general-purpose default, asserting that Import is faster for most workloads. |
| [[Implicit/Edges/exemplifies/claim-incremental-refresh-game-changer--exemplifies--incremental-refresh]] | ****: Incremental refresh exemplifies the performance optimisation for append-only data sources like GA4 and daily feeds. |
| [[Implicit/Edges/exemplifies/bravo-for-power-bi--exemplifies--column-pruning]] | ****: Bravo for Power BI exemplifies a tool that surfaces unused columns to support column pruning for model size reduction. |
| [[Implicit/Edges/exemplifies/claim-bi-directional-ambiguity--exemplifies--bi-directional-filtering]] | ****: Bi-directional cross-filtering exemplifies the anti-pattern that causes ambiguous filter context and row duplication. |
| [[Implicit/Edges/contradicts/claim-bi-directional-ambiguity--contradicts--one-to-many-relationship]] | ****: The ambiguity claim contradicts defaulting to bi-directional filtering; single-direction one-to-many is the correct defa |
| [[Implicit/Edges/exemplifies/claim-measures-preferred-over-calculated-columns--exemplifies--dax-measure]] | ****: DAX measures exemplify query-time evaluated expressions that respond to slicer context. |
| [[Implicit/Edges/contradicts/claim-measures-preferred-over-calculated-columns--contradicts--calculated-column]] | ****: The claim contradicts calculated columns as a general-purpose choice, asserting that they do not respond to slicers and  |
| [[Implicit/Edges/exemplifies/claim-date-table-unlocks-time-intelligence--exemplifies--date-table]] | ****: A dedicated date dimension table exemplifies the prerequisite for enabling YTD, MTD, and SAMEPERIODLASTYEAR in Power BI. |
| [[Implicit/Edges/builds_on/claim-date-table-unlocks-time-intelligence--builds_on--time-intelligence]] | ****: DAX time intelligence functions build on the presence of a properly configured date dimension table. |
| [[Implicit/Edges/builds_on/account-code-ranges--builds_on--pl-line-structure]] | ****: Account code ranges (100-199 Revenue, 200-299 Cost of Sales, etc.) form the classification system that maps to P&L line  |
| [[Implicit/Edges/builds_on/chart-of-accounts--builds_on--pl-mapping-table]] | ****: The Chart of Accounts provides the account codes that the P&L Mapping Table maps to P&L sections. |
| [[Implicit/Edges/builds_on/pl-mapping-table--builds_on--pl-line-structure]] | ****: The P&L Mapping Table resolves raw account codes into the standard P&L line structure hierarchy. |
| [[Implicit/Edges/exemplifies/claim-duplicates-distort-metrics--exemplifies--duplicate-records]] | ****: Duplicate records exemplify the specific data quality failure that distorts revenue, profit, customer count, and invento |
| [[Implicit/Edges/exemplifies/claim-inconsistent-dates-wrong-grouping--exemplifies--inconsistent-date-formats]] | ****: Inconsistent date formats exemplify the data quality failure that causes Power BI to group transactions into wrong month |
| [[Implicit/Edges/contradicts/iso-date-format--contradicts--inconsistent-date-formats]] | ****: ISO date format contradicts inconsistent date formats by providing a universal unambiguous standard that eliminates loca |
| [[Implicit/Edges/exemplifies/claim-missing-values-break-calculations--exemplifies--missing-values]] | ****: Missing values exemplify the silent data quality failure that corrupts averages, slicers, and forecasting models. |
| [[Implicit/Edges/exemplifies/claim-inconsistent-categories-fragment-charts--exemplifies--inconsistent-categories]] | ****: Inconsistent categories exemplify the text quality failure that splits bar charts into many small bars instead of one ag |
| [[Implicit/Edges/builds_on/text-transform--builds_on--inconsistent-categories]] | ****: Text.Trim and Text.Clean in Power Query remove whitespace and invisible characters that cause false inconsistencies betw |
| [[Implicit/Edges/exemplifies/claim-outliers-warp-averages--exemplifies--outlier]] | ****: Outliers exemplify the extreme value failure that distorts means, trend lines, and forecasting models without raising ex |
| [[Implicit/Edges/builds_on/min-max-qa--builds_on--outlier]] | ****: The min/max QA check is the primary detection method for catching data entry errors that produce outliers. |
| [[Implicit/Edges/exemplifies/claim-median-robust-to-outliers--exemplifies--median]] | ****: The median exemplifies a central tendency measure that is robust to extreme values and does not get distorted by outlier |
| [[Implicit/Edges/contradicts/claim-median-robust-to-outliers--contradicts--outlier]] | ****: Using the median contradicts ignoring outliers by providing a robust measure when outliers are genuine data rather than  |
| [[Implicit/Edges/exemplifies/dashboard-health-checklist--exemplifies--duplicate-records]] | ****: The Dashboard Health Checklist includes a duplicate check as the first of five pre-publish quality questions. |
| [[Implicit/Edges/exemplifies/dashboard-health-checklist--exemplifies--inconsistent-date-formats]] | ****: The Dashboard Health Checklist includes date format standardisation as the second of five pre-publish quality questions. |
| [[Implicit/Edges/exemplifies/dashboard-health-checklist--exemplifies--missing-values]] | ****: The Dashboard Health Checklist includes blank value handling as the third of five pre-publish quality questions. |
| [[Implicit/Edges/exemplifies/dashboard-health-checklist--exemplifies--inconsistent-categories]] | ****: The Dashboard Health Checklist includes category normalisation as the fourth of five pre-publish quality questions. |
| [[Implicit/Edges/exemplifies/dashboard-health-checklist--exemplifies--outlier]] | ****: The Dashboard Health Checklist includes outlier review as the fifth of five pre-publish quality questions. |
| [[Implicit/Edges/builds_on/countrows-vs-distinctcount--builds_on--duplicate-records]] | ****: COUNTROWS vs DISTINCTCOUNT is the DAX technique used to detect whether duplicate records exist in a table. |
| [[Implicit/Edges/builds_on/countrows-vs-distinctcount--builds_on--primary-key]] | ****: COUNTROWS vs DISTINCTCOUNT requires a unique primary key column to accurately detect duplicate rows. |
| [[Implicit/Edges/exemplifies/data-cleaning-pipeline--exemplifies--duplicate-records]] | ****: The Data Cleaning Pipeline starts with duplicate detection as step one, applied before any aggregation or join operation |
| [[Implicit/Edges/exemplifies/data-cleaning-pipeline--exemplifies--missing-values]] | ****: The Data Cleaning Pipeline handles missing values as step two, after deduplication. |
| [[Implicit/Edges/exemplifies/data-cleaning-pipeline--exemplifies--inconsistent-date-formats]] | ****: The Data Cleaning Pipeline standardises date formats (ISO) as part of format standardisation, before relationship buildi |
| [[Implicit/Edges/exemplifies/data-cleaning-pipeline--exemplifies--inconsistent-categories]] | ****: The Data Cleaning Pipeline validates and normalises text categories as step four, before slicer creation. |
| [[Implicit/Edges/exemplifies/data-cleaning-pipeline--exemplifies--outlier]] | ****: The Data Cleaning Pipeline reviews outliers (min/max check) as step five, before loading clean data into the semantic mo |
| [[Implicit/Edges/exemplifies/claim-pipeline-step-order-matters--exemplifies--data-cleaning-pipeline]] | ****: The ordered sequence of the data cleaning pipeline (duplicates first, then blanks, formats, categories, outliers) exempl |
| [[Implicit/Edges/exemplifies/claim-countrows-distinctcount-detects-duplicates--exemplifies--countrows-vs-distinctcount]] | ****: COUNTROWS vs DISTINCTCOUNT exemplifies the specific DAX QA technique that reveals duplicate records before publishing. |
| [[Implicit/Edges/exemplifies/claim-remove-duplicates-early--exemplifies--duplicate-records]] | ****: Removing duplicates early exemplifies the correct pipeline position to prevent downstream corruption of aggregations and |
| [[Implicit/Edges/exemplifies/claim-medallion-habit-no-evaluation--exemplifies--architecture-by-habit]] | ****: Automatically applying Bronze/Silver/Gold without evaluating schema change frequency, team structure, platform governanc |
| [[Implicit/Edges/contradicts/architecture-by-habit--contradicts--medallion-architecture]] | ****: Architecture by habit contradicts evidence-based medallion adoption by applying layers as a default rather than in respo |
| [[Implicit/Edges/builds_on/star-schema--builds_on--surrogate-key]] | ****: Star schema in Power BI builds on surrogate integer keys for memory-efficient fact-to-dimension joins at scale. |
| [[Implicit/Edges/builds_on/star-schema--builds_on--one-to-many-relationship]] | ****: Star schema is defined by single-direction one-to-many relationships radiating from dimension tables to the central fact |
| [[Implicit/Edges/builds_on/star-schema--builds_on--bridge-table]] | ****: Star schema handles many-to-many scenarios by inserting a bridge table to maintain the single-direction relationship pri |
| [[Implicit/Edges/builds_on/star-schema--builds_on--date-table]] | ****: Star schema includes a dedicated date dimension table to support time intelligence across all fact tables. |
| [[Implicit/Edges/authored_by/jesse-ruiz--authored_by--3-easy-data-architecture-interview-questions-source]] | ****: Jesse Ruiz authored the 3 Easy Data Architecture Interview Questions article covering data lakes, medallion, and batch v |
| [[Implicit/Edges/authored_by/bill-donofrio--authored_by--stop-building-slow-power-bi-reports-source]] | ****: Bill Donofrio authored the Stop Building Slow Power BI Reports checklist article covering star schema, surrogate keys, a |
| [[Implicit/Edges/authored_by/anurodh-kumar--authored_by--source-5-mistakes-in-power-bi-data-modeling]] | ****: Anurodh Kumar authored the 5 Mistakes in Power BI Data Modeling article covering flat tables, relationships, and date ta |
| [[Implicit/Edges/authored_by/digitalbykewat--authored_by--5-data-cleaning-mistakes-digitalbykewat-source]] | ****: DigitalBYKewat authored the 5 Data Cleaning Mistakes article covering duplicates, dates, blanks, categories, and outlier |
| [[Implicit/Edges/authored_by/yadullah-abidi--authored_by--author-yadullah-abidi]] | ****: Yadullah Abidi is the author covered in the MakeUseOf contributor profile for PostgreSQL and database tooling content. |
| [[Implicit/Edges/authored_by/digitalbykewat--authored_by--author-digitalbykewat]] | ****: DigitalBYKewat is the author of the Medium profile covering data cleaning, Power Query, and Power BI content. |
| [[Implicit/Edges/exemplifies/case-inconsistency-splits-aggregations--exemplifies--text-normalization]] | ****: Case variations like Mumbai/MUMBAI/Bombay demonstrate how text inconsistency silently splits aggregation groups. |
| [[Implicit/Edges/builds_on/text-normalization--builds_on--power-query-transforms]] | ****: Text normalization uses Power Query transforms like Text.Trim and Text.Clean to remove invisible characters and standard |
| [[Implicit/Edges/exemplifies/iso-8601-unambiguous--exemplifies--date-format-standardization]] | ****: The date mis-parsing example demonstrates why ISO 8601 (YYYY-MM-DD) is the only unambiguous date format. |
| [[Implicit/Edges/builds_on/date-format-standardization--builds_on--power-query-transforms]] | ****: Date format standardization is applied using Power Query locale settings and type transformations. |
| [[Implicit/Edges/exemplifies/layer-must-have-distinct-responsibility--exemplifies--medallion-architecture]] | ****: The medallion architecture principle states that each layer must have a distinct responsibility boundary to be justified |
| [[Implicit/Edges/builds_on/medallion-architecture--builds_on--landing-layer]] | ****: Medallion architecture includes a Landing layer for initial data ingestion from source systems. |
| [[Implicit/Edges/builds_on/medallion-architecture--builds_on--curated-layer]] | ****: Medallion architecture includes a Curated layer for data quality and star schema modeling. |
| [[Implicit/Edges/builds_on/medallion-architecture--builds_on--analytics-layer]] | ****: Medallion architecture may include an Analytics layer for pre-aggregated datasets. |
| [[Implicit/Edges/builds_on/materialized-views-eliminate-silver--builds_on--curated-layer]] | ****: Materialized views in Fabric can enforce data quality directly in the Curated layer, potentially eliminating a separate  |
| [[Implicit/Edges/exemplifies/materialized-views-eliminate-silver--exemplifies--materialized-views]] | ****: Fabric Lakehouse materialized views can apply NOT NULL, range, and required field constraints during materialization. |
| [[Implicit/Edges/builds_on/materialized-views-eliminate-silver--builds_on--data-quality-constraints]] | ****: Materialized views enforce data quality constraints (NOT NULL, positive values, required fields) directly in the Curated |
| [[Implicit/Edges/exemplifies/medallion-architecture--exemplifies--microsoft-fabric]] | ****: Microsoft Fabric implements medallion architecture via OneLake containers (Bronze, Silver, Gold). |
| [[Implicit/Edges/builds_on/medallion-architecture--builds_on--onelake]] | ****: OneLake serves as the single logical data lake in Fabric hosting all medallion layer containers. |
| [[Implicit/Edges/builds_on/direct-lake-mode--builds_on--onelake]] | ****: Direct Lake mode allows Power BI to read Gold layer data directly from OneLake without importing into memory. |
| [[Implicit/Edges/exemplifies/materialization-overhead-accumulation--exemplifies--medallion-architecture]] | ****: Each materialized medallion layer adds ownership, maintenance, storage, and monitoring overhead that accumulates across  |
| [[Implicit/Edges/exemplifies/semantic-model-replaces-gold-aggregates--exemplifies--power-bi-semantic-model]] | ****: Power BI semantic models can dynamically calculate measures via VertiPaq, making pre-aggregated Gold tables potentially  |
| [[Implicit/Edges/contradicts/semantic-model-replaces-gold-aggregates--contradicts--medallion-architecture]] | ****: The semantic model claim contradicts the assumption that a Gold layer with pre-aggregates is always necessary. |
| [[Implicit/Edges/exemplifies/star-schema--exemplifies--microsoft-fabric]] | ****: Fabric's Gold layer is where the star schema (fact and dimension tables) lives and is exposed to Power BI via Direct Lak |
| [[Implicit/Edges/builds_on/star-schema--builds_on--direct-lake-mode]] | ****: Power BI connects to the Fabric Gold layer star schema via Direct Lake mode, reading fact and dimension tables from OneL |
| [[Implicit/Edges/exemplifies/bridge-table--exemplifies--many-to-many-relationship]] | ****: Bridge tables resolve many-to-many relationships where one fact row maps to multiple dimension values (events affecting  |
| [[Implicit/Edges/exemplifies/list-columns-not-index-parallel--exemplifies--bridge-table]] | ****: Real-world data shows comma-separated list columns in the same row are often independent, not index-aligned, making brid |
| [[Implicit/Edges/builds_on/bridge-table--builds_on--fact-table]] | ****: Bridge tables maintain the fact table grain (one event = one row) while adding the dimension relationship layer without  |
| [[Implicit/Edges/builds_on/missing-values-handling--builds_on--power-query-transforms]] | ****: Missing values are handled via Power Query transforms: Fill Down/Up, Replace Nulls, Replace Errors, and Remove Rows with |
| [[Implicit/Edges/authored_by/boniface-muchendu--authored_by--boniface-muchendu-source]] | ****: Boniface Muchendu authored the decision framework article on medallion architecture necessity. |
| [[Implicit/Edges/authored_by/anurodh-kumar--authored_by--medallion-architecture-fabric]] | ****: Anurodh Kumar authored the Fabric medallion architecture guide. |
| [[Implicit/Edges/authored_by/anurodh-kumar--authored_by--star-schema-fabric]] | ****: Anurodh Kumar authored the star schema in Fabric pattern note. |
| [[Implicit/Edges/authored_by/digitalbykewat--authored_by--inconsistent-categories-normalisation]] | ****: DigitalBYKewat authored the text normalization article on case inconsistency. |
| [[Implicit/Edges/authored_by/digitalbykewat--authored_by--inconsistent-date-formats-iso]] | ****: DigitalBYKewat authored the date format standardization article. |
| [[Implicit/Edges/authored_by/digitalbykewat--authored_by--missing-values-handling-strategy]] | ****: DigitalBYKewat authored the missing values handling strategy article. |
| [[Implicit/Edges/exemplifies/cleansed-layer--exemplifies--cdc-column]] | ****: The Cleansed Layer establishes CDC as part of its transformation pass using the CDC column. |
| [[Implicit/Edges/exemplifies/cleansed-layer--exemplifies--multi-source-merge]] | ****: The Cleansed Layer applies multi-source merge logic when the same entity exists in multiple source tables. |
| [[Implicit/Edges/builds_on/schema-first-design--builds_on--cdc-column]] | ****: Schema-first design requires knowing the source table behavior (insert-only vs upsert) to select the correct CDC column. |
| [[Implicit/Edges/builds_on/watermark-table--builds_on--cdc-column]] | ****: A watermark table depends on a well-chosen CDC column to track progress across incremental loads. |
| [[Implicit/Edges/builds_on/normalized-tables--builds_on--postgres-constraints]] | ****: Normalized tables define the entities that Postgres constraints then enforce through type and referential integrity. |
| [[Implicit/Edges/builds_on/schema-first-design--builds_on--flag-and-preserve]] | ****: Schema-first design surfaces data quality problems, which are then handled using the flag-and-preserve philosophy rather |
| [[Implicit/Edges/exemplifies/excel-to-postgres-migration--exemplifies--schema-first-design]] | ****: The migration workflow's first step is schema-first design, treating it as the foundational step before any code. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--kimball-dimensional-modeling]] | ****: The Baylas 2026 case study applies and validates Kimball dimensional modeling in a real-world project. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--medallion-architecture]] | ****: The Baylas project uses medallion architecture (raw, cleansed, dimensional) as its three-layer structure. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--flag-and-preserve]] | ****: The case study applies the flag-and-preserve data quality philosophy rather than silently discarding mismatched values. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--cdc-column]] | ****: The case study demonstrates CDC column selection as a key architectural decision in the cleansing layer. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--multi-source-merge]] | ****: The project encountered the multi-source merge problem and resolved it using archive-priority load sequencing. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--indexing-strategy]] | ****: The project deferred indexing until schema stabilization and applied indexes based on concrete join scenarios. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--junk-dimension]] | ****: The project applied junk dimension criteria to decide whether to combine or separate low-cardinality attributes. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--upsert-table]] | ****: The project used updated date as the CDC column for tables with upsert behavior where records are modified over time. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--insert-only-table]] | ****: The project used created date as the CDC column for tables with insert-only behavior where records are never updated. |
| [[Implicit/Edges/exemplifies/kimball-baylas-2026--exemplifies--elt-pattern]] | ****: The project used ELT (transformation inside the target database) rather than a separate ETL processing layer. |
| [[Implicit/Edges/authored_by/kimball-baylas-2026--authored_by--source-yadullah-abidi]] | ****: The Baylas 2026 case study article was authored by Kaan Baylas. |
| [[Implicit/Edges/authored_by/schema-first-design--authored_by--source-yadullah-abidi]] | ****: The schema-first migration pattern article was sourced from Yadullah Abidi's work. |
| [[Implicit/Edges/authored_by/excel-to-postgres-migration--authored_by--source-yadullah-abidi]] | ****: The Excel to Postgres migration workflow was sourced from Yadullah Abidi's work. |
| [[Implicit/Edges/authored_by/postgres-constraints--authored_by--source-yadullah-abidi]] | ****: The constraints article was sourced from Yadullah Abidi's work. |
| [[Implicit/Edges/authored_by/normalized-tables--authored_by--source-yadullah-abidi]] | ****: The normalized tables vs flat rows article was sourced from Yadullah Abidi's work. |
| [[Implicit/Edges/cites/medallion-architecture--cites--kimball-baylas-2026]] | ****: The medallion architecture article cites the Baylas 2026 case study as its primary source and real-world example. |
| [[Implicit/Edges/contradicts/inmon-edw--contradicts--kimball-dimensional-modeling]] | ****: Inmon and Kimball are competing methodologies with opposite directional approaches (top-down vs bottom-up) and different |
| [[Implicit/Edges/contradicts/inmon-edw--contradicts--data-vault]] | ****: Inmon's top-down 3NF approach and Data Vault's middle-out hub-link-satellite structure represent fundamentally different |
| [[Implicit/Edges/contradicts/kimball-dimensional-modeling--contradicts--data-vault]] | ****: Kimball's dimensional modeling and Data Vault's hub-link-satellite approach target different concerns (fast delivery vs  |
| [[Implicit/Edges/builds_on/medallion-architecture--builds_on--inmon-edw]] | ****: Medallion architecture can be applied on top of an Inmon EDW, where the dimensional layer serves as the presentation lay |
| [[Implicit/Edges/builds_on/medallion-architecture--builds_on--data-vault]] | ****: Data Vault always requires a dimensional presentation layer on top since it is not suitable for direct business user con |
| [[Implicit/Edges/builds_on/dimensional-layer--builds_on--junk-dimension]] | ****: The Dimensional Layer is where the junk dimension pattern is applied as a Kimball modeling decision. |
| [[Implicit/Edges/builds_on/dimensional-layer--builds_on--indexing-strategy]] | ****: Indexes are applied in the Dimensional Layer after schema stabilization and before BI reporting begins. |
| [[Implicit/Edges/contradicts/etl-run-date--contradicts--cdc-column]] | ****: ETL run date is identified as an anti-pattern for CDC: it has no business meaning and changes every load regardless of w |
| [[Implicit/Edges/builds_on/excel-to-postgres-migration--builds_on--postgres-constraints]] | ****: The migration workflow uses Postgres constraints in Step 4 to catch bad data after cleaning in Step 3. |
| [[Implicit/Edges/exemplifies/degenerate-dimensions-save-storage--exemplifies--degenerate-dimension]] | ****: The degenerate dimensions pattern exemplifies the storage optimization benefit of storing transaction IDs in the fact ta |
| [[Implicit/Edges/builds_on/grain-must-be-locked--builds_on--grain]] | ****: The grain-locking constraint pattern builds on the fundamental importance of grain definition. |
| [[Implicit/Edges/exemplifies/dual-timestamp-prevents-trend-spikes--exemplifies--dual-timestamp]] | ****: The dual timestamp pattern exemplifies handling late-arriving data to preserve trend accuracy. |
| [[Implicit/Edges/exemplifies/multi-key-partitioning-reduces-cost--exemplifies--multi-key-partitioning]] | ****: Multi-key partitioning by (quarter, region_id) exemplifies the 60% compute cost reduction from dual-dimension partition  |
| [[Implicit/Edges/exemplifies/pre-denormalize-at-load-time--exemplifies--denormalized-metrics]] | ****: The denormalized metrics pattern exemplifies pre-computing exchange rates at load time to avoid query-time joins. |
| [[Implicit/Edges/exemplifies/constraint-enforcement-pattern--exemplifies--postgres]] | ****: Postgres constraint enforcement exemplifies how databases enforce data quality at the engine level. |
| [[Implicit/Edges/exemplifies/constraint-catches-three-data-quality-issues--exemplifies--postgres]] | ****: The three caught issues exemplify how Postgres constraints catch data quality problems Excel silently allows. |
| [[Implicit/Edges/builds_on/code-column-reliability--builds_on--dimension-table]] | ****: The code column reliability issue builds on dimension table design by showing why text values are more reliable than num |
| [[Implicit/Edges/authored_by/source-excel-postgres-weekend-yadullah--authored_by--yadamullah-abidi]] | ****: The Excel-to-Postgres migration article was authored by Yadullah Abidi. |
| [[Implicit/Edges/authored_by/star-schema-fact-tables-source--authored_by--rohan-dutt]] | ****: The star schema fact tables deep-dive was authored by Rohan Dutt. |
| [[Implicit/Edges/exemplifies/rely-constraint--exemplifies--rely-optimizer-eliminates-joins]] | ****: RELY constraint is the mechanism that enables query planner join elimination |
| [[Implicit/Edges/builds_on/rely-constraint--builds_on--snowflake]] | ****: RELY constraint is implemented in Snowflake |
| [[Implicit/Edges/builds_on/rely-constraint--builds_on--redshift]] | ****: RELY constraint is implemented in Redshift |
| [[Implicit/Edges/builds_on/rely-constraint--builds_on--bigquery]] | ****: RELY constraint is implemented in BigQuery |
| [[Implicit/Edges/exemplifies/rely-optimizer-eliminates-joins--exemplifies--rely-plus-pbi-0-8s]] | ****: Join elimination via RELY is demonstrated by the 12s to 0.8s benchmark |
| [[Implicit/Edges/builds_on/rely-constraint--builds_on--assume-referential-integrity]] | ****: Power BI's Assume Referential Integrity achieves similar optimization at the semantic layer |
| [[Implicit/Edges/exemplifies/rollup-flags-pattern--exemplifies--rollup-flags-replaces-20-mviews]] | ****: Rollup flags pattern eliminates need for 20 materialized views |
| [[Implicit/Edges/exemplifies/zstd-encoding--exemplifies--zstd-500gb-to-70gb]] | ****: ZSTD encoding is illustrated by the 500GB to 70GB compression claim |
| [[Implicit/Edges/exemplifies/column-clustering--exemplifies--clustering-reduces-io-40]] | ****: Column clustering reduces I/O by approximately 40% |
| [[Implicit/Edges/exemplifies/surrogate-key--exemplifies--surrogate-keys-low-cardinality]] | ****: Surrogate keys are recommended for low-cardinality dimensions |
| [[Implicit/Edges/exemplifies/surrogate-key--exemplifies--scd-type-2-requires-surrogate]] | ****: Surrogate keys are required for Type 2 SCD historical tracking |
| [[Implicit/Edges/builds_on/surrogate-key--builds_on--scd-type-2]] | ****: Surrogate keys enable Type 2 SCD because they persist through attribute changes |
| [[Implicit/Edges/exemplifies/natural-key--exemplifies--natural-keys-high-volume-fact]] | ****: Natural keys are recommended for high-volume fact tables without SCD requirements |
| [[Implicit/Edges/contradicts/surrogate-key--contradicts--natural-key]] | ****: For high-volume fact tables, natural keys are preferred over surrogate keys to avoid join overhead |
| [[Implicit/Edges/exemplifies/primary-key-verification--exemplifies--verify-primary-key-with-count]] | ****: Primary key verification uses COUNT(*) = COUNT(DISTINCT) test |
| [[Implicit/Edges/exemplifies/primary-key-verification--exemplifies--blind-upsert-silently-overwrites]] | ****: Skipping verification leads to silent upsert overwrites |
| [[Implicit/Edges/builds_on/primary-key-verification--builds_on--composite-key]] | ****: If single-column key fails uniqueness test, composite key should be tested |

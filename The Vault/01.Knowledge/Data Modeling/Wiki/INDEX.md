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
| [[medallion-architecture]] | Medallion Architecture (Bronze / Silver / Gold)

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
| [[simple-vs-variant-products]] | Simple vs Variant Products

The two fundamental product types in a retail dimension — each requiring different join and  |
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
## Relationships & Cardinality  (2 notes)

| Note | Description |
|------|-------------|
| [[many-to-many-bridge-table-pattern]] | Many-to-Many Bridge Table Pattern

A data modelling pattern that resolves survey response many-to-many relationships cle |
| [[powerpivot-data-model-load-access-diagram-view-relationships]] | PowerPivot Data Model: Load from Access, Diagram View, Relationships

A step-by-step pattern for loading multiple relate |

## Architecture  (2 notes)

| Note | Description |
|------|-------------|
| [[data-lake-vs-data-warehouse]] | Data Lake vs Data Warehouse

Two foundational storage patterns for analytical workloads — each optimised for different s |
| [[data-warehouse-architectures-inmon-kimball-datavault]] | You just landed a job as a Data Architect, and you’re tasked with building the company’s brand-new data warehouse. |

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
| [[pl-line-structure-reference]] | P&L Line Structure Reference

| [[5-Data-Cleaning-Mistakes-DigitalBYKewat-source.md]] | 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)

Source note: duplicate records, inconsistent date formats, missing values, inconsistent categories, ignoring outliers — with PQ/SQL fixes and a 5-point health checklist.

| [[Author-DigitalBYKewat.md]] | DigitalBYKewat

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

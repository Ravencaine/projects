---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
source_url: "https://www.makeuseof.com/excel-database-15-years-postgres-ended-in-weekend/"
author: "[[Yadullah Abidi]]"
site: https://www.makeuseof.com
published: 2026-07-29
source_type: article
kb_routing: Data Modeling
tags: [excel, postgres, migration, database-design, normalization, constraints, foreign-key, pandas, psycopg2, docker]
---

# Excel was my Database for 15 Years, and Postgres Ended that in a Weekend

Yadullah Abidi · MakeUseOf · makeuseof.com · 2026-07-29

## What this article covers

Personal account of migrating from Excel-as-database to PostgreSQL. Spreadsheets outgrew themselves through organic growth (1 tab → 10 → cross-referencing 3 sheets). Postgres via Docker solved it in one weekend. Key insight: constraints enforce data quality rules automatically — replacing manual vigilance.

## Key themes

- Spreadsheets grow organically; nobody plans the outgrow
- Excel safeguards are all optional; habits break under deadline
- Postgres unique/NOT NULL/foreign key constraints replace manual checks
- Schema design exposes duplicate data before scripting
- Python pandas + psycopg2 for migration
- Constraints catch type errors, not formatting inconsistencies
- Excel still right for sharing + ad-hoc analysis with non-SQL users

## Migration steps

1. Sketch normalized tables (customers, orders, payments)
2. Write Python script with pandas (clean) + psycopg2 (insert)
3. Postgres constraints catch duplicates, missing FKs, wrong types
4. Local LLMs query the same DB — AI-assisted data retrieval

## Tools mentioned

- Docker Compose + named volume for Postgres
- psycopg2 — Postgres adapter for Python
- pandas — data cleaning before insert
- DBweaver — Postgres GUI client

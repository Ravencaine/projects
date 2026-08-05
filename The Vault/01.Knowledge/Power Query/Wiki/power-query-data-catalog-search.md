---


title: "Power Query Data Catalog Search"
created: 2026-07-28
updated: 2026-08-02
tags: [power-query, pattern]
note_type: reference
description: "Power Query Data Catalog Search — curated web search for tables in Wikipedia and Census data. Not a full search engine. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Query: Data Catalog Search

A curated search of public data websites (Wikipedia, Census Bureau, etc.) that returns tables in a structured format.

## Access

```
Power Query → Data Catalog Search
```

## How It Works

1. Enter a search term (e.g., "most populated countries")
2. Results show previews — hover to see data
3. Click **Load** to import directly, or **Edit** to open in Query Editor first

## Search Behavior

The Data Catalog search is **not a full search engine**. It works best with queries that start with words like:

| Works Well | Less Effective |
|-----------|----------------|
| "most populated countries" | "population by country" |
| "S&P 500 performance" | "stock market annual returns 1970" |
| "largest companies by revenue" | "fortune 500 list" |

## Corporate Use

If logged into a corporate network, the Data Catalog can also search **corporate databases**: shared queries within an organization.

## My Data Catalog Queries

Stores and manages personal queries shared with other users.

## Source Reference

Chapter 8, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).

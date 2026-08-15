---
title: "Building a Data Warehouse from Scratch: A Case Study in Kimball Modeling"
source: "https://medium.com/@kbaylas/building-a-data-warehouse-from-scratch-a-case-study-in-kimball-modeling-bcbcaacd5b95"
author:
  - "[[Kaan Baylas]]"
published: 2026-07-02
created: 2026-08-04
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/0!mDLMCWNkZJqvoSNC.webp)

Photo by Growtika on Unsplash

*This article is based on lessons learned from a data warehouse project built from the ground up. Company, industry, and system names have been generalized; the goal is not to promote any specific organization, but to offer a guide distilled from real decisions for data engineers, architects, and analysts about to embark on a similar journey.*

## Introduction

There’s no shortage of articles, books, and courses about building data warehouses. Most start with a clean slate and draw a perfect schema. Real life doesn’t work that way. Your source systems are inconsistent, column names are in another language, some “unique” keys aren’t actually unique, and the business side tells you “we want to be able to analyze everything” without quite knowing yet what questions they’ll ask.

This is the story of a data warehouse built in exactly that kind of environment. We take you through the entire process of transforming transactional data produced by operational teams into a reliable, reportable analytical layer accessible through any BI tool. Along the way, we share the architectural decisions we made, the data quality issues we encountered, and how we solved them.

This is not a “here is the right answer” article. Our goal is to ensure that anyone starting a similar project knows at least which questions to ask — because more often than not, the challenge isn’t finding the right answer, it’s asking the right question at the right time.

## Why You Need a Data Warehouse

The answer to this question is usually less technical and more organizational than people expect.

Operational systems (a ticket management system, a CRM, an order management platform) are designed to do one thing well: “close this ticket,” “serve this customer.” They typically suffer from three problems:

**Performance collision.** Running a heavy analytical query on an operational system risks slowing down the real-time operations that depend on it. A customer service representative’s order-closing screen shouldn’t slow down because someone is trying to pull “the last 3 years of trend analysis.”

**Data model mismatch.** Operational systems are typically normalized, transaction-oriented structures. This is ideal for “insert/update a record” operations but inefficient for aggregation queries like “how many events occurred in the past 6 months, broken down by category.”

**Multiple source problem.** Answering a single business question often requires combining data from multiple systems. An event might live in one system, the related customer information in another, and the assignment/transaction history in a third. Doing this combination manually every time is not sustainable.

A data warehouse solves all three of these problems: it provides a single source of truth that is separate from operational systems, optimized for analysis, and capable of bringing together multiple sources.

## Choosing a Methodology: Which Approach Is Right for You

Once you’ve decided to build a data warehouse, the first big question you face is: **how will you model it?** There are a few well-established answers, and which one you choose depends on the nature of your project.

## The Three Main Approaches

**The Inmon Approach (Enterprise Data Warehouse / EDW)**

Pioneered by Bill Inmon, this approach advocates for first consolidating all of an organization’s data into a normalized (3NF) central data warehouse, then deriving subject-specific data marts from that central warehouse. It’s a top-down approach — the enterprise model is built first, then departmental needs are served from it.

*When it fits:* Strong for large organizations that need to manage many subject areas consistently and simultaneously, and that have a long-term enterprise data strategy. If data consistency and a single enterprise truth are paramount, this approach has clear advantages.

*The risk:* It takes a long time to set up. Months can pass before the first valuable report is produced. For teams that need fast iteration, it can feel slow.

**The Kimball Approach (Dimensional Modeling / Bus Architecture)**

Pioneered by Ralph Kimball, this approach works bottom-up. A dimensional model (fact and dimension tables) is built directly for each subject area. Different subject areas come together over time through shared (conformed) dimensions, forming an enterprise “data warehouse bus.”

*When it fits:* Ideal for teams that want to deliver value quickly and prefer to focus on a specific business process (such as sales, order management, or customer support tickets) first. It produces an intuitive model that business users can understand directly.

*The risk:* When applied without discipline, each subject area can become its own island and enterprise consistency can erode over time. Tools like the bus matrix should be used to plan cross-subject-area consistency.

**The Data Vault Approach**

Developed by Dan Linstedt, this approach divides data into three building blocks: Hubs (business keys), Links (relationships), and Satellites (attributes and history). It offers an extremely flexible and auditable structure that is resilient to changes in source systems.

*When it fits:* Strong in environments where many source systems change frequently, where regulatory/audit requirements are high (such as finance or healthcare), and where preserving long-term data history is critical.

*The risk:* Modeling complexity is high. It is not a layer intended to be served directly to business users — you must build a dimensional view (typically Kimball-style) on top of it, which means an additional layer.

## Questions to Ask Before Deciding

Before deciding which approach is right for you, ask yourself:

- **How large is your team and how quickly do you need to show value?** If you’re a small team inside an organization that expects fast results, Inmon’s long setup time may wear you out.
- **How many source systems do you have and how often do they change?** If you have many frequently-changing source systems, Data Vault’s flexibility may be worth it.
- **Are you focusing on a single subject area first, or modeling the entire organization at once?** If you want to start from a single subject area and grow organically, Kimball’s bottom-up nature suits you well.
- **How heavy are your regulatory/audit requirements?** In highly regulated sectors like finance and healthcare, Data Vault’s auditability advantage can be significant.
- **What does your reporting layer (BI tool) expect?** Most BI tools work naturally with dimensional models. Even if you choose Inmon or Data Vault, you’ll typically need to add a Kimball layer for presentation to the BI layer.

## Our Decision and Why

We chose Kimball dimensional modeling for this project. Here’s why:

**Starting from a single subject area.** Rather than modeling every department simultaneously, we wanted a first model focused on a single operational process that could deliver value quickly. Kimball’s bottom-up nature fit this perfectly — other subject areas can be added to the same architecture later.

**Closeness to the business user.** The ultimate consumers of the model were operational and management teams reading reports through a BI tool. Even if these users don’t know the concepts of “fact” and “dimension,” they intuitively understand concepts like “an event, a location, a priority level.” Kimball’s model naturally delivers that intuitive clarity.

**Team size and speed priority.** With a relatively small data engineering team, we needed to produce usable tables in weeks, not months spent building an enterprise model.

**Low regulatory pressure.** The data we were working with didn’t carry the heavy audit requirements of finance or healthcare, which made Data Vault’s added complexity unnecessary.

## Beyond Kimball: Modern Practices We Layered In

Kimball’s books were written in the late 1990s. Since then, the data engineering world has changed significantly: cloud data warehouses, cheap storage, the preference of ELT (Extract-Load-Transform) over ETL (Extract-Transform-Load), and more. Rather than applying pure Kimball methodology as-is, we blended it with modern practices. This blending had two main components.

## Layering with the Medallion Architecture

In classic Kimball architecture, you typically move directly from a staging area to the dimensional model. Instead, we adopted the **medallion architecture** (bronze → silver → gold) that has become widespread in data engineering, adapting it to our own terminology:

- **Raw layer** (bronze equivalent): stores data coming from source systems exactly as-is, with no transformations
- **Cleansed layer** (silver equivalent): an intermediate layer where column names are standardized, unnecessary columns are removed, and a CDC (Change Data Capture) mechanism is established
- **Dimensional layer** (gold equivalent): where Kimball’s fact/dimension model lives and which the BI tool queries directly

The benefit of this three-layer approach: the raw layer acts as a safety net (if something goes wrong at the source, we can always answer “what actually came in?”), the cleansed layer resolves data quality issues before they reach the dimensional model, and the dimensional layer can focus solely on the question “how should this be modeled” — without simultaneously wrestling with “how dirty is the data.”

## ELT Approach and CDC Discipline

In classic ETL thinking, transformations happen in a separate processing layer before data is loaded into the target system. We preferred ELT — loading data into the target in its raw form first, then performing transformations within the target system (in SQL). The practical reason was that modern relational databases (and big data processing engines) handle transformation work quite efficiently; the benefit of a separate transformation server or cluster didn’t justify the cost.

We also established a consistent **CDC (Change Data Capture) discipline** for every table. We clearly defined which column each table uses to determine “has this changed,” and tracked where each load should pick up from using a control table (a watermark table). This is a practice not elaborated in Kimball’s original text but that has become nearly mandatory in modern data engineering.

## Limiting Surrogate Key Usage

Classic Kimball methodology recommends that every foreign key in fact tables use a surrogate key (an artificial, meaningless key generated by the system) — the reason being that natural keys coming from source systems may change over time, or that historical tracking (Type 2 SCD) may be needed.

We took a more pragmatic path here: **if we didn’t need historical tracking (because the source system already only keeps current state), we only used surrogate keys for low-cardinality dimensions (like status, priority, or category).**For high-volume tables that change frequently (like the main fact table), we preferred to use the natural key directly (such as the source system’s UUID). This let us avoid unnecessary surrogate key generation and lookup overhead.

## The Layered Architecture: Why Three Layers, Not Two

You might wonder: why not go directly from source to dimensional model? In practice, there are strong reasons not to.

**Easier debugging.** When you see a strange number in the dimensional model, you need to figure out whether the problem is in the source system, the transformation logic, or the modeling decision. Without an intermediate cleansed layer, you have to simultaneously compare all three possibilities against the source data. In a three-layer setup, each layer owns its responsibility and isolating the error is much faster.

**Flexibility to reprocess.** Your dimensional modeling decisions (for example, changing a dimension’s grain) may change over time. If you have a cleansed intermediate layer, you can rebuild the dimensional layer from scratch without going back to the source system.

**Separation of concerns.** The raw layer answers “what came in,” the cleansed layer answers “what is correct/reliable,” and the dimensional layer answers “how should this be analyzed.” These three questions require different expertise and change at different rates — mixing them together makes maintenance harder.

## Classic Problems in the Cleansed Layer

This section covers problems you’ll encounter in almost every data warehouse project — but that every time you’ll hope will be different this time. Spoiler: they won’t be. The examples below are generalized but each comes from a real decision.

## The “Unique” Key That Isn’t

Almost every table in source systems has an `id` column, and your instinct is to use it as a primary key. But **always test this assumption** — never accept it at face value.

One example: we discovered that an `id` column in a detail table (one that tracked each sub-record associated with an event) was only taking ten distinct values — despite millions of rows. The column was acting not as a record identifier but like a category or type code. If we had blindly used it as a primary key, our upsert (update-or-insert) logic would have been silently overwriting the wrong rows.

**Our approach:** Before using any column as a primary key candidate, always run this check:

```c
SELECT COUNT(*), COUNT(DISTINCT id)
FROM source_table;
```

If these two numbers differ significantly, that column is not a reliable key. You then have two options: find a combination of columns that truly makes a row unique (composite key), or if no combination works, generate your own surrogate key.

## Same Code, Different Meanings

Another common trap: assuming that a “code” column (like a status code or type code) always means the same thing. In reality, source systems change over time, different modules start using the same code differently, and before you know it, the same code value holds entirely different meanings.

In our case, we found that a status code column had multiple different status text values corresponding to the same numeric code. Using this column directly as a dimension table key would have created silent misclassifications in reports — one of the hardest error types to detect, because the query doesn’t error out, it just returns wrong results.

**Our approach:** We excluded the unreliable code column entirely and instead used the **cleaned text value** as the natural key. A small performance cost (text comparison is slightly slower than numeric), but a significant gain in reliability.

## Duplicate Rows

Fully duplicate rows — same content, same everything — are common in source systems, often caused by integration errors or reprocessing workflows. Detecting them is simple with a `GROUP BY ... HAVING COUNT(*) > 1` query, but deciding what to do about them is the more important decision.

Two main options:

**Silently clean and load** — use `DISTINCT ON` (in PostgreSQL) or a similar window function to keep the most recent row for each natural key and discard the rest. This is the right approach for most insert-only tables.

**Don’t clean it, fix the source** — if duplicates are low volume and communication with the source system team is feasible, fixing the problem at the source is always healthier. But this ties your data warehouse timeline to the source team’s priorities — in practice, you often have to apply the first option and **document** the situation.

Even when we applied the second approach, we kept the cleaning logic transparent: we always documented which column combination determined “most recent” and how many rows were discarded.

## Choosing Your CDC Column: Subtler Than It Looks

The question of “which column do we use to detect changed records” for Change Data Capture seems simple but isn’t. A table often has multiple candidates: a “created date,” an “updated date,” and sometimes a separate “date the ETL ran.”

The difference matters:

- **ETL run date** only shows when data arrived in the system — it has no business meaning.
- **Created date** shows when a record was first created, but won’t catch subsequent updates.
- **Updated date** shows when a record last changed — if records can be updated, this is usually the right CDC column.

Which you choose depends on the source table’s behavior: are records only ever written once (insert-only), or do they change over time (upsert)? Don’t choose a CDC column before answering this question — the wrong choice leads to either unnecessarily rescanning the entire table every time, or worse, silently missing updated records.

**Practical rule:** for upsert tables, use the updated date; for insert-only tables, use the created date. If you’re unsure which behavior applies, ask the source system team — this is one of the most critical architectural decisions in your project.

## Type Mismatches and Silent Failures

Assuming a column “looks like an integer” and casting it directly is one of the sneakiest runtime errors. In our experience, we only discovered that what looked like an integer ID column was actually in UUID text format when millions of rows hit a cast error on the first load attempt.

**Our approach is simple but disciplined:** never cast any column without first verifying its actual type from the source database’s `information_schema` (or equivalent). And when casting, use safe conversion patterns to prevent bad values from stopping the entire load (for example, converting empty strings to NULL before casting).

## Dimensional Modeling Decisions

Once the cleansed layer is ready, the interesting part begins: how do you transform this data into a fact/dimension structure? This section focuses on three types of decisions we faced in our project that are often not covered in sufficient depth in textbooks.

## Junk Dimension: When to Combine, When to Separate

Imagine an event has several related but low-cardinality attributes: its “type,” “category,” “sub-category.” Should you create four separate dimension tables, or combine them into one?

In Kimball literature, this kind of combined table is called a **junk dimension**, and when used correctly, it significantly improves query performance and model simplicity. Our decision criterion was:

**If these attributes are always queried together and none of them will be used independently in another fact table, combine them as a junk dimension.** For example, consider a combination of “event type + category + infrastructure + work qualification” — an analyst will almost always filter on all of them together (“critical-category fiber events”). Making them separate tables would require four joins in every query; combining them into one required only a single join.

**If an attribute will also be used independently as a dimension in other fact tables, keep it separate.** Universal dimensions like date or location should never be buried in a junk dimension — these are conformed dimensions reused across every fact table.

A useful gut-check question: “Is there any reporting scenario where someone would want to filter on one of these attributes without the others?” If the answer is no, you can probably combine them.

## Bridge Tables: Before Many-to-Many Relationships Catch You Off Guard

Standard fact table design assumes each fact row joins to each dimension exactly once (many-to-one relationship). But in real data, this assumption often breaks: one event might affect multiple locations, one order might belong to multiple categories, one patient might receive multiple diagnoses.

The classic solution is a **bridge table** — an intermediate table placed between fact and dimension, with one row for each many-to-many relationship.

We had a real-world example of this in our project: in the source data, the locations affected by an event were stored as a comma-separated list in a single row (something like `"City A, City B, City C"`). Our first instinct was to parse this list and reduce it to a single "primary location" column in the fact table — but this would have made basic analytical questions like "how many locations were affected" impossible to answer.

Instead, we unpacked the list into rows (using PostgreSQL’s `UNNEST` function) and built a bridge table with one row per location. This allowed us to correctly model the many-to-many relationship without breaking the fact table's grain (still "one event = one row").

**An important subtlety:** if the same row has multiple list columns (for example, both a “locations” list and an “access points” list), **never assume** there is an index-based correspondence between the lists. When we tested this assumption, we found an event with three locations but four access points — the lists were not parallel. We had to model the two lists as independent, separate bridge tables. Trying to match by index would have produced silently incorrect results.

## Establishing Priority When Merging Multiple Sources

In many real-world scenarios, the same conceptual entity (an order, an event, a request) is represented in more than one source table — typically one holding “active” records and another holding “completed/archived” ones. When you want to merge these two into a single fact table, you face two problems:

**Problem one: the same record appearing in both tables.** A record may not be immediately removed from the active table when it’s archived — meaning the same natural key can temporarily (or sometimes permanently) appear in both sources. You need to decide which version is “correct.” Our rule was simple: **the archive version always takes priority**, because being archived represents the final, confirmed state of that record.

**Problem two: consistency across loads.** If a record was active in this load but becomes archived in the next, you need to prevent two separate rows from lingering in your fact table — you must clean up the old “active” row and add the new “archive” row. This can’t be solved with a simple upsert; it requires a multi-step process that respects load order:

1. First, upsert from the archive source (always the priority)
2. Delete old active rows for records now in the archive
3. Finally, upsert from the active source for records not in the archive

Without this sequencing discipline, you’ll end up with a silent double-counting error where the same record is counted twice in reports (once as “active,” once as “archived”) — one of the hardest error types to detect.

## A Philosophy for Dealing with Data Quality Problems

In this section, rather than walking through data quality issues one by one, we want to share a **philosophy** for how we approached them — because what outlasted any individual problem we fixed was the consistent principle we adopted when fixing it.

## The “Delete or Assume” Trap

When you encounter a data quality problem, the two easiest paths are: **deleting** the problematic record (ignoring it) or **assuming** missing information (for example, quietly labeling an empty field “unknown” and moving on). Both make life easier in the short term but carry a significant long-term cost: **data loss becomes silent.**

Consider a concrete example. When we were trying to standardize a location field, we encountered a column with inconsistent capitalization and spelling variations that didn’t match our reference list. Our first instinct was to quietly dump every non-matching value into an “Unknown” category. If we’d done that, everything would look “clean” in the report — but we would have lost which specific values were problematic. Six months later, when someone asked “why do we have so many ‘Unknown’ locations,” we wouldn’t have been able to answer.

## Our Approach: Flag and Preserve

Instead, the principle we adopted was: **never silently lose a non-matching or suspicious value. Preserve it in its raw form and mark it with a flag column.**

In practice, this took the following shape: for every column we were trying to match against a reference table, if the match succeeded we stored the standardized value; if it failed, we kept the **original raw value** from the record, and added an `is_matched` boolean column alongside it.

This brought three concrete benefits:

**No data loss.** The report still shows a meaningful value (the actual raw data, not a generic “Unknown” label).

**Data quality becomes observable.** A simple query filtering on `is_matched = false` instantly surfaces which values need to be added to your reference table. This transforms data quality from a one-time cleanup task into a continuously improving process.

**Transparency.** Business users can, if they want, distinguish between records that are “definitively verified” and those that are “raw/unverified.”

## Generalizing This Principle

This approach wasn’t specific to location data — we applied the same principle in other corners of the project:

**Keeping measurement source transparent.** When we had to choose between two possible “end time” columns for a duration calculation — one wasn’t always populated — we added a separate “source” column indicating which one was used for the calculation. This way, “was this duration calculated from the actual end time or a fallback field” is always answerable.

**Explicitly documenting meaningless placeholder values.** When we found a test data remnant in a source column (for example, a cell literally containing “string” instead of a real value), rather than quietly lumping it with other null values, we marked it as an explicitly commented condition in the code — so someone reading that code six months later can immediately understand “why does this special case exist.”

**The general rule:** when making a data quality decision, ask yourself: *“Six months from now, if someone asks why this decision was made, can the code and the data give them the answer?”* If the answer is no, you’re probably hiding the problem, not solving it.

## When Should You Add Indexes

This is a question that comes up in every project but is discussed less than you’d expect: **should you add indexes while designing your model, or after the design is complete?**

## Why Indexing Too Early Is Wrong

At the start of the modeling process, you can’t fully know which queries will run frequently or which joins will truly be critical. Early indexing typically leads to one of two problems:

**Speculative indexes.** Indexes added with the logic “maybe someone will filter on this column” often go unused but continue to impose maintenance costs on every write operation (insert/update).

**Missing indexes.** If you add indexes before all your fact and dimension tables are on the table, you can’t yet see the critical join paths connecting them (for example, a common business key linking two separate fact tables) and you’ll miss them.

## Our Approach: After the Schema Is Complete, All at Once

The right moment for indexing is after all your fact and dimension table designs have been finalized, but before real reports are written on the BI tool. At this point you can clearly see:

- Which columns are used as dimension foreign keys (almost always index these)
- Which columns are critical for date-based filtering (the vast majority of reports filter on date ranges)
- Which columns serve as bridges connecting fact tables (for example, a common business key joining two separate fact tables)
- Which columns in bridge tables are used for joins

Tie every indexing decision to the question “is there a concrete join or filter scenario for this?” If the only justification you can give for an index is “it will probably be useful,” it probably shouldn’t be added.

## Don’t Forget Write Frequency

One final nuance: when deciding how many indexes to add, consider the table’s **write frequency**. Adding around ten indexes to a fact table that is batch-loaded once a day has a negligible cost. But the same number of indexes on a table receiving thousands of rows per second continuously can seriously degrade write performance. Always think about your indexing decisions together with the table’s actual loading pattern.

## Closing: Five Lessons and a Quick Checklist

## Five General Lessons

**1\. Choosing a methodology is not a religious war, it’s a compatibility question.** There’s no “best” among Inmon, Kimball, and Data Vault — there’s only which one fits your team size, speed, number of source systems, and regulatory environment. Don’t be afraid to blend a pure methodology with modern practices (medallion architecture, ELT, measured surrogate key use).

**2\. Never accept any assumption without testing it.** Assumptions like “this column is unique,” “these two lists are parallel,” “this column is always populated” — if any of them enter your model without being verified against real data, they become a time bomb that silently produces wrong results. Verify every important assumption with a SQL query.

**3\. Layered architecture is not a luxury, it’s a debugging strategy.** Separating raw, cleansed, and dimensional layers may look like extra work upfront, but when a problem arises, it lets you answer “where is the error” in minutes — if you had combined all three layers into one step, that could take hours.

**4\. Don’t hide data quality problems — document them.** The delete-or-assume approach provides short-term comfort but erodes trust over time. The flag-and-preserve approach takes a bit more initial effort but transforms data quality into a continuously improving, transparent process.

**5\. Don’t do performance optimization (like indexing) early.** Indexes added before your model is complete come back either as unused overhead or missing coverage. After the schema stabilizes but before reporting begins is the right moment for optimization.

## Quick Checklist

Questions to ask yourself when starting a new data warehouse project:

**Methodology and architecture**

- Which modeling approach (Inmon / Kimball / Data Vault) best fits my team size, speed, and regulatory environment?
- How many layers will my architecture have, and does each layer have a clear, distinct responsibility?
- How will I set up my CDC mechanism (watermark tracking), and how will I determine the right CDC column for each table?

**Data quality**

- Have I verified that every “unique” key candidate is actually unique?
- Have I verified that every code/ID column carries a consistent meaning?
- Have I decided how to detect and handle duplicate records?
- Am I planning to flag and preserve non-matching or suspicious values rather than deleting them?

**Dimensional modeling**

- Which groups of low-cardinality attributes can I combine as a junk dimension?
- Which relationships are actually many-to-many and require a bridge table?
- When merging the same conceptual entity from multiple sources, have I decided which source takes priority and in which order to load them?

**Performance**

- Am I deferring indexing decisions until my schema is fully stabilized?
- Am I tying every indexing decision to a concrete join or filter scenario?
- Am I factoring the table’s write frequency into my indexing decisions?

Building a data warehouse is less about memorizing the right answers and more about asking the right questions at the right time. We hope this article serves as a useful reference point for similar decisions you’ll face on your own journey.
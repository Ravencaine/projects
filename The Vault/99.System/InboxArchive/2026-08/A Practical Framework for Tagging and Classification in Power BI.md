---
title: "A Practical Framework for Tagging and Classification in Power BI"
source: "https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49"
author:
  - "[[Jacob Westendorp]]"
published: 2026-08-02
created: 2026-08-09
description: "How tagging and bridge tables unlock flexible, reliable classification in Power BI"
Processed: "Unprocessed"
---
## How tagging and bridge tables unlock flexible, reliable classification in Power BI

*This article was written with assistance from AI. Read my note on AI writing at the bottom of this article*

Data models are designed to simplify reality — but sometimes that simplification hides the very relationships we need to understand.

Hierarchical dimensions have long been the standard approach to organizing data. They are intuitive, structured, and easy to navigate. But as data becomes more interconnected and business questions become more flexible, these rigid structures start to show their limits.

This article walks through a practical approach to solving that problem using tagging and bridge tables in Power BI — allowing data to be classified across multiple dimensions without sacrificing control or reliability.

**Problem Statement**

Most data models rely on hierarchical dimensions to organize and classify information. These structures assume that each data element fits neatly into a single path — moving from a broad parent category down to increasingly specific subcategories. In well-defined domains, this works efficiently: relationships are clear, filtering is predictable, and users can navigate the data with confidence.

The problem is that real-world data rarely behaves this cleanly. Many entities naturally span multiple categories and forcing them into a single hierarchy introduces tradeoffs. A service might be relevant to both logistics and compliance, but a traditional model requires choosing one primary classification. That decision simplifies the model, but it makes the data less accurate and harder to use — because users approaching the data from a different perspective will miss relevant information.

In practice, this limitation shows up in consistent ways:

· Categories are forced to be mutually exclusive, even when they are not

· Secondary relationships are lost

· Users miss relevant data depending on how they navigate the hierarchy

· Rigid structures become harder to maintain as business needs evolve

A service can belong to only a single category

![Hierarchical models force each service into a single path, making it difficult to represent relationships that span multiple categories.](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8ZFhLsNnLg5Y1qIUTHzVAA.png)

Hierarchical models force each service into a single path, making it difficult to represent relationships that span multiple categories.

By contrast, a service can belong to multiple tags simultaneously.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*dy3tDT61V-_GeGBK_nz-4Q.png)

Tagging allows a single service to be associated with multiple categories at the same time, preserving relationships that cannot be represented in a hierarchical structure.

At its core, the issue is structural: hierarchies are designed for clarity and simplicity, but they cannot represent multi-dimensional relationships without distortion. Once data belongs in more than one category, the hierarchy no longer reflects how the data actually behaves**.**

**Solution Overview**

To address the limitations of hierarchical models, we need a way to classify data that allows for flexibility without sacrificing control. Instead of forcing each data element into a single category, the solution is to introduce a tagging-based approach, where items can be associated with multiple classifications at once.

In this model, categories are no longer embedded in a rigid structure. They are defined as independent tags that can be applied to any relevant data element. A service can be tagged as both *Logistics* and *Compliance*, preserving the full context of how it should be analyzed. This shifts classification from a fixed hierarchy to a many-to-many relationship, where both tags and services can relate to multiple counterparts.

However, this flexibility introduces a new challenge: many-to-many relationships can introduce ambiguous filtering and incorrect aggregations if implemented directly. To solve for this, the model introduces a bridge table that sits between the tagging layer and the fact table. This creates a controlled path for filters to flow, ensuring that selections made on tags propagate cleanly and predictably through the dataset.

At a high level, the approach looks like this:

· Define a governed set of tags (e.g., Logistics, Compliance)

· Map those tags to data elements through an assignment table

· Introduce a bridge table to manage relationships and filter context

· Use that structure to safely filter the fact table

This design preserves the flexibility of tagging while maintaining the clarity and stability of a well-structured data model. It allows users to explore data across multiple dimensions without being constrained by a single hierarchical path or introducing the risks typically associated with unmanaged many-to-many relationships.

**Data Model Design**

The tagging solution works because each table in the model has a clear, specific role. Instead of collapsing everything into a single structure, the design separates concerns — tags, assignments, and filtering — so each piece can be managed and scaled independently.

The model below shows how these components fit together:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*felADoZWizR7U8oBCCDgFg.png)

Filters flow from tags to the fact table through a controlled path, avoiding direct many-to-many relationships.

At a high level, the model introduces three supporting tables alongside the fact table:

· Tag definition table

· Tag assignment table

· Bridge table to control filtering

Each plays a specific role in making the overall design both flexible and reliable.

**1) service\_tags — Tag Definition Layer**

This table defines the controlled vocabulary used for classification.

It typically includes:

· TagKey (unique identifier)

· TagName (business-friendly label)

· TagStatus (e.g., Active/Inactive)

This table serves two purposes:

· It provides a clean, governed list of tags exposed to end users

· It allows tags to be managed independently from the services they apply to

A key design choice here is keeping tags separate from assignments. This ensures that a tag can be renamed or retired in one place, and changes propagate cleanly without reworking service mappings

**2) tagged\_services — Assignment Layer**

This table maps services to tags, creating the many-to-many relationship.

Core fields:

· KeyFieldID (from the fact table)

· TagKey (from service\_tags)

· Optional: Notes (internal context, not user-facing)

This is where flexibility is introduced:

· A single service can appear multiple times (once per tag)

· A single tag can map to many services

This table is typically the most operationally intensive to maintain, because it requires input from business stakeholders to ensure tagging is accurate and meaningful.

**3) dim\_service\_bridge — Filter Control Layer**

This is the most important technical component.

It is a distinct list of KeyFieldID values, usually created directly from the fact table. For example:

Table.Distinct(Table.SelectColumns(Data, {“KeyFieldID”}))

Its role is simple but critical:

· It acts as a controlled intersection point between tagging and the fact table

· It ensures filters propagate cleanly and predictably

Without this bridge, you would need to rely on direct many-to-many relationships, which can introduce ambiguity and incorrect aggregations.

**4) Data — Fact Table**

This is your core dataset, containing:

· transactional or analytical measures

· service identifiers (KeyFieldID)

· other business attributes

Importantly:

· The fact table does not directly connect to tags

· All filtering flows through the bridge table

**How the Relationships Work Together**

The structure creates a deliberate filter path:

1\. User selects a tag in service\_tags

2\. Filter applies to tagged\_services (one-to-many)

3\. Filter flows to dim\_service\_bridge (many-to-one, bi-directional)

4\. Bridge filters the Data table (one-to-many)

This avoids:

· direct many-to-many joins

· ambiguous filter propagation

· the need for complex custom measures

**Why This Design Holds Up**

This model works because it balances two competing needs:

· Flexibility → services can belong to multiple tags

· Control → filtering is still deterministic and explainable

Each layer does one job:

· service\_tags → defines meaning

· tagged\_services → encodes relationships

· bridge → controls behavior

That separation is what allows the model to scale without becoming fragile. At this point, the structure is in place. The remaining challenge is not technical, it’s behavioral. Tagging introduces new patterns in how data aggregates and how users interpret totals.

**How Filtering Works**

The strength of this model is not just that it supports tagging, it keeps filtering predictable and controlled. That comes down to how relationships are structured and how filter context flows through the model.

**The Filter Path (Step-by-Step)**

Filtering does not happen directly between tags and the fact table. Instead, it flows through a defined sequence:

1\. User selects a tag in service\_tags

2\. That selection filters tagged\_services (one-to-many relationship)

3\. The filtered rows propagate to dim\_service\_bridge (many-to-one, bi-directional)

4\. The bridge table filters the fact table (Data) (one-to-many)

**Why This Matters**

This extra step — the bridge table — is what makes the model stable.

If you tried to connect tags directly to the fact table:

· You’d create a many-to-many relationship

· Filters could propagate in ambiguous or unintended ways

· Aggregations could become unreliable or incorrect

Instead, the bridge table acts as a control point:

· It reduces the problem to a series of standard one-to-many relationships

· It ensures that only valid KeyFieldID values flow into the fact table

· It keeps filter behavior deterministic

Conceptually, when a user selects a tag, the model identifies all services associated with that tag and filters the fact table to only those services. The bridge table simply ensures that this happens cleanly.

**Why Bi-Directional Filtering Is Used**

You’ll notice the relationship between tagged\_services and the bridge table is bi-directional.

This is intentional:

· It allows filters from tags to propagate forward to the fact table

· It also ensures consistency if additional dimensions interact with the bridge

Without this, the filter path would be incomplete.

That said, this is a controlled use of bi-directional filtering — not a blanket approach across the model. The bridge isolates where this complexity lives.

**Mental Model (Simple Way to Think About It)**

If the relationships feel abstract, simplify it to this:

· service\_tags → defines what you select

· tagged\_services → defines what matches that selection

· bridge → defines what is allowed to filter the fact

· Data → contains what you ultimately measure

Each step narrows the dataset in a controlled way.

**What to Emphasize to Users**

From an end-user perspective, all this complexity is hidden. But it does impact how results behave:

· Tag selections will return all relevant services, even if they belong to multiple categories

· Filters will behave consistently across visuals

· Results are reliable — even with overlapping classifications

What users don’t see is that this consistency depends entirely on not shortcutting the model design. At this point, the filtering mechanics are in place. The final piece to cover is how this affects interpretation, specifically how overlapping tags impact totals and why results may not behave the way users initially expect.

**User Caveats and Interpretation**

The model is designed to behave predictably from a filtering perspective — but interpretation becomes more nuanced once tagging is introduced. This is where users can get tripped up if expectations are still anchored to hierarchical thinking.

The key shift is that tags are not mutually exclusive, and results are not meant to roll up cleanly across them. In a hierarchical model, users expect totals to behave additively — subcategories sum neatly into a parent. That mental model does not apply here.

**What Changes with Tagging**

When a service can belong to multiple tags, the same underlying data can appear in multiple selections.

Using the earlier example:

· A service tagged as both Logistics and Compliance will be included in both views

· Each tag returns a complete slice of all relevant services

· Those slices can and often do overlap

This leads to a subtle but important behavior:

· Individual tag values are correct

· But they are not independent of each other

**Where Confusion Shows Up**

The most common point of confusion is at the total level.

For example:

· Logistics = 71 units

· Compliance = 10 units

A user might expect:

· Combined total = 71 units

But in reality:

· Some of the same services may contribute to both categories

· The totals are not additive

This can make results look incorrect, even though the model is behaving as designed.

**How to Frame This for Users**

This isn’t a flaw — it’s a reflection of the data. A clearer way to position it:

***Each tag represents a lens on the data, not a partition of it.***

Or more practically:

· Tags answer: *“What data relates to this topic?”*

· Not: *“What share of the data belongs exclusively to this topic?”*

**What Users Should Understand**

To use the model correctly, users need to internalize a few points:

· Tag-based views are overlapping, not additive

· Totals across tags should not be summed

· A single record may appear in multiple tag selections

· Results are best interpreted within the context of a selected tag, not across tags

Tagging increases flexibility, but it also requires users to rethink how they interpt data. Once that shift is made, the model becomes significantly more powerful, it allows users to explore relationships that a traditional hierarchy would hide.

**Governance and Maintenance**

The technical design enables tagging, but governance is what determines whether it remains useful over time or degrades into confusion. Unlike hierarchical models, where structure enforces discipline, a tagging model introduces flexibility that must be actively managed. Without clear ownership and standards, tags can quickly become inconsistent, overlapping in unintended ways, or misapplied. Over time, this erodes trust in the model and reduces its analytical value.

**Why Governance Matters**

Tagging shifts complexity from structure to process. Instead of relying on rigid hierarchies, consistency now depends on definitions, discipline, and governance.

· consistent definitions

· disciplined application of tags

· ongoing alignment with business use

That’s what keeps the model coherent. Left unmanaged, common failure modes include:

· Duplicate or synonymous tags (e.g., “Biofuel” vs “Logistics”)

· Tags drifting in meaning over time

· Incomplete or inconsistent tagging across services

· Over-tagging, where everything is tagged with everything

**Core Governance Principles**

To keep the model effective, a few principles should be established early:

**1) Defined Ownership**

· Assign responsibility for the tag set and tagging decisions

· This is typically a data steward or domain owner

· Avoid ad hoc updates from multiple independent contributors

**2) Controlled Vocabulary**

· Treat service\_tags as a governed asset

· Changes to tag names, definitions, or status should be intentional and reviewed

· Avoid creating new tags unless they clearly add analytical value

**3) Clear Definitions**

· Each tag should have a documented meaning

· Ambiguity leads to inconsistent tagging and unreliable results

**4) Lifecycle Management**

· Use fields like TagStatus to manage active vs inactive tags

· Don’t delete old tags — retire them cleanly

· Ensure reporting behavior for inactive tags is understood

**Managing the Assignment Layer**

The tagged\_services table is where governance becomes operational.

This is the layer most prone to drift because it requires:

· business input

· interpretation

· ongoing updates as services evolve

To manage it effectively:

· Establish guidelines for tagging decisions

· Periodically review assignments for consistency

· Keep the structure simple — avoid unnecessary attributes unless they serve a clear purpose

**Maintenance Approach**

In practice, this model works best when maintained outside of Power BI, using a more flexible and collaborative tool. For early stage, initial sandboxing an Excel workbook is sufficient. As tagging matures and governance is jointly managed a shared list or collaborative tool makes collaboration easier. This allows for easier updates, version control, and shared ownership across stakeholders. From there, Power BI simply consumes the curated tables.

**Scaling Considerations**

As the model grows:

· The number of tags increases

· The number of assignments increases

· The likelihood of overlap increases

At that point, governance becomes even more important — not less. A well-maintained tagging model scales cleanly. A poorly governed one becomes:

· harder to understand

· harder to trust

· harder to fix later

**Closing Thought**

Tagging solves a real limitation in traditional modeling, but it replaces structural simplicity with organizational discipline. The design gives you flexibility, but governance is what makes that flexibility usable. When done well, this approach creates a model that is both adaptable and reliable, something hierarchical models alone cannot achieve on their own.

1 I think one thing that gets lost in the “AI wrote this” conversation is how AI tools can function as training wheels. When I look back at what I wrote in early 2026, it’s cringy and obviously AI‑shaped. But it got me writing, it gave me a voice to start from, even when I wasn’t sure of myself. I could plunk out a rough draft and use AI to edit, transform, and craft my writing. It was great in that the tools used language, structure, and form that made my idea seem more impressive and artificially smooth.

Except it did not, not really, it puffed up and hyperbolized simple ideas and used more and more words to describe complex ideas until they lost meaning. Even with careful line by line editing, the writing was still not my own. I see that now and am working to develop as a better writer on my own. While I still use AI, I am consciously using less and less as I find a more authentic tone in my own work.
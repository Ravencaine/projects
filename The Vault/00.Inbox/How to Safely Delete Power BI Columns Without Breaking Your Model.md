---
title: "How to Safely Delete Power BI Columns Without Breaking Your Model"
source: "https://medium.com/gitconnected/how-to-safely-delete-power-bi-columns-without-breaking-your-model-56f00cbeac53"
author:
  - "[[Thebitoolbox]]"
published: 2026-08-07
created: 2026-08-11
description: "The column looks useless. Your cursor is already over Delete. Then doubt appears."
Processed: "Unprocessed"
---
## The column looks useless. Your cursor is already over Delete. Then doubt appears.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6dKNsy44UhIuaRqsgPltjA.png)

Generated with ChatGPT

Every Power BI developer eventually inherits a model containing columns like these:

- LegacyCode
- CustomerFax
- MigrationID
- OldCategory
- InternalFlag
- ArchiveReference
- TemporaryStatus

They are not used in any obvious chart.

Nobody on the team remembers why they were added.

Some values look as though they came from a system retired years ago.

You right-click one of the columns.

Your cursor moves toward **Delete**.

Then it stops.

> *What if a measure still depends on it?  
> What if it is used in a relationship?  
> What if removing it breaks row-level security?*

That hesitation is reasonable.

Deleting the wrong column can break calculations, relationships, sorting, security rules, and reports. But keeping every suspicious column “just in case” also has a cost.

The real question is not:

> ***“Does this column look old?”***

It is:

> ***“Can I prove that this column is no longer needed?”***

This article explains how to make that decision safely.

You will learn:

- why “not visible in a report” does not mean unused,
- where column dependencies can hide,
- why unused columns still consume model memory,
- why some columns cost far more than others,
- how to inspect semantic-model dependencies,
- how to measure the actual cost of a column,
- and how to remove candidates without turning cleanup into production damage.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6ctkFhPX_L_eLp62VrdKcQ.png)

The hardest part is rarely deleting the column. It is proving that the deletion is safe

## “Not used in a visual” does not mean unused

Suppose `LegacyCode` does not appear on any visible report page.

That tells us only one thing:

> The column is not obviously being displayed in the visuals we checked.

It does not prove that the column is unused.

A column can influence the model without ever being placed directly on a chart.

It might be referenced by:

- a measure,
- a calculated column,
- a calculated table,
- a relationship,
- a hierarchy,
- a **Sort by column** setting,
- a row-level security rule,
- a perspective,
- a report-level filter,
- a hidden visual,
- or another object that depends on it indirectly.

Power BI’s Model Explorer exposes many semantic-model object types in one place, including tables, measures, relationships, roles, calculation groups, perspectives, and translations. Microsoft also notes that many objects that are not used directly in visuals still affect how the model and reports behave.

That means a column can look irrelevant in Report view while still performing an important job elsewhere.

## A practical example

Start with a simple measure:

```c
Sales Amount :=
SUM ( Sales[SalesAmount] )
```

Now create another measure:

```c
Legacy Customer Sales :=
CALCULATE (
    [Sales Amount],
    LEFT ( Sales[LegacyCode], 4 ) = "LG-1"
)
```

The `LegacyCode` column does not need to appear in a visual.

It is still required by the measure.

The dependency is:

```c
Sales[LegacyCode]
        ↓
Legacy Customer Sales
```

Deleting the column breaks the calculation.

The same problem can occur with security.

For example, a role could contain this filter:

```c
Sales[InternalFlag] = "Y"
```

`InternalFlag` might be hidden and absent from every report page.

It is still part of the security design.

A technical key presents another common example. A user may never see `ProductKey`, but it can be essential to the relationship between `DimProduct` and `FactSales`.

```c
DimProduct[ProductKey]
          1
          │
          *
FactSales[ProductKey]
```

Removing the key does not merely clean up the model.

It removes the relationship.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7DJHbv2iS0JT-gRgbd5bDw.png)

A column can be invisible to report users and still be essential to the semantic model

## Why unused columns still have a cost

Power BI Import models do not query the source for every visual interaction.

The imported data is loaded into the VertiPaq storage engine.

VertiPaq creates internal storage structures separately for each column. Numeric columns can use value encoding, while text and other nonnumeric columns commonly require hash encoding, where unique values are assigned identifiers and stored in a dictionary.

That has an important consequence:

> *A loaded column does not become free because nobody uses it in a chart.*

If the column is included in the imported table, it is still processed and stored as part of the model.

This does not mean every extra column destroys performance.

A small flag in a table containing a few thousand rows may be practically irrelevant.

But a wide fact table containing tens of millions of rows can accumulate significant waste when it includes dozens of unnecessary columns.

Microsoft explicitly recommends reducing the number of imported columns and reviewing high-cardinality columns as part of semantic-model optimization.

Unused columns can contribute to:

- larger in-memory models,
- higher refresh resource requirements,
- longer processing,
- increased capacity memory pressure,
- more metadata for developers to understand,
- and a more confusing field list.

The effect depends on the column.

And this is where an important nuance appears.

## Not all columns cost the same

Compare two columns, each containing one million rows.

## Column A: a simple flag

```c
InternalFlag
Y
N
Y
N
Y
N
...
```

Cardinality:

> ***2 unique values***

## Column B: a nearly unique identifier

```c
ArchiveReference
```
```c
AR-100001
AR-100002
AR-100003
AR-100004
...
```

Cardinality:

> ***Almost one unique value per row***

Both columns have one million rows.

Their memory cost can be very different.

The flag repeats only two values and can compress efficiently.

The archive identifier requires a much larger set of unique values. Text values use dictionary-style encoding, and Microsoft notes that converting suitable text identifiers to numeric values can produce significant reductions, especially for unique or high-cardinality columns in large tables.

Therefore, this rule is too simplistic:

> ***“Remove every unused column because every column is equally expensive.”***

A better rule is:

> ***Find unused columns, then prioritize them by actual cost.***

An unused two-value flag might be safe to remove but have almost no measurable impact.

An unused, nearly unique text identifier in a 100-million-row fact table may deserve immediate attention.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*S5-W3dKNVLEVoS5L8SXg7Q.png)

Row count is only part of the story. Cardinality and data type strongly influence storage cost

## Hiding a column is not the same as removing it

Power BI allows authors to hide columns from the report field list.

This is useful for:

- technical relationship keys,
- helper columns,
- fields that should be accessed only through explicit measures,
- or columns that would confuse report authors.

But hiding is a usability decision.

It does not remove the underlying data.

Microsoft describes hiding as a way to control which objects report authors are expected to use. The hidden object remains part of the semantic model.

Therefore:

> ***HIDDEN ≠ REMOVED***

A hidden, high-cardinality column can still consume memory.

To reduce an Import model, the column must stop being loaded.

That can happen:

- in the source query,
- in a database view,
- in a dataflow,
- or in Power Query using **Choose columns** or **Remove columns**.

Power Query’s remove-column operation changes the table passed to subsequent transformation steps and ultimately to the model.

## Prefer selecting what you need

For stable source schemas, this Power Query approach is often safer:

```c
Table.SelectColumns (
    Source,
    {
        "SalesID",
        "OrderDate",
        "ProductID",
        "CustomerID",
        "Quantity",
        "SalesAmount"
    }
)
```

Instead of loading every source column and deleting selected unwanted fields, `Table.SelectColumns` creates an explicit contract describing what the model needs.

Another option is:

```c
Table.RemoveColumns (
    Source,
    {
        "CustomerFax",
        "ArchiveReference",
        "MigrationID"
    }
)
```

Both can work.

Selecting required columns is often easier to review because the approved schema is visible in one place.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vXIMOV15T1unVNWd1jF7BA.png)

Hiding cleans the interface. Removing reduces the model

## How can you check whether a column is used?

Power BI contains much of the required information, but it does not always present it as one simple answer.

There is no universal native button that says:

> Where is this column used?

Instead, the information can be distributed across different parts of the model.

## Model Explorer

Model Explorer can help you navigate:

- tables,
- measures,
- relationships,
- roles,
- calculation groups,
- perspectives,
- translations,
- and other semantic-model objects.

It is useful for browsing the model.

However, browsing objects is not the same as automatically producing a full dependency tree for one selected column.

## Power Query dependencies

Power Query can visualize dependencies between queries.

This helps answer questions such as:

> Which query references this staging query?

It does not answer every semantic-model question, such as:

> Which DAX measure references this column?

or:

> Is this column used by an RLS role?

Power Query dependencies describe query-to-query processing relationships, not the complete dependency graph of the semantic model.

## DAX metadata functions

Current versions of DAX provide metadata functions that can expose object dependencies directly.

One useful example is:

```c
EVALUATE
    INFO.DEPENDENCIES()
```

`INFO.DEPENDENCIES()` returns metadata describing dependencies and relationships between semantic-model objects. Its output can include the object, its type, its expression, and the referenced table and object.

A simplified result might look like this:

```c
OBJECT                  REFERENCED_TABLE    REFERENCED_OBJECT
----------------------------------------------------------------
Legacy Customer Sales   Sales               LegacyCode
Old Category A Sales    Sales               OldCategory
```

You can filter the results:

```c
EVALUATE
FILTER (
    INFO.DEPENDENCIES(),
    [REFERENCED_TABLE] = "Sales"
        && [REFERENCED_OBJECT] = "LegacyCode"
)
```

This gives you a direct view of semantic-model objects that reference the selected column.

`INFO.DEPENDENCIES()` is particularly useful for:

- auditing,
- technical documentation,
- dependency exports,
- impact analysis,
- and building automated model-review processes.

Microsoft notes that metadata access and available results can depend on the host and permissions.

## An important limitation

A semantic-model dependency query should not automatically be treated as proof that the column is unused everywhere.

That is an inference from its documented scope: `INFO.DEPENDENCIES()` describes semantic-model dependencies. External reports, exports, downstream processes, custom applications, or other artifacts may require separate validation.

Therefore:

```c
No detected model dependency
```

means:

> ***Candidate for review***

It does not always mean:

> ***Delete immediately***

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KEKN4T1S4IWZVh_anCVQtQ.png)

Dependency metadata turns “I think it is unused” into a question that can be investigated systematically

## Measure the column before prioritizing it

Knowing that a column is unused is only half of the decision.

You also need to know whether removing it is likely to matter.

DAX Studio’s **View Metrics** feature can analyze model memory and display statistics for tables, columns, relationships, and partitions. Its Column Metrics view presents columns in a flat list, while the Table Metrics view can expand each table to show its columns.

Typical metrics include:

- cardinality,
- data size,
- dictionary size,
- hierarchy size,
- total size,
- data type,
- encoding information.

In DAX Studio:

```c
Advanced
    ↓
View Metrics
    ↓
Columns
    ↓
Sort by Total Size
```

This allows you to distinguish between:

```c
CustomerFax
Unused
Total size: 0.2 MB
```

and:

```c
ArchiveReference
Unused
Total size: 180 MB
```

Both might be safe candidates.

Only one is likely to produce a meaningful model-size reduction.

## Memory size versus file size

DAX Studio’s model metrics describe memory used when the model is loaded. The saved file can have a different size because additional compression can be applied on disk.

Do not expect:

```c
Removing a 100 MB in-memory column
```

to reduce the PBIX file by exactly 100 MB.

The more reliable comparison is:

1. capture model metrics before removal,
2. remove the column,
3. refresh the model,
4. capture the same metrics again.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kELFdDriJsLSgNwQGUlV6A.png)

Unused tells you whether a column might be removable. Model metrics tell you whether it is worth prioritizing

## Which columns should you remove first?

Use two dimensions:

1. **Usage**
- used,
- unused.
1. **Memory cost**
- low,
- high.

That produces four categories.

## Used and expensive

Example:

```c
LegacyCode
12.4 MB
Used by three measures
```

Decision:

```c
REVIEW — DO NOT DELETE
```

This is an optimization candidate, not a deletion candidate.

Possible actions include:

- changing the data type,
- reducing cardinality,
- replacing text with a numeric key,
- moving logic upstream,
- or redesigning the dependent calculations.

## Unused and expensive

Example:

```c
ArchiveReference
18.7 MB
No detected dependencies
```

Decision:

```c
FIRST REMOVAL CANDIDATE
```

This is where cleanup can deliver the greatest return.

## Used and small

Example:

```c
InternalFlag
0.1 MB
Used in RLS
```

Decision:

```c
KEEP
```

The storage cost is low, and the column serves an important purpose.

## Unused and small

Example:

```c
CustomerFax
0.2 MB
No detected dependencies
```

Decision:

```c
LOW-PRIORITY CANDIDATE
```

It can still be removed to simplify the model.

But it should not distract you from much larger opportunities.

The practical prioritization rule is:

```c
USED OR UNUSED?
        ↓
CHEAP OR EXPENSIVE?
        ↓
PRIORITIZE THE IMPACT
```

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-QIJ_hqjHEx0k4Hv-qV8bg.png)

The best first candidate is not simply unused. It is unused, expensive, and verified as safe to remove

## A safe five-step cleanup process

Removing columns should be a controlled model change, not an improvised act of bravery.

## Step 1: Identify a candidate

Start with suspicious columns such as:

- legacy technical fields,
- duplicated descriptions,
- free-text notes,
- timestamps with unnecessary precision,
- GUIDs,
- source-system audit columns,
- migration identifiers,
- fields with no detected usage.

Do not delete anything yet.

Create a review list.

## Step 2: Check dependencies

Investigate:

- measures,
- calculated columns,
- calculated tables,
- relationships,
- hierarchies,
- Sort by column settings,
- RLS roles,
- perspectives,
- report visuals,
- page and report filters,
- downstream reports and processes.

A dependency can be direct:

```c
LegacyCode
    ↓
Legacy Customer Sales
```

or indirect:

```c
LegacyCode
    ↓
Legacy Customer Sales
    ↓
Executive KPI
```

Both matter.

## Step 3: Measure the cost

Use model metrics to check:

- cardinality,
- dictionary size,
- data size,
- total size,
- and table row count.

Prioritize columns where:

```c
No usage
+
High memory cost
=
High-value candidate
```

## Step 4: Remove it in a test copy

Do not begin in the only production version of the file.

Use:

- source control for PBIP projects,
- a copied PBIX,
- a development branch,
- or a separate test workspace.

Remove the column in the source or Power Query.

Then perform a full refresh.

## Step 5: Validate the result

Check:

- refresh completion,
- DAX measures,
- calculated objects,
- relationships,
- report pages,
- hidden pages,
- bookmarks,
- drillthrough,
- tooltips,
- RLS roles,
- exported reports,
- downstream connected reports,
- and any automation depending on the model.

Only after validation should the cleanup move into production.

## What most developers get wrong

## “The column is not in a visual, so it is unused.”

False.

A measure, relationship, sorting rule, security role, or another semantic-model object may still reference it.

## “Hidden columns do not consume memory.”

False.

Hiding changes field-list visibility. It does not remove the column’s data from the model.

## “Every unused column is a major performance problem.”

False.

Some columns are tiny and compress extremely well.

Measure the cost before claiming that removal will transform the report.

## “All text columns are bad.”

False.

Text columns are often necessary for filtering and reporting.

The concern is unnecessary text — particularly high-cardinality text in large tables. Microsoft’s optimization guidance focuses on reducing imported columns and reviewing high-cardinality data, not eliminating all descriptive fields.

## “No DAX dependency means safe to delete.”

Not necessarily.

The column may be involved in a relationship, sorting, RLS, a report visual, or a downstream artifact.

DAX expressions are only one layer of dependency.

## “A deletion candidate should be deleted automatically.”

No.

Automated auditing should reduce search effort.

It should not replace validation.

## “I can remove it now and fix anything that breaks later.”

That can work in a small personal report.

It is a dangerous cleanup strategy for a shared enterprise semantic model.

## Enterprise unused-column checklist

## Candidate identification

- Is the column visible in any active report?
- Is it used in page, visual, or report filters?
- Is it used in a tooltip or drillthrough page?
- Is it included in a bookmark-dependent visual?
- Is it used by Analyze in Excel or another downstream report?
- Does the business still require the underlying attribute?

## Semantic-model dependencies

- Is it referenced by a measure?
- Is it referenced by a calculated column?
- Is it referenced by a calculated table?
- Does it participate in a relationship?
- Is it used by a hierarchy?
- Is it used as a Sort by column?
- Is it referenced by an RLS role?
- Is it included in a perspective?
- Are there indirect dependencies?

## Storage impact

- What is the column’s data type?
- How many rows does it contain?
- What is its cardinality?
- What is its dictionary size?
- What is its total in-memory size?
- Is it located in a large fact table?
- Could the data type be optimized instead of removing it?

## Removal safety

- Is the model under source control?
- Is there a test copy?
- Can the model complete a full refresh after removal?
- Have all measures been validated?
- Have relationships been reviewed?
- Has RLS been tested with **View as**?
- Have downstream reports been checked?
- Is there a rollback path?

## Final decision

- Is the column unused?
- Is it expensive enough to prioritize?
- Has the absence of dependencies been verified?
- Has the change passed testing?

Only when all four answers are clear should the column move from:

```c
CANDIDATE
```

to:

```c
APPROVED FOR REMOVAL
```

## FAQ

## Should I remove every unused Power BI column?

Removing genuinely unnecessary columns is good model hygiene.

However, prioritize by impact. Start with wide fact tables and expensive high-cardinality columns rather than spending hours removing tiny fields that save almost no memory.

## Does removing columns always make visuals faster?

Not necessarily.

The most immediate effect is usually model-size and refresh-resource reduction.

Query improvement depends on whether the column or its structures were relevant to the queries and memory pressure involved.

## Are unused columns more important in fact tables?

Often, yes.

Fact tables typically contain far more rows than dimensions, so an unnecessary column repeated across tens of millions of rows can be far more costly than a similar column in a small dimension.

The actual answer still depends on compression, cardinality, and data type.

## Should I delete technical key columns?

Not when they are required by relationships.

Technical keys are often hidden from report authors but remain essential to model integrity.

## Is hiding a column enough?

Hiding is enough when the goal is improving usability.

It is not enough when the goal is reducing imported data or model memory.

## Can INFO.DEPENDENCIES prove that a column is safe?

It can provide valuable semantic-model dependency metadata.

Treat the output as evidence, not as the entire validation process. Report objects and external dependencies might require separate checks.

## Can DAX Studio find unused columns automatically?

DAX Studio can expose model metrics and metadata that help with the analysis. Its View Metrics feature is particularly useful for understanding memory usage by table and column.

Determining “unused” still requires combining usage and dependency information.

## Should I remove the column in Power Query or directly from the source?

Removing it at the source is often preferable when you control the source and the field is unnecessary for every consumer.

Power Query is appropriate when the source is shared or cannot be changed.

In both cases, the goal is to prevent the unnecessary column from being loaded into the semantic model.

## The final rule

Do not keep every column because deleting it feels risky.

Do not delete a column because its name looks old.

Instead:

```c
FIND
  ↓
VERIFY
  ↓
MEASURE
  ↓
REMOVE
  ↓
VALIDATE
```

A clean model is not one with the smallest possible number of columns.

It is one where every loaded column has a clear purpose — or a justified reason to remain.

## Watch the visual explanation

I created a video showing the exact moment every Power BI developer recognizes:

> *“Can I delete this column?”*

The video demonstrates:

- a column that looks unused but is referenced by DAX,
- the difference between low and high cardinality,
- the memory cost of loaded columns,
- and a safe process for removing candidates.

## Audit unused-column candidates with ModelLens

Finding one suspicious column is easy.

Reviewing hundreds of columns across:

- DAX expressions,
- relationships,
- and indirect dependency chains

is much more time-consuming.

ModelLens helps turn semantic-model metadata into a focused audit.

Instead of manually searching every object, you can identify unused-column candidates and inspect why another apparently unnecessary column must remain.

An audit does not make the final deletion decision.

It gives you the evidence needed to make that decision faster.

**ModelLens:**  
[ModelLens: Automated Power BI Semantic Model Auditor & Documentation](https://thebitoolbox.gumroad.com/l/modellens)

![](https://miro.medium.com/v2/resize:fit:1182/format:webp/1*UZHGU5Qex1EQRufeT9Ftdw.png)

Automation should identify candidates and explain dependencies — not blindly delete model objects
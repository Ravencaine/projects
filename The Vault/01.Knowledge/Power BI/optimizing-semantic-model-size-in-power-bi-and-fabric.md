---
title: "Optimizing semantic model size in Power BI and Fabric"
source: "https://share.google/VmcQURd6Y8GqJiNrH"
author: "share.google"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Reduce semantic model size in Power BI and Fabric with six practical optimization patterns.

Optimizing semantic model size in Power BI and Fabric: a comprehensive guide Optimizing semantic model size in Power BI and Fabric: a comprehensive guide Published: March 3, 2026 | Updated: July 1, 2026 Just Blindbæk Field CTO Just Blindbæk is Field CTO at Tabular Editor. During his two decades of working with BI, Just has educated and inspired Power BI professionals across Europe, earning both an MVP and a SSAS Maestro status – work he continues in his role as Field CTO, where he helps our European users to create even more value from Tabular Editor. Fabric Power BI Semantic Model Optimization Key takeaways Smaller models perform better and cost less: Reducing model size improves performance, cuts cost, and keeps you under tenant limits, whether you use Import or Direct Lake . This article presents six patterns to do it. Simple optimizations remove what you don't need: Drop unnecessary columns and rows first, then reduce precision, split high- cardinality columns like DateTime , choose appropriate data types, and disable unneeded attribute hierarchies via  . Advanced optimizations tailor the design: User-defined aggregations shift detailed data to DirectQuery while keeping aggregates in Import, trading memory for query time. You can also split a large model into smaller subject-oriented ones. Compression techniques are situational: Optimizing for run-length encoding can further reduce the footprint once structural optimizations are already in place. Understanding model size optimization This article is the second in a series on optimizing semantic model memory in Microsoft Fabric. In the first article , we explained that: Memory refers to the size that your semantic model takes on disk in Power BI and Microsoft Fabric. There’s hard memory limits for Power BI semantic models; if you exceed these limits, then you experience query and refresh errors. Fabric enforces memory per semantic model, and full refresh requires headroom. You can measure where memory is consumed by using the VertiPaq Analyzer by SQLBI in Tabular Editor 3 or DAX Studio , or in Fabric notebooks (where it’s called the “Memory Analyzer”). This article shifts from understanding to action : practical modeling decisions that measurably reduce semantic model size. The goal isn't to blindly apply tricks, but to understand what you can do, why each pattern works, and how to validate its impact. The following six patterns are concrete design choices that reduce memory usage, each building on the principles from Part 1: Pattern one: reduce unnecessary data Reducing unnecessary data is the simplest and most effective way to lower model size: reduce the width (columns) and height (rows) of your tables to only what reporting and analysis require. Apply this to every model, new or existing. It sounds obvious, but in practice it takes discipline. It’s common to include columns in a semantic model “just in case” someone needs it. It’s also common to import years of detailed history because it’s available in the source. A question you should ask is: does this data serve a concrete reporting requirement today? If not, it is probably better left out. You can always add it later, if and when it’s needed. Include only the data analysis requires. Is ten years of detailed transactions necessary for YTD and year-over-year analysis? Often current and previous year suffice at detailed grain, while older data can be aggregated. Removing rows through filters or incremental refresh can significantly reduce model size without affecting business value. Columns are often the bigger problem. Audit fields, GUIDs, technical identifiers, and rarely used attributes frequently consume disproportionate memory, especially when they have high cardinality. Once such columns are used in measures or report visuals, removing them becomes difficult. It is therefore safer to identify and exclude them early during model design and development, rather than to remove them later, when they might be already used in some obscure visual or reporting process. NOTE Even if someone is asking for obscure columns or data ranges, it doesn’t mean that you should include it. You should always engage with users to understand the why behind their request, particularly if it’s coming from a small number of vocal individuals. You might be able to help them find alternative solutions that are more effective, efficient, or reasonable. Also, don’t be afraid to stand your ground and say “no” if the request isn't reasonable and will result in a net negative for the rest of the user base. Just make sure to explain clearly, simply, and empathetically if that is the case. Why this works This pattern is the simplest to do and understand; if you exclude or remove a column or table, then it’s not contributing to the model size. To reiterate, the difficulty here isn’t in the implementation. It comes in deciding what to remove , the implications for your model and report designs, and how you’ll fulfill inevitable user requests when they do need that information. WARNING More and more developers are turning to AI tools to help them optimize semantic models. This can be very helpful and efficient; however, it can also lead to disaster. An AI agent can’t decide for you which columns to remove. This decision must be made with the broader context of your users, the business process, and the reporting requirements. How to reduce unnecessary data To implement this pattern, define the narrowest range of data you need (via filters and table/column selection), for any category, not just date ranges. Once you exclude columns, remember to aggregate your data too. Focus on which columns take up the most size, and identify whether you can remove them outright. Consider the highlighted columns from the previous article's example: These two columns account for 84% of the model size. It’s likely that we need the Pickup Datetime field (but can optimize it, further), but Payment Identifier is a key field we might r

## Code / Examples

```
IsAvailableInMDX
```
```
SE-GBG-E-2019-0045821
```
```
OrderID
```
```
IsAvailableInMDX
```
```
IsAvailableInMDX
```
```
Hier Size
```
```
IsAvailableInMDX
```
```
false
```


---
*Source: [share.google](https://share.google/VmcQURd6Y8GqJiNrH)*

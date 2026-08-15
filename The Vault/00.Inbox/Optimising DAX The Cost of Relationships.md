---
title: "Optimising DAX: The Cost of Relationships"
source: "https://endjin.com/blog/optimising-dax-the-cost-of-relationships?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Carmel Eve]]"
published: 2026-07-02
created: 2026-08-08
description: "Relationships in Power BI aren't free. This post explains how the cardinality of the relationship key determines traversal cost, and why this has big implications for model design."
Processed: "Unprocessed"
---
Hello again. In the [previous post](https://endjin.com/blog/optimising-dax-why-cardinality-matters), we looked at why column cardinality is so important for compression and scan speed. But cardinality also has a major impact on something else: how expensive it is to follow relationships between tables.

This concept is important - and it has direct implications for model design. Look out for the next post where we'll put all of this together!

## Relationship Cost = Key Cardinality

The cost of traversing a relationship in VertiPaq depends on the **cardinality of the key column**. A relationship with a small key (say, a handful of product categories) is cheap. A relationship with a high-cardinality key (say, CustomerKey across millions of customers) is expensive.

This sounds intuitive enough, but there's a subtlety that's easy to miss.

## The Subtle Bit

Consider this setup:

- A **Customers** table with `CustomerKey` and `Gender`.
- An **Orders** table with `OrderNumber` and `CustomerKey`.

If you want to slice orders by Gender (low cardinality), you might think that would be cheap - Gender only has a couple of unique values, right? But to resolve that filter, the engine has to traverse the **CustomerKey relationship**, which is high-cardinality. The cost is determined by the relationship key, not the column you're ultimately filtering by. So it's still relatively expensive.

## Why This Matters for Model Design

Now think about a header/detail model design, where you have two large tables linked by a primary key. That key has 100% cardinality - every value is unique. This means:

**Every single query** that crosses that relationship pays the maximum possible traversal cost. It's not just that the model is large (because the ID column is stored in both tables with no compression benefit). It's that you're *also* constantly paying this high traversal cost on top.

It's a double hit. Thinking about header/detail designs - basically everything has to traverse that high-order relationship, so not only is the model huge, but you're constantly paying this cost. Linking two large fact tables via their primary key is about the worst thing you can possibly do.

## FAQs

What determines the cost of a relationship in Power BI? The cost of traversing a relationship is driven by the cardinality of the relationship key, not the column you're ultimately filtering by. A relationship via a high-cardinality key (like CustomerKey across millions of customers) is expensive even if you're filtering on a low-cardinality column (like Gender).
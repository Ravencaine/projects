---
title: "Optimising DAX"
source: "https://endjin.com/blog/optimising-dax-the-cost-of-relationships"
author: "endjin.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> Relationships in Power BI aren't free. This post explains how the cardinality of the relationship key determines traversal cost, and why this has big implications for model design.

Optimising DAX: The Cost of Relationships Skip to content Who We Are We are a UK consultancy who specialise in Data, Analytics, AI, and Cloud Native App Dev on Microsoft Fabric, Databricks & Azure. What We Do We help small teams achieve big things! We specialize in modernising data & analytics platforms, infusing AI, and creating compelling apps. Who We Help Whether a global brand, or an ambitious scale-up, we help the small teams who power them, to achieve more. What We Think We love to share our hard won learnings, through blogs, talks or thought leadership. This is the good stuff! Contact Us If you would like to ask us a question, talk about your requirements, or arrange a chat, we would love to hear from you. Want to know more about how endjin could help you? By Carmel Eve Software Engineer II 2nd July 2026 · 1 min read Hello again. In the previous post , we looked at why column cardinality is so important for compression and scan speed. But cardinality also has a major impact on something else: how expensive it is to follow relationships between tables. This concept is important - and it has direct implications for model design. Look out for the next post where we'll put all of this together! Relationship Cost = Key Cardinality The cost of traversing a relationship in VertiPaq depends on the cardinality of the key column . A relationship with a small key (say, a handful of product categories) is cheap. A relationship with a high-cardinality key (say, CustomerKey across millions of customers) is expensive. This sounds intuitive enough, but there's a subtlety that's easy to miss. The Subtle Bit Consider this setup: A Customers table with  and  . An Orders table with  and  . If you want to slice orders by Gender (low cardinality), you might think that would be cheap - Gender only has a couple of unique values, right? But to resolve that filter, the engine has to traverse the CustomerKey relationship , which is high-cardinality. The cost is determined by the relationship key, not the column you're ultimately filtering by. So it's still relatively expensive. Why This Matters for Model Design Now think about a header/detail model design, where you have two large tables linked by a primary key. That key has 100% cardinality - every value is unique. This means: Every single query that crosses that relationship pays the maximum possible traversal cost. It's not just that the model is large (because the ID column is stored in both tables with no compression benefit). It's that you're also constantly paying this high traversal cost on top. It's a double hit. Thinking about header/detail designs - basically everything has to traverse that high-order relationship, so not only is the model huge, but you're constantly paying this cost. Linking two large fact tables via their primary key is about the worst thing you can possibly do. FAQs What determines the cost of a relationship in Power BI? The cost of traversing a relationship is driven by the cardinality of the relationship key, not the column you're ultimately filtering by. A relationship via a high-cardinality key (like CustomerKey across millions of customers) is expensive even if you're filtering on a low-cardinality column (like Gender). Optimising DAX: How VertiPaq Stores Your Data Carmel Eve 27/05/2026 VertiPaq stores Power BI data column-by-column rather than row-by-row. That makes aggregations fast and cross-column queries the trickiest part of DAX. Optimising DAX: Model Design Comparisons and Testing Tips Carmel Eve 10/07/2026 Star schema vs flat table vs header/detail - which Power BI model design gives you the best performance? This post compares all three and covers practical testing tips. Optimising DAX: Why Cardinality Matters Carmel Eve 30/06/2026 Column cardinality is one of the biggest factors in Power BI model size and query speed. This post explains why, and covers practical techniques for reducing it. X LinkedIn GitHub Carmel is a software engineer and LinkedIn Learning instructor. She worked at endjin from 2016 to 2021, focused on delivering cloud-first solutions to a variety of problems. These included highly performant serverless architectures, web applications, reporting and insight pipelines, and data analytics engines. After a three-year career break spent travelling around the world, she rejoined endjin in 2024. Carmel has written many blog posts covering a huge range of topics, including deconstructing Rx operators , agile estimation and planning and mental well-being and managing remote working . Carmel has released two courses on LinkedIn Learning - one on the Az-204 exam (developing solutions for Microsoft Azure) and one on Azure Data Lake . She has also spoken at NDC, APISpecs, and SQLBits, covering a range of topics from reactive big-data processing to secure Azure architectures. She is passionate about diversity and inclusivity in tech. She spent two years as a STEM ambassador in her local community and taking part in a local men

## Code / Examples

```
CustomerKey
```
```
Gender
```
```
OrderNumber
```
```
CustomerKey
```


---
*Source: [endjin.com](https://endjin.com/blog/optimising-dax-the-cost-of-relationships)*

---
created: 2026-08-01
updated: 2026-08-02
source: "When a Simple Variance Measure Breaks Power BI Lessons from Cross-Fact DAX.md"
source_url: "https://medium.com/microsoft-power-bi/when-a-simple-variance-measure-breaks-power-bi-lessons-from-cross-fact-dax-84cdd81420a4"
author: "Mark Chen"
published: 2026-03-07
note_type: source
tags: [dax, cross-fact, variance, grain, treatas, iterators, selectedvalue, key-normalization]
---

# Cross-Fact Variance DAX — Mark Chen Case Study

Real-world: compare payroll vehicle hours vs equipment hours from different systems. Problem: no relationship between fact tables, grain mismatch between measures, leading spaces in keys. Fix: TREATAS virtual relationship, REMOVEFILTERS to equalize grain, SUMX iterator for totals, LTRIM/TRIM normalization.

**6 atomic notes extracted.**
